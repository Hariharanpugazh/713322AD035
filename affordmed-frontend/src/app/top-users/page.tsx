'use client';

import { useEffect, useState } from "react";

interface User {
  user_name: string;
  post_count: number;
}

export default function TopUsers() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  const getInitials = (name: string) => {
    const words = name.split(' ');
    const initials = words.map(word => word[0]).join('');
    return initials.toUpperCase();
  };

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        const res = await fetch("http://localhost:8000/top-users/");
        const data = await res.json();
        setUsers(data);
      } catch (err) {
        console.error("Failed to fetch top users:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4 sm:p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-2xl sm:text-3xl font-bold text-center mb-6 text-purple-900">
          🔥 Top 5 Active Users
        </h1>

        {loading ? (
          <div className="flex justify-center items-center h-40">
            <div className="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
          </div>
        ) : users.length === 0 ? (
          <div className="text-center text-gray-500 mt-10">
            <p className="text-lg font-medium">
              No user data available right now.
            </p>
            <p className="text-sm mt-1">
              Please check your <strong className="text-purple-700">AUTH_TOKEN</strong> or try again later.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            {users.map((user, index) => (
              <div
                key={index}
                className="bg-white shadow-md rounded-2xl p-4 flex items-center space-x-4 hover:scale-105 transition-transform"
              >
                <div className="w-16 h-16 bg-purple-500 text-white rounded-full flex items-center justify-center text-xl font-bold">
                  {getInitials(user.user_name)}
                </div>
                <div>
                  <h2 className="font-semibold text-lg text-gray-800">
                    {user.user_name}
                  </h2>
                  <p className="text-sm text-gray-600">
                    Posts: {user.post_count}
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

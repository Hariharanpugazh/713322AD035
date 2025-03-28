'use client';

import { useEffect, useState } from "react";

export default function TopUsers() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/top-users/")
      .then((res) => res.json())
      .then((data) => setUsers(data));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4 sm:p-6">
      <h1 className="text-2xl sm:text-3xl font-bold text-center mb-6 text-purple-900">
        🔥 Top 5 Active Users
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
        {users.map((user, index) => (
          <div
            key={index}
            className="bg-white shadow-md rounded-2xl p-4 flex items-center space-x-4 hover:scale-105 transition-transform"
          >
            <img
              src={`https://i.pravatar.cc/150?img=${Math.floor(Math.random() * 70)}`}
              alt="profile"
              className="w-16 h-16 rounded-full object-cover"
            />
            <div>
              <h2 className="font-semibold text-lg text-gray-800">{user.user_name}</h2>
              <p className="text-sm text-gray-600">Posts: {user.post_count}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

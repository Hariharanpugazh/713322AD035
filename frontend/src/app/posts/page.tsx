'use client';

import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Post {
  id: number;
  userid: number;
  content: string;
  user_id: string;
  user_name: string;
  comment_count: number;
}

export default function TrendingPostsPage() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTrending = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://localhost:8000/posts?type=popular');
        setPosts(response.data);
      } catch (error) {
        console.error('Error fetching trending posts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchTrending();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4 sm:p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl sm:text-4xl font-bold text-center text-purple-700 mb-6">
          🔥 Trending Posts
        </h1>

        {loading ? (
          <div className="flex justify-center items-center h-40">
            <div className="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
          </div>
        ) : posts.length === 0 ? (
          <div className="text-center text-gray-500 mt-10">
            <p className="text-lg font-medium">
              No posts available at the moment.
            </p>
            <p className="text-sm mt-1">
              Please verify your <strong className="text-purple-700">AUTH_TOKEN</strong>.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {posts.map((post) => (
              <div key={post.id} className="bg-white rounded-2xl shadow p-5 hover:shadow-lg transition">
                <h2 className="text-lg font-semibold text-gray-800">
                  {post.content || 'Untitled Post'}
                </h2>
                <p className="text-sm text-gray-500 mt-1">
                  by {post.user_name || 'Anonymous'}
                </p>
                <p className="text-sm text-gray-400 mt-1">
                  💬 {post.comment_count} comments
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

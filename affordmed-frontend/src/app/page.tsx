'use client';

import Link from 'next/link';
import { Flame, Sparkles } from 'lucide-react';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-100 px-6 py-12">
      <h1 className="text-3xl sm:text-4xl font-bold text-purple-800 mb-10 text-center">
        🚀 Affordmed Dashboard
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 w-full max-w-xl">
        <Link
          href="/top-users"
          className="bg-white rounded-2xl p-6 shadow-md hover:shadow-lg transition duration-200 flex items-center gap-4"
        >
          <Flame className="text-orange-500 w-8 h-8" />
          <div>
            <h2 className="text-lg font-semibold text-gray-800">Top Users</h2>
            <p className="text-sm text-gray-600">View most active users</p>
          </div>
        </Link>

        <Link
          href="/posts"
          className="bg-white rounded-2xl p-6 shadow-md hover:shadow-lg transition duration-200 flex items-center gap-4"
        >
          <Sparkles className="text-blue-600 w-8 h-8" />
          <div>
            <h2 className="text-lg font-semibold text-gray-800">Trending Posts</h2>
            <p className="text-sm text-gray-600">Explore popular posts</p>
          </div>
        </Link>
      </div>
    </div>
  );
}

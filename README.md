# 🚀 Affordmed - Social Media Analytics Dashboard

This is a **Next.js + TypeScript + Tailwind CSS** based frontend project developed for the **Affordmed Campus Hiring Evaluation**. It visualizes analytical insights from a simulated social media platform through a responsive and interactive dashboard.

---

## 📂 Folder Structure

```
📦 affordmed-dashboard
┣ 📁 app
┃ ┣ 📄 page.tsx             # Home with 3 navigation cards
┃ ┣ 📁 top-users
┃ ┃ ┗ 📄 page.tsx           # Top 5 active users
┃ ┣ 📁 posts
┃ ┃ ┗ 📄 page.tsx           # Trending posts
┃ ┣ 📁 feed
┃ ┃ ┗ 📄 page.tsx           # Real-time latest posts
┣ 📁 public
┣ 📄 package.json
┣ 📄 tailwind.config.js
┣ 📄 next.config.js
┣ 📄 README.md
```

---

## 📌 Features

### 1. Top Users
- Displays top 5 users based on number of posts.
- Shows profile initials as avatars.
- Responsive layout with hover effects.

### 2. Trending Posts
- Displays posts with the highest comment count.
- Uses loader while fetching.
- Graceful message if token is invalid.

### 3. Feed
- Displays latest posts in real-time order.
- Clean scrollable UI, dynamically updates.

---

## 🚪 API Endpoints Used

These APIs are consumed from Affordmed’s provided backend:

- **Top Users**: `GET http://localhost:8000/top-users/`
- **Trending Posts**: `GET http://localhost:8000/posts?type=popular`
- **Latest Feed**: `GET http://localhost:8000/posts?type=latest`

> Note: Token must be provided where required.

---

## 🌐 Local URLs

```bash
http://localhost:3000           # Home
http://localhost:3000/top-users # Top Users
http://localhost:3000/posts     # Trending Posts
http://localhost:3000/feed      # Latest Feed
```

---

## 💡 Tech Stack

- **Framework**: [Next.js 15.2.4](https://nextjs.org/)
- **Styling**: Tailwind CSS
- **Language**: TypeScript
- **Icons**: Lucide React

---

## 🔧 Setup & Installation

```bash
# 1. Clone the repository
$ git clone https://github.com/Hariharanpugazh/affordmed-dashboard.git
$ cd affordmed-dashboard

# 2. Install dependencies
$ npm install

# 3. Run development server
$ npm run dev
```

Ensure that the backend server is running at `http://localhost:8000` with valid authentication.

---

## 📸 Screenshots

- ✅ Mobile and Desktop Responsive
- ✅ Spinner-based Loaders
- ✅ Informative error states (e.g. token issue)

---

## 📢 Notes

- All three required pages are implemented.
- API integration is complete and dynamic.
- Loading, fallback, and responsiveness all prioritized.
- Designed keeping user experience and clarity in mind.
- Modular code and structured folder system.

---

## 👤 Author

**Hariharan P**  
Email: hariharanpugazh@gmail.com  
GitHub: [Hariharanpugazh](https://github.com/Hariharanpugazh)
Contact: [Harlee](https://www.harlee.pro)
---

This project was developed as part of a 3-hour assessment challenge. All requirements from Affordmed’s documentation were followed, with care taken to ensure a clean, maintainable frontend experience.

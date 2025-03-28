import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzMTU1NTg1LCJpYXQiOjE3NDMxNTUyODUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImNhYzY4ZjBiLWFlNDQtNDAxYS1hYzhhLTY4MjliYzAzZmJhOSIsInN1YiI6ImhhcmloYXJhbnB1Z2F6aEBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJTTlNDRSIsImNsaWVudElEIjoiY2FjNjhmMGItYWU0NC00MDFhLWFjOGEtNjgyOWJjMDNmYmE5IiwiY2xpZW50U2VjcmV0IjoiU3lobGxjRmZjeWtNSWREViIsIm93bmVyTmFtZSI6IkhhcmloYXJhbiBQIiwib3duZXJFbWFpbCI6ImhhcmloYXJhbnB1Z2F6aEBnbWFpbC5jb20iLCJyb2xsTm8iOiI3MTMzMjJBRDAzNSJ9.woXXmHS1VM6lSE4ggMFe0vZfPWncxg3Kfjwq2eankZM"

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

@api_view(['GET'])
def top_users(request):
    try:
        # Step 1: Fetch all users
        users_response = requests.get("http://20.244.56.144/test/users", headers=HEADERS)
        users_data = users_response.json()
        print("Users API Raw Response:", users_data)

        users = users_data.get("users", {})
        print("Extracted Users Dictionary:", users)

        results = []

        # Step 2: Count posts per user
        for user_id, user_name in users.items():
            posts_url = f"http://20.244.56.144/test/users/{user_id}/posts"
            posts_response = requests.get(posts_url, headers=HEADERS)
            posts = posts_response.json().get("posts", [])
            post_count = len(posts)
            print(f"{user_name} (ID: {user_id}) → {post_count} posts")

            results.append({
                "user_id": user_id,
                "user_name": user_name,
                "post_count": post_count
            })

        # Step 3: Sort and return top 5 users
        top5 = sorted(results, key=lambda x: x["post_count"], reverse=True)[:5]
        return Response(top5, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_posts(request):
    post_type = request.GET.get('type')
    print("Query param 'type':", post_type)

    if post_type not in ['popular', 'latest']:
        return Response(
            {"error": "Invalid query param. Use type=popular or type=latest"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Step 1: Fetch users
        users_response = requests.get("http://20.244.56.144/test/users", headers=HEADERS)
        users_data = users_response.json()
        print("Users API Response:", users_data)

        users = users_data.get("users", {})
        print("Extracted Users:", users)

        all_posts = []

        # Step 2: For each user, get their posts
        for user_id, user_name in users.items():
            posts_url = f"http://20.244.56.144/test/users/{user_id}/posts"
            posts_response = requests.get(posts_url, headers=HEADERS)
            posts_data = posts_response.json()
            posts = posts_data.get("posts", [])

            print(f"{user_name} (ID: {user_id}) has {len(posts)} posts")

            for post in posts:
                post["user_id"] = user_id
                post["user_name"] = user_name

                # Step 3: Fetch comments for each post
                post_id = post.get("id")
                comments_url = f"http://20.244.56.144/test/posts/{post_id}/comments"
                comments_response = requests.get(comments_url, headers=HEADERS)
                comments_data = comments_response.json()
                comments = comments_data.get("comments", [])

                print(f"Post ID {post_id} → {len(comments)} comments")

                post["comment_count"] = len(comments)
                all_posts.append(post)

        print("Total posts collected:", len(all_posts))

        # Step 4: Sort & Slice
        if post_type == "popular":
            sorted_posts = sorted(all_posts, key=lambda x: x["comment_count"], reverse=True)
        else:  # latest
            sorted_posts = sorted(all_posts, key=lambda x: x["id"], reverse=True)

        top_posts = sorted_posts[:5]
        print("Final Posts to return:", top_posts)

        return Response(top_posts, status=status.HTTP_200_OK)

    except Exception as e:
        print("Error occurred:", str(e))
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

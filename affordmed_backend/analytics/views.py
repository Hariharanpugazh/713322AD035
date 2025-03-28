import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzMTUyMjAxLCJpYXQiOjE3NDMxNTE5MDEsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImNhYzY4ZjBiLWFlNDQtNDAxYS1hYzhhLTY4MjliYzAzZmJhOSIsInN1YiI6ImhhcmloYXJhbnB1Z2F6aEBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJTTlNDRSIsImNsaWVudElEIjoiY2FjNjhmMGItYWU0NC00MDFhLWFjOGEtNjgyOWJjMDNmYmE5IiwiY2xpZW50U2VjcmV0IjoiU3lobGxjRmZjeWtNSWREViIsIm93bmVyTmFtZSI6IkhhcmloYXJhbiBQIiwib3duZXJFbWFpbCI6ImhhcmloYXJhbnB1Z2F6aEBnbWFpbC5jb20iLCJyb2xsTm8iOiI3MTMzMjJBRDAzNSJ9.ENuNV1O2L22E0DSqptir6_V9pjCb9zPKLHhmF9nX9uw"

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
    

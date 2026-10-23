
import requests

url = "https://jsonplaceholder.typicode.com/posts/2"

response = requests.get(url, timeout=10)

print("Status code:", response.status_code)

response.raise_for_status()

data = response.json()

print("Complete response:", data)
print("Post title:", data["title"])
print("Post body:", data["body"])

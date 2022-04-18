from requests import get, post, delete

print(delete('http://localhost:5000/api/news/1').json())

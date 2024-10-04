import requests

response = requests.get('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAm2jX10ExlwoIG2AQXa5BAk5aopIyh2is')

output = response.json()
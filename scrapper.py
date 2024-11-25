import requests
import webbrowser


url = requests.get('https://pornhub.com')
htmlText = url.text
print(htmlText)


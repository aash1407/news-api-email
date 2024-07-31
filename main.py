import requests
import smtplib, ssl

from send_email import send_email

topic = "tesla"
api_key = "a67c7e01d74649978bcbeb1de28af140"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-06-30&" \
      "sortBy=publishedAt&" \
      "apiKey=a67c7e01d74649978bcbeb1de28af140&" \
      "language=en"

request = requests.get(url)
content = request.json()
message = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" + article["description"] \
                  + "\n" + article["url"] + 2 * "\n"

send_email(message)
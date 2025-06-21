url = input("URL:").strip()
print(url)

#url.replace
url = input("URL:").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

#removeprefix
url = input("URL:").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")

#re.IGNORECASE

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))
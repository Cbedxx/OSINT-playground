import requests

username = input("Enter username: ")

sites = [
f"https://github.com/{username}",
f"https://twitter.com/{username}",
f"https://www.reddit.com/user/{username}"
]

for site in sites:
    response = requests.get(site)

if response.status_code == 200:
    print(f"[?] Possible match: {site}")
else:
    print(f"[-] Not Found: {site}")
  

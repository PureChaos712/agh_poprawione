import httpx

user = "purechaos712"
response = httpx.get(f"https://api.github.com/users/{user}/repos")
repos = response.json()

for repo in repos:
    print("Project:", repo.get('name'))
    print("URL:", repo.get('url'))

#git status
#git add
#git commit -m "A message describing what you have done to make this snapshot different"
#git push
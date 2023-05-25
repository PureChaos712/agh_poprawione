import aiohttp
import asyncio

async def main(user):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.github.com/users/{user}/repos") as repos:
            repos = await repos.json()
            for repo in repos:
                print("Project:", repo.get('name'))
                print("URL:", repo.get('url'))
                
asyncio.run(main('github'))

#git branch - dostępne gałęzie
#git branch <<branch>>
#git checkout <<branch>> - przełączenie się między gałęziami


import httpx

response = httpx.get(f"https://www.agh.edu.pl/")

print(response.text.count("AGH"))
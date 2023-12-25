import requests

organization = "your-organization"
access_token = "your-github-access-token"

url = f"https://api.github.com/orgs/{organization}/settings/billing/actions"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    usage = data.get("total_minutes_used", 0)

    print(f"GitHub Actions minutes used by {organization}: {usage} minutes")
else:
    print(
        f"Failed to fetch GitHub Actions usage. Status code: {response.status_code}, Response: {response.text}")

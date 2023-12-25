import requests

organization = "your-organization"
access_token = "your-github-access-token"

# GraphQL query to get the list of users in the organization
query = """
{
  organization(login: "%s") {
    members(first: 100) {
      nodes {
        login
      }
    }
  }
}
""" % organization

url = "https://api.github.com/graphql"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers, json={"query": query})

if response.status_code == 200:
    data = response.json()
    users = data["data"]["organization"]["members"]["nodes"]

    print(f"Users in the {organization} organization:")
    for user in users:
        print(user["login"])
else:
    print(
        f"Failed to fetch user list. Status code: {response.status_code}, Response: {response.text}")

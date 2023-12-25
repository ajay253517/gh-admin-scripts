import requests

access_token = "your-github-access-token" ## Ensure it has access for enterprise 

# Replace 'enterprise-name' with your actual GitHub Enterprise hostname
enterprise_name = "enterprise-name"

# Get total consumed licenses for the GitHub Enterprise
url = f"https://api.github.com/enterprises/{enterprise_name}/settings/license"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    total_licenses = response.json().get("total_all_users", 0)
    print(f"Total consumed licenses for the GitHub Enterprise: {total_licenses}")
else:
    print(f"Failed to fetch total consumed licenses. Status code: {response.status_code}, Response: {response.text}")
    exit()

# Get license breakdown per organization
orgs_url = f"https://api.github.com/enterprises/{enterprise_name}/organizations"
orgs_response = requests.get(orgs_url, headers=headers)

if orgs_response.status_code != 200:
    print(f"Failed to fetch organizations. Status code: {orgs_response.status_code}, Response: {orgs_response.text}")
    exit()

organizations = orgs_response.json()

print("\nLicense breakdown per organization:")
for org in organizations:
    org_name = org["login"]
    url = f"https://api.github.com/enterprises/{enterprise_name}/organizations/{org_name}/settings/license"
    org_response = requests.get(url, headers=headers)

    if org_response.status_code == 200:
        org_licenses = org_response.json().get("total_users", 0)
        print(f"Organization: {org_name}, Consumed licenses: {org_licenses}")
    else:
        print(f"Failed to fetch license usage for {org_name}. Status code: {org_response.status_code}, Response: {org_response.text}")

import requests 
import sys 
organization = 'YOUR_ORG' 
access_token = 'YOUR_ACCESS_TOKEN' 
team_ids = ["TEAM_ID_1", "TEAM_ID_2"]

# Check if username_to_invite is provided as a command line argument 
if len(sys.argv) < 2: 
    print("Usage: python invite_user.py <username_to_invite>") 
    sys.exit(1) 
username_to_invite = sys.argv[1] 
url = f'https://api.github.com/orgs/{organization}/invitations' 

headers = { 
   'Authorization': f'token {access_token}', 
   'Accept': 'application/vnd.github.v3+json' 

} 

data = { 
    'invitee_id': username_to_invite, 
    'role': 'direct_member', 
    'team_ids': team_ids 
}  
response = requests.post(url, headers=headers, json=data)  

if response.status_code == 201: 
    print(f'Successfully sent an invitation to {username_to_invite}.') 
else: 
    print(f'Failed to send an invitation to {username_to_invite}. Status code: {response.status_code}, Response: {response.text}') 
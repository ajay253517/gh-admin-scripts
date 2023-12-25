# Create a new SAML SSO organization credential 
resource "github_organization_saml_sso" "sso_config" {

  organization = "your-org"
  enabled      = true
  auto_start   = true
  sync_teams   = true
}

# Create a team for team synchronization 
resource "github_team" "sync_team" {
  name         = "SyncTeam"
  privacy      = "closed"
  auto_init    = true
  organization = "your-org"
}

# Add members to the team for synchronization 
resource "github_team_membership" "team_members" {
  for_each = {
    "member1" = "your-username1",
    "member2" = "your-username2"
    # Add more members as needed 
  }
  team_id  = github_team.sync_team.id
  username = each.value
}

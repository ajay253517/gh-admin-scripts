# Output the SAML SSO configuration details 

output "sso_configuration" {
  value = github_organization_saml_sso.sso_config
} 

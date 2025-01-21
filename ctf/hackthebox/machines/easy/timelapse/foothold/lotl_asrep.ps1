
# get all user accounts in the domain
$users = Get-ADUser -Filter {Enabled -eq $true} -Properties UserPrincipalName, PasswordLastSet

# iterate through each user to check for ASREP roastable condition
foreach ($user in $users) {
    # Check if the user's password doesn't expire and hasn't been set
    if ($user.PasswordLastSet -eq $null -and $user.UserPrincipalName) {
        Write-Host "AS-REP Roastable user found: $($user.UserPrincipalName)"
    }
}
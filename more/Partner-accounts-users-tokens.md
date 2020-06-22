Each of your customer’s businesses (not each user) that use your platform connected to Adobe Sign must have their own Adobe Sign account which may contain one or more users/senders.

Each of those accounts must have either; 1. An api token with “account wide” permissions that can be used “on behalf of” any sender/user in that account or 2. Each user has their own “self” scoped token.  In the case of #1 there is only a single oAuth process needed for all users in that account.  For #2 each user in that account has to go through the oAuth process to get their own individual token.

There is no way for a sender/user to get a token (account admin for an “account-wide” token OR non-admin-user for a “self” scoped token) without going through the oAuth token exchange where they log in and accept the permissions on that connected token.  This process can’t happen “behind the scenes” because we require that explicit consent to the permissions as part of the connection process.


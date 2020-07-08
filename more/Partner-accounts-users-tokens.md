### Partners - Accounts, Users, and oAuth

Each of your customer’s businesses (not each user) that use your platform connected to Adobe Sign must have their own Adobe Sign account which will contain one or more users/senders.

"Best Practice" is for each user of your platform to also have a corresponding Adobe Sign "sender"/user inside that account so that they as a business are the "data owners" of all agreements that originate from your platform as sent by employees of that company/entity.

#### API Tokens

To access the API from your platform, each of those accounts must use one (or more) of the following scenarios. 

1. An API token acquired by an account admin of their Adobe Sign account with “account wide” permissions that can be used “on behalf of” any sender/user in that account. 

   In this scenario the oAuth process only needs to happen once by an account admin and that token can be used "on behalf of" any user in that Adobe Sign account. To originate agreements for other users with the token "owned" by the account admin, all calls are made with a "header" parameter "x-api-user" with the value "email:sender@yourdomain.com".

2. An API token acquired by a "group admin" with "group" scoped permissions, from one of the groups in the Adobe Sign account.  In this case that same token can be used to create agreements "on behalf of" any user in that "group" in that Adobe Sign account.  All calls made in the "context" of specific originators using the same "x-api-user" header parameter as for an "account" scoped token as in #1.

3. An API token acquired by each user in that account with "self" scoped permissions.

In the case of #1 and #2 there is only a single oAuth request process needed for all users in that account or group.  For #3 each user in that account has to go through the oAuth process to get their own individual token.



#### Can I skip the "manual" process? .....

There is no way for a sender/user to get a token (account/group admin for an “account”/group scoped token OR non-admin-user for a “self” scoped token) without going through the oAuth token exchange where they log in and accept the permissions on that connected token.  This process can’t happen “behind the scenes” because we require that explicit consent to the permissions as part of the connection process.

#### Send AS - How do we use one token for multiple other "senders" ("context")

In all API calls (even if the contex belongs to the token "owner") "Best Practice" is to use the header parameter "x-api-user".

All tokens are "owned" by some user and if API calls are made without passing the "x-api-user" header parameter, then that call will be made in the "context" of that token's owner/user but it's always recommended to pass this parameter so that the "sender" is easily identifiable in the API call itself.  This is especially useful when dealing with the API logs for troubleshooting purposes.


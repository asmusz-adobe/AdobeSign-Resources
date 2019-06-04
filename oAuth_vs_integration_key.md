## When should you use oAuth vs Integration key?
Generally speaking [oAuth](https://secure.echosign.com/public/static/oauthDoc) is the preferred API authentication method for both partner (used by multiple Adobe Sign customers) and customer (used by a single Adobe Sign account) integrations.

Why, you may ask? Because it's more secure! At least once per hour, you are changing the string used to authenticate to our API.  The oAuth refresh token you get back from the initial request->response process is valid for 60 days but then every time you use that refresh token to get a new access token, you are pushing that expiration back out to 60 days from that point in time.

For partner applications, oAuth is __required__ for your "production app" because your app/integration will be used by many customers and we need to have a way to centrally disable the integration if some major security vulnerability is found. All that said however, during your developement work while you are testing api calls and processes, it is usually easier to use an integration key. 

### How do I get one?  
Simple, follow the instructions [here](https://helpx.adobe.com/sign/kb/how-to-create-an-integration-key.html).

You may need support to enable your account to use the integration key.  If so, please email support@echosign.com with the email address of the admin user in your account and ask.

### How do I use it?
This is also really straight forward.  You simply replace the "token" in your calls.

As an example, for REST V5 you pass an "Access-Token" header parameter with all calls made against the end-points. Just use the integration key as the value.  

For V6 of our API, you use an "Authorization" parameter with the value as "Bearer {{token}}" so in this case you only need to replace {{token}} with your integration key.

#### REMINDER FOR PARTNER DEVELOPERS
If you are developing a partner app so your customers can use Adobe Sign functionality from your app or platform, eventually, for *certification*, __you WILL BE REQUIRED to use oAuth__ so please start thinking about how you'll need to handle this process. For more info on oAuth, please see my oAuth walkthrough for partner integration development [here](https://github.com/skaboy71/AdobeSign-resources/blob/master/Partner%20oAuth%20Walkthrough.md).

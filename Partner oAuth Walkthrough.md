### Setting up a partner oAuth application
####
####
1. Read the [Adobe Sign oAuth doc](https://secure.echosign.com/public/static/oauthDoc) Start here to get an “overview” but don’t stress as there are more details the below to help walk you through it.
2. Create a “partner" app in your dev account The necessary first action.[->](https://github.com/skaboy71/AdobeSign-resources/blob/master/Partner%20oAuth%20Walkthrough.md#create-partner-app-in-your-dev-account)
3. Configure oAuth for the new app What permissions and access level do you need for your application?[->](https://github.com/skaboy71/AdobeSign-resources/blob/master/Partner%20oAuth%20Walkthrough.md#configure-oauth-for-the-new-app)
4. Add link to your platform for oAuth request This is how your customer’s will need to start the oAuth process.[->](https://github.com/skaboy71/AdobeSign-resources/blob/master/Partner%20oAuth%20Walkthrough.md#add-link-to-your-platform-for-oauth-request)
5. What does this oAuth process look like for your customers? More detail on the end-user experience, and some code/process discussion.
6. What’s needed on the “redirect URI” page? More “nuts and bolts” for the developers.
####
####
#### Create “partner" app in your dev account

To start you will need a [developers account on Adobe Sign](https://acrobat.adobe.com/us/en/why-adobe/developer-form.html).

Once you have the account set-up, you will need to log in and create a new partner application.

Account > Adobe Sign API  > API Applications > +
![image](http://drive.google.com/uc?export=view&id=1mvav1zi-aXa7P9zVKv4YHMI4JTfjrvUO)

Fill out as shown:

![image](http://drive.google.com/uc?export=view&id=1L3MnC-eIwTxhx5nOfO3rg-LAOBH4aZgR)

Your new partner application will be “uncertified” until you have gone through the partner certification process but you will be able to test the process of getting Adobe Sign accounts connected to it by changing some settings in the test/customer account. These details will be discussed in another note.

Ok … now we can move on to Configuring oAuth for your new Adobe Sign app!

####
####
#### Configure oAuth for the new app
##### What permissions and access level do you need for your application?
To configure oAuth setting for a partner app you will need to log into the developers account where you created the new partner app.

Find the app, select and click "Configure oAuth for application".

Account > Adobe Sign API  > API Applications > AppName > Configure oAuth for application

![image](http://drive.google.com/uc?export=view&id=1KzAGIsW-8_E9M7Kar4DU5mcCbOBocxMg)

You now need to add the permissions and “scopes” that will be used by your application when it interacts with the Adobe Sign APIs, as well as the **_redirect URI_** that will be **_a URL available publicly (internet) on your infrastructure that can capture the account details and code for from the request for oAuth process driven by the link that you will eventually add to your application or platform to get it connected to the customer’s Adobe Sign account._**

The process of capturing this data and making the API call to get the “refresh" and “access” tokens for API use by your platform/application will need to be done through code on your redirect URI page housed on your servers.

These “scopes” are not determining what the token will be, but are setting the “upper limit” or "scope" of **_what can be requested._** 

The request URL you use to link your customer’s instance of your application to the Adobe Sign account will contain the parameters for the permissions and level (self,group, or account) that your API integration will need for the actions you utilize in your integration.

Note that only Group Admins can approve OAuth requests that use the ":group" scope modifier, and only Account Admins can approve OAuth requests that use the ":account" scope modifier.

You may not (and probably don’t) need all the possible permissions available on this configuration, but during dev cycles, before you have decided how much API interaction with Adobe Sign your app may need to leverage, it may be best to enable everything since it is relatively easy to come back later and adjust.

When you adjust later, please limit the scopes that you enable to the minimum set necessary for your application, which is one of the requirements for Certification.

![image](http://drive.google.com/uc?export=view&id=1IVEu6A0XY15I6oAFgjXuF2t-e0XyoOvs)

Once you have this set as you’d like it, click “Save” and then we can talk about how to add a link in your app to start the oAuth process (getting oAuth tokens to link your customer’s app/platform instance to their Adobe Sign account).

####
####
#### Add link to your platform for oAuth request

In your app you will need a URL link for your customers to start the oAuth request process.

This link will give the parameters you’ll need to pass to the oAuth process.

The link URL should look something like this:

>https://secure.echosign.com/public/oauth?redirect_uri=https://your-oAuthInteraction-Server/your-oAuth-Page.html&response_type=code&client_id=CBJCHBCAABAAAbjw-szq8_Pg2Ljg7_b_vuaYiCAK1i4q&state=uhuhygtf576534&scope=user_read:account+user_write:account+user_login:account+agreement_read:account+agreement_write:account+agreement_send:account+widget_read:account+widget_write:account+library_read:account+library_write:account+workflow_read:account+workflow_write:account

##### How this breaks down:
1.  Base URL to start process - May seem obvious but we had to say it.  **_For partner apps this should NOT contain the "shard" of an account (na1, na2, eu1, jp1, etc.)_**
2.  Redirect URI "redirect_uri="- This comes from your application (configured on the app in your Adobe Sign developers account) oAuth settings. **_This must match the configured URI exactly. If not you will get errors._**
3.  Response Type “&response_type=code” -  This just tells the process you’re looking for the oAuth code on the redirect URI once your customer logs in and accepts the auth permissions. - Use this exactly as quoted (no replacement for your scenario)
4.  Client ID "&client_id=" - tells Adobe Sign what application your customer is requesting a token for. (The one for your app/platform)
5.  State "&state=" - This can be used to pass a unique ID that will be “passed through” to the redirect URI which is typically a unique identifier for the instance of your application so your system knows which client/instance requested the token and so where to save it inside your platform.
6. Scopes and permissions "&scope=" - This is the “good stuff” that tells Adobe Sign what permissions are needed for the token your app will need for all the wonderful things your platform can do for them when interacting with the Sign API. 

OK … got all that?  Next we look at what this process will look like for your customers.

####
####
#### What does this oAuth process look like for your customers?

When your customer goes through the oAuth process starting by clicking the link in your app, they will start by being taken to the main login page for Adobe Sign.

They might already have that browser logged into their account but if not they need to log in:

![image5](http://drive.google.com/uc?export=view&id=1L0RnfTHb5XqCVyX2HTarhWKdmX8U0ik2)

Next they’ll be presented with the permissions needed for your app as defined by the URL parameters in your starting link:

![image6](http://drive.google.com/uc?export=view&id=1LI2XG3Z8e5RWXzrr1t4Hztz46JADtcDI)

And next, they’ll be “redirected” to …… wait for it …… Yes!!     The redirect URI defined on your server.  😉

In the URL will be a number of things your system will need to get the refresh and access tokens that your app/platform will need to start making calls against the API.

The URL with those extra bits will look something like this:

>https://your-oauthinteraction-server/your-oAuth-Page.html?code=CBNCKBAAHBCAABAApvoU1TLVOj_GuGynhtExjJbQNOmst9KP&api_access_point=https%3A%2F%2Fapi.na1.echosign.com%2F&state=uhuhygtf576534&web_access_point=https%3A%2F%2Fsecure.na1.echosign.com%2F

What are all those extra bit about?

code=CBNCKBAAHBCAABAApvoU1TLVOj_GuGynhtExjJbQNOmst9KP — This is the code your system will use to make the actual API call to get those tokens. You need to use this fairly immediately as it’s only valid for 5 minutes.

api_access_point=https%3A%2F%2Fapi.na1.echosign.com%2F — This is the encoded URL which is the base URL for the account where you will need to start all your REST calls for getting tokens, sending agreements and all the other cool stuff.

&state=uhuhygtf576534 — This is that “state” string your system gave us so you could know which instance of your application/platform made this request.  You need this so you know where to take your customer “back” to and so you know which instance of your app you need to store the tokens for.

&web_access_point=https%3A%2F%2Fsecure.na1.echosign.com%2F  — This is the “web access” URL (where your customer can log in)

Great!! you may say but I still don’t have a token? 

True… please go to the next section to see a discussion of what the redirect URI page on your server needs to do.

####
####
####  What’s needed on the “redirect URI” page?

Ok …. whew … that was a lot and we still don’t have a token once we’ve been re-directed to that darn redirect URI page.

Yup, you still have some work.

As mentioned the params have all been passed to your page though on the URL so we can start with grabbing them.

in our example:

>https://your-oauthinteraction-server/your-oAuth-Page.html?code=CBNCKBAAHBCAABAApvoU1TLVOj_GuGynhtExjJbQNOmst9KP&api_access_point=https%3A%2F%2Fapi.na1.echosign.com%2F&state=uhuhygtf576534&web_access_point=https%3A%2F%2Fsecure.na1.echosign.com%2F

We have:

code = CBNCKBAAHBCAABAApvoU1TLVOj_GuGynhtExjJbQNOmst9KP
api_access_point = https://api.na1.echosign.com/
state = uhuhygtf576534

In addition to these you will need the Client/Application ID and “secret” from the partner app oAuth config page in your developer account:

![image7](http://drive.google.com/uc?export=view&id=12M6qmBQJHQ3tg0VLV3Nk288ReraMCefY)

Remember when we saw that while doing the oAuth configuration?

The POST call needs to hit that:
$api_access_point/oauth/token end point

So in this case (where the customer’s account is on na1) we need to hit:

https://secure.na1.echosign.com/oauth/token

This REST call has one header param:  Content-Type: application/x-www-form-urlencoded

In the body are a bunch of other params which you can construct from the data you now have from the URL plus your client ID and “secret”.

In POSTMAN (A great tool I highly recommend) this call would look something like this:

![image8](http://drive.google.com/uc?export=view&id=1ZA-ewTwf85ElSepjs_n8LX9CpNgHB0Bc)

The “raw” call looks like:

>POST /oauth/token HTTP/1.1
Host: secure.na1.echosign.com
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

code=CBNCKBAAHBCAABAAOhqFxpG1VorkQqCpTcsWQZrdlPAe6p4v&client_id=CBJCHBCAABAA-bAGKL5EGoAVa0uQnFR_k--pCMoA589W&client_secret=HCLtG15GhovoBD2HBlPJ7su5FJ7tMkHd&redirect_uri=https%3A%2F%2Faaronsmusz.com%2Foauth%2FoauthSuccess_app222.php&grant_type=authorization_code

The JSON response to this call will look something like this:

```JSON
{
    "access_token": "3AAABLblqZhDuw8mHJD5axQYRFV36l4U1A3csEcBxYcf9tr6OGtXghh8mGFNbEm9zulVHavW99-yDijJONs3syC49qiAtX-FA",
    "refresh_token": "3AAABLblqZhCxjXUfsx_pz44l8opXqFPXVUUPjr72JJ-uoBMvpo-xMgwiX_j6AUIfbskIaYyC34M*",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

Ok !!! We finally have a token ! Woooooooot !!

Now we can find this Customer’s instance using the state ID and store the tokens.

The “refresh” token is used to get new “access” tokens, but “Why?" you mays ask? 

The access token only lives for one hour(expires_in: 3600) so at least once an hour you need to make another call using the refresh token to get a new access token.

Again we need to hit that:
$api_access_point = https://api.na1.echosign.com
But now we need to POST to:

https://api.na1.echosign.com/oauth/refresh

This call looks like this:

>POST /oauth/refresh HTTP/1.1
Host: api.na1.echosign.com
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

refresh_token=3AAABLblqZhCxjXUfsx_pz44l8opXqFPXVUUPjr72JJ-uoBMvpo-xMgwiX_j6AUIfbskIaYyC34M*&client_id=CBJCHBCAABAA-
>bAGfU0EGoAVa0uQnFR_k--pCMoA589W&client_secret=HCLtG15GhovoBD2HBlKF4su5FJ7tMkHd&grant_type=refresh_token

Ok ….FYI …. The “refresh” token will also expire but it works a bit differently.
This token expires after 60 days, but every time you use the “refresh" token to get a new “access" token, you reset the expiration on the “refresh” token to 60 days from that point.  Cool?

If you are concerned about slow/no activity causing the “refresh” token to expire, you can set up a job that just refreshes the access token every 50 days or so if the date is getting “stale”. 

Once you have the tokens, and you know how to get new access tokens using the refresh token you can redirect the customer back to their instance of your app and ask them if they want to take a break for coffee ヽ(•‿•)ノ.

This concludes our crash course on oAuth and Adobe Sign!  
Hope you’re having a great day!



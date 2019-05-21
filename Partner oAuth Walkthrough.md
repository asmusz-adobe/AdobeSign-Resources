### Setting up a partner oAuth application
####
####
1. Read the [Adobe Sign oAuth doc](https://secure.echosign.com/public/static/oauthDoc) Start here to get an “overview” but don’t stress as there are more details the below to help walk you through it.
2. Create “partner" app in your dev account The necessary first action.[->](https://github.com/skaboy71/AdobeSign-resources/blob/master/Partner%20oAuth%20Walkthrough.md#create-partner-app-in-your-dev-account)
3. Configure oAuth for the new app What permissions and access level do you need for your application?[->](https://github.com/skaboy71/AdobeSign-resources/blob/master/Partner%20oAuth%20Walkthrough.md#configure-oauth-for-the-new-app)
4. Add link to your platform for oAuth request This is how your customer’s will need to start the oAuth process.
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

```
https://secure.echosign.com/public/oauth?redirect_uri=https://your-oAuthInteraction-Server/your-oAuth-Page.html&response_type=code&client_id=CBJCHBCAABAAAbjw-szq8_Pg2Ljg7_b_vuaYiCAK1i4q&state=uhuhygtf576534&scope=user_read:account+user_write:account+user_login:account+agreement_read:account+agreement_write:account+agreement_send:account+widget_read:account+widget_write:account+library_read:account+library_write:account+workflow_read:account+workflow_write:account
```

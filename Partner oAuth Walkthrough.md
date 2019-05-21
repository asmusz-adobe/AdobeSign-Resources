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

![image](https://drive.google.com/open?id=1KzAGIsW-8_E9M7Kar4DU5mcCbOBocxMg)

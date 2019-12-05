## Partner Application "Certification" 

There are some things you should be aware of and do as part of your dev process.

Your platform will normally be required to allow instance users to connect to their own Adobe Sign accounts to your platform through oAuth.  this is usually required so you will need to have developed and set things up on your side to account for this.

We need to make sure you are following the [OWASP top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) as well as making sure you're encrypting all the tokens as well as your partner "App Secret". 

During the security review and "Certification" process, we will do a few things.

*  Meet to go over the process of connecting your application/platform to Adobe Sign. (This meeting will typically include the partner manager from Adobe + someone from the security group + the Solution Consultant you've been working with) In this meeting we will want to see the oAuth process from your app plus basic instructions on sending and/or signing for your app typical use case.  This is normally recorded so our security folks can refer back when doing their testing.

*  Next, the security team will follow the instructions in an instance of your app/platform where you have given them access.  During this process

## Partner Application "Certification" 

There are some things you should be aware of and follow through on as part of your dev process.

Your platform will normally be required to allow instance users to connect their own Adobe Sign accounts (whether provision for them by you as a partner or acquired by them direct from Adobe) to your platform through oAuth.  This is usually __required__ so you will need to have developed and set things up on your side to account for this.

We need to make sure you are following the [OWASP top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) as well as making sure you're __encrypting all the tokens as well as your partner "App Secret"__. 

You should be finished or nearly finished with your integration development and be able to allow our reviewers to log into an instance to do their testing.

You can help speed up the process by providing any recent 3rd party security testing summary reports you may already have related to the OWASP parameters.

During the security review and "Certification" process, we will do a few things.

*  Meet to go over the process of connecting your application/platform to Adobe Sign and typical use of the functions related. (This meeting will typically include the partner manager from Adobe + someone from the security group + the Solution Consultant you've been working with) In this meeting we will want to see the oAuth process from your app plus basic instructions on sending, tracking and/or signing for your app's typical eSign use case.  This is normally recorded so our security folks can refer back when doing their testing.

*  Next, the security team will follow the instructions in an instance of your app/platform where you have given them access.  During this process they will connect the instance of your platform to Adobe Sign, Send and track or use other functions you've implemented for your integrations and do some light sniffing to make sure the integration is not exposing our mutual customers to any major security or data breach vulnerabilities.  They will __verify with you that you are storing all tokens for the integration in an encrypted format.__

*  If there are any major issues, the group will get back to your development team with the discovered issue/s and ask you to address.

*  Once all concerns have been addressed, your app will be certified and you will be able to make it available to your customers for general use.  If your integration functionality or permissions realted to your app need to change in the future, the application will need to be re-certified.



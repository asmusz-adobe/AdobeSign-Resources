## Browser Security and iFrames - Adobe Sign

#### These days, end users are bombarded contsantly with things they are asked to click on related to website security and tracking.  Most of these are in the form of "allow cookies" buttons on websites.

What are these [cookies](https://www.whoishostingthis.com/resources/cookies-guide/#history) that everyone is so concerned with?  Well they started as a way to track the current user so that profile preferences, or other individualization could be saved to the browser for current or possibly future session use/reference on a website.  Nice and convenient right? The concern is that like most things that make life "convenient" on the internet, these cookies can also be used to collect info about the web browsing behavior and possibly other details about you and your internet habits, sometimes across a number of sites and locations across the web.

#### What's a "3rd party" cookie?

From: 'Browser Cookies: What Are They & Why Should You Care?' ~ https://www.whoishostingthis.com/resources/cookies-guide/#types

> "**Third-party cookies**" are cookies added by a domain that is not the domain you are currently visiting. The most common use of third-party cookies is to track users who click on advertisements and associate them with the referring domain.
>
> For example, when you click on an ad on a website, a third-party cookie is used to associate your traffic with the site where the ad appeared.
>
> While cookies are a necessary part of the modern web, they can also pose a considerable risk of invasion of privacy as well as a security risk to the websites that use them."

#### What does this have to do with Adobe Sign and integrated applications/platforms that "embed" elements of our UI as part of their workflows to access e-sign functionality?

*<u>Adobe Sign uses these cookies to track user entered data in both the signing and authoring stages of the workflow so that the details are "saved" in case the opened process is abandoned or times out.</u>*  

In my work with partners who are "embedding" Adobe Sign functions inside their web based apps and other platforms, the way to allow the user access to these functions was to create an agreement via our API, and then get a "view" which consists of a URL that contains a sub section of the UI that's available while using our AdobeSign.com site's "Web UI".  Most commonly, partners want to embed the "signing experience" in an [iFrame](https://www.w3schools.com/html/html_iframe.asp) or "[modal](https://www.w3schools.com/w3css/w3css_modal.asp)" on a page inside their own application so that signers are not taken "out" of their platform to sign agreements.  This is also sometimes done for the "sender" where the partner's platform exposes the "compose"(same as the website send page) or the "authoring" UI page views.  

*In 2017 with Safari for iOS 11, Apple started a trend to increase mobile browser security by controlling access to 3rd party cookies with a default Safari setting to disallow it. This trend is now being promoted again by Apple as the front-runner.  Chrome, FireFox, and likely others based on those 2 browsers will likely follow soon.*

**What does this mean for partners and their integrations with Adobe Sign?**

This means that partners should start thinking about changing the way they deal with integrations which in the past were called "embedded".  One good way to handle this currently with Adobe Sign is to use a "new tab" workflow where the view URL returned through the API from the Sign platform is opened using a [javascript window.open](https://www.w3schools.com/jsref/met_win_open.asp) call. It's also recommended to use [button.onclick](https://www.w3schools.com/jsref/event_onclick.asp) in conjunction with the new tab/pop-up.  This allows for a more consistent experience across browsers.

This is the workflow experience that we have seen Microsoft use for oAuth pop-ups and similar integrations of 3rd party apps into their web based platforms. Given their massive range of use cases it seems like the best method to allow for this integrated functionality while keeping the need for continuously changing/managing their code to adjust for different browsers to a minimum.  

Adobe Sign has included the capability for this process to leverage [event listeners](https://www.w3schools.com/js/js_htmldom_eventlistener.asp) from the page where the window.open was launched. This means you can open a new tab or pop-up window and then ["listen" for the post-author or post-sign "page load" event](https://www.adobe.io/apis/documentcloud/sign/docs.html#!adobedocs/adobe-sign/master/events.md) so your code knows when those actions are finished and can then close the pop-up, returning the user to your own platform/UI.

This is the new "best practice" we are recommending instead of using iFrames and/or modals.  It also allows for the "view" to load without the need to adjust the page in the partner's application to accomodate  for different screen sizes on different devices since the Adobe Sign view is in itself designed to be as screen-adaptive as we were able to make it.  This also creates a better end user experience.


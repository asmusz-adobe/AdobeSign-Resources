## Browser Security and iFrames - Adobe Sign

#### These days, end users are bombarded contsantly with things they are asked to click on related to website security and tracking.  Most of these are in the form of "allow cookies" buttons on websites.

What are these [cookies](https://www.whoishostingthis.com/resources/cookies-guide/#history) that everyone is so concerned with?  Well they started as a way to track the current user so that profile preferences, or other individualization could be saved to the browser for current or possibly future session use/reference on a website.  Nice and convenient right? The concern is that like most things that make life "convenient" on the internet, these cookies can also be used to collect info about the web browsing behavior and possibly other details about you and your internet habits, sometimes across a number of sites and locations across the web.

#### What is a "3rd party" cookie?

[Browser Cookies: What Are They & Why Should You Care?]:https://www.whoishostingthis.com/resources/cookies-guide/#types

> "**Third-party cookies**" are cookies added by a domain that is not the domain you are currently visiting. The most common use of third-party cookies is to track users who click on advertisements and associate them with the referring domain.
>
> For example, when you click on an ad on a website, a third-party cookie is used to associate your traffic with the site where the ad appeared.
>
> While cookies are a necessary part of the modern web, they can also pose a considerable risk of invasion of privacy as well as a security risk to the websites that use them."

#### What does this have to do with Adobe Sign and integrated applications/platforms that "embed" elements of our UI as part of their access e-sign functionality?

In my work with partners who are embedding Adobe Sign functions inside their web based apps and other platforms, the way to allow the user access to these functions was to create an agreement via our API, and then get a "view" which consisted of a URL which is a segmented section of the UI that's available while using our "Web UI".  Most commonly, partners want to embed the "signing experience" on a page inside their own application so that signers are not taken "out" of their platform to sign their agreements.  This is also sometimes done for the "sender" where the partner's platform exposes the "compose"(same as send page) or the "authoring" views.

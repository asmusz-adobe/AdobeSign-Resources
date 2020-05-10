## Adobe Sign Webhook failure retry info

If a webhook "reciever" stops responding for any reason, the webhoook will start the "retry" process and will continue to retry for up to 72 hours, while "doubling" the interval betweek retries starting with 30 seconds.  

This will result in:

* Retry #1 in 30 seconds
* #2 in one min
* #3 in 2 minutes
* #4 in 4 mins
* and so on

This continues till the total time since the 1st failure is equal to or greater than 72 hours.

At this point that webhook will be "disabled".

Web hooks can be checked to determine whether they are enabled or disabled via API if monitoring is desired using the [GET /webhooks/{webhook ID}](https://secure.echosign.com/public/docs/restapi/v6#!/webhooks/getWebhookInfo) call, but this does not tell you if the webhook is failing but has not yet been disabled.

To make sure your system is always getting updates and to ensure the best possible reliability pleas see the following:

[Webhooks for Partner and Customer Integrated Platforms](https://github.com/skaboy71/AdobeSign-resources/blob/master/more/agreement_status_updates_webhooks_polling.md)


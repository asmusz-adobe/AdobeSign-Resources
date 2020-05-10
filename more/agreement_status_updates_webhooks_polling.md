# Adobe Sign - Agreement Status Updates and  Webhooks for Partner and Customer Integrated Platforms

While *we have webhooks that can be created by customers in the web UI "Front End"*, **we do not recommend that partners use this method when setting up their platform integrations.** We recommend partners set up webhooks via API as **"resource" or per-agreement webhooks**. There are a few reasons for this.

1. *Webhooks set up in the UI will fire for ALL agreements* created by ANY means for that user, all users in the group or all agreements for ALL users in the entire account.  You would then have to determine a way to distinguish between the agreements created by your integrated platform or application and any other agreements going through that user's account that were initiated elsewhere.
2. *With a single webhook, if there is an issue causing the webhook to fail, the entire webhook "train" stops until the failing instance of the webhook can go through.* The 72hour "retry" process starts but all the agreements created after that failure continue to "back up" behind that failed instance and that single 72 hour clock.  If using the "best practice" of creating pre-agreement webhooks, each agreement has it's own 72hour clock which starts on the 1st failure. This means that if there is some issue that causes webhooks to start failing, there will be less data loss if the failure is long enough to cause a webhook to get disabled.
3. If using this "per-agreement" process, your system will immediately detect that there is a webhook issue. You will not have to wait till customers start complaining about their agreements not updating.

### Polling as "backup" update method

*I't is also recommended to set up some sort of "polling" mechanism* and some way to re-create these "per-agreement" web-hooks if the creation step is has failed and the agreements are still in some "non-terminal" state.  It's also recommended to configure some monitoring+alerting on your side to let you know if the webhook creation process is failing.  If you're using the "per-agreement" process, your system will recognise that the issue has happened right away instead of needing to wait till customers complain about their agreement statuses not staying "current".  It would also be a good idea to automatically start the "polling" process for those agreements when the webhook creation failure is detected.

### Update Agreement Status "manual" option

An additional "best practice" is to add an "update agreement status" button or trigger in your interface which "polls" Adobe Sign for a single agreement so that if there is an issue happening, the user can manually update a particularly critical agreement to get their status and/or a copy of the completed agreement immediately. We do this in all the integrations that we (Adobe Sign) build.

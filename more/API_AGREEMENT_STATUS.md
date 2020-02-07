## API Related agreement "Statuses" AND [AGREEMENT EVENTS](./API_AGREEMENT_STATUS.md#agreement-events) AND [Webhook Events](./API_AGREEMENT_STATUS.md#webhook-events)

Most states relate to specific Adobe Sign ["roles"](https://helpx.adobe.com/sign/using/set-up-signer-approver-roles.html)
PDF can be found [here](https://documentcloud.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3A4eec32fd-527e-4133-9666-08fb35286d7e).

## STATUSES

|  Status                                  |  Status meaning/description
| :--------------------------------------- | :-------------------------------------------------- |
| 'OUT_FOR_SIGNATURE' | Waiting for Signature by one or more Signers|
| 'OUT_FOR_DELIVERY' | Waiting for acceptance by "Certified Recipient" (non-signer)|
| 'OUT_FOR_ACCEPTANCE' | waiting for acceptance by "Acceptor" (non-signer) |
| 'OUT_FOR_FORM_FILLING' | Waiting for "form filler" recipient to fill out data in fields (non-signer) |
| 'OUT_FOR_APPROVAL' | Waiting for "Approver" to approve (non-signer) |
| 'AUTHORING' | Agreement not yet finished with "authoring" so not yet sent to 1st recipient |
| 'ABORTED' | Cancelled(by sender) OR rejected(by recipient) __- Terminal State__ |
| 'CANCELLED' | Cancelled(by sender) OR rejected(by recipient) -- Legacy status, now = ABORTED __- Terminal State__ |
| 'SIGNED' | Completed "signed" __- Terminal State__ |
| 'APPROVED' | Completed "approved" __- Terminal State__ |
| 'DELIVERED' | Completed by "Certified Recipient" __- Terminal State__ |
| 'ACCEPTED' | Completed by "Acceptor" __- Terminal State__ |
| 'FORM_FILLED' | Filled out by "Form filler" |
| 'EXPIRED' | Agreement has passed "Expiration Date/Time" __- Terminal State__ |
| 'ARCHIVED' | Applies only to files "archived" to Adobe Sign for secure storage __- Terminal State__ |
| 'PREFILL' | Waiting to be pre-filled by sender |
| 'WIDGET_WAITING_FOR_VERIFICATION' | If email verification is on, signed web-forms(widgets) must have signer verify email address provided during signing before agreement is "complete"/fully executed |
| 'DRAFT' | From an API perspective think of this as a "stub record" state where no doc conversion has taken place so there is not yet an "authoring" or signing experience but you can change any related data before starting the steps to create an agreement. There is an agreement ID (stubbed) and associated data but nothing else has happened.  Agreements in this state can be deleted without incurring a transaction. |
| 'DOCUMENTS_NOT_YET_PROCESSED' | Request has been made to create an agreement but Adobe Sign is still working on processing the docs for the agreement. |
|'WAITING_FOR_FAXIN' | When agreement has been sent and forced WRITTEN. This status references legacy "Faxin" feature now deprecated but is still used for "written"(print, wet-sign, scan and upload) transactions |
|'WAITING_FOR_VERIFICATION' | OLD status same as WIDGET_WAITING_FOR_VERIFICATION |

## Status related to recipients

|  Status                                  |  Status meaning/description
| :--------------------------------------- | :-------------------------------------------------- |
|'COMPLETED'|Your required action is complete|
|'CANCELLED'|You (or someone before you in the recipient order) has cancelled the agreement|
|'EXPIRED'|The agreement expired whie waiting for you to take the required action|
|'NOT_YET_VISIBLE'|Recipients before you have not finished their required action/s|
|'WAITING_FOR_OTHERS'|Recipients after you still need to take their required actions|
|'WAITING_FOR_MY_APPROVAL'|You are the current recipient (APPROVER) and need to approve|
|'WAITING_FOR_AUTHORING'|You are the current sender and need to finish the authoring step and set the agreement to 'IN_PROCESS'|
|'WAITING_FOR_MY_ACKNOWLEDGEMENT'|You are the current recipient (CERTIFIED_RECIPIENT) and need to Acknowledge your reciept|
|'WAITING_FOR_MY_ACCEPTANCE'|You are the current recipient (ACCEPTOR) and need to Accept|
|'WAITING_FOR_MY_FORM_FILLING'|You are the current recipient (FORM_FILLER) and need to fill out the fields|
|'WAITING_FOR_MY_DELEGATION'|You are the current recipient (DELEGATOR) and need to delegate the agreement to someone|
|'WAITING_FOR_MY_SIGNATURE'|You are the current recipient (SIGNER) and need to sign|
|'WAITING_FOR_MY_VERIFICATION'| You have signed a web form (widget) but have not completed the post signing email verification step|
|'WAITING_FOR_PREFILL'| You are the 1st recipient where the sender has marked fields to be pre-filled (by her/him) but has not finished prefilling and sending|

## AGREEMENT EVENTS:

| Event Name                 | Description of Event               | Status Change                      |
| :------------------------- | :--------------------------------- | :--------------------------------- |
| 'CREATED' | When an agreement or Draft is created | A new resource with DRAFT status or AUTHORING or with one of the OUT_FOR_ status depending on the participants roles. |
| 'AGREEMENT_MODIFIED' | Agreement modified by sender modify document in flight | No change in the status. |
| 'USER_ACK_AGREEMENT_MODIFIED' | When signer acknowledge modification before signing | No change in the status. |
| 'SIGNED' | Agreement is fax signed | Either change in status based on the next participants role if there are more recipients or the status changes to SIGNED. |
| 'ESIGNED' | When agreement is signed | Either change in status based on the next participants role if there are more recipients or the status changes to SIGNED.|
| 'SIGNED' | When agreement is written (scanned+uploaded) signed | Either change in status based on the next participants role if there are more recipients or the status changes to SIGNED. |
| 'DIGSIGNED' | When agreement is digitally signed | Either change in status based on the next participants role if there are more recipients or the status changes to SIGNED.|
| 'APPROVED' | When agreement is approved | Either change in status based on the next participants role if there are more recipients or the status changes to one of SIGNED or APPROVED. |
| 'ACCEPTED' | When agreement is accepted | Either no change in status if there are more recipients or the status changes to one of SIGNED, APPROVED or ACCEPTED. |
| 'DELIVERED' | When agreement is delivered | Either no change in status if there are more recipients or the status changes to one of SIGNED, APPROVED, ACCEPTED, FORM_FILLED or DELIVERED. |
| 'FORM_FILLED' | When agreement is filled | Either no change in status if there are more recipients or the status changes to one of SIGNED, APPROVED, ACCEPTED or FORM_FILLED. |
| 'OFFLINE_SYNC' | When agreement is signed offline using mobile device | Either no change in status if there are more recipients or the status changes to SIGNED. |
| 'UPLOADED_BY_SENDER' | When signed agreement is uploaded by sender in esign workflow | Agreement status is computed based on next participant's role if there are more recipients or changes to SIGNED |
| 'FAXED_BY_SENDER' | When signed agreement is uploaded by sender in fax workflow | Agreement status is computed based on next participant's role if there are more recipients or changes to SIGNED This feature - (Fax in workflow) has been deprecated |
| 'SIGNATURE_REQUESTED' | When agreement is sent to signer for signature | Agreement status OUT_FOR_SIGNATURE |
| 'APPROVAL_REQUESTED' | When agreement is sent to signer for approval | Agreement status OUT_FOR_APPROVAL |
| 'ACKNOWLEDGEMENT_REQUESTED' | When agreement is sent to signer for acknowledgement | Agreement status OUT_FOR_DELIVERY |
| 'FORM_FILLING_REQUESTED' | When agreement is sent to signer for filling | Agreement status OUT_FOR_FORM_FILLING |
| 'ACCEPTANCE_REQUESTED' | When agreement is sent to signer for acceptance | Agreement status OUT_FOR_ACCEPTANCE |
| 'RECALLED' | When agreement is cancelled by sender | Status changes to ABORTED |
| 'REJECTED' | When agreement is rejected by signer | Status changes to ABORTED |
| 'EXPIRED' | When some custom expiry is set by sender and agreement reached that date | Status changes to EXPIRED |
| 'EXPIRED_AUTOMATICALLY' | When agreement is expired automatically | Status changes to EXPIRED |
| 'SHARED' | When agreement has been shared by a participant | No change in status |
| 'EMAIL_VIEWED' | When signer view's the esign mail | No change in status | 
| 'EMAIL_BOUNCED' | When email not delivered to signer | No change in status |
| 'AUTO_CANCELLED_CONVERSION_PROBLEM' | When agreement conversion failed due to which agreement is auto cancelled | Status changes to CANCELLED |
| 'PASSWORD_AUTHENTICATION_FAILED' | As name suggests | No change in status |
| 'KBA_AUTHENTICATION_FAILED' | As name suggests | No change in status |
| 'KBA_AUTHENTICATED' | As name suggests | No change in status |
| 'WEB_IDENTITY_AUTHENTICATED' | As name suggests | No change in status |
| 'WEB_IDENTITY_SPECIFIED' | As name suggests | No change in status |
| 'WIDGET_ENABLED' | When widget is marked enabled from disabled | Status of widget is changed to ENABLED |
| 'WIDGET_DISABLED' | When widget is marked disabled from enabled | Status of widget is changed to DISABLED |
| 'DELEGATED' | Agreement is delegated by signer | No change in status |
| 'AUTO_DELEGATED' | when auto delegation is on and agreement is delegated because of that | No change in status |
| 'REPLACED_SIGNER' | Sender replaced current signer | No change in status |
| 'VAULTED' | When agreement has vaulting enabled and a callback is sent to vault provided to perform vaulting | No change in status |
| 'DOCUMENTS_DELETED' | When document retention policy is enabled and documents of an agreement are deleted | Agreement changes to CANCELLED only if it is not in a terminating state |
| 'DRAFT_MODIFIED' | Agreement Draft has been modified | No change in status |

## Webhook Events

| Event Name                                         | Fires When |
| -------------------------------------------------- | ---- |
| AGREEMENT_ACTION_COMPLETED                         |The recipient has completed their required action, including all roles.(Singer, Approver, Acceptor, Certified Recipient, Form Filler, Delegator)|
| AGREEMENT_ACTION_DELEGATED                         |A delegation has occurred|
| AGREEMENT_ACTION_REPLACED_SIGNER                   |A Signer was replaced|
| AGREEMENT_ACTION_REQUESTED                         |The agreement has moved from one recipient to the next which requests the next person to take action (including all roles)|
| AGREEMENT_ALL                                      |Will fire on ALL possible events|
| AGREEMENT_AUTO_CANCELLED_CONVERSION_PROBLEM        |There can sometimes be issues converting the uploaded file that cause the agreement to fail. This is not always caught during the send action and can happen after agreement creation.|
| AGREEMENT_CREATED                                  |Agreement is created|
| AGREEMENT_DOCUMENTS_DELETED                        |The files in an agreement (documents) are deleted either via retention policy or via an API call to Adobe Sign to make that action. Audit info for the agreement is retained.|
| AGREEMENT_EMAIL_BOUNCED                            |AN email to a recipient is "bounced" by the recieving server.  Usually due to a bad address.|
| AGREEMENT_EMAIL_VIEWED                             |The email from Adobe Sign asing a recipient to take action is viewed in their email client|
| AGREEMENT_EXPIRED                                  |The expiration date/time has elapsed. This is a terminating event for the entire agreement.|
| AGREEMENT_KBA_AUTHENTICATED                        |A signer using KBA has successfully authenticated|
| AGREEMENT_MODIFIED                                 |The "document" in an "in-flight" un-signed agreement has been replaced/changed|
| AGREEMENT_OFFLINE_SYNC                             |An agreement sent to someone using the iOS app with off-line signing capabilities has "synced" the agreement to their Adobe Sign mobile app for later signing while off-line.|
| AGREEMENT_RECALLED                                 |The agreement was cancelled by the sender or the senders designated admin|
| AGREEMENT_REJECTED                                 |The agreement was cancelled by a recipient.|
| AGREEMENT_SHARED                                   |The agreement was shared by the sender OR by a signer who has access to a signed agreement.|
| AGREEMENT_UPLOADED_BY_SENDER                       |A "wet signed", scanned copy was sent to the sender and she/he uploaded it as the "signed copy" in the web UI.|
| AGREEMENT_USER_ACK_AGREEMENT_MODIFIED              |After send, a signer may decide that there is somthing incorrect in the agreement document which needs to be changed.  If they don't sign or reject, they can notify the sender and the sender can "replace" the document with a corrected copy. In this case there is a notification to the signer that the doc has been modified.|
| AGREEMENT_VAULTED                                  |When an agreement is vaulted vie the eOriginal integration.|
| AGREEMENT_WEB_IDENTITY_AUTHENTICATED               |When a signer authenticates for signing via social ID (google facebook etc.)|
| AGREEMENT_WORKFLOW_COMPLETED                       |When an agreement reaches a terminal state.  This includes recall (sender action), rejection (signer action), and completion when all recpients have taken their required action/s|
| LIBRARY_DOCUMENT_CREATED                           |A library doc is created (document or form field template)|
| LIBRARY_DOCUMENT_AUTO_CANCELLED_CONVERSION_PROBLEM |If via API "POST" or during save in the UI there is an issue with document conversion on a library doc/template add|
| LIBRARY_DOCUMENT_MODIFIED                          |When a library doc or template is modified.|
| LIBRARY_DOCUMENT_ALL                               |ALL possible doc library events|
| MEGASIGN_ALL                                       |      |
| MEGASIGN_CREATED                                   |      |
| MEGASIGN_RECALLED                                  |      |
| MEGASIGN_SHARED                                    |      |
| WIDGET_ALL                                         |      |
| WIDGET_AUTO_CANCELLED_CONVERSION_PROBLEM           |      |
| WIDGET_CREATED                                     |      |
| WIDGET_DISABLED                                    |      |
| WIDGET_ENABLED                                     |      |
| WIDGET_MODIFIED                                    |      |
| WIDGET_SHARED                                      |      |

## API Related agreement "Statuses" AND [EVENTS](https://github.com/skaboy71/AdobeSign-resources/blob/master/more/API_AGREEMENT_STATUS.md#events)

Most states relate to specific Adobe Sign ["roles"](https://helpx.adobe.com/sign/using/set-up-signer-approver-roles.html)
PDF can be found [here](https://documentcloud.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3A4eec32fd-527e-4133-9666-08fb35286d7e).

## STATUSES

|  Status                                  |  Status meaning/description
| :--------------------------------------- | :-------------------------------------------------- |
| 'OUT_FOR_SIGNATURE' | Waiting for Signature |
| 'OUT_FOR_DELIVERY' | Waiting for acceptance by "Certified Recipient" (non-signer)|
| 'OUT_FOR_ACCEPTANCE' | waiting for acceptance by "Acceptor" (non-signer) |
| 'OUT_FOR_FORM_FILLING' | waiting for "form filler" recipient to fill out data in fields (non-signer) |
| 'OUT_FOR_APPROVAL' | waiting for "Approver" to approve (non-signer) |
| 'AUTHORING' | agreement not yet finished with "authoring" so not yet sent to 1st recipient |
| 'ABORTED' | 'cancelled(by sender) OR rejected(by recipient) |
| 'CANCELLED' | cancelled(by sender) OR rejected(by recipient) -- Legacy status now = ABORTED |
| 'SIGNED' | completed "signed" |
| 'APPROVED' | completed "approved" |
| 'DELIVERED' | completed by "Certified Recipient" |
| 'ACCEPTED' | completed by "Acceptor" |
| 'FORM_FILLED' | Filled out by "Form filler" |
| 'EXPIRED' | 'agreement has passed "Expiration Date/Time" |
| 'ARCHIVED' | Applies only to files "archived" to Adobe Sign for secure storage |
| 'PREFILL' | waiting to be pre-filled by sender |
| 'WIDGET_WAITING_FOR_VERIFICATION' | If email verification is on, signed web-forms(widgets) must have signer verify email address provided during signing before agreement is "complete"/fully executed |
| 'DRAFT' | From an API perspective think of this as a "stub record" state where no doc conversion has taken place so there is not yet an "authoring" or signing experience but you can change any related data before starting the steps to create an agreement. There is an agreement ID (stubbed) and associated data but nothing else has happened.  Agreements in this state can be deleted without incurring a transaction. |
| 'DOCUMENTS_NOT_YET_PROCESSED' | request has been made to create an agreement but Adobe Sign is still working on processing the docs for the agreement. |
|'WAITING_FOR_FAXIN' | This is a deprecated status related to Fax in feature no longer offered. |
|'WAITING_FOR_VERIFICATION' | OLD status same as WIDGET_WAITING_FOR_VERIFICATION |

## EVENTS:

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
| 'FAXED_BY_SENDER' | When signed agreement is uploaded by sender in fax workflow | Agreement status is computed based on next participant's role if there are more recipients or changes to SIGNED This feature - (Fax in orkflow) has been deprecated |
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
| 'DOCUMENTS_DELETED' | When document retention policy is enabled and documents of an agreement is deleted | Agreement changes to CANCELLED only if it is not in a terminating state |
| 'DRAFT_MODIFIED' | Agreement Draft has been modified | No change in status |


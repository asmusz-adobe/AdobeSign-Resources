## API Related agreement "Statuses" AND [EVENTS](https://github.com/skaboy71/AdobeSign-resources/blob/master/more/API_AGREEMENT_STATUS.md#events)

Most states relate to specific Adobe Sign ["roles"](https://helpx.adobe.com/sign/using/set-up-signer-approver-roles.html)
PDF can be found [here](https://documentcloud.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3A4eec32fd-527e-4133-9666-08fb35286d7e).

*  __'OUT_FOR_SIGNATURE'__ = Waiting for Signature
*  __'OUT_FOR_DELIVERY'__ = Waiting for acceptance by "Certified Recipient" (non-signer)
*  __'OUT_FOR_ACCEPTANCE'__ = waiting for acceptance by "Acceptor" (non-signer)
*  __'OUT_FOR_FORM_FILLING'__ = waiting for "form filler" recipient to fill out data in fields (non-signer)
*  __'OUT_FOR_APPROVAL'__ = waiting for "Approver" to approve
*  __'AUTHORING'__ = agreement not yet finished with "authoring" so not yet sent to 1st recipient
*  __'CANCELLED'__ = cancelled(by sender) OR rejected(by recipient) 
*  __'SIGNED'__ = completed "signed"
*  __'APPROVED'__ = completed "approved"
*  __'DELIVERED'__ = completed by "Certified Recipient"
*  __'ACCEPTED'__ = completed by "Acceptor"
*  __'FORM_FILLED'__ = Filled out by "Form filler"
*  __'EXPIRED'__ = agreement has passed "Expiration Date/Time"
*  __'ARCHIVED'__ = Applies only to files "archived" to Adobe Sign for secure storage
*  __'PREFILL'__ = waiting to be pre-filled by sender
*  __'WIDGET_WAITING_FOR_VERIFICATION'__ = If email verification is on, signed web-forms(widgets) must have signer verify email address provided during signing before agreement is "complete"/fully executed
*  __'DRAFT'__ = From an API perspective think of this as a "stub record" state where no doc conversion has taken place so there is not yet an "authoring" or signing experience but you can change any related data before starting the steps to create an agreement. There is an agreement ID (stubbed) and associated data but nothing else has happened.  Agreements in this state can be deleted without incurring a transaction.

*  __'DOCUMENTS_NOT_YET_PROCESSED'__ = request has been made to create an agreement but Adobe Sign is still working on processing the docs for the agreement.

*  __'WAITING_FOR_FAXIN'__ = This is a deprecated status related to Fax in feature no longer offered.

*  __'WAITING_FOR_VERIFICATION'__ = OLD status same as WIDGET_WAITING_FOR_VERIFICATION


## EVENTS:

*  __'CREATED'__ = When an agreement or Draft is created A new resource with DRAFT status or AUTHORING or with one of the OUT_FOR_ status depending on the participants roles.

*  __'AGREEMENT_MODIFIED'__ = Agreement modified by sender modify document in flight -- No change in the status.

*  __'USER_ACK_AGREEMENT_MODIFIED'__ = When signer acknowledge modification before signing -- No change in the status.

*  __'SIGNED'__ = Agreement is fax signedEither change in status based on the next participants role if there are more recipients or the status changes to SIGNED.

*  __'ESIGNED'__ = When agreement is signedEither change in status based on the next participants role if there are more recipients or the status changes to SIGNED.

*  __'SIGNED'__ = When agreement is written signedEither change in status based on the next participants role if there are more recipients or the status changes to SIGNED.

*  __'DIGSIGNED'__ = When agreement is digitally signedEither change in status based on the next participants role if there are more recipients or the status changes to SIGNED.

*  __'APPROVED'__ = When agreement is approvedEither change in status based on the next participants role if there are more recipients or the status changes to one of SIGNED or APPROVED.

*  __'ACCEPTED'__ = When agreement is acceptedEither no change in status if there are more recipients or the status changes to one of SIGNED, APPROVED or ACCEPTED.

*  __'DELIVERED'__ = When agreement is delivered Either no change in status if there are more recipients or the status changes to one of SIGNED, APPROVED, ACCEPTED, FORM_FILLED or DELIVERED.

*  __'FORM_FILLED'__ = When agreement is filledEither no change in status if there are more recipients or the status changes to one of SIGNED, APPROVED, ACCEPTED or FORM_FILLED.

*  __'OFFLINE_SYNC'__ = When agreement is signed offline using mobile deviceEither no change in status if there are more recipients or the status changes to SIGNED.

*  __'UPLOADED_BY_SENDER'__ = When signed agreement is uploaded by sender in esign workflowAgreement status is computed based on next participant's role if there are more recipients or changes to SIGNED

*  __'FAXED_BY_SENDER'__ = When signed agreement is uploaded by sender in fax workflowAgreement status is computed based on next participant's role if there are more recipients or changes to SIGNED  -- This feature - (Fax in workflow) has been deprecated

*  __'SIGNATURE_REQUESTED'__ = When agreement is sent to signer for signature -- Agreement status OUT_FOR_SIGNATURE

*  __'APPROVAL_REQUESTED'__ = When agreement is sent to signer for approval -- Agreement status OUT_FOR_APPROVAL

*  __'ACKNOWLEDGEMENT_REQUESTED'__ = When agreement is sent to signer for acknowledgement -- Agreement status OUT_FOR_DELIVERY

*  __'FORM_FILLING_REQUESTED'__ = When agreement is sent to signer for filling -- Agreement status OUT_FOR_FORM_FILLING

*  __'ACCEPTANCE_REQUESTED'__ = When agreement is sent to signer for acceptance -- Agreement status OUT_FOR_ACCEPTANCE

*  __'RECALLED'__ = When agreement is cancelled by sender -- Status changes to ABORTED

*  __'REJECTED'__ = When agreement is rejected by signer -- Status changes to ABORTEDE

*  __'XPIRED'__ = When some custom expiry is set by sender and agreement reached that date -- Status changes to EXPIRED

*  __'EXPIRED_AUTOMATICALLY'__ = When agreement is expired automatically -- Status changes to EXPIRED

*  __'SHARED'__ = When agreement has been shared by a participant -- No change in status

*  __'EMAIL_VIEWED'__ = When signer view's the esign mail -- No change in status 

*  __'EMAIL_BOUNCED'__ = When email not delivered to signer -- No change in status

*  __'AUTO_CANCELLED_CONVERSION_PROBLEM'__ = When agreement conversion failed due to which agreement is auto cancelled -- Status changes to CANCELLED

*  __'PASSWORD_AUTHENTICATION_FAILED'__ = As name suggests -- No change in status

*  __'KBA_AUTHENTICATION_FAILED'__ = As name suggests -- No change in status

*  __'KBA_AUTHENTICATED'__ = As name suggests -- No change in status 

*  __'WEB_IDENTITY_AUTHENTICATED'__ = As name suggests -- No change in status

*  __'WEB_IDENTITY_SPECIFIED'__ = As name suggests -- No change in status

*  __'WIDGET_ENABLED'__ = When widget is marked enabled from disabled -- Status of widget is changed to ENABLED

*  __'WIDGET_DISABLED'__ = When widget is marked disabled from enabled -- Status of widget is changed to DISABLED

*  __'DELEGATED'__ = Agreement is delegated by signer -- No change in status

*  __'AUTO_DELEGATED'__ = when auto delegation is on and agreement is delegated because of that -- No change in status

*  __'REPLACED_SIGNER'__ = Sender replaced current signer -- No change in status

*  __'VAULTED'__ = When agreement has vaulting enabled and a callback is sent to vault provided to perform vaulting -- No change in status

*  __'DOCUMENTS_DELETED'__ = When document retention policy is enabled and documents of an agreement is deleted -- Agreement changes to CANCELLED only if it is not in a terminating state

*  __'DRAFT_MODIFIED'__ = Agreement Draft has been modified -- No change in status 


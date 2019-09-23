## API Related agreement "Statuses"

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

*  __'WAITING_FOR_VERIFICATION'__ = OLD status same as WIGET_WAITING_FOR_VERIFICATION

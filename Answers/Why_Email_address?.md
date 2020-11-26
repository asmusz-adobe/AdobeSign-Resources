##  Signer Identity and "Email Address" in the Documented Signing Process

Electronic signatures can’t be thought of in quite the same way as other IT related functions.
It really is a documanted “process”.

An electronic signature does (at a high level) 3 things:

1. Captures the “intent to sign”
2. Identifies the “signers” (or other possible “participants”) in some way
3. Captures the date and time the signature took place. Additionally (but not necessarily required for legality) it captures the “location” the signing took place.

Point #2 is where the email address becomes an issue … almost all e-signature platforms (All that I’m aware of) rely on email as the most basic way to identify the participants in the documentation of the “process”.  This documentation is what we call an “audit trail”.

Without having an email address, you really need to provide some other means of identifying those participants either on the “agreement” (the article that represents a transaction between parties) or in the audit info.

We do “require” an email address to represent those participants and it’s possible from a technical perspective to use some generic address like esigner@yourdomain.com as representing the participant but this is not best practice or recommended since it then negates that identification in the documentation (audit trail) of those participants.

In some cases, there are things in the agreement (other than the signature itself) that ID the participant like a social, drivers license, or other PII but even then, you have really lost the metadata about the process and lost some of the credibility on the way.

###  Why Email makes sense 

Ok so we understand the need for some PII in the audit trail, but why email specifically?

An email address is usually associated to a person, it usually does not change once in place, and it's usually ok that it's "public" -ish :-).

*  We could use a physical address but what happens when you move?
*  We could use phone number but those are re-used quite often.
*  We don't want to expose things like social security number, drivers license numbers, etc due ti ID theft and fraud risks.

While email is not "perfect", it is one of the _best possible_ ways that really makes the most sense given it's properties.

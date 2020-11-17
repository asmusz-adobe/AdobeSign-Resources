## Where is my data?

          -- Last updated Nov 15 2020

Look at the URL after you are logged in.

Here is an example:

secure(or something else).**na2**.adobesign(or echosign).com/public/login

Depending on the "shard"(**na1, na2, na3, na4, eu1,** etc.) which shows in the URL after login to Adobe Sign, your data is in a datacenter in the below locations:

### North America

*  NA1 - Amazon Web Services - Ashburn Virginia/Madison Wisconsin
*  NA2 - Amazon Web Services - Portland/Beaverton Oregon
*  NA3 - MicrosoftS Azure - Ashburn/Boydton Virginia
*  NA4 - Amazon Web Services - Boardman Oregon/San Diego CA

### EU Region

*  EU1 - Amazon Web Services - Frankfurt Germany
*  EU2 - Amazon Web Services - Dublin Ireland

### Japan

*  JP1 - Amazon Data Services Japan - Tokyo

### Australia

*  AU1 - Amazon Web Services - Sydney

### India

*  IN1 - Amazon Data Services India - Mumbai

## Verify this yourself

If you open a terminal window (Command prompt in a Microsoft OS), you can "ping" your shard.

For example "ping na1.adobesign.com" will return an IP address something like "52.71.63.231".

If you then go to https://whatismyipaddress.com/ip/52.71.63.231 (put the ip address you got back at the end of the URL) , you will get the "lookup" info on where that ip address resolves to, including the city, state, and who owns (company where that address is hosted) that specific address.

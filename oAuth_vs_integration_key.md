### Why should you use oAuth vs Integration key?
Generally speaking oAuth is the preferred API authentication method for both partner (used by multiple Adobe Sign customers) and customer (used by a single Adobe Sign account) integrations.

For partner applications, oAuth is required for the "production app" because your app/integration will be used by many customers and we need to have a way to centrally disable the functionality if some security vulnerability is found, etc.

During your developement process while you are testing api calls and processes, it is usually recommended to use an [integration key](https://helpx.adobe.com/sign/kb/how-to-create-an-integration-key.html).   

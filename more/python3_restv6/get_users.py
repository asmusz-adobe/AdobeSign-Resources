'''
This function uses Adobe Sign rest V6 api to get list of users in your account
usage:
your_list_of_users = get_user_list(your_shard, your_api_token)
'''
import requests, json

#################################
def get_userlist(ac_shard, api_token):
    # api endpoint
    api_u = 'https://api.' + ac_shard + '.echosign.com/api/rest/v6' + '/users'
    # headers for rest call
    headers = {
        'Authorization': 'Bearer ' + api_token,
    }
    # make request to API and load userInfoList text to json
    users = (json.loads((requests.get(api_u, headers=headers)).text))['userInfoList']
    # return userInfoList as json
    return users
#################################

# Set var for your api 'access token' or integration key
a_token = '3AAABLblqZhD7gPDMJ5vj *** Your integration key or access token goes here *** U2WqAsaG1oYtllVLaHv9e'

#  Set var for your shard goes here.  Examples: na1, na2, eu1, eu2, jp1, au1, etc
shard = 'na2'

# get the list of users to all_users var
all_users = get_user_list(shard, a_token)

# print out
print(json.dumps(all_users, indent=4))

# print 1st user data from list
print(json.dumps(all_users[0], indent=4))

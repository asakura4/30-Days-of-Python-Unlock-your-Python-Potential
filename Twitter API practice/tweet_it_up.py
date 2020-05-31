import twitter

API_key="<YOUR API KEY>"
API_secret_key="<YOUR API SECRET KEY>"
Access_token="<YOUR ACCESS TOKEN>"
Access_token_secret="<YOUR ACCESS TOKEN SECRET>" 


api = twitter.Api(consumer_key=API_key, 
				consumer_secret=API_secret_key,
				access_token_key=Access_token,
				access_token_secret=Access_token_secret
				)

print(api.VerifyCredentials())

followers = api.GetFollowers()
friends = api.GetFriends()

status_var = "Test 3 #TwitterAPITest #Python is amazing! https://www.coursera.org/"
#post_update = api.PostUpdates(status=status_var)


length_status = twitter.twitter_utils.calc_expected_status_length(status=status_var)

new_message = api.PostDirectMessage(user_id='', text='Hi there')
print(new_message)


# api.PostDirectMessage(user, text)
# api.GetUser(user)
# api.GetReplies()
# api.GetUserTimeline(user)
# api.GetHomeTimeline()
# api.GetStatus(status_id)
# api.GetStatuses(status_ids)
# api.DestroyStatus(status_id)
# api.GetFriends(user)
# api.GetFollowers()
# api.GetFeatured()
# api.GetDirectMessages()
# api.GetSentDirectMessages()
# api.PostDirectMessage(user, text)
# api.DestroyDirectMessage(message_id)
# api.DestroyFriendship(user)
# api.CreateFriendship(user)
# api.LookupFriendship(user)
api.VerifyCredentials()


print(followers)
print(friends)

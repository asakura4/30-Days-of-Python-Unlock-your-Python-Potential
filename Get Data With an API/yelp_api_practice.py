import requests


API_Key = '' # get the API key via Yelp fusion page
url = "https://api.yelp.com/v3/businesses/search"
headers = {
		'Authorization': 'Bearer {}'.format(API_Key)
	}

def do_search(term="food", location="San Francisco"):
	url = "https://api.yelp.com/v3/businesses/search"
	headers = {
		'Authorization': 'Bearer {}'.format(API_Key)
	}

	# Method 1
	# term = term.replace(' ', '+')
	# location = location.replace(' ','+')
	# url = "{url}?term={term}&location={location}".format(
	# 		url=url,
	# 		term=term,
	# 		location=location
	# 	)
	# r = requests.get(url, headers=headers)
	

	# Method 2
	params = {
		"term": term,
		"location": location
	}
	r = requests.get(url, headers=headers, params=params)
	return r.json()


serach_result = do_search()

for i in serach_result["businesses"]:
	print(i["name"])
	print(i["phone"])
	print(i["location"]["display_address"])
	print(i["location"]["city"])
	print(i.get('location').get('area'))
	print("\n")
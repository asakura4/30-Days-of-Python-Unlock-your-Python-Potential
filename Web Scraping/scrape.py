import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
loc = 'NewPort Beach, CA'
current_page = 0

while current_page < 201:
	print
	url = base_url + loc + "&start=" + str(current_page)
	yelp_r = requests.get(url)
	#yelp_r -- <response 200>
	yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
	file_path = 'yelp-{loc}-title.txt'.format(loc=loc)
	# with open(file_path, "a", encoding='UTF-8') as textfile:
	# #print(yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}))
	# 	for name in yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE', 'role':None}):
	# 		print(name.text)
	# 		page_line="{title}\n".format(title=name.text)
	# 		textfile.write(page_line)
	for name in yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE', 'role':None}):
		print(name.text)
		page_line="{title}\n".format(title=name.text)
		textfile.write(page_line)	

	current_page += 10
# for address in yelp_soup.findAll('span',{'class':'lemon--span__373c0__3997G raw__373c0__3rcx7'}):
# 	print(address.text)

	# 		textfile.write(page_line)
	for name in yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE', 'role':None}):
		print(name.text)







# print(yelp_r.status_code) #200

# yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

# print(yelp_soup.prettify())

# print(yelp_soup.findAll('a'))

# for link in yelp_soup.findAll('a', {'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE', 'role': None}):
# 	print(link)
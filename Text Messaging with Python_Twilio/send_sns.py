import requests
import xml.dom.minidom

username = '<your_account_sid>' #account_sid
password = '<your_Auth_token>' #auth_token
account_sid = username

number_to_text = '<your_number_to_text>'
twilio_number = '<your_twilio_number>'

message_body = 'Hi there, this is my message!'

def xml_pretty(xml_string):
	import xml.dom.minidom
	xml = xml.dom.minidom.parseString(xml_string)
	pretty_xml_ = xml.toprettyxml()
	print(pretty_xml_)

base_url = 'https://api.twilio.com/2010-04-01/Accounts'
message_url = base_url + '/' + account_sid + '/Messages'
auth_cred = (username, password)

# 1 send SMS to the phone number
post_data = {
	"From": twilio_number,
	"To": number_to_text,
	"Body": message_body,
	#"MediaUrl": "" #img,
}

#r = requests.post(message_url, data=post_data, auth=auth_cred)
# print(r.status_code)
# xml_pretty(r.text)


# 2 use the Sid to look up message infor

message_url_ind = message_url + "/<Change to Sid you send in step 1>"

get_r = requests.get(message_url_ind, auth=auth_cred)
print(get_r.status_code)
xml_pretty(get_r.text)

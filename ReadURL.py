import  requests
import validators # Check if a string is a valid URL or not
from requests.exceptions import Timeout #the time it will wait on a response once your client has established a connection

URL=input("Hello, Enter your link:")
valid=validators.url(URL)

while valid!=True:
    print("You entered invalid Link(URL)!! ")
    url=input("Enter the Link(URl) again: ")
    valid = validators.url(url)
    URL=url
else:

    print("The Link(Url) is valid")
    g=requests.get(URL)
    print(g.text)


try:
    response = requests.get(URL, timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')


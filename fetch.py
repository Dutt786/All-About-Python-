import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
url = 'http://www.asfaa.org/members.php?id=1'
url='http://www.asfaa.org/members.php?id=5'
parsed = urlparse.urlparse(url)

print("This is Prameter Id=",parse_qs(parsed.query)['id'])
#print("This is an http Get request of User")
url_parts = list(urlparse.urlparse(url))
#print(url_parts)
query = dict(urlparse.parse_qsl(url_parts[4]))
url_parts[4] = urlencode(query)
print("This is an url entered by user =",(urlparse.urlunparse(url_parts)))




try:
    import urlparse
    from urllib import urlencode
except: 
    import urllib.parse as urlparse
    from urllib.parse import urlencode

url = "https://physlab.lums.edu.pk/api.php?action=login&lgname=user&lgpassword=password"
#params = {'lang':'en','tag':'python'}

url_parts = list(urlparse.urlparse(url))
query = dict(urlparse.parse_qsl(url_parts[4]))
#query.update(params)

url_parts[4] = urlencode(query)

print(urlparse.urlunparse(url_parts))

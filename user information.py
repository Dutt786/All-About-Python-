import urllib2
response = urllib2.urlopen('https://www.pythonforbeginners.com/')
print response.info()
print(response)
html = response.read()
# do something
response.close()  # best practice to close the file

#Note: you can also use an URL starting with "ftp:", "file:", etc.).

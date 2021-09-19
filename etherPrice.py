# In using-http.py

import cgi
import http.client
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        parseFile = open("parseOutput.txt", "a")
        parseFile.write("Data: " + data + '\n')
        if data[0] == '$':
            print("Ether Price: " + data)
        parseFile.close()

parser = MyHTMLParser()

server = 'etherscan.io'
url = '/'
conn = http.client.HTTPSConnection(server)
conn.request('GET', url)
response = conn.getresponse()
content_type = response.headers.get('Content-Type')
_, params = cgi.parse_header(content_type)
encoding = params.get('charset')
data = response.read()
text = data.decode(encoding)

print(f'Response returned: {response.status} ({response.reason})')
oFile = open("output.txt", "r+")
oFile.write(text)
parser.feed(text)
oFile.close()

import requests

r = requests.get('https://api.crossref.org/works?query=%22artificial%20photosynthesis%22&rows=1000')
r.status_code

r.headers['content-type']

'application/json; charset=utf8'

r.status_code

r.encoding

'utf-8'

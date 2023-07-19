#Connect to the cluster
import redshift_connector
import requests

r = requests.get('', auth=('user', 'pass'))
r.status_code

conn = redshift_connector.connect(
host='data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com',
     database='data-engineer-database',
     port=5439,
     user='julianaherrera38_coderhouse',
     password='0fGD9NH8aY'
  )
  
# Create a Cursor object
cursor = conn.cursor()

# Query a table using the Cursor
cursor.execute("select * from book")
                
#Retrieve the query result set
result: tuple = cursor.fetchall()
print(result)
(['One Hundred Years of Solitude', 'Gabriel García Márquez'], ['A Brief History of Time', 'Stephen Hawking'])
                





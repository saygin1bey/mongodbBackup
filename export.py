import pymongo
token = "YOUR CONNECT TOKEN"
try:
    client = pymongo.MongoClient(token,
                                 tls=True,
                                 tlsAllowInvalidCertificates=True)
    db = client['DATABASE']
    col = db['COL']
    print("SUCCES")
except Exception as e:
    print("ERROR: ",e)
    client.close()

data = col.find()
file = open("name.txt","w")

for i in data:
    file.write(str(i))
    file.write("\n")

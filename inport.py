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

file = open("data.txt","r")
data = []
for i in file:
    data.append(i)

bigData = {}
counter = 0
for i in data:
    set = i.split(",")
    set[0] = set[0].strip("{")
    set[-1] = set[-1].strip("}")
    for j in set:
        data2 = j.split(": ")
        try:
            d1 = data2[1].split("'")
            k1 = data2[0].split("'")
            a = {k1[1]:d1[1]}
        except:
            pass
        bigData.update(a)
    col.insert_one(bigData)
    #print(bigData)
    bigData = {}
    counter += 1
    print("Data Added")
print("Amount of Data Added: ",counter)
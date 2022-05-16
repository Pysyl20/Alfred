from datetime import date, datetime
import random
import string
import json

oLettre = []
lettre = string.ascii_letters + string.digits

for l in lettre:
    oLettre.append(l)

result = []
count = 0
listKey = []
olistKey = []


def generateKey(site, indentifiant):
    randomKey = ""
    for loop in range(26):
        randomKey += random.choice(oLettre)
    newKey = {'name': site, 'identifiant': indentifiant, 'key': randomKey, 'datecreate': str(datetime.now())}
    return newKey


def saveKey(newKey):
    data = []
    with open('key.json') as json_data:
        data_dict = json.load(json_data)
    for d in data_dict:
        data.append(d)
    data.append(newKey)
    writenewFile = open('key.json', "w")

    json.dump(data, writenewFile)
    writenewFile.close()
    return True




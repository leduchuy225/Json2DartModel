import json


data = open('json.txt', "r").read()

jsonLoad = json.loads(data)

for key in jsonLoad:
  try:
    jsonLoad[key] = json.loads(jsonLoad[key])
  except:
    jsonLoad[key] = jsonLoad[key]
    continue


with open("sample.json", "w") as outfile:
  outfile.write(json.dumps(jsonLoad))

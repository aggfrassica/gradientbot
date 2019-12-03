import json

# legge il file dalla cartella
with open('gradeint.json') as json_file:
    data = json.load(json_file)
print(data["Purple"])
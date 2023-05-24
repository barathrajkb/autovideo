import requests

prompt = input("Enter the prompt: ")
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': 'Write a short narrative script for ' + prompt,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
fileName = prompt.replace(" ", "_").lower()[0:10]
with open(fileName + ".txt", "w") as file:
    file.write(r.json()["output"])
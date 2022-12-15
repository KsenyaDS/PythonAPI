import requests
response = requests.get("https://playground.learnqa.ru/api/hello", params={'name':'Ксения'})
parsed_response_text = response.json()
print(parsed_response_text['answer'])
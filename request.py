from requests import post

url = "http://127.0.0.1:8000/predict_value/"
json_data = {"inputs": [[0.5, 0.5, 0.5], [0.6, 0.6, 0.6]]}
response = post(url=url, json=json_data)

print("Status Code:", response.status_code)
print("Response Content:", response.text)  # Print raw response text

try:
    json_res = response.json()
    print("JSON Response:", json_res)
except Exception as e:
    print("Failed to decode JSON:", str(e))

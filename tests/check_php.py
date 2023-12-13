import requests

response = requests.get("http://localhost")

if "Hello Tony" not in response.text:
    raise ValueError("We didn't see the right output from the php script")
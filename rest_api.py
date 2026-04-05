import requests
import json

#LM Studio API endpoint
API_URL = "http://127.0.0.1:1234/api/v1/chat"


Model_name = "liquid/lfm2.5-1.2b"
SYSTEM_PROMPT = "You answer only straight"
USER_INPUT = "What is the capital of France?"

# Prepare the payload for the API request
payload = {
    "model": Model_name,
    "system_prompt": SYSTEM_PROMPT,
    "input": USER_INPUT
}

headers={
    "Content-Type": "application/json"
}

response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    result = response.json()
    print("---LLM Studio Response---")
    print(result)
    if "output" in result:
        print("\nModel Output:")
        print(result["output"])
else:    print(f"Request failed with status code: {response.status_code}")
print
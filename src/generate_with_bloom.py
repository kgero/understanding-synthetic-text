import json
import requests

with open(".env", "r") as f:
	for line in f:
		if line.split("=")[0] == "HF_API_KEY":
			API_TOKEN = line.strip("\n").split("=")[1]

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"

# docs: https://huggingface.co/docs/api-inference/detailed_parameters#text-generation-task

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query({
	"inputs": "Write a three sentence story about a teenager and a sweatshirt.\n\nJamie's favorite sweatshirt was purple with bright yellow cow spots. She loved this sweatshirt so much she wore it every day for a year. Then, her little brother stole the sweatshirt and she no longer thought it was cool.\n\nWrite a three sentence story about a toddler and a toy rabbit.\n\n",
	"parameters": {
		"do_sample": True,
		"temperature": 1,
		"max_new_tokens": 100
		},
	"options": {
		"wait_for_model": True
		}
	})
print(data)


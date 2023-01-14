import os
import openai
import json
import csv
import time

with open(".env", "r") as f:
	for line in f:
		if line.split("=")[0] == "OPENAI_API_KEY":
			openai.api_key = line.strip("\n").split("=")[1]

prompts = {
	"bland": "Write a three sentence story about a toddler and a toy rabbit.",
	"saucy": "Write a three sentence story about a CEO and a scandal."
	}

prompts = {
	"happy": "Write a happy three sentence story about a toddler and a toy rabbit.",
	"truck": "Write a three sentence story about a toddler and a toy truck."
	}

prompts = {
	"exciting": "Write a funny three sentence story about a toddler and a toy rabbit.",
	"standard": "Write a three sentence story about a toddler and a toy rabbit."
	}

prompts = {
	"girl": "Write a three sentence story about a little girl and a toy rabbit.",
	"boy": "Write a three sentence story about a little boy and a toy rabbit."
	}

data = []

uid = "funny"

t = 1 		# temperature
m = 256 	# max tokens to generate
n = 100 	# number responses per request
c = 1 		# number requests to make

for key, prompt in prompts.items():

	print(f"{key}: {prompt}")

	for i in range(c):

		response = openai.Completion.create(
			model="text-davinci-002", 
			prompt=prompt, 
			temperature=t, 
			max_tokens=m,
			n=n,
			logprobs=1)

		for r in response["choices"]:
			logprobs = r["logprobs"]["token_logprobs"]
			data.append([prompt, r["text"].strip("\n"), t, m, sum(logprobs)/len(logprobs)])

		with open(f"data/{uid}_r{c}_{key}.json", "w") as f:
			f.write(json.dumps(response))

		time.sleep(60)

with open(f"data/{uid}_completions.csv", "w") as f:
	writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
	for row in data:
	    writer.writerow(row)

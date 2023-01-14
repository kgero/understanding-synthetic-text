import os
import openai
import json
import csv
import time

with open(".env", "r") as f:
	for line in f:
		if line.split("=")[0] == "OPENAI_API_KEY":
			openai.api_key = line.strip("\n").split("=")[1]

t = 1 		# temperature
m = 4   	# max tokens to generate
n = 2   	# number responses per request

prompt = "As I sat at the cafe I"

response = openai.Completion.create(
			model="text-davinci-002", 
			prompt=prompt, 
			temperature=t, 
			max_tokens=m,
			n=n,
			logprobs=3)

print(response)
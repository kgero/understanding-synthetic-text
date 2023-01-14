import os
import openai
import json
import csv
import time

with open(".env", "r") as f:
	for line in f:
		if line.split("=")[0] == "OPENAI_API_KEY":
			openai.api_key = line.strip("\n").split("=")[1]

t = .5 		# temperature
m = 6   	# max tokens to generate
n = 1   	# number responses per request
l = 5		# number of logprobs to return

# prompt = "As I sat at the cafe I"

# documentation on lobprobs: https://beta.openai.com/docs/api-reference/completions/create#completions/create-logprobs

def get_gpt_response(prompt):

	response = openai.Completion.create(
				model="text-davinci-002", 
				prompt=prompt, 
				temperature=t, 
				max_tokens=m,
				n=n,
				logprobs=l)

	return response
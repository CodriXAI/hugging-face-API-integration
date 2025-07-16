from huggingface_hub import InferenceClient 
from machineBasic import machineWrite
from dotenv import load_dotenv
import os
import sys

#Load variables from .env
load_dotenv()

#Token imported from HuggingFace
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

#I check whether the Token exists or not to use it
if not HF_TOKEN:
    print("Error: Token not found to use the program")
    sys.exit(1)
else:
    print("The Token has been loaded successfully")

# Client with model Llama 3:
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN
)
while(True):
    # User message
    prompt = input("YOU: ")

    # We send the message to the model
    answer = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256
    )

    # Show answer
    msg = "BOT:" + f"{answer.choices[0].message.content}"
    machineWrite(msg)


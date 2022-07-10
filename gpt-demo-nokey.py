import os
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = ""

conversation = ""

while True:
    conversation = input("==> ")
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=conversation,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    print(response["choices"][0]["text"].replace("\n",""))

    # Write your code here :-)

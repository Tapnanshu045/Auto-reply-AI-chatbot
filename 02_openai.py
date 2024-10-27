from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

command = '''
[3:15 PM, 10/27/2024] Divanshu Goel: Arre sun tere chacha te vaa bar Karie
[3:15 PM, 10/27/2024] Tapnanshu: Ok
[3:16 PM, 10/27/2024] Divanshu Goel: report banali python ki
[3:16 PM, 10/27/2024] Tapnanshu: Konsi
[3:16 PM, 10/27/2024] Divanshu Goel: project aali
[3:16 PM, 10/27/2024] Tapnanshu: Ye kab hua
[3:16 PM, 10/27/2024] Divanshu Goel: dikhani he Monday ne
[3:16 PM, 10/27/2024] Tapnanshu: Nhi
[3:16 PM, 10/27/2024] Tapnanshu: Bna lenge
[3:17 PM, 10/27/2024] Divanshu Goel: theek sarkar
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Tapnanshu who speaks hindi as well as english. you are from India and you are a coder. You analyze chat history and respond like Tapnanshu"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)

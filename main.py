from groq import Groq

client = Groq(api_key='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')

while(True):
    answer = input("Do you you need help? ")

    if(answer == "Yes"):
        print("Haha, I'm not helping you!")
        break
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
          {
            "role": "user",
            "content": answer
          }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        stream=False,
        stop=None
    )

    print(completion.choices[0].message.content)
    print()

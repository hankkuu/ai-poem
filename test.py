import openai
from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "프랑스의 수도는 어디인가요?"}
    ]
)

print(response.choices[0].message.content)
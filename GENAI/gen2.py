from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

# ahiya aapde OpenAI no client banaviye chie
# api_key ma aapdi purchased / generated API key store hoy che
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
    )

# aa "message" list che je conversation history store kare che
# ChatGPT ne old messages yaad rahe ena mate use thay che
message = [
    {
        # "system" role AI ne instruction aape che
        # etle AI nu behavior set kare che
        "role": "system",

        # AI kem behave karse eni instruction
        "content": "you are a helpful assistant."
    }
]

# aa loop 3 vakhat user pase input leshe
for i in range(3):

    # user pase thi message/input levu
    user_input = input("user: ")

    # user no message message list ma add karvo
    # "user" role etle aa message user taraf thi aavyo che
    #and aana lidhe ai model ,user na according banto
    message.append({
        "role": "user",
        "content": user_input
    })

    # OpenAI model ne call kariye chie
    response = client.chat.completions.create(

        # kai AI model use karvo e
        model="gpt-3.5-turbo",

        # pura conversation messages mokliye chie
        # jethi AI ne context yaad rahe
        messages=message
    )

    # AI taraf thi aavelo reply extract kariye chie
    assistant_response = response.choices[0].message.content

    # terminal ma AI no response print karvo
    print("Assistant:", assistant_response)

    # AI no response pan message history ma add kariye chie
    # jethi next prompt ma AI ne previous answer yaad rahe
    message.append({
        "role": "assistant",
        "content": assistant_response
    })
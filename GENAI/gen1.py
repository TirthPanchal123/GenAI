from openai import OpenAI

api_key ="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"

client = OpenAI(
    api_key=api_key
)

response = client.responses.create(
    model="gpt-3.5-turbo",
    instructions = "act as my helpful assistant",
    input=input("Enter your question:"),
)

print(response.output_text)
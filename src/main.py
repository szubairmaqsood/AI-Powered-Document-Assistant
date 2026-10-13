
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from src.config import OPENROUTER_API_KEY, OPENROUTER_MODEL


def generate_response(prompt, temperature):
    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=temperature
    )

    response = llm.invoke(prompt)
    return response


prompt = "Write a short, creative paragraph about artificial intelligence."

for temperature in [0.0, 0.25, 0.5, 0.75, 1.0]:
    response = generate_response(prompt, temperature)

    print(f"\nTemperature: {temperature}")
    print(response.content)
    print("Token Usage:", response.usage_metadata)


llm = ChatOpenAI(
    model=OPENROUTER_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

chat_history = []

query = "Hi! Give me a recipe to make a Margherita pizza from scratch."

chat_history.append(HumanMessage(content=query))
response = llm.invoke(chat_history)
chat_history.append(AIMessage(content=response.content))

print("\nAI Response:")
print(response.content)

print("\nChat History:")
for message in chat_history:
    print(message)
    print()

print("Token Usage:")
print(response.usage_metadata)

token_query = "Now please help me find the nearest supermarket from where I can buy the ingredients."

chat_history.append(HumanMessage(content=token_query))
token_response = llm.invoke(chat_history)
chat_history.append(AIMessage(content=token_response.content))

print("\nFollow-up Response:")
print(token_response.content)

print("\nFollow-up Token Usage:")
print(token_response.usage_metadata)

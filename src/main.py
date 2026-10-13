
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from src.config import OPENROUTER_API_KEY, OPENROUTER_MODEL


def get_response(messages, max_output_tokens):
    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
        max_tokens=max_output_tokens
    )

    return llm.invoke(messages)


chat_history = []

query = "Explain XGBoost and Random Forest with real-life use cases."

for max_output_tokens in [100, 300, 700]:
    print(f"\n--- Max Output Tokens: {max_output_tokens} ---")

    chat_history.append(HumanMessage(content=query))

    try:
        response = get_response(chat_history, max_output_tokens)
        print(response.content)
        print("Token Usage:", response.usage_metadata)

        chat_history.append(AIMessage(content=response.content))

    except Exception as e:
        chat_history.pop()
        print(f"Skipped due to error: {e}")

print("\n--- Chat History ---")
for message in chat_history:
    print(f"{type(message).__name__}: {message.content}\n")

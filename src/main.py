
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from src.config import OPENROUTER_API_KEY, OPENROUTER_MODEL


def get_response(prompt, top_k):
    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
        extra_body={"top_k": top_k}
    )

    return llm.invoke([HumanMessage(content=prompt)])


prompt = "Explain XGBoost and Random Forest with real-life use cases."

for k in [1, 4, 16, 32, 40]:
    print(f"\n--- Top K: {k} ---")

    try:
        response = get_response(prompt, k)
        print(response.content)
        print("\nToken Usage:", response.usage_metadata)

    except Exception as e:
        print(f"Skipped due to error: {e}")

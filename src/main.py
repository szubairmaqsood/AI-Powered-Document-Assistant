
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from src.config import OPENROUTER_API_KEY, OPENROUTER_MODEL


def get_response(prompt, candidate_count=1):
    if candidate_count != 1:
        raise ValueError(
            "This experiment currently supports candidate_count=1 only."
        )

    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )

    return llm.invoke([HumanMessage(content=prompt)])


prompt = "Explain XGBoost and Random Forest with real-life use cases."

response = get_response(prompt, candidate_count=1)

print("Candidate Count: 1")
print(response.content)
print("\nToken Usage:")
print(response.usage_metadata)

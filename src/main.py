from langchain_openai import ChatOpenAI
from src.config import OPENROUTER_API_KEY, OPENROUTER_MODEL

llm = ChatOpenAI(
    model=OPENROUTER_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
)

prompt = "Explain Retrieval-Augmented Generation (RAG) in simple terms."
response = llm.invoke(prompt)

print("Response from the language model:")
print(response.content)
import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root.
load_dotenv()

# Read the OpenRouter API key from the environment.
# This key authenticates our requests to OpenRouter.
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Read the model name from the environment.
# This allows us to change models without editing main.py.
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

# Stop the application early if required configuration is missing.
if not OPENROUTER_API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY is missing. Please check your .env file."
    )

if not OPENROUTER_MODEL:
    raise ValueError(
        "OPENROUTER_MODEL is missing. Please check your .env file."
    )
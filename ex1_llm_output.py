
import os
from openai import AzureOpenAI

# Load environment variables (use a .env file in development)
from dotenv import load_dotenv
load_dotenv()

# Get config from environment variables
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

# Initialize Azure OpenAI client
API_VERSION = os.getenv("API_VERSION", "2024-12-01-preview")
client = AzureOpenAI(
    azure_endpoint=ENDPOINT_URL,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=API_VERSION
)

def explain_llm(user_input):
    print(f"\n--- LLM Logic Demo ---")
    print(f"Input: \"{user_input}\"")
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a demo assistant explaining how LLMs work. "
                                          "When given a sentence fragment, provide 3 likely next words "
                                          "and a brief explanation of why they are statistically probable."},
            {"role": "user", "content": f"Complete this: {user_input}"}
        ]
    )
    print(f"LLM Response:\n{response.choices[0].message.content}")

if __name__ == "__main__":
    # Test the 'Autocomplete' nature
    explain_llm("The weather today is surprisingly")
    #explain_llm("The capital of France is")

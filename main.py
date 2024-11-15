import os
from dotenv import load_dotenv
import getpass
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Check if the OPENAI_API_KEY is already set in the environment
if not os.getenv("OPENAI_API_KEY"):
    # Prompt the user for the API key if not set
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")

# Initialize the model with the environment key
model = ChatOpenAI(model="gpt-4o-mini")


from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)
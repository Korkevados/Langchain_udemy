from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    print(os.environ['COOL_API_KEY'])

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv(
        dotenv_path=".env"
)


def get_embeddings():


    embeddings = GoogleGenerativeAIEmbeddings(

        model="models/gemini-embedding-001"

    )


    return embeddings
from hindsight_client import Hindsight
from dotenv import load_dotenv
import os

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

print("Connected Successfully!")
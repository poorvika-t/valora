from hindsight_client import Hindsight
from dotenv import load_dotenv
import os

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "echoproof"

try:
    client.create_bank(
        bank_id=BANK_ID,
        name="EchoProof Memory"
    )
except:
    pass

client.retain(
    bank_id=BANK_ID,
    content="Investor rejected startup because pricing was unclear."
)

print("Memory Stored!")
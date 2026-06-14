from hindsight_client import Hindsight
from dotenv import load_dotenv
import os

load_dotenv()

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

memories = [

# Pricing (10)
"Meeting Date: 2026-05-01 | Investor: Accel | Outcome: Rejected | Reason: Pricing model was unclear.",
"Meeting Date: 2026-05-03 | Investor: Peak XV | Outcome: Rejected | Reason: Enterprise pricing strategy was missing.",
"Meeting Date: 2026-05-05 | Investor: Nexus Venture Partners | Outcome: Rejected | Reason: Revenue projections did not match pricing assumptions.",
"Meeting Date: 2026-05-08 | Investor: Blume Ventures | Outcome: Rejected | Reason: Customer willingness to pay was unproven.",
"Meeting Date: 2026-05-10 | Investor: Lightspeed | Outcome: Rejected | Reason: Pricing tiers were confusing.",
"Meeting Date: 2026-05-12 | Investor: Matrix Partners | Outcome: Rejected | Reason: Monetization strategy lacked clarity.",
"Meeting Date: 2026-05-14 | Investor: Kalaari Capital | Outcome: Rejected | Reason: Profit margins appeared too low.",
"Meeting Date: 2026-05-17 | Investor: Y Combinator | Outcome: Rejected | Reason: Subscription pricing lacked validation.",
"Meeting Date: 2026-05-19 | Investor: Sequoia | Outcome: Rejected | Reason: Pricing differentiation was weak.",
"Meeting Date: 2026-05-21 | Investor: Elevation Capital | Outcome: Rejected | Reason: Revenue model seemed unsustainable.",

# Traction (10)
"Meeting Date: 2026-05-22 | Investor: Accel | Outcome: Rejected | Reason: Monthly active users were too low.",
"Meeting Date: 2026-05-23 | Investor: Peak XV | Outcome: Rejected | Reason: Growth metrics lacked consistency.",
"Meeting Date: 2026-05-24 | Investor: Lightspeed | Outcome: Rejected | Reason: Retention data was unavailable.",
"Meeting Date: 2026-05-25 | Investor: Matrix Partners | Outcome: Rejected | Reason: Customer acquisition numbers were weak.",
"Meeting Date: 2026-05-26 | Investor: Sequoia | Outcome: Rejected | Reason: Startup lacked market traction.",
"Meeting Date: 2026-05-27 | Investor: Blume Ventures | Outcome: Rejected | Reason: User engagement metrics were poor.",
"Meeting Date: 2026-05-28 | Investor: Kalaari Capital | Outcome: Rejected | Reason: Revenue growth was stagnant.",
"Meeting Date: 2026-05-29 | Investor: Y Combinator | Outcome: Rejected | Reason: Product adoption was slower than expected.",
"Meeting Date: 2026-05-30 | Investor: Nexus Venture Partners | Outcome: Rejected | Reason: User growth curve was flat.",
"Meeting Date: 2026-05-31 | Investor: Elevation Capital | Outcome: Rejected | Reason: Not enough paying customers.",

# Competition (10)
"Meeting Date: 2026-06-01 | Investor: Accel | Outcome: Rejected | Reason: Strong competitors already dominate the market.",
"Meeting Date: 2026-06-02 | Investor: Peak XV | Outcome: Rejected | Reason: Startup lacked clear differentiation.",
"Meeting Date: 2026-06-03 | Investor: Lightspeed | Outcome: Rejected | Reason: Competitive moat was unclear.",
"Meeting Date: 2026-06-04 | Investor: Matrix Partners | Outcome: Rejected | Reason: Similar products already exist.",
"Meeting Date: 2026-06-05 | Investor: Sequoia | Outcome: Rejected | Reason: Defensibility strategy was weak.",
"Meeting Date: 2026-06-06 | Investor: Blume Ventures | Outcome: Rejected | Reason: Competitors had stronger partnerships.",
"Meeting Date: 2026-06-07 | Investor: Kalaari Capital | Outcome: Rejected | Reason: Product advantages were not obvious.",
"Meeting Date: 2026-06-08 | Investor: Y Combinator | Outcome: Rejected | Reason: Market positioning was unclear.",
"Meeting Date: 2026-06-09 | Investor: Nexus Venture Partners | Outcome: Rejected | Reason: Brand recognition was low.",
"Meeting Date: 2026-06-10 | Investor: Elevation Capital | Outcome: Rejected | Reason: Existing players had greater resources.",

# Market Size (10)
"Meeting Date: 2026-06-11 | Investor: Accel | Outcome: Rejected | Reason: Total addressable market appeared small.",
"Meeting Date: 2026-06-12 | Investor: Peak XV | Outcome: Rejected | Reason: Expansion opportunities were unclear.",
"Meeting Date: 2026-06-13 | Investor: Lightspeed | Outcome: Rejected | Reason: Startup targeted a niche audience.",
"Meeting Date: 2026-06-14 | Investor: Matrix Partners | Outcome: Rejected | Reason: Global scalability was uncertain.",
"Meeting Date: 2026-06-15 | Investor: Sequoia | Outcome: Rejected | Reason: Growth potential seemed limited.",
"Meeting Date: 2026-06-16 | Investor: Blume Ventures | Outcome: Rejected | Reason: Market demand was not validated.",
"Meeting Date: 2026-06-17 | Investor: Kalaari Capital | Outcome: Rejected | Reason: Customer segment was too narrow.",
"Meeting Date: 2026-06-18 | Investor: Y Combinator | Outcome: Rejected | Reason: Long-term market opportunity was unclear.",
"Meeting Date: 2026-06-19 | Investor: Nexus Venture Partners | Outcome: Rejected | Reason: Geographic expansion strategy was weak.",
"Meeting Date: 2026-06-20 | Investor: Elevation Capital | Outcome: Rejected | Reason: TAM estimates lacked evidence.",

# Team (10)
"Meeting Date: 2026-06-21 | Investor: Accel | Outcome: Rejected | Reason: Founding team lacked industry experience.",
"Meeting Date: 2026-06-22 | Investor: Peak XV | Outcome: Rejected | Reason: Hiring roadmap was unclear.",
"Meeting Date: 2026-06-23 | Investor: Lightspeed | Outcome: Rejected | Reason: Leadership team was incomplete.",
"Meeting Date: 2026-06-24 | Investor: Matrix Partners | Outcome: Rejected | Reason: Technical expertise was insufficient.",
"Meeting Date: 2026-06-25 | Investor: Sequoia | Outcome: Rejected | Reason: Execution timeline seemed unrealistic.",
"Meeting Date: 2026-06-26 | Investor: Blume Ventures | Outcome: Rejected | Reason: Advisory support was lacking.",
"Meeting Date: 2026-06-27 | Investor: Kalaari Capital | Outcome: Rejected | Reason: Team structure was immature.",
"Meeting Date: 2026-06-28 | Investor: Y Combinator | Outcome: Rejected | Reason: Key roles remained unfilled.",
"Meeting Date: 2026-06-29 | Investor: Nexus Venture Partners | Outcome: Rejected | Reason: Operational experience was limited.",
"Meeting Date: 2026-06-30 | Investor: Elevation Capital | Outcome: Rejected | Reason: Scaling capability was uncertain."
]

for memory in memories:
    client.retain(
        bank_id="echoproof",
        content=memory
    )

print(f"{len(memories)} memories stored successfully!")
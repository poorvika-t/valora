from hindsight_client import Hindsight
from dotenv import load_dotenv
import os

load_dotenv()

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

memories = [

"""
Investor: Sequoia
Startup: FoodSense AI
Sector: FoodTech SaaS
Stage: Seed
MRR: $18000
Customers: 50 restaurants
Outcome: Rejected
Reason: Customer retention dropped below 40%.
Investor Concern: Weak long-term engagement.
Suggested Improvement: Improve retention and annual contracts.
""",

"""
Investor: Accel
Startup: FinPilot
Sector: FinTech
Stage: Pre-Seed
MRR: $8000
Customers: 120 users
Outcome: Rejected
Reason: Pricing model unclear.
Investor Concern: Revenue projections did not match assumptions.
Suggested Improvement: Simplify pricing strategy.
""",

"""
Investor: Peak XV
Startup: HealthTrack
Sector: HealthTech
Stage: Seed
MRR: $22000
Customers: 15 hospitals
Outcome: Accepted
Reason: Strong traction and measurable ROI.
Investor Observation: Clear market demand.
Suggested Improvement: Geographic expansion.
""",

"""
Investor: Lightspeed
Startup: TutorMind
Sector: EdTech
Stage: Seed
MRR: $14000
Customers: 500 students
Outcome: Rejected
Reason: High churn rate.
Investor Concern: Students stopped using after exams.
Suggested Improvement: Increase long-term engagement.
""",

"""
Investor: Matrix Partners
Startup: GreenGrid
Sector: ClimateTech
Stage: Seed
MRR: $26000
Customers: 22 factories
Outcome: Accepted
Reason: Strong sustainability ROI.
Investor Observation: Clear enterprise demand.
Suggested Improvement: Expand into manufacturing sector.
""",

"""
Investor: Sequoia
Startup: LegalFlow
Sector: LegalTech
Stage: Pre-Seed
MRR: $5000
Customers: 30 law firms
Outcome: Rejected
Reason: Market too small.
Investor Concern: Limited TAM.
Suggested Improvement: Expand product offering.
""",

"""
Investor: Accel
Startup: FleetIQ
Sector: Logistics
Stage: Seed
MRR: $32000
Customers: 80 businesses
Outcome: Accepted
Reason: Revenue growth 18% monthly.
Investor Observation: Strong operational metrics.
Suggested Improvement: Expand nationally.
""",

"""
Investor: Peak XV
Startup: ShopBrain
Sector: Retail AI
Stage: Seed
MRR: $12000
Customers: 40 stores
Outcome: Rejected
Reason: Similar competitors existed.
Investor Concern: Weak differentiation.
Suggested Improvement: Build unique AI features.
""",

"""
Investor: Lightspeed
Startup: MedConnect
Sector: HealthTech
Stage: Seed
MRR: $28000
Customers: 12 hospitals
Outcome: Accepted
Reason: Clear cost reduction metrics.
Investor Observation: Hospitals reported 30% savings.
Suggested Improvement: Increase integrations.
""",

"""
Investor: Kalaari Capital
Startup: CropVision
Sector: AgriTech
Stage: Seed
MRR: $9000
Customers: 200 farmers
Outcome: Rejected
Reason: Slow user growth.
Investor Concern: Adoption too slow.
Suggested Improvement: Improve distribution channels.
""",

"""
Investor: Nexus Venture Partners
Startup: HireFlow
Sector: HRTech
Stage: Seed
MRR: $24000
Customers: 100 companies
Outcome: Accepted
Reason: Strong recurring revenue.
Investor Observation: Low churn.
Suggested Improvement: Enterprise expansion.
""",

"""
Investor: Blume Ventures
Startup: SafePay
Sector: FinTech
Stage: Pre-Seed
MRR: $7000
Customers: 300 users
Outcome: Rejected
Reason: Regulatory uncertainty.
Investor Concern: Compliance risk.
Suggested Improvement: Strengthen legal framework.
""",

"""
Investor: Sequoia
Startup: TravelLens
Sector: TravelTech
Stage: Seed
MRR: $19000
Customers: 400 travelers
Outcome: Rejected
Reason: Seasonal demand.
Investor Concern: Revenue fluctuations.
Suggested Improvement: Diversify customer base.
""",

"""
Investor: Accel
Startup: DevMate
Sector: Developer Tools
Stage: Seed
MRR: $34000
Customers: 600 developers
Outcome: Accepted
Reason: Strong developer retention.
Investor Observation: Organic growth.
Suggested Improvement: Expand enterprise offering.
""",

"""
Investor: Peak XV
Startup: BuildTrack
Sector: ConstructionTech
Stage: Seed
MRR: $21000
Customers: 45 builders
Outcome: Accepted
Reason: Clear productivity gains.
Investor Observation: Strong customer testimonials.
Suggested Improvement: Expand into infrastructure projects.
""",

"""
Investor: Lightspeed
Startup: VoiceLearn
Sector: EdTech
Stage: Seed
MRR: $11000
Customers: 700 students
Outcome: Rejected
Reason: Weak monetization.
Investor Concern: Revenue per user too low.
Suggested Improvement: Premium subscription plans.
""",

"""
Investor: Matrix Partners
Startup: CarbonMap
Sector: ClimateTech
Stage: Seed
MRR: $17000
Customers: 50 enterprises
Outcome: Accepted
Reason: Strong ESG demand.
Investor Observation: Regulatory tailwinds.
Suggested Improvement: Global expansion.
""",

"""
Investor: Kalaari Capital
Startup: FitTrack AI
Sector: HealthTech
Stage: Pre-Seed
MRR: $6000
Customers: 1000 users
Outcome: Rejected
Reason: Low paid conversions.
Investor Concern: Weak monetization.
Suggested Improvement: Better premium features.
""",

"""
Investor: Nexus Venture Partners
Startup: SupplySense
Sector: Supply Chain
Stage: Seed
MRR: $30000
Customers: 70 companies
Outcome: Accepted
Reason: Reduced logistics costs by 18%.
Investor Observation: Strong customer retention.
Suggested Improvement: Expand internationally.
""",

"""
Investor: Blume Ventures
Startup: AutoQuote
Sector: InsurTech
Stage: Seed
MRR: $15000
Customers: 200 brokers
Outcome: Rejected
Reason: Sales cycle too long.
Investor Concern: Slow revenue growth.
Suggested Improvement: Shorten onboarding process.
"""
]

for memory in memories:
    client.retain(
        bank_id="echoproof",
        content=memory
    )

print(f"Uploaded {len(memories)} rich memories successfully!")
client.close()
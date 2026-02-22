from knowledge_store import init_db, add_article

init_db()

add_article(
    "What is SIP?",
    "A Systematic Investment Plan (SIP) allows you to invest a fixed amount regularly in mutual funds. It helps in rupee cost averaging and disciplined investing."
)

add_article(
    "Emergency Fund",
    "An emergency fund should cover 3 to 6 months of expenses and be kept in liquid instruments like savings accounts or liquid funds."
)

add_article(
    "ExpressVPN Setup",
    "To set up ExpressVPN, download the app, sign in, choose a location, and connect. For troubleshooting, restart the app and check your internet connection."
)

print("✅ Articles loaded into SQLite database.")

import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now the environment variables are available throughout your project
LOGGING_ENABLED = os.getenv("LOGGING_ENABLED", "false").lower() == "true"

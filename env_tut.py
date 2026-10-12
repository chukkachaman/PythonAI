import os

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"Using database: {database}")
print(api_key)
 #---------------------------------------------
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')
database = os.environ.get('DATABASE_URL', 'default.db')

print(f"Using database: {database}")

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
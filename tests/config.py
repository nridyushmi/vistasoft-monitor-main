from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROME_DRIVER = "./driver/chromedriver_mac"
    FIREFOX_DRIVER = "./driver/geckodriver"
    HEADLESS_TEST = True  # Run browser tests headless (no UI)

    # Credentials
    USER = os.getenv("USER") or "user"
    PASSWORD = os.getenv("PASSWORD") or "password"
    
    VSM_BASE_URL = "https://vsmonitor.com" 
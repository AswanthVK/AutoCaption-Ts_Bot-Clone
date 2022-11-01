import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1823808722:AAErb2W2txaOmUeA859Qz4pahi8d3wMwfqw")
      API_ID = int(os.environ.get("APP_ID", "663122"))
      API_HASH = os.environ.get("API_HASH", "23dac54b523173b5f83014ae566584bd")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "AswanthVK")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", "662933911")) 
      DB_URL = os.environ.get("DATABASE_URL", "")

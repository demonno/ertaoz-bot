from environs import Env

env = Env()
env.read_env()

BOT_ERTAOZ_TOKEN = env.str("BOT_ERTAOZ_TOKEN")
CORONA_API_ID = env.str("CORONA_API_ID")

IMGFLIP_API_USERNAME = env.str("IMGFLIP_API_USERNAME")
IMGFLIP_API_PASSWORD = env.str("IMGFLIP_API_PASSWORD")

WEATHER_API_ID = env.str("WEATHER_API_ID")

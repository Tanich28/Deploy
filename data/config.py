import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str('1237217182:AAFGbtocD9w_nsfM2cwIdwyO6PYJj8FgVCw')
APP_URL = str('https://tanichbot.herokuapp.com/')
admins = [
    180481708
]
allowed_users = [

]
channels = [-1001521594094]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

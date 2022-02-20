from src.models import User
from src.constants import ADMIN_PASSWORD

admin = User.objects.create(email="aloha@mail.com", password=ADMIN_PASSWORD)

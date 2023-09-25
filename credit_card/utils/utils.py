import os
import uuid

from cryptography.fernet import Fernet


def generate_uuid():
    return str(uuid.uuid4())


fernet = Fernet(os.getenv("CRYPTOGRAPHY_KEY"))

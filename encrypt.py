from cryptography.fernet import Fernet

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    try:
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        generate_key()
        return load_key()

key = load_key()
fernet = Fernet(key)

def encrypt(text: str) -> bytes:
    return fernet.encrypt(text.encode())

def decrypt(token: bytes) -> str:
    return fernet.decrypt(token).decode()

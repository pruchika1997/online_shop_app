from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    # bcrypt only supports up to 72 bytes safely
    if len(password.encode("utf-8")) > 72:
        password = password[:72]
    return pwd_context.hash(password)

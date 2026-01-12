from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "secret123"
hashed = pwd_context.hash(password)
print("Hashed:", hashed)
print("Verify:", pwd_context.verify("secret123", hashed))

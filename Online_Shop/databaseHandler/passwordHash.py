import bcrypt

salt = bcrypt.gensalt(rounds=16)
def hash_password(password):
    return bcrypt.hashpw(password.encode(), salt).decode('UTF-8')

def check_hashed_password(password,hashedPassword):
    return bcrypt.checkpw(password.encode(), hashedPassword.encode())

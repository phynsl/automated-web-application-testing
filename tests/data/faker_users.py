from faker import Faker

fake = Faker()

def generate_user():
    return {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
    }

# This contains a hardcoded password for Snyk to detect

def connect_to_db():
    password = "SuperSecretPassword123!"  # Hardcoded password
    print(f"Connecting to DB with password: {password}")

if __name__ == "__main__":
    connect_to_db()
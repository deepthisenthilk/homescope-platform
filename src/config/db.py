DB_CONFIG = {
    "user": "homescope_user",
    "password": "homescope_pass",
    "host": "localhost",
    "port": "5432",
    "database": "homescope"
}

def get_db_url():
    return (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
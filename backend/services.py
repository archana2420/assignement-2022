import database

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    except:
        print("Could not access database")
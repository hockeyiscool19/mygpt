import firebase_admin
from firebase_admin import credentials
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CRED = credentials.Certificate("postmanServiceAccount.json")
firebase_admin.initialize_app(CRED)


class Firebase:
    def __init__(self):
        self.database_url = DATABASE_URL
        self.cred = CRED

    def load_dict(self, data, path='/', url=DATABASE_URL):
        """
        Load a dictionary to Firebase.
        :param data: Dictionary to load
        :param path: Path to load the dictionary to. Default is root.
        """
        ref = db.reference(path=path, url=url)
        ref.push(data)

    def read_dict(self, path='/', url=DATABASE_URL):
        """
        Load a dictionary to Firebase.
        :param data: Dictionary to load
        :param path: Path to load the dictionary to. Default is root.
        """
        ref = db.reference(path=path, url=url)
        return ref.get()

    def delete_dict(self, path='/', url=DATABASE_URL):
        """
        Load a dictionary to Firebase.
        :param data: Dictionary to load
        :param path: Path to load the dictionary to. Default is root.
        """
        ref = db.reference(path=path, url=url)
        ref.delete()


FIRE = Firebase()

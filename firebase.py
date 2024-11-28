import firebase_admin
from firebase_admin import credentials, firestore

# Inisialisasi Firebase
cred = credentials.Certificate("C:/Users/Acer/Documents/Materi Kuliah Semester 5/Bangkit Academy/Capstone Project/backend-app-seo/capstone-project-443105-firebase-adminsdk-1saun-00614bec8a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user_by_email(email):
    users_ref = db.collection('users')
    query = users_ref.where('email', '==', email).stream()
    for user in query:
        return user.to_dict()
    return None

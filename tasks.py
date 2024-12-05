from celery import Celery
from helper_functions import main_audit_process

# Konfigurasi Celery dengan broker dan backend Redis
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',  # Broker untuk Celery, menggunakan Redis
    backend='redis://localhost:6379/0'  # Hasil dari tugas disimpan di Redis
)

@celery.task(bind=True)
def audit_task(self, url):
    try:
        # Menggunakan fungsi main_audit_process untuk audit SEO
        result = main_audit_process(url)
        return result
    except Exception as exc:
        raise self.retry(exc=exc)

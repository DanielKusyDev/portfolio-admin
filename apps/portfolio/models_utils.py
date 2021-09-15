from uuid import uuid4

from django.db.models import FileField


def get_encoded_file_name(instance: FileField, filename: str) -> str:
    try:
        ext = f".{filename.split('.')[-1]}"
    except KeyError:
        ext = ""
    return f"{uuid4().hex}{ext}"

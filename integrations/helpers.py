from django.core.files.storage import FileSystemStorage
import os
import uuid

def upload_media(request, platform):

    extension = os.path.splitext(str(request.FILES['photo']))[1]
    unique_filename = uuid.uuid4().hex

    if extension.lower() in ['.jpg', '.png', '.jpeg']:
        media_type = "image"

    elif extension.lower() in ['.mp4']:
        media_type = "video"
    
    dest = f"integrations/{platform}/{media_type}/{unique_filename}{extension}"

    fs = FileSystemStorage()
    filename = fs.save(dest, request.FILES['photo'])
    media_url = fs.url(filename)

    url = f"https://tsec-hacks.vercel.app{media_url}"

    return url


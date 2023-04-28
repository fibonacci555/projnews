from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from core.models import *
from django.views import View
from telegram import Bot
from telegram.ext import Updater

TOKEN = "5994891219:AAFzlN3phFPj6Aa6ZWldYMZxvOCwV6hf5Sg"
updater = Updater(TOKEN)


def send(msg,img):
    bot = Bot(TOKEN)
    chat_id = "-996057893"
    if img != None:
        bot.send_photo(chat_id=chat_id, photo=open(img, 'rb'), caption=msg)
    else: 
        bot.send_message(chat_id=chat_id, text=msg)
    
    
    

class Index(View):
    def get(self,request):
        
        return render(request, 'index.html')
    def post(self,request):
        msg = request.POST.get('msg')
        img = request.FILES.get('img')
        print(img)
        if img:
            if isinstance(img, InMemoryUploadedFile):
                img_path = 'uploaded_photo.jpg'
                with open(img_path, 'wb') as f:
                    f.write(img.read())
            else:
                img_path = img.temporary_file_path()
            send(msg, img_path)
          
        else:
            send(msg,None)
           
        return render(request, 'index.html')
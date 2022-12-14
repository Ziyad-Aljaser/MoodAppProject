from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from MoodAppProject import settings
import os
import openai
from dotenv import load_dotenv
from MoodAppProject import settings

# Used to load env
load_dotenv()

# Used to generate the random AI image based on the user mood
def get_AI_image(mode):
    # Used to get the hidden API Key
    openai.api_key = os.getenv('API_KEY')  # api key
    test = openai.Image.create(prompt=mode, n=1, size="1024x1024")
    url = str(test["data"][0])[12:-3]
    return url

def index(request):
    template = loader.get_template('MoodAppPage.html')
    print("Test")
    print(os.getenv('API_KEY'))
    return HttpResponse(template.render())

def happy(request):
    template = loader.get_template('HappyPage.html')
    HappyDatabase = happy_database.objects.all().values_list('id', 'author', "phrase", "authorPic")
    context = {
        'myDataBase': HappyDatabase,
        'get_AI_image': get_AI_image("happy person"),
    }
    return HttpResponse(template.render(context))

def sad(request):
    template = loader.get_template('SadPage.html')
    SadDatabase = sad_database.objects.all().values_list('id', 'author',
                                                             "phrase", "authorPic")
    context = {
        'myDataBase': SadDatabase,
        'get_AI_image': get_AI_image("sad person"),
    }
    return HttpResponse(template.render(context))

def angry(request):
    template = loader.get_template('AngryPage.html')
    AngryDatabase = angry_database.objects.all().values_list('id', 'author',
                                                             "phrase", "authorPic")
    context = {
        'myDataBase': AngryDatabase,
        'get_AI_image': get_AI_image("angry person"),
    }
    return HttpResponse(template.render(context))

def nervous(request):
    template = loader.get_template('NervousPage.html')
    NervousDatabase = nervous_database.objects.all().values_list('id', 'author',
                                                             "phrase", "authorPic")
    context = {
        'myDataBase': NervousDatabase,
        'get_AI_image': get_AI_image("nervous person"),
    }
    return HttpResponse(template.render(context))

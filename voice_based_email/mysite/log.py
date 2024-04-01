import smtplib
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.models import User

i = 1
addr = ''
passwrd = ''
file = 'filename'
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

def texttospeech(text, filename):
    filename = f'{filename}.mp3'
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            flag = False
        except Exception as e:
            print('Trying again', e)
            os.remove(filename)
    if os.path.exists(filename):
        playsound(filename)
        os.remove(filename)
    else:
        print("The file does not exist")
    return

def speechtotext(duration):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=duration)
    try:
        response = r.recognize_google(audio)
    except:
        response = 'N'
    return response

def login_view(request):
    global i, addr, passwrd
    if request.user.is_authenticated:
        return redirect('homepage:options')

    if request.method == 'POST':
        texttospeech("Welcome to our Voice Based Email. Login with your Gmail account to continue.", f'{file}{i}')
        i += 1

        # Speech recognition for email address
        flag = True
        while flag:
            texttospeech("Please say your Gmail address.", f'{file}{i}')
            i += 1
            addr = speechtotext(10)
            if addr != 'N':
                texttospeech("You said " + addr + ". Is that correct? Say yes or no.", f'{file}{i}')
                i += 1
                say = speechtotext(3)
                if say.lower() == 'yes':
                    flag = False
            else:
                texttospeech("Sorry, I couldn't understand you. Please repeat your Gmail address.", f'{file}{i}')
                i += 1

        addr = addr.strip().lower()

        # Speech recognition for password
        flag = True
        while flag:
            texttospeech("Please say your Gmail password.", f'{file}{i}')
            i += 1
            passwrd = speechtotext(10)
            if passwrd != 'N':
                texttospeech("You said your password. Is that correct? Say yes or no.", f'{file}{i}')
                i += 1
                say = speechtotext(3)
                if say.lower() == 'yes':
                    flag = False
            else:
                texttospeech("Sorry, I couldn't understand you. Please repeat your password.", f'{file}{i}')
                i += 1

        passwrd = passwrd.strip()

        try:
            # Authenticate the user
            user = User.objects.get(email=addr)
            if user.check_password(passwrd):
                login(request, user)
                texttospeech("Congratulations! You have successfully logged in.", f'{file}{i}')
                i += 1
                return JsonResponse({'result': 'success'})
            else:
                texttospeech("Invalid login details. Please try again.", f'{file}{i}')
                i += 1
                return JsonResponse({'result': 'failure'})
        except User.DoesNotExist:
            texttospeech("No user found with this email address. Please try again.", f'{file}{i}')
            i += 1
            return JsonResponse({'result': 'failure'})

    return render(request, 'homepage/login.html')

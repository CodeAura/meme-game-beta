# Antwoorden:
## 1. Gabe the Dog
## 2. Ron Jans
## 3. Pablo
## 4. I like ya cut g
## 5. Smooth like butter
## 6. Nyan cat
## 7. James its Valtteri & Lando norris radio check & Kiki Ra
## 8.
## 9. 
## 10.


import time
import webbrowser
import os
import colorsys

print("++++++++++++++++++++++++++++++++++++++")
print("The Meme Mind - Official 0.0.1 Beta Version")
print("1. Spelen")
print("2. Settings")
print("++++++++++++++++++++++++++++++++++++++")
invoer = input()
if invoer == "Spelen":
    print("Welkom bij The Meme Mind")
    time.sleep(1)
    print("In dit spel ga je allemaal verschillende memes krijgen. Als je een vraag goed heb krijg je een punt.")
    time.sleep(0.3)
    print("Zo laten we beginnen!")
    Vraag1 = input("Welke hond is zo bekend door het blaffen? ")
    if Vraag1 == "Gabe the Dog":
        print("Correct. Je browser word geopend om een video te laten zien van deze meme.")
        time.sleep(2)
        webbrowser.open("https://youtu.be/Ye6TI_iYEV0")
        time.sleep(5)
        vraag2 = input("Welke Nederlandse Internet gekkie is bekend door het woord keukenrol? ")
        if vraag2 == "Ron Jans":
           print("Correct. Je browser word geopend om een video te laten zien van deze meme.")
           time.sleep(2)
           webbrowser.open("https://youtu.be/F4PKT9SBvHA")
           time.sleep(5)
           vraag3 = input("Bij welke meme springt er iemand van een brug? ")
           if vraag3 == "Pablo":
               print("Correct. Je browser word geopend om een video te laten zien van deze meme.")
               time.sleep(2)
               webbrowser.open("https://youtu.be/tJpSVqmG27I")
               time.sleep(9)
               vraag4 = input("You Playing minecraft, ")
               if vraag4 == "i like ya cut g":
                   print("Correct. Je browser word geopend om de meme video te zien.")
                   time.sleep(2)
                   webbrowser.open("https://youtu.be/hRPpgleML1o")
                   time.sleep(4)
                   vraag5 = input("Welke meme is ook wel bekend met boter? ")
                   if vraag5 == "Smooth like butter":
                       print("Correct. Je browser word geopend om een video te laten zien van deze meme.")
                       time.sleep(2)
                       webbrowser.open("https://youtu.be/Pq301GSRuYM")
                       vraag6 = input("Wat is de regenboog kat? ")
                       if vraag6 == "Nyan cat":
                           print("Correct.")
                           time.sleep(2)
                           webbrowser.open("https://youtu.be/QH2-TGUlwu4")
                           vraag7 = input("Welke F1 meme is erg bekend. ")
                           if vraag7 == "Lando norris radio check":
                               print("Correct.")
                               time.sleep(2)
                               webbrowser.open("https://youtu.be/kfYOkEIfWwI")
                               time.sleep(5)
                               print("+++++++++++++++")
                               print("Laatste vraag")
                               print("+++++++++++++++")
                               time.sleep(2)
                               Vraag8 = input("Moet deze meme game langer of korter? ")
                               if Vraag8 == "Korter":
                                   webbrowser.open("https://youtu.be/ypSKDY4Jp3g?t=44")
                                   time.sleep(3)
                                   print("+++++++++++++++")
                                   print("Het einde")
                                   print("+++++++++++++++")
                                   time.sleep(1)
                                   print("Terug naar het menu?")
                                   menu2 = input()
                                   if menu2 == "Ja":
                                       exec(open("beta_game.py").read())
                                   else:
                                       webbrowser.open("https://youtu.be/r94vuvwUSkY")
                               else:
                                   webbrowser.open("https://youtu.be/JH642hpJtFs")
                           elif vraag7 == "James its Valtteri":
                                print("Correct.")
                                time.sleep(2)
                                webbrowser.open("https://youtu.be/J2nKdlygIHc?list=LL")
                                time.sleep(5)
                                print("+++++++++++++++")
                                print("Laatste vraag")
                                print("+++++++++++++++")
                                time.sleep(2)
                                Vraag8 = input("Moet deze meme game langer of korter? ")
                                if Vraag8 == "Korter":
                                   webbrowser.open("https://youtu.be/ypSKDY4Jp3g?t=44")
                                   time.sleep(3)
                                   print("+++++++++++++++")
                                   print("Het einde")
                                   print("+++++++++++++++")
                                   time.sleep(1)
                                   print("Terug naar het menu?")
                                   menu2 = input()
                                   if menu2 == "Ja":
                                       exec(open("beta_game.py").read())
                                   else:
                                       webbrowser.open("https://youtu.be/r94vuvwUSkY")
                                else:
                                   webbrowser.open("https://youtu.be/JH642hpJtFs")
                           elif vraag7 == "Kiki Ra":
                               print("Niet te veel daniel riccardo kijken, je hebt hem goed.")
                               time.sleep(2)
                               webbrowser.open("https://youtu.be/_uPTHKobAAc")
                               time.sleep(5)
                               print("+++++++++++++++")
                               print("Laatste vraag")
                               print("+++++++++++++++")
                               time.sleep(2)
                               Vraag8 = input("Moet deze meme game langer of korter? ")
                               if Vraag8 == "Korter":
                                   webbrowser.open("https://youtu.be/ypSKDY4Jp3g?t=44")
                                   time.sleep(3)
                                   print("+++++++++++++++")
                                   print("Het einde")
                                   print("+++++++++++++++")
                                   time.sleep(1)
                                   print("Terug naar het menu?")
                                   menu2 = input()
                                   if menu2 == "Ja":
                                       exec(open("beta_game.py").read())
                                   else:
                                       webbrowser.open("https://youtu.be/r94vuvwUSkY")
                               else:
                                   webbrowser.open("https://youtu.be/JH642hpJtFs")
                           else:
                               print("Fout.")
                               time.sleep(1)
                               webbrowser.open("https://youtu.be/7ODcC5z6Ca0")
                               exec(open("beta_game.py").read())
                       else:
                           print("Fout.")
                           time.sleep(1)
                           webbrowser.open("https://youtu.be/l60MnDJklnM")
                           exec(open("beta_game.py").read())
                   else:
                       print("Fout.")
                       time.sleep(1)
                       webbrowser.open("https://youtu.be/7ODcC5z6Ca0")
                       exec(open("beta_game.py").read())
               else:
                   print("Fout.")
                   time.sleep(1)
                   webbrowser.open("https://youtu.be/l60MnDJklnM")
                   exec(open("beta_game.py").read())
           else:
               print("Fout")
               time.sleep(1)
               webbrowser.open("https://youtu.be/7ODcC5z6Ca0")
               exec(open("beta_game.py").read())
        else:
           print("Fout")
           time.sleep(1)
           webbrowser.open("https://youtu.be/l60MnDJklnM")
           exec(open("beta_game.py").read())
    else:
        print("Fout.")
        time.sleep(1)
        webbrowser.open("https://youtu.be/7ODcC5z6Ca0")
        exec(open("beta_game.py").read())
else:
    print("Er zijn geen settings!")
    time.sleep(2)
    webbrowser.open("https://youtu.be/HtTUsOKjWyQ?t=13")
    time.sleep(3)
    print("Terug naar hoofdmenu?")
    menu = input()
    if menu == "Ja":
        exec(open("beta_game.py").read())
    else:
        webbrowser.open("https://youtu.be/aMhiu7BPAt4") 
        def countdown(t):    
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
        t = int(10)
        countdown(int(t))
        exit()
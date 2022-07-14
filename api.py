from fastapi import FastAPI, Path
plik=open("plik")
plik=plik.read().split()
plik2 = open("slowa.txt", 'w')
for i in range(len(plik)):
    if(len(plik[i])==5):
        plik2.write(plik[i] + "\n")
app = FastAPI()
def znajdz_slowa(x, miejsce, slownik):
    nowy = []
    for i in range(len(slownik)):
        slowo = slownik[i]
        if (slowo[miejsce - 1] == x):

            nowy.append(slownik[i])
    return nowy

def litera_w_slowie(x, miejsce, slownik):
    nowy = []
    for i in range(len(slownik)):
        if (x in slownik[i] and x != slownik[i][miejsce - 1]):
            nowy.append(slownik[i])
    return nowy

def litera_nie_w_slowie(x, slownik):
    nowy = []
    for i in range(len(slownik)):
        if (x not in slownik[i]):
            nowy.append(slownik[i])
    return nowy
#żeby włączyć w terminalu napisz "uvicorn nazwa programu:app --reload przykład do tego (uvicorn api:app --reload)"
@app.get("/")
def home():
    return {"message": "Hello World"}
@app.get("/get-word")
def get_word(word: str = None, opcje: str=None):
    plik = open("slowa.txt")
    plik = plik.read().split()
    slowa = []
    plik2 = open("slowa.txt", 'w')


    for i in range(len(plik)):
        slowo = plik[i]
        if (len(slowo) == 5):
            slowa.append(slowo)

    slowo = str(word)
    opcje = str(opcje)
    for i in range(5):
        litera = slowo[i]
        if (opcje[i] == '1'):
            slowa = znajdz_slowa(litera, i + 1, slowa)
        if (opcje[i] == '2'):
            slowa = litera_w_slowie(litera, i + 1, slowa)
        if (opcje[i] == '3'):
            slowa = litera_nie_w_slowie(litera, slowa)
    for i in range(len(slowa)):
        plik2.write(slowa[i]+"\n")
    return slowa
@app.get("/reset")
def reset():
    plik = open("C:\\Users\\bartosz kebel\\PycharmProjects\\Git_projekt1.0\\plik")
    plik = plik.read().split()
    plik2 = open("slowa.txt", 'w')
    for i in range(len(plik)):
        if (len(plik[i]) == 5):
            plik2.write(plik[i] + "\n")
    return ""
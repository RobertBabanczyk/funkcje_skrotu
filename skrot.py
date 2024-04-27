import hashlib
import secrets
import time

class Serwer:
    def __init__(self):
        self.uzytkownicy = {}

    def dodaj_uzytkownika(self, nazwa_uzytkownika, haslo):
        sol = secrets.token_hex(16)
        haslo_hash = hashlib.sha256((haslo + sol).encode()).hexdigest()
        self.uzytkownicy[nazwa_uzytkownika] = {'haslo_hash': haslo_hash, 'sol': sol}

    def uwierzytelnij_uzytkownika(self, nazwa_uzytkownika, haslo):
        if nazwa_uzytkownika in self.uzytkownicy:
            zapisane_haslo_hash = self.uzytkownicy[nazwa_uzytkownika]['haslo_hash']
            sol = self.uzytkownicy[nazwa_uzytkownika]['sol']
            if hashlib.sha256((haslo + sol).encode()).hexdigest() == zapisane_haslo_hash:
                return True
        return False

class Klient:
    def __init__(self, serwer):
        self.serwer = serwer

    def zarejestruj(self, nazwa_uzytkownika, haslo):
        self.serwer.dodaj_uzytkownika(nazwa_uzytkownika, haslo)

    def zaloguj(self, nazwa_uzytkownika, haslo):
        return self.serwer.uwierzytelnij_uzytkownika(nazwa_uzytkownika, haslo)

serwer = Serwer()
klient = Klient(serwer)

start_time = time.time()
klient.zarejestruj('uzytkownik1', 'haslo123')
end_time = time.time()
print("Czas rejestracji: {:.10f} s".format(end_time - start_time))

start_time = time.time()
print("Logowanie udane:", klient.zaloguj('uzytkownik1', 'haslo123'))
end_time = time.time()
print("Czas logowania z poprawnym hasłem: {:.10f} s".format(end_time - start_time))

start_time = time.time()
print("Logowanie udane:", klient.zaloguj('uzytkownik1', 'niepoprawne_haslo'))
end_time = time.time()
print("Czas logowania z niepoprawnym hasłem: {:.10f} s".format(end_time - start_time))

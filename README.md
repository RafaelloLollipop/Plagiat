Witamy w projekcie Plagiat :) 

Celem projektu było stworzenie programu, który będzie porównywał pliki tekstowe różnych formatów i stwierdzał czy dane zdania są uznane za plagiat. Celem dodatkowym było stworzenie wygodnego i intuicyjnego interfejsu graficznego oraz zaimplementowanie dwóch metod porównywania tekstów.

![Screen programu Plagiat](http://wrzuc.se/images/53a951d3c1f06.png)

Jesteśmy, tzn. _Rafał i Kamil_, bardzo dumni z tego projektu.

[![](https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpa1/t1.0-1/c0.0.160.160/p160x160/1527077_747523745270734_902786671_n.jpg)](https://www.facebook.com/rafaellolizotto?fref=ts)

[![](https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/t1.0-1/c136.0.160.160/p160x160/1486840_10203140153359063_5462384558952645275_n.jpg)](https://www.facebook.com/kamil.rogalski.507)

# Podstawowe funkcjonalności programu:
- porównanie tekstu badanego z tekstami referencyjnymi (txt, pdf, doc, html)
- podążanie za linkami pojawiającymi się w tekście badanym oraz w tekstach referencyjnych
- generowanie raportu ogólnego pokazującego statystyki dotyczące plagiatu oraz raportu szczegółowego, w którym można sprawdzić, jakie dokładnie zdania uznaliśmy za plagiat
- możliwość zapisania układu tekstu badanego, referencyjnych, ustawień oraz raportów jako projektu, przerywania pracy i wznawiania jej od miejsca zakończenia

# Instrukcja obsługi:

**Nowy projekt** - pozwala otworzyć plik, który będzie badany pod względem plagiatu. Przyjmowane formaty plików: txt, doc, pdf, html. Plik zostanie załadowany do pola po lewej stronie okna. Po otwarciu pliku automatycznie zostanie stworzony i zapisany nowy projekt, w którym zapisywane są postępy w badaniu plagiatu.

**Otwórz projekt** - pozwala otworzyć wcześniej utworzony projekt.

**Dodaj plik** - pozwala dodać plik w formacie txt, doc, pdf, html, który zostanie dodany po prawej stronie okna i porównany po względem plagiatu z plikiem głównym.

**Dodaj WWW** - pozwala dodać odnośnik www, który zostanie ściągnięty z Internetu i porównany z plikiem głównym. Domyślnie zostają dodane odnośniki znalezione wewnątrz pliku głównego, który został załadowany po lewej stronie. Po zakończeniu wyboru linków należy ponownie kliknąć Dodaj WWW.

**Usuń plik** - pozwala usunąć dodany już z plik z listy plików porównywanych po względem plagiatu.

**Statystyka** - zawiera podstawowe informacje na temat stopnia splagiatyzowania  pliku.

**Lista plików referencyjnych** - nad prawą częścią okna znajduje się pokolorowana lista plików referencyjnych. Po kliknięciu wybranego pliku, jego zawartość zostanie załadowana do prawej części ekranu.

**Lewa strona okna** - zawiera tekst tekst główny podzielony na zdania. Poszczególnymi kolorami zostały zaznaczone zdania, które zostały znalezione w innych plikach referencyjnych. Po kliknięciu w poszczególne zdanie zostanie po prawej stronie ekranu załadowany odpowiedni plik i zaznaczone dane zdanie.

**Prawa strona okna** - zawiera tekst referencyjny podzielony na zdania.

**Dolna część ekranu** zawiera konsolę na błędy oraz pasek postępu ładowania plików.

# Przykład użycia:
1. Wybierz 'Nowy Projekt', aby załadować plik główny
2. Wybierz 'Dodaj plik' oraz 'Dodaj www', aby dodać pliki referencyjne oraz pliki www z Internetu.
3. Po lewej stronie został załadowany plik główny. Zdania, które zostały uznane za plagiat zostały odpowiednio pokolorowane (poszczególny kolor odpowiada za inny plik referencyjny)
4. Po prawej stronie znajduje się załadowany tekst referencyjny. Powyżej istnieje możliwość wyboru innego pliku referencyjnego


# Metody porównywania tekstu:
**1 metoda** - usuwa wszystkie znaki interpunkcyjne, polskie znaki oraz słowa dodane do słownika jako łączniki. Z każdego zdania wyliczana jest sygnatura. Poszczególne sygnatury są ze sobą porównywane i takie same są oznaczane jako plagiat.

**2 metoda** - używa biblioteki ngram (powtarzanie się ciągu znaków, ich długość) do porównania kolejnych zdań. Współczynnik odrzucenia wskazuje przy jakim progu podobieństwa zdania zostaną uznane za plagiat (mniejsza wartość oznacza, że program szybciej uzna dwa zdania za plagiat, większa wartość oznacza, że program będzie mniej skłonny do uznania dwóch zdań za plagiat)

# Opis poszczególnych klas oraz metod:
* [Source](https://github.com/Vallher/Plagiat/wiki/Klasa-Source)
* [MainFile](https://github.com/Vallher/Plagiat/wiki/Klasa-MainFile)
* [File](https://github.com/Vallher/Plagiat/wiki/Klasa-File)
* [OutFile](https://github.com/Vallher/Plagiat/wiki/Klasa-OutFile)
* [GUI](https://github.com/Vallher/Plagiat/wiki/GUI)

# Wykorzystane biblioteki:
* PyQt4
* nltk
* StringIO
* PyPDF2
* urllib
* re
* hashlib
* Tkinter
* tkFileDialog

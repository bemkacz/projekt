import random
import time
from kraj import Kraj

class Game:
    def __init__(self):
        self.actions = [
            {
                "pytanie": "Ograniczyć budżet wojska?",
                "skutki": {"wojsko": -40, "ekonomia": 20},
            },
            {
                "pytanie": "Rozpocząć śledztwo dotyczące żołnierzy szmuglujących broń?",
                "skutki": {"ludnosc": 20, "wojsko": -20},
            },
            {
                "pytanie": "Szukać złóż oleju?",
                "skutki": {"ekonomia": 50},
            },
            {
                "pytanie": "Przywrócić obowiązkowy pobór do wojska?",
                "skutki": {"ludnosc": -40, "wojsko": 40, "satysfakcja": -20},
            },
            {
                "pytanie": "Zezwolić na eksperymenty na zbożu?",
                "skutki": {"ekologia": 20, "ekonomia": -20},
            },
            {
                "pytanie": "Zwiększyć budżet wojska?",
                "skutki": {"wojsko": 15, "ekonomia": -20},
            },
            {
                "pytanie": "Ukarać ruskich trolli?",
                "skutki": {"ludnosc": -15, "ekonomia": 15, "satysfakcja": 40},
            },
            {
                "pytanie": "Zwiększyć wyposażenie wojska?",
                "skutki": {"ekonomia": -15, "wojsko": 20},
            },
            {
                "pytanie": "Zafundować X-menów?",
                "skutki": {"wojsko": 90, "ekonomia": -20},
            },
            {
                "pytanie": "Wydać 70 milionów polskich złociszy na wybory które się nie odbędą?",
                "skutki": {"ekonomia": -2137},
            },
            {
                "pytanie": "Zwiększenie produkcji kremówek?",
                "skutki": {"satysfakcja": 100 , "ekonomia": -5},
            },
            {
                "pytanie": "Zwiększenie produkcji wódki 42.0%?",
                "skutki": {"satysfakcja": 30 , "ekonomia": -10, "ludnosc": -10},
            },
            {
                "pytanie": "Zezwolić na małżeństwa homoseksualne?",
                "skutki": {"satysfakcja": -10000000 , "ekonomia": -10000000, "ludnosc": -10000000, "wojsko": -10000000, "ekologia": -10000000},
            },
        ]
        self.tury = 20
        self.Kraj = Kraj("Państwo")

    def play(self):
        while self.tury > 0:
            self.Kraj.koniec()
            print(self.Kraj)
            print("-"*100)
            action = random.choice(self.actions)
            time.sleep(1)
            print(action["pytanie"])
            time.sleep(1)
            choice = input("y/n\n")
            time.sleep(1)
            print("-"*100)

            if choice == "y":
                for key, value in action["skutki"].items():
                    setattr(self.Kraj, key, getattr(self.Kraj, key) + value)
                    self.Kraj.checker()
            if choice == "n":
                pass
            elif choice != "y" and choice != "n":
                print("DEBILU NAUCZ SIĘ MYŚLEĆ!!!!!!!!!!!!!!!!!!!!!!!")

            self.tury -= 1

        print("Koniec ruchów elo!")
        print(self.Kraj)
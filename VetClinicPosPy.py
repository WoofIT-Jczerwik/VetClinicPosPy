# -*- coding: cp1250 -*-
from abc import ABC, abstractmethod
from datetime import datetime
import uuid

# Model danych

class Animal(ABC):  # Klasa abstrakcyjna dzięki dziedziczeniu po ABC
    def __init__(self, name: str, age: int, owner_name: str):
        self.id = str(uuid.uuid4())[:8]  # Identyfikator obiektu (unikalny skrócony GUID zasugerowany przez AI)
        self.name = name
        self.age = age
        self.owner_name = owner_name

    @property
    @abstractmethod
    def species(self) -> str:
        pass

    def display_info(self):
        print(f"[{self.species}] ID: {self.id}, Imię: {self.name}, Wiek: {self.age} lat(a), Właściciel: {self.owner_name}")


class Dog(Animal):
    def __init__(self, name: str, age: int, owner_name: str, breed: str):
        super().__init__(name, age, owner_name)  # Wywołanie konstruktora klasy bazowej
        self.breed = breed

    @property
    def species(self) -> str:
        return "Pies"

    def display_info(self):
        # Nadpisanie metody (Polimorfizm)
        print(f"[{self.species}] ID: {self.id}, Imię: {self.name}, Rasa: {self.breed}, Wiek: {self.age} lat(a), Właściciel: {self.owner_name}")


class Cat(Animal):
    def __init__(self, name: str, age: int, owner_name: str, is_indoor: bool):
        super().__init__(name, age, owner_name)
        self.is_indoor = is_indoor

    @property
    def species(self) -> str:
        return "Kot"

    def display_info(self):
        typ = "Domowy" if self.is_indoor else "Wychodzący"
        print(f"[{self.species}] ID: {self.id}, Imię: {self.name}, Typ: {typ}, Wiek: {self.age} lat(a), Właściciel: {self.owner_name}")


class Bird(Animal):
    def __init__(self, name: str, age: int, owner_name: str, feather_color: str):
        super().__init__(name, age, owner_name)
        self.feather_color = feather_color

    @property
    def species(self) -> str:
        return "Ptak"


# System POS

class PosSystem:
    def __init__(self, patient: Animal):
        self._patient = patient    # Agregacja (POS ma pacjenta) oraz Enkapsulacja (zmienna chroniona z '_')
        self.__cart = []           # Enkapsulacja - pole ściśle prywatne (Double underscore)

    def add_service(self, service_name: str, price: float):
        if price < 0:
            return
        self.__cart.append((service_name, price))
        print(f"Dodano usługę: {service_name} ({price:.2f} zł)")

    def calculate_total(self) -> float:
        return sum(item[1] for item in self.__cart)

    def print_receipt(self):
        print("\n" + "="*40)
        print("       PARAGON - KLINIKA WETERYNARYJNA  ")
        print("="*40)
        print(f" Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" Pacjent: {self._patient.name} ({self._patient.species})")
        print(f" Właściciel: {self._patient.owner_name}")
        print("-"*40)
        print(" Wykonane usługi:")
        
        if not self.__cart:
            print("   Brak zarejestrowanych usług.")
        else:
            for name, price in self.__cart:
                print(f" - {name:<25} {price:>10.2f} zł")
                
        print("-"*40)
        total = self.calculate_total()
        print(f" SUMA DO ZAPŁATY: {total:>20.2f} zł")
        print("="*40)
        print("        Dziękujemy za wizytę!           ")
        print("="*40)
        input("\nNaciśnij Enter, aby kontynuować...")


# Interfejs i uruchomienie

def main():
    # Autopopulowanie listy
    patients = [
        Dog("Burek", 5, "Jan Kowalski", "Owczarek"),
        Cat("Mizia", 3, "Anna Nowak", True)
    ]

    while True:
        print("\n=== SYSTEM POS KLINIKI WETERYNARYJNEJ (PYTHON) ===")
        print("1. Wyświetl listę pacjentów")
        print("2. Dodaj nowego pacjenta")
        print("3. Rozpocznij wizytę i wystaw paragon")
        print("4. Wyjście")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            print("\n=== LISTA PACJENTÓW ===")
            for idx, p in enumerate(patients):
                print(f"{idx + 1}. ", end="")
                p.display_info() # Polimorficzne wywołanie metody
            input("\nNaciśnij Enter...")

        elif wybor == "2":
            print("\n=== DODAWANIE NOWEGO PACJENTA ===")
            typ = input("1. Pies | 2. Kot | 3. Ptak: ")
            name = input("Imię: ")
            age = int(input("Wiek: ") or 0)
            owner = input("Właściciel: ")

            if typ == "1":
                breed = input("Rasa: ")
                patients.append(Dog(name, age, owner, breed))
            elif typ == "2":
                indoor = input("Czy domowy? (t/n): ").lower() == 't'
                patients.append(Cat(name, age, owner, indoor))
            elif typ == "3":
                color = input("Kolor piór: ")
                patients.append(Bird(name, age, owner, color))
            print("Dodano pacjenta!")
        
        elif wybor == "4":
            break

        elif wybor == "3":
            if not patients:
                print("Brak pacjentów.")
                continue
            print("=== ROZPOCZĘCIE WIZYTY ===")
    
            if not patients:  
                print("Brak pacjentów w bazie. Dodaj pacjenta przed wizytą.")
                input()  
                return

            for i, patient in enumerate(patients):
                print(f"{i + 1}. {patient.name} ({patient.species}) - {patient.owner_name}")
        
            user_input = input("Wybierz numer pacjenta: ")
    
            try: # Parsowanie do int i sprawdzenie zakresu
                index = int(user_input)
                if index < 1 or index > len(patients):
                    raise ValueError
            except ValueError:
                print("Nieprawidłowy numer.")
                input()
                return

            selected_patient = patients[index - 1]
            pos = PosSystem(selected_patient)

            # Menu wyboru usług
            billing = True
            while billing:
                print(f"=== KOSZYK USŁUG DLA: {selected_patient.name} ===")
                print("1. Konsultacja weterynaryjna (100,00 zł)")
                print("2. Szczepienie (60,00 zł)")
                print("3. Operacja/Zabieg chirurgiczny (450,00 zł)")
                print("4. Wpisz własną usługę")
                print("5. Zakończ i drukuj paragon")
        
                wybor = input("Wybierz opcję: ")

                if wybor == "1":
                        pos.add_service("Konsultacja lekarska", 100.00)
                elif wybor == "2":
                        pos.add_service("Szczepienie", 60.00)
                elif wybor == "3":
                        pos.add_service("Zabieg chirurgiczny", 450.00)
                elif wybor == "4":
                        name = input("Nazwa usługi: ")
                        try:
                            price = float(input("Cena usługi (zł): "))
                        except ValueError:
                            price = 0.0
                        pos.add_service(name, price)
                elif wybor =="5":
                        billing = False
                        pos.print_receipt()

                if billing:
                    input("\nNaciśnij enter aby kontynuować...")
if __name__ == "__main__":
    main()

Program VetClinicPOS to program, który ma pełnić funkcję POS (Point of Sale) dla kliniki weterynaryjnej. 
Klasy:
- Animal - klasa abstrakcyjna, po której dziedziczą inne "zwierzęce" klasy, a sama dziedziczy po ABC (Abstract Base Classes)
- Dog - klasa dziedzicząca po Animal do obsługi psich pacjentów
- Cat - klasa dziedzicząca po Animal do obsługi kocich pacjentów
- Bird - klasa dziedzicząca po Animal do obsługi ptasich pacjentów
- PosSystem - klasa z obsługą logiki kasy fiskalnej

Program korzysta z klas, obiektów, metod, konstruktorów (np. super().__init__), a także właściwości @property.

Użyto enkapsulacji poprzez zmienne chronione wyróżnione "_"

Dziedziczenie: Klasy Dog, Cat, Bird dziedziczą po Animal

Polimorfizm: zastosowany poprzez nadpisywanie metody w klasie dziedziczącej DisplayInfo().

Abstrakcja: klasa Animal jest zdefiniowana jako abstracyjna i nie możemy zainicjalizować jej instancji.

Program działa (uruchomiony w Visual Studio), a AI było używane tylko aby pomóc wykryć błędy w napisanym kodzie (skorygować błędne metody, dodać unikalne ID dla obiektów)

class Singer(Musician):
    def __init__(self, instrument, sex, year_of_birth, city, song):
        super().__init__(instrument, sex, year_of_birth, city)
        self.song = song

    def play_music(self):
        print(f"I`m singing {self.song}!")

    def performance(self):
        print('I`m singing and dancing!')


Richter = Pianist('Piano', 'male', 1966, 'London')
print(Richter.instrument)
print(Richter.__dict__)
Richter.play_music()
Richter.play_modern()
Richter.concert()
# Richter.concerts()

Bessonov = Pianist("Grand_piano", "male", 2002, "Moscow")
print(Bessonov.__dict__)
Bessonov.play_modern()
Bessonov.concerts()

Adele = Singer('Voice','female', 1988, "London", "Skyfall")
print(Adele.__dict__)
Adele.concert()
Adele.play_music()
Adele.performance()

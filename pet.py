import json
import os

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.tricks = []
        self.load_state()
        self.degrade_state()

    def degrade_state(self):
        self.hunger = min(10, self.hunger + 1)
        self.energy = max(0, self.energy - 1)
        self.happiness = max(0, self.happiness - 1)

    def eat(self):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(10, self.happiness + 5)
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has eaten.")

    def sleep(self):
        self.hunger = min(10, self.hunger + 2)
        self.energy = min(10, self.energy + 5)
        self.happiness = min(10, self.happiness + 5)
        print(f"{self.name} had a good sleep.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had fun!")
        else:
            print(f"{self.name} is too tired to play.")

    # def train(self, trick):
    #     self.tricks.append(trick)
    #     print(f"{self.name} learned a new trick: {trick}!")

    # def show_tricks(self):
    #     if self.tricks:
    #         print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
    #     else:
    #         print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def save_state(self):
        data = {
            'name': self.name,
            'hunger': self.hunger,
            'energy': self.energy,
            'happiness': self.happiness,
            'tricks': self.tricks
        }
        with open("pet_data.json", "w") as f:
            json.dump(data, f)

    def load_state(self):
        if os.path.exists("pet_data.json"):
            with open("pet_data.json", "r") as f:
                data = json.load(f)
                self.hunger = data.get('hunger', self.hunger)
                self.energy = data.get('energy', self.energy)
                self.happiness = data.get('happiness', self.happiness)
                self.tricks = data.get('tricks', [])

    def needs_attention(self):
        return self.hunger == 10 and self.energy == 0 and self.happiness == 0
from pet import Pet  # Assuming Pet class is in pet.py

my_pet = Pet("Averex")
my_pet.get_status()

if my_pet.needs_attention():
    print("\n WARNING: Your pet is very hungry, and needs some sleep!")
    my_pet.eat()
    my_pet.sleep()

my_pet.save_state()

cat_attributes = {
    "intelligence": 20,
    "energy": 50,
    "weight": 10,
}

print("Welcome to my cat game!")

name = input("Enter name: ")
colour = input("Enter colour: ")
loop = True

while loop == True:
    option = input("What would you like to do? 1 = Play with your cat, 2 = Train your cat, 3 = show stats, 4 = Put it to sleep, 5 = Feed your cat. ")
    if option == '1':
        getEnergy = cat_attributes.get("energy")
        getEnergy -= 10
        cat_attributes.update(energy=getEnergy)
        pass
    elif option == '2':
        getIntelligence = cat_attributes.get("intelligence")
        getIntelligence += 5
        cat_attributes.update(intelligence=getIntelligence)
        getEnergy -= 5
        cat_attributes.update(energy=getEnergy)
        pass
    elif option == '3':
        print("\n".join("{}\t{}".format(k, v) for k, v in cat_attributes.items()))
    elif option == '4':
        getEnergy = cat_attributes.get("energy")
        getEnergy += 10
        cat_attributes.update(energy = getEnergy)
        pass
    elif option == '5':
        getEnergy = cat_attributes.get("energy")
        getEnergy += 5
        cat_attributes.update(energy = getEnergy)
        getWeight = cat_attributes.get("weight")
        getWeight += 1
        cat_attributes.update(weight = getWeight)
        pass
    else:
        pass
    if cat_attributes['energy'] < 5:
        print("Your cat has no energy, you can no longer play with him!")
        print("Game over")
        loop = False
    if cat_attributes['weight'] >= 20:
        print("Your cat ate too much, now he cant move")
        print("Game over")
        loop = False
    if cat_attributes['energy']>= 100:
        print("Your cat gained too much energy and ran away!")
        print("Game over")
        loop = False
    
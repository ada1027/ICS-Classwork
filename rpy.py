# Done by Ada and Katelyn
pokeballs_price = 300
eeveeLocation =  (4,6)
jigglypuffLocation = (7,3)
dittoLocation = (-3,5)
pidgeottoLocation = (-2, -4)
wild_pokemon = ["Eevee", "Jigglypuff", "Ditto", "Pidgeotto"]
pokemon_location = [eeveeLocation,jigglypuffLocation, dittoLocation, pidgeottoLocation]
shop = [pokeballs_price] 
shop_location = (0,0)
inventory = ["Pikachu"]
money = 3000
total_balls = 0
listActions = ["Run right", "Run left", "Run down", 'Run up', "See inventory", "See Wild Pokemon", "See Shop Location"]

x=0
y=0
playerActive = True
player_location = (x,y)
print(*listActions, sep="\n")
while playerActive:
  action = input("Choose an action. ").lower()
  if action == "run right": 
    x += 1
  elif action == "run left":
    x -= 1
  elif action == "run up":
    y += 1
  elif action == "run down":
    y -= 1
  elif action == "see inventory":
    print ("Here is your inventory", *inventory, sep = "\n")
  elif action == "see wild pokemon":
    print ("Here are the locations:", *pokemon_location, sep ="\n")
  elif action == "see shop location":
    print ("The shop is at 5,10")
  elif player_location == shop_location:
    print(f'You have arrived at a shop. You have ${money}.')
    balls_bought = int(input('How many balls would you like to buy? Each ball is $300.'))
    cost = balls_bought * 300
    if cost > money :
      print ('You do not have enough money.')
    else:
      print (f'You have bought {balls_bought} balls.')
      money = money - cost
      print (f'You have ${money} remaining.')
      total_balls = total_balls + balls_bought    
  elif player_location in pokemon_location:
    indexOfPokemon = pokemon_location.index(player_location)
    print("You have encountered " + wild_pokemon[indexOfPokemon])
    print(f"{total_balls} balls left.")
    action = input("1. Catch \n2. Run \n3. Fight").lower()
    if action == 'catch':
      if total_balls <= 0:
        print ('You do not have any balls.')
      if total_balls > 0:
        total_balls -= 1
        print("You have caught " + wild_pokemon[indexOfPokemon])
        inventory.append (wild_pokemon[indexOfPokemon])
        del wild_pokemon [indexOfPokemon]
        del pokemon_location [indexOfPokemon]
    if action == 'run':
        x -= 1
        print ('You ran from the battle.') 
    if action == 'fight':
      import random
      number = random.randrange (1,10)
      if number > 5:
        print ('Your Pikachu used tackle. It was a critical hit!')
        print ('The wild '+ wild_pokemon[indexOfPokemon]+ ' has fainted.')
      if number < 5:
        print ('Your Pikachu used tackle.')
  player_location = (x,y)
  print (f"You are now at {player_location}")
  if len(pokemon_location) == 0:
    print ('You have caught all the Pokemon! You have caught these pokemon:', *inventory)
    playerActive = False
print("You have won the game! ")
    

  

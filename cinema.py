films = {
    "Avatar: The Way of Water ": [13,5],  #fist element is age #second element is tickets left 
    "Missing": [18,5],
    "ANT-MAN AND THE WASP: QUANTUMANIA": [13,5],
    "PUSS IN BOOTS: THE LAST WISH": [1, 5]
     }
    
while True:
      
    choice = input("What film would you like tickets for today?: ").strip().title()
      
    if choice in films:
        age = int(input("How old are you: ").strip())
        
        #check user age
        
        if age >= films[choice][0]:
            
            #check for seats
            num_seats = films[choice][1]
            
            if num_seats > 0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are to young to see the film!")
    else:
        print("We dont have the film at this theater. Sorry")
         
          
          
          
      
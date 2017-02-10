import random # this will randomly pic a room for the treasure to be placed each time the game is ran

def msg(room):
    if room['msg'] == '': 
        return "You have entered the " + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room,dir):
    if dir=='N':
        choice = 0
    elif dir=='E':
        choice = 1
    elif dir=='S':
        choice = 2
    elif dir=='W':
        choice = 3
    else:
        return -1
    
    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0) #these are the directins N S E W. this section will define the rooms

    gates = {'name':'Castel Gates','directions':dirs,'msg':''}
    court = {'name':'Inner Court','directions':dirs,'msg':''}
    stables = {'name':'Stables','directions':dirs,'msg':''}
    library = {'name':'Library','directions':dirs,'msg':''}
    greathall = {'name':'Great Hall','directions':dirs,'msg':''}
    keep = {'name':'Keep','directions':dirs,'msg':''}

    #This is to set the directions for the above so they follow the map
    gates['directions'] = (library,court,0,0)
    court['directions'] = (greathall,0,0,gates)
    stables['directions'] = (0,library,0,keep)
    library['directions'] = (0,greathall,gates,stables)
    greathall['directions'] = (0,0,court,library)
    keep['directions'] = (0,stables,0,0)

    #rooms where treasure may excluding the gates
    rooms = [court,stables,library,greathall,keep]
    room_with_treasure = random.choice(rooms)
    treasure_returned = False
    room = gates
    print('Greatings traveler and welcome to adventure Call! My name is Falconhoof and I shall be your guide.' +
          '\nYou are at the entrance to a large castle. You seek the treasure. Make your way through the castle. \n\n')
    
    while True:
        if treasure_returned and room['name'] == 'Castel Gates':
            print('You have found the treaure and returned to the Castle Gates! ' +
                  'You may now leave. \nWell done traveler.')
            break;
        elif not treasure_returned and room['name'] == room_with_treasure['name']:
            treasure_returned = True
            print(msg(room) + ' There\'s the treasure and a kings guard is sleeping next to it! ' +
                  'You have fround the treasure traveler ' +
                  '\nNow get out quick!')
            room['msg'] = ('You are back in the ' + room['name'] +
                           '! You already found the treasure. ' +
                        'Get out of here before the guard wakes up!')
        else:
            print(msg(room))
            room['msg'] = 'You are back in the ' + room['name']
            
        
        stuck = True
        while stuck:
            dir = input("Which direction do you want to go: N,E,S, or W? ")
            choice = get_choice(room,dir)
            if choice == -1:
                print("Please enter N,E,S, or W? ")
            elif choice == 4:
                print("You cannot go in that direction.")
            else:
                room = room['directions'][choice]
                stuck = False
main()

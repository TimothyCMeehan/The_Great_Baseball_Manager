import random

at_bat_complete = False
print("The pitcher winds up and pitches")
walk_roll = random.randrange(1,21)
print("Walk Roll: {}".format(walk_roll))
if (walk_roll < 3):
    print("Pitcher Walks the Batter")
    at_bat_complete = True
else:
    if (walk_roll == 13):
        #roll for special Event
        special_roll = random.randrange(1,21)
        print("Special Roll: {}".format(special_roll))
        if (special_roll < 3):
            print("Pitcher Hits the Batter, Batter takes First Base")
            at_bat_complete = True
        elif (special_roll < 9):
            print("Wild Pitch, Runners Advance")
            at_bat_complete = True
    if (at_bat_complete == False):
        
        strike_roll = random.randrange(1,21)
        print("Strike Roll: {}".format(strike_roll))
        if (strike_roll > 16):
            print("Strike Out!!")
            at_bat_complete = True
        else:
            print("Ball in Play")
            hit_roll = random.randrange(1,21)
            print("Hit Roll: {}".format(hit_roll))
            if (hit_roll > 15):
                #print("Hit!!")
                power_roll = random.randrange(1,21)
                print("Power Roll: {}".format(power_roll))
                if (power_roll > 18):
                    print("Home Run!!")
                    at_bat_complete = True
                elif (power_roll > 17):
                    print("Triple!!")
                    at_bat_complete = True
                elif (power_roll > 13):
                    print("Double!!")
                    at_bat_complete = True
                else:
                    print("Single!!")
                    at_bat_complete = True
            else:
                print("Caught for an out.")
                at_bat_complete = True
                
            
            
            
        
        
    

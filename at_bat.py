import random

def deliver_the_pitch():
    at_bat_complete = False
    play_by_play = "The pitcher winds up and pitches...\n"
    walk_roll = random.randrange(1,21)
    play_by_play += "Walk Roll: {}\n".format(walk_roll)
    if (walk_roll < 3):
        play_by_play += "Pitcher Walks the Batter\n\n"
        at_bat_complete = True
        return play_by_play
    else:
        if (walk_roll == 13):
            #roll for special Event
            special_roll = random.randrange(1,21)
            play_by_play += "Special Roll: {}\n".format(special_roll)
            if (special_roll < 3):
                play_by_play += "Pitcher Hits the Batter, Batter takes First Base\n\n"
                at_bat_complete = True
                return play_by_play
            elif (special_roll < 9):
                play_by_play += "Wild Pitch, Runners Advance\n\n"
                at_bat_complete = True
                return play_by_play
        if (at_bat_complete == False):
        
            strike_roll = random.randrange(1,21)
            play_by_play += "Strike Roll: {}\n".format(strike_roll)
            if (strike_roll > 16):
                play_by_play += "Strike Out!!\n\n"
                at_bat_complete = True
                return play_by_play
            else:
                play_by_play += "Ball in Play\n"
                hit_roll = random.randrange(1,21)
                play_by_play += "Hit Roll: {}\n".format(hit_roll)
                if (hit_roll > 15):
                    #print("Hit!!")
                    power_roll = random.randrange(1,21)
                    play_by_play += "Power Roll: {}\n".format(power_roll)
                    if (power_roll > 18):
                        play_by_play += "Home Run!!\n\n"
                        at_bat_complete = True
                        return play_by_play
                    elif (power_roll > 17):
                        play_by_play += "Triple!!\n\n"
                        at_bat_complete = True
                        return play_by_play
                    elif (power_roll > 13):
                        play_by_play += "Double!!\n\n"
                        at_bat_complete = True
                        return play_by_play
                    else:
                        play_by_play += "Single!!\n\n"
                        at_bat_complete = True
                        return play_by_play
                else:
                    play_by_play += "Caught for an out.\n\n"
                    at_bat_complete = True
                    return play_by_play
def main():
    outs = 0

    while outs < 3:
        print(deliver_the_pitch())
        outs += 1

main()
 

               
            
            
            
        
        
    

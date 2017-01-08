import random
import player



class At_Bat:

    def __init__(self, pitcher, batter, base_path, outs):
        self.__pitcher = pitcher
        self.__batter = batter
        self.__base_path = base_path
        self.__outs = outs
        self.__play_by_play = ""
        self.deliver_the_pitch()

    def deliver_the_pitch(self):
        at_bat_complete = False
        self.__play_by_play += "The pitcher winds up and pitches...\n"
        walk_roll = random.randrange(1,21)
        self.__play_by_play += "Walk Roll: {}\n".format(walk_roll)
        if (walk_roll < 3):
            self.__play_by_play += "Pitcher Walks the Batter\n\n"
            self.__base_path.append(self.__batter)
            at_bat_complete = True
            
        else:
            if (walk_roll == 13):
                #roll for special Event
                special_roll = random.randrange(1,21)
                self.__play_by_play += "Special Roll: {}\n".format(special_roll)
                if (special_roll < 3):
                    self.__play_by_play += "Pitcher Hits the Batter, Batter takes First Base\n\n"
                    self.__base_path.append(self.__batter)
                    at_bat_complete = True
                    
                elif (special_roll < 9):
                    self.__play_by_play += "Wild Pitch, Runners Advance\n\n"
                    at_bat_complete = True
                    
            if (at_bat_complete == False):
            
                strike_roll = random.randrange(1,21)
                self.__play_by_play += "Strike Roll: {}\n".format(strike_roll)
                if (strike_roll > 16):
                    self.__play_by_play += "Strike Out!!\n\n"
                    self.__outs += 1
                    at_bat_complete = True
                    
                else:
                    self.__play_by_play += "Ball in Play\n"
                    hit_roll = random.randrange(1,21)
                    self.__play_by_play += "Hit Roll: {}\n".format(hit_roll)
                    if (hit_roll > 15):
                        #print("Hit!!")
                        power_roll = random.randrange(1,21)
                        self.__play_by_play += "Power Roll: {}\n".format(power_roll)
                        if (power_roll > 18):
                            self.__play_by_play += "Home Run!!\n\n"
                            at_bat_complete = True
                            
                        elif (power_roll > 17):
                            self.__play_by_play += "Triple!!\n\n"
                            at_bat_complete = True
                            
                        elif (power_roll > 13):
                            self.__play_by_play += "Double!!\n\n"
                            at_bat_complete = True
                            
                        else:
                            self.__play_by_play += "Single!!\n\n"
                            at_bat_complete = True
                            
                    else:
                        self.__play_by_play += "Caught for an out.\n\n"
                        self.__outs += 1
                        at_bat_complete = True

    def get_play_by_play(self):
        return self.__play_by_play

    def get_outs(self):
        return self.__outs

def main():
    player1 = player.Player("Eddy Money")
    player2 = player.Player("Juan Solo")
    base_path = []
    outs = 1
    current_at_bat = At_Bat(player2, player1, base_path, outs)
    print (current_at_bat.get_play_by_play())
    print ("Outs: {}".format(current_at_bat.get_outs()))
    

main()

 

               
            
            
            
        
        
    

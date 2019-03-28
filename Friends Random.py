import os
import potplayer
from random import randint

class RandomEpisode:
    season=1
    episode_name=""
    def pick_random_episode(self):
        self.season=randint(1,10)
        folder='E:/Series/F.R.I.E.N.D.S/Friends Season '+str(self.season)
        total_episodes=os.listdir(folder)
        episode=randint(1,len(total_episodes))
        print ('Season ',self.season,' Episode ',episode, total_episodes[episode-1])
        self.episode_name=total_episodes[episode-1]
        self.check_recent()
    
    def check_recent(self):
        if os.path.isfile('Data_Friends.txt'):
            recent_episodes = [line.rstrip('\n') for line in open('Data_Friends.txt')]
            for episode in recent_episodes:
                if(episode==self.episode_name):
                    self.pick_random_episode()
        if len(recent_episodes)==15:
            del recent_episodes[0]
            recent_episodes.append(self.episode_name)
            file=open('Data_Friends.txt','w')
            for line in recent_episodes:
                file.write(line+'\n')
        else:   
            file=open('Data_Friends.txt','a')
            file.write(self.episode_name+'\n')
        file.close()
        potplayer.run('E:/Series/F.R.I.E.N.D.S/Friends Season '+str(self.season)+'/'+self.episode_name)
        
randomEpisode=RandomEpisode()
randomEpisode.pick_random_episode()

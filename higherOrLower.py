import art 
import game_data
import random 


#randomly select two keys from a dict 
len_data = len(game_data.data)
person_1 = random.randint(0,len_data-1)
person_2 = random.randint(0,len_data-1)
if(person_1==person_2):
  person_2 = random.randint(0,len_data-1)




#comparing it
score = 0 
stop = False
while(not stop):
  clear()
  print(art.logo)
  print("A" + game_data.data[person_1]['name'])
  print(art.vs)
  print("B" + game_data.data[person_2]['name'])
  answer = input("Who has got not follower A or B")
  if(answer=="a" or answer=="A"):
    if(game_data.data[person_1]['follower_count']>game_data.data[person_2]['follower_count']):
      person_1 = person_1
      person_2 = random.randint(0,len_data-1)
      
      score = score + 1
    else:
      stop = True 
  
  elif(answer=="b" or answer=="B" ):
    if(game_data.data[person_1]['follower_count']<game_data.data[person_2]['follower_count']):
      person_1 = person_2
      person_2 = random.randint(0,len_data-1)
      score = score + 1
    else :
      stop = True

print("final score = " + str(score))
  
  

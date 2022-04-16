#fighting game OOPS concept in python - date:::2022/04/13(start) -- 2022/04/16(end)
import time
import random
import json
import os
data={
      }
def save_data():
    with open("game_data.json","w") as f:
       json.dump(data,f)
       
def read_data():
    global data
    with open("game_data.json","r") as f:
     data=json.load(f)       
read_data()
class creator:
    def __init__(self,life,damage,defense):
        self.life=life
        self.damage=damage
        self.defense=defense 
        self.level=1
        self.experience=0
        self.critical=10
        self.penetrating=10
        self.boss_level=1
    def attack(self,user):
        if random.randint(1,100)<=self.critical:
            if random.randint(1,100)<=self.penetrating:
                user.life-=(self.damage)*2
            else:
                user.life-=(self.damage-user.defense)*2    
        else:
            if random.randint(1,100)<=self.penetrating:
                user.life-=self.damage
            else:
                user.life-=(self.damage-user.defense)    
def increase_level():
    hero.level+=1
    data["level"]+=1
    save_data()
    print(f"Your level is {hero.level}.")    
    print("""
          1. To increase the life
          2. To increase the defense
          3. To increase the damage
          4. To increase the critical
          5. To increae the penetrating""")
    option = int(input("Choose the option:"))
    if option==1:
        hero.life+=10
        data["life"]+=10
        save_data()
        print(f"Now you have {hero.life} life")
    elif option==2:
        hero.defense+=3
        data["defense"]+=3
        save_data()
        print(f"Now you have {hero.defense} defense")
    elif option==3:
        hero.damage+=3
        data["damage"]+=3
        save_data()
        print(f"Now you have {hero.damage} damage")
    elif option==4:
        hero.critical+=3
        data["critical"]+=3
        save_data()
        print(f"Now you have {hero.critical} critical hit chance") 
    elif option==5:
        hero.penetrating+=3
        data["penetrating"]+=3
        save_data()
        print(f"Now you have {hero.penetrating} penetrating")
    else: 
        pass        
hero = creator(data["life"],data["damage"],data["defense"])
hero.level=data["level"]
hero.experience=data["experience"]
hero.boss_level=data["boss_level"]
hero.critical=data["critical"]
hero.penetrating=data["penetrating"]
creature= creator(40,20,10)
def show(a):
    print(f"""
          life:{a.life} 
          defense:{a.defense}
          damage:{a.damage}
          penetrating:{a.penetrating}
          critical:{a.critical}
         """)
def boss_attack():
    
 boss=creator(100+ (10*hero.boss_level),30+ (10*hero.boss_level),12+ (10*hero.boss_level))
 print("The current power of hero are:")
 show(hero)
 print("The current power of boss are::")
 show(boss)
 exp_hero=hero.life
 print("""
       1.Enter 1 for detail version
       2.Enter 2 for short version
       """)
 version=int(input("Choose the version"))
 if version==1:
  while True:
     input("press enter to attack the boss")
     time.sleep(2)
     hero.attack(boss)
     if boss.life<=0:
         print("Boss is death, You won!!")
         hero.boss_level+=1
         hero.life=exp_hero
         data["boss_level"]+=1
         save_data()
         break
     print(f"The remainning life of boss is {boss.life}")
     time.sleep(2)
     print("Boss is attacking you")
     boss.attack(hero)
     if hero.life<=0:
         print("You are death, You lost !!!")
         hero.life=exp_hero
         break
     print(f"You have {hero.life} life left")
 elif version==2:
     while True:
      hero.attack(boss)
      if boss.life<=0:
         print("Boss is death, You won!!")
         hero.life=exp_hero
         hero.boss_level+=1
         data["boss_level"]+=1
         save_data()
         break
      boss.attack(hero)
      if hero.life<=0:
         print("You are death, You lost !!!")
         hero.life=exp_hero
         break
def creature_attack():
 creature_no=int(input("how many creatures you want to attack at once?"))
 exp_no=creature_no
 exp_hero=hero.life
 print("""
       1.Enter 1 for detail version
       2.Enter 2 for short version
       """)
 version=int(input("Choose the version"))
 if version==1:
  while True:
     input("press enter to attack the creature")
     time.sleep(2)
     hero.attack(creature)
     if creature.life<=0 and creature_no==1:
         print("Creatue is death, You won!!")
         hero.experience+=exp_no*50
         data["experience"]+=exp_no*50
         save_data()
         hero.life=exp_hero
         if hero.experience>=hero.level*100:
             increase_level()
             hero.experience=0
             data["experience"]=0
             
         break
     elif creature.life<=0 and creature_no>1:
         creature_no-=1
         print(f"you killed 1 creature and {creature_no} creature left")
         creature.life=90
         
     print(f"The remainning life of creature is {creature.life}")
     time.sleep(2)
     
     for i in range(creature_no):
      print("Creature is attacking you")
      creature.attack(hero)
     if hero.life<=0:
         print("You are death, You lost !!!")
         hero.life=exp_hero
         break
     print(f"You have {hero.life} life left")
 elif version==2:
     while True:
      time.sleep(2)
      hero.attack(creature)
      if creature.life<=0 and creature_no==1:
         print("Creatue is death, You won!!")
         hero.experience+=exp_no*50
         data["experience"]+=exp_no*50
         save_data()
         hero.life=exp_hero
         if hero.experience>=hero.level*100:
             increase_level()
             hero.experience=0
             data["experience"]=0
         break
      elif creature.life<=0 and creature_no>1:
         creature_no-=1
         creature.life=90
      
      time.sleep(2)
     
      for i in range(creature_no):
       creature.attack(hero)
      if hero.life<=0:
         print("You are death, You lost !!!")
         hero.life=exp_hero
         break

def main():
    while True:
     print(data)
     print(""""
Enter 1:: To attack creature
Enter 2:: To attack boss
Enter 3:: Exit
          """)
    
     chose = int(input("Enter the number:"))
     os.system('clr' if os.name == 'nt' else 'clear')
     if chose==1:
         creature_attack()
     if chose==2:
         boss_attack()
     if chose==3:
         break
main()
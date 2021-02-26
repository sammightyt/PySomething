
import time
import os
import math
import replit
import repltalk


def search():
  print("\nFile/Repl Number")
  file = input()
  if file == "1":
	  print("URL: https://docs.google.com/document/d/1gc5E3JaSgThEZhvn8QDqqv6zuJCcs1z2FTkF2_1dCtA/edit?usp=sharing")
    
	
  elif file == "2":
	  print("URL: https://docs.google.com/document/d/1YzKuKKu5UD4nUo3LM_8M83AJ_5LxoLUQv6VJvU4oJEo/edit?usp=sharing")
		
		
  elif file == "3":
	  print("URL: https://docs.google.com/document/d/1mlzIbQfHM_oE9sg6dVeDgfQryC1Po6oVE3ZcSVEDYdE/edit?usp=sharing")
		

  elif file == "4":
	  print("URL: https://flappybirdgame.sammightyt.repl.co/")

  elif file == "5":
    print("URL: https://flappy-birdgame.suryabhattiprol.repl.co/")
  
  elif file == "6":
    print("URL: https://flappyoops.laksh123.repl.co/")

  elif file == "7":
    print("URL: https://flappyoops.nishwanthgopu.repl.co/")

  elif file == "8":
    print("URL: https://pong-js.sammightyt.repl.co/")

  elif file == "9":
    print("URL: https://snowman-template.sammightyt.repl.co/")

  elif file == "10":
    print("URL: https://google.sammightyt.repl.co/")

  elif file == "11":
    print("URL: https://google-homepagefun.suryabhattiprol.repl.co/")

  elif file == "12":
    print("URL: https://dangerous-forest.diyasateesh21.repl.co/")

  elif file == "13":
    print("URL: https://picture-this.diyasateesh21.repl.co/")

  elif file == "14":
    print("URL: https://repl.it/@sammightyt/RPS?v=1")

  else:
	  print("\nFile does not exist")
  time.sleep(1)
  print("\nDo you want to search again?")
  whut = input()
  if whut == "yes":
    search()
  else:
    print("\nOk bye!")
    

	

		
	

def start():
  print("\nDr.Code: Welcome to Pysearcher!")
  print("\nFiles:")
  print("\n[1] 001-A-X")
  print("[2] 001-B-Y")
  print("[3] 001-B-Z")
  print("\nIn Progress:")
  print("\n[4] Flappy Bird-Samhith")
  print("[5] Flappy Bird-Surya") 
  print("[6] Flappy Bird-Laksh")
  print("[7] Flappy Bird-Nishwanth")
  print("\nSamhith:")
  print("\n[8] Pong")
  print("[9] Canvas Snowman")
  print("\nExclusive Content:")
  print("\n[10] Google-Samhith")
  print("[11] Google-Surya")
  print("[12] Dangerous Forest-Diya/Riya")
  print("[13] Picture This!-Diya")
  print("[14] Rock Paper Scissors-Samhith")
  search()

def a():
  print("\nPassword pls")
  some = input()
  waa = os.getenv('TOKEN')
  if some == waa:
    time.sleep(1)
    replit.clear()
    print("\nloading Pysearcher...")
    time.sleep(3)
    print("\nloading drCode...")
    time.sleep(3)
    print("\nloading kinPy...")
    time.sleep(5)
    print("\nloading samPy...")
    time.sleep(7)
    replit.clear()
    start()
    

  else:
    print("\nI will give u one more chance")
    a()
a()

def restart():
  search()
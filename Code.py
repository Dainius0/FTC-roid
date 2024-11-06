x = float(input("Įveskite sumą, kurią norėtumėte išleisti:"))
print("Galite įsigyti:")

if x >= 1.5: 
  print("1. Saldainiai")
  print("2. Kramtomoji guma")
  print("3. Traškučiai") 
  print("4. Gėrimas")

elif x>=1:
  print("1. Saldainiai")
  print("2. Kramtomoji guma")
  print("3. Traškučiai")
elif x>=0.75:
  print("1. Saldainiai")
  print("2. Kramtomoji guma")
elif x>=0.5: 
  print("1. Saldainiai")
else:
  print(f'Jūsų įvestos sumos nepakanka jokiems daiktams įsigyti')
        
        
a = int(input(f"Įveskite passirinkimo numerį: "))     
if a == 1 and x >= 0.5:
  print("Pasirinkote Saldainiai.")
  b=x-0,5
  print(f"ėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
  
if a == 2 and x >= 0.75:
  print("Pasirinkote Kramtomoji guma.")
  b=x-0,75
  print(f"ėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
  
if a == 3 and x>=1:
  print("Pasirinkote Traškučiai.")
  b=x-1
  print(f"ėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
if a == 4 and x >= 1.5:
  print("Pasirinkote Gėrimas.")
  b=x-1,5

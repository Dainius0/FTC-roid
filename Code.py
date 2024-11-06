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
  b=float(x-0.5)
  b=round(b,2)
  print(f"Dėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
elif a == 2 and x >= 0.75:
  print("Pasirinkote Kramtomoji guma.")
  b=float(x-0.75)
  b=round(b,2)
  print(f"Dėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
  
elif a == 3 and x>=1:
  print("Pasirinkote Traškučiai.")
  b=float(x-1)
  b=round(b,2)
  print(f"Dėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
elif a == 4 and x >= 1.5:
  print("Pasirinkote Gėrimas.")
  b=float(x-1.5)
  b=round(b,2)
  print(f"Dėkojame už Jūsų pirkinį. Jūsų likutis yra €{b}.")
else:
  print(f'Nėra sąraše')

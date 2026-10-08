
def check (Regist, Curn, Region, Brand, Color, Power, CarYear, Milage = 'none'):
  if type(Regist) == str and len(Regist) <= 10:

    if type(Curn) == str and len(Curn) <= 6:

      if type(Region) == int:

        if type(Brand) == str and len(Curn) <= 50:

          if type(Color) == str and len(Curn) <= 50:

            if type(Power) == int and Power > 50:

              if type(CarYear) == int:

                if type(Milage) == int:
                  return(True)
  
            
 
carsData = [('9844720488', 'E340BT', 77, 'Lada Granta','Красный', 87, 2017, 35), 
            ('6239572784', 'H109OK', 178, 'Volkswagen Polo','Синий', 15, 2018, 40), 
            ('6239572784', 'A822EY', 99, 'Skoda Rapid','Черный', 125, 2021, 35), 
            ('7984672834', 'T120AA', 98, 'Hyundai Solaris','Черный', 123, 2019, 20), 
            ('7478679847', 'B971HP', 199, 'Kia Sportage','Белый', 184, 2017, 35), 
            ('4728472878', 'T120AA', 77, 'Toyota RAV4','Серебристо-серый', 146, 2008, ), 
            ('4782487387', 'H454EE', 98, 'Skoda Rapid','Черный', 75, 2021, 0), 
            ('9884274842', 'O638OA', 173, 'Mitsubishi Outlander','Белый', 230, 2021, ), 
            ('7284728297', 'T120AA', 77, 'Hyundai Solaris','Синий', 123, 2021, 0), 
            ('8779854025', 'A352EE', 98, 'Lada Granta','Белый', 87, 2017, 54)]

result = []
for i in carsData:
  if check(*i):
    print(i)
  


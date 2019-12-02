import pandas as pd
############################################################################
# CSV Files 
#Rates_Info = pd.read_csv("Rates.csv")
Variations_Info = pd.read_csv("Variations.csv")
############################################################################
# Rates 
Posi_Truck = 143            #/hr
Excavator_5_T = 121         #/hr
Excavator_15_T = 135        #/hr
Supervisor = 90             #/hr
Spotter = 65                #/hr
Asphalt_Disposal = 850      #/Truck
Geotech_Inspection = 1430   #/hr
Saw_Cut = 150               #/hr
############################################################################
Dates = []
Resources = []
Units = []
Quantities = []
Amounts = []

for i in range(len(Variations_Info)):
    Date = Variations_Info.at[i,"Date"]
    Dates.append(Date)
    Resource = Variations_Info.at[i,"Resource"]
    Resources.append(Resource)
    Unit = Variations_Info.at[i,"Unit"]
    Units.append(Unit)
    Quantity = Variations_Info.at[i,"Quantity"]
    Quantities.append(Quantity)
    if Resource == "15T Excavator":
        Amount = Quantity * Excavator_15_T
        Amounts.append(Amount)
    elif Resource == "5T Excavator":
        Amount = Quantity * Excavator_5_T
        Amounts.append(Amount)
    elif Resource == "Spotter":
        Amount = Quantity * Spotter
        Amounts.append(Amount)
    elif Resource == "Supervisor":
        Amount = Quantity * Supervisor
        Amounts.append(Amount)
    elif Resource == "Positruck" or "Positrack" or "Posi Truck":
        Amount = Quantity * Posi_Truck
        Amounts.append(Amount)
    else:
        print("Typo or not in if-statement!")

############################################################################    
Dates_Table = pd.DataFrame({'Date': Dates})
Resources_Table = pd.DataFrame({'Resource': Resources})
Units_Table = pd.DataFrame({'Unit': Units})
Quantities_Table = pd.DataFrame({'Quantity': Quantities})
Amounts_Table = pd.DataFrame({'Amounts': Amounts})
Final_Table = pd.concat([Dates_Table, Resources_Table, Units_Table, Quantities_Table, Amounts_Table], axis=1)
print(Final_Table)
Final_Table.to_csv("Completed_Variations.csv")
############################################################################

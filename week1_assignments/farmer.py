Total_acres=80
Each_segement_acres=Total_acres/5
# for tomato

Acres_30_percent = 0.3 * Each_segement_acres
Acres_70_percent = 0.7 * Each_segement_acres

Number_of_tonnes_of_tomato_on_30 = Acres_30_percent * 10
Number_of_tonnes_of_tomato_on_70 = Acres_70_percent * 12
Total_Number_of_tonnes_of_tomato = Number_of_tonnes_of_tomato_on_30 + Number_of_tonnes_of_tomato_on_70
Total_Number_of_kg_of_tomato = Total_Number_of_tonnes_of_tomato * 1000
Cost_of_each_kg_of_tomato = 7
Sales_of_tomato = Total_Number_of_kg_of_tomato * Cost_of_each_kg_of_tomato
# for potatoes
Number_of_tonnes_of_potato_per_acres = 10
Total_Number_of_tonnes_of_potato = 10 * Each_segement_acres
Total_Number_of_kg_of_potato = Total_Number_of_tonnes_of_potato * 1000
Cost_of_each_kg_of_potato = 20
Sales_of_potato = Total_Number_of_kg_of_potato * Cost_of_each_kg_of_potato
# for cabbage 
Number_of_tonnes_of_cabbage_per_acres = 14
Total_Number_of_tonnes_of_cabbage = 14 * Each_segement_acres
Total_Number_of_kg_of_cabbage = Total_Number_of_tonnes_of_cabbage * 1000
Cost_of_each_kg_of_cabbage = 24
Sales_of_cabbage = Cost_of_each_kg_of_cabbage * Total_Number_of_kg_of_cabbage
# for sunflower
Number_of_tonnes_of_sunflower_per_acres = 0.7
Total_Number_of_tonnes_of_sunflower = 0.7 * Each_segement_acres
Total_Number_of_kg_of_sunflower = Total_Number_of_tonnes_of_sunflower * 1000
Cost_of_each_kg_of_sunflower = 200
Sales_of_sunflower = Total_Number_of_kg_of_sunflower * Cost_of_each_kg_of_sunflower
# for sugarcane
Number_of_tonnes_of_sugarcane_per_acres = 45
Total_Number_of_tonnes_of_sugarcane = Number_of_tonnes_of_sugarcane_per_acres * Each_segement_acres
Total_Number_of_kg_of_sugarcane = Total_Number_of_tonnes_of_sugarcane * 1000
Cost_of_each_kg_of_sugarcane = 4000
Sales_of_sugarcane = Cost_of_each_kg_of_sugarcane * Total_Number_of_kg_of_sugarcane
overall_sales = Sales_of_cabbage + Sales_of_potato + Sales_of_sugarcane + Sales_of_sunflower + Sales_of_tomato
print("overall sales achieved by mahesh from the 80 acres of land is :",overall_sales)
Sales_realisation_from_chemical_free_farming_at_the_end_of_11_months = Sales_of_cabbage + Sales_of_potato +Sales_of_sunflower + Sales_of_tomato
print("Sales realisation from chemical-free farming at the end of 11 months",Sales_realisation_from_chemical_free_farming_at_the_end_of_11_months )
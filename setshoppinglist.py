Shopping_list_Iteam=[]
Iteam_price=[]
num_list = int(input("How many iteams in list?"))

for i in range(num_list):
    Iteams= input(f"\nEnter iteam name{i+1}:")
    Price= int(input(f"\nEnter the  Price of {Iteams}:"))
    Shopping_list_Iteam.append(Iteams)
    Iteam_price.append( Price)
    
print("\n---SHOPPING LIST---")
for i in range(len(Shopping_list_Iteam)):
    print(f"{Shopping_list_Iteam[i]}-{Iteam_price[i]} Price")

highest_Iteam_Price = max(Iteam_price)
lowest_Iteam_Price = min(Iteam_price)
average_Of_All = sum(Iteam_price)/ len(Iteam_price)

print("\n---SHOPPING LIST STATIC---")
print("Highest Price Iteam In The List:",highest_Iteam_Price)
print("Lowest Price Iteam In The List ",lowest_Iteam_Price)
print("Average Price Of All Iteams In The List\n",average_Of_All)
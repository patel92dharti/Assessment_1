import csv
class Fruit_Manager:

    def add_fruit(self,f_name,f_qty,f_price):
        
        
        self.f_name=f_name
        self.f_qty=f_qty
        self.f_price=f_price
        filed_name=['Fruit_Name','Fruit_Qty','Fruit_Price']

        
        all={'Fruit_Name':self.f_name,'Fruit_Qty':self.f_qty,'Fruit_Price':self.f_price}
        print(all)
        with open("data.csv","a") as d:
            writer=csv.DictWriter(d,fieldnames=filed_name)
            writer.writeheader()
            writer.writerow(all)
         
        d.close()

        print("Successfully Added")


    def view_fruit(self):

        with open("data.csv",newline='') as d:
            reader=csv.DictReader(d)
            for row in reader:
                print(row)
        d.close()
    def update_fruit_Qty(self,f_qty):
        self.f_qty=f_qty
        return self.f_qty
    def update_fruit_Price(self,f_price):
        self.f_price=f_price
        return self.f_price
       
fm=Fruit_Manager()


while True:

    print("*"*30+" Welcome to Fruit Market "+"*"*30)
    print("1). Manager")
    print("2). Customer")
    print("3). Exit")

    choice=int(input("Select Your Role: "))
    if choice==1:
        while True:
            print("*"*30+" Fruit Market Manager "+"*"*30)
            print("1). Add Fruit Stock")
            print("2). View Fruit Stock")
            print("3). Update Fruit Stock")
            print("4). Exit")

            choice=int(input("Enter Your Role: "))
            
            if choice==1:
                print("*"*30+" ADD Fruit STOCK "+"*"*30)
                F_name=input("Enter Fruit Name:")
                F_Oty=int(input("Enter Qty (in kg): "))
                F_price=int(input("Enter Price (For Kg) :"))
                fm.add_fruit(F_name,F_Oty,F_price)
                print("*"*30+" Your Stock has been Added Successfully "+"*"*30)
                choice=input("Do You want to perform more operation: Press y for Yes and n for No: ")
                
                if choice=="y":
                    continue
                            
                else:
                    break
            elif choice==2:
                print("*"*30+" View Fruit STOCK "+"*"*30)
                fm.view_fruit()
                continue
            elif choice==3:
                print("*"*30+" Update Fruit STOCK "+"*"*30)
                fm.view_fruit()
                F_name=input("Enter Fruit Name:")
                with open("data.csv","r") as d:
                    reader=csv.DictReader(d)
                    for key,row in reader:
                        print(key)
                        print(row)
                        if F_name==row:
                            while True:
                                print("1). Update Qty")
                                print("2). Update Price")
                                print("3). Exit")
                                choice=int(input("Enter your Choice: "))
                                if choice==1:
                                    F_Oty=int(input("Enter Qty (in kg): "))
                                    fm.update_fruit_Qty(F_Oty)
                                    print("Qty Updated Succesfully")
                                    continue
                                elif choice==2:
                                    F_price=int(input("Enter Price (For Kg) :"))
                                    fm.update_fruit_Price(F_price)
                                    print("Price Updated Successfully")
                                    continue
                                else:
                                    break
            
            else:
                break
    elif choice==2:
        print("*"*30+" View Fruit STOCK "+"*"*30)
        fm.view_fruit()
        continue
    else:
        print("*"*30+" Good Bye "+"*"*30)
        break
        
                





        


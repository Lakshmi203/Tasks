try:
    amount = int(input("enter the amount "))
    def breakdown(amount):
     
        notes = [2000, 500, 200, 100,
                50, 20, 10, 5, 1]
                
        noteCounter = [0, 0, 0, 0, 0,
                        0, 0, 0, 0]
     
        denominations = {}
        for i, j in zip(notes, noteCounter):
        
            if amount >= i:
                j = amount // i
                amount = amount - j * i
            
        
            denominations[i]=j
        print(denominations)
    breakdown(amount)
except:
    print("an error occurred")

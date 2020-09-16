
# Skapa ett program där användaren får upp fyra frågor 
# om att mata in ett tal. Spara alla talen i en array. 
# Loopa igenom arrayen och ta fram det tal som är störst. 
# Skriv tillbaka resultatet på skärmen för användaren. 
allNumbers = []
for num in range(0,4):
    print(f"Mata in tal nummer:{num+1}:")     
    number = int(input())
    allNumbers.append(number)

biggestSoFar = allNumbers[0]
for num in allNumbers:
    if(num > biggestSoFar):
        biggestSoFar = num

print(f"Störst var {biggestSoFar}")       

#Dynamisk datastruktur (en låda som kan rymma
#många saker - och vi behöver inte veta
#på förhand hur många) 

#KLUMPA IHOP MÅNGA SAKER -> SAMMA NAMN

stefansBarn = ["Fanny", "Josefine", "Oliver"]
for namn in stefansBarn:
    print(namn)

print(stefansBarn[0])

stefansBarn[1] = "Josefin"



listOfPlayers = []

while True:
    print("*** HOCKEYSPELARDATABASEN ***")
    print("1. Skapa ny")
    print("2. Lista")
    print("3. Exit")
    selection = input("Välj:")
    if(selection == "3"):
        break
    if(selection == "2"):
        print("*******LISTA PÅ ALLA******")
        for namn in listOfPlayers:
            print(namn)
    if (selection == "1"):
        namn = input("Ange namn på den legendariska spelaren:")
        listOfPlayers.append(namn)



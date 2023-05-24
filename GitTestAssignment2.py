def main():

    #Input user's systolic and diastolic pressure and determine the user's pulse pressure
    def inFunction():
        sp = float(input("What is your systolic pressure?(SP):"))
        dp = float(input("What is your diastolic pressure(DP):"))

        pulsePressure = sp - dp

        print("Your Pulse Pressure(PP) is:", pulsePressure)

        return pulsePressure, sp, dp

    #Check the user's pulse and determine if it is within a normal range
    def pulseCheck(pulsePressure):
        if pulsePressure >= 80:
            print("Your blood pressure is high! Seek medical attention!")
        elif pulsePressure <= 80:
            print("Your blood pressure is normal")
        else:
            print("Invalid Input")


    def mapCalculation(dp, pulsePressure):
        map = dp + (pulsePressure / 3)
        print("Your mean artial pressure is: ", pulsePressure)

        return map
        
    def mapCheck(map):
        if map >= 60:
            print("Your Mean Artial Pressure is within acceptable limits")
        elif map <= 60:
            print("Your Mean Artial Pressure is low. Seek medical attention immediately!")

        return map

    pulsePressure = 0
    dp = 0
    map = 0

    inFunction()

    pulseCheck(pulsePressure)

    mapCalculation(dp,pulsePressure)

    mapCheck(map)

main()
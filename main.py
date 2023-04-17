# import elev
import studentHandler

looping = True
school = studentHandler.PrintMeny()


while looping == True:

    mainMenuVal = school.testprint()

    
    if mainMenuVal == "4":
        break
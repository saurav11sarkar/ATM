while True:
    try:
        number = int(input("Enter your number : "))
        break
    except ValueError:
        print("You did'n enter your number")
    except:
        print("a unknow error")
print("thank you for Enter your number")

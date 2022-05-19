Answer = input("Do you take the red pill, or the blue pill?").lower()
if Answer == "red":
    raise NameError("It's time to go postal.")
if Answer == "blue":
    raise NameError("Wake up.")
else:
    raise NameError(". . .")
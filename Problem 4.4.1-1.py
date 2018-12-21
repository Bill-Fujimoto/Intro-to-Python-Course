def saveUserInfo(username, value, password):
    usernameFile = open("Username.txt", "w")
    accountValueFile = open("AccountValue.txt", "w")
    passwordFile = open("Password.txt", "w")
    usernameFile.write(username)
    print(value, file = accountValueFile)#accountValueFile.write(value)
    passwordFile.write(password)
    usernameFile.close()
    accountValueFile.close()
    passwordFile.close()

saveUserInfo("RamblinWreck20", 222, "burd311")
saveUserInfo("SpursFan14", str(150), "ginobili!")
saveUserInfo("Jolteon911", str(225), "thunderbolt")

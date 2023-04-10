from cryptographyFramework import *

initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, "magrão = kanye west")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "kanye west = magroncio")
saveNewLine(encryptedText)


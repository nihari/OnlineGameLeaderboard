from BoardGame.gameControl import gameControl

print("inside project")
print("inside projectrr")

gameController = gameControl()

gameController.UPSERT_USER("niha", "India", "niharika@gmail.com")
gameController.UPSERT_USER("Nilay", "India", "nilay@letstransport.team")
gameController.UPSERT_USER("Parijat", "India", "parijat@letstransport.team")

A = gameController.userDetails
for i in range(len(A)):
  print(A[i].name + " ")

gameController.UPSERT_SCORE("niharika@gmail.com", 10)
gameController.UPSERT_SCORE("parijat@letstransport", 1)
gameController.UPSERT_SCORE("nilay@letstransport.team", 15)

gameController.UPSERT_USER("Keshow", "Argentina", "keshow@l")

gameController.GET_TOP(3)


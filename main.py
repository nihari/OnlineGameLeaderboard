from BoardGame.gameControl import gameControl

gameController = gameControl()

gameController.UPSERT_USER("niha", "India", "niharika@gmail.com")
gameController.UPSERT_USER("Nilay", "china", "nilay@letstransport.team")
gameController.UPSERT_USER("Parijat", "India", "parijat@letstransport.team")
gameController.UPSERT_USER("Parat", "India", "parijat@letstransport.team")

gameController.UPSERT_SCORE("niharika@gmail.com", 1)
gameController.UPSERT_SCORE("parijat@letstransport.team", 0)
gameController.UPSERT_SCORE("nilay@letstransport.team", 10)

gameController.UPSERT_USER("Keshow", "Argentina", "keshow@l")

gameController.UPSERT_SCORE("keshow@l", 1)

gameController.GET_TOP(3)
gameController.GET_TOP(2, "India")
gameController.GET_TOP(0)


gameController.GET_USERS_WITH_SCORE(-2)
gameController.GET_USERS_WITH_SCORE(1)

gameController.SEARCH(None, None, "India")
gameController.SEARCH(None, 15, "India")
gameController.SEARCH(None, 10, None)
gameController.SEARCH(None, 10, "India")

gameController.GET_RANGE(1,10)
gameController.GET_RANGE(5,10)

gameController.SEARCH_NAME("ha")
gameController.SEARCH_NAME("ihhj")




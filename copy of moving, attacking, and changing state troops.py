    for player1NumTroop in range(len(player1TroopTypeList)):

        annimateAndmoveTroops("swordMan", player1SwordmanRange, swordManSpeedX, swordManPic, swordManY)

        #sword man 
        if player1TroopTypeList[player1NumTroop] == "swordMan" and player1TroopHealthList[player1NumTroop] > 0:

            # changes state to moving when there are no enemies in front
            player1TroopStateList[player1NumTroop] = "moving"

            if len(player2TroopTypeList) > 1:

                # change state to attacking when enemy in front
                if player1TroopXList[player1NumTroop] >= player2FirstTroop + player1SwordmanRange:
                    player1TroopStateList[player1NumTroop] = "attacking"

            elif len(player2TroopTypeList) == 1:

                # changes state to attacking when tower in front
                if player1TroopXList[player1NumTroop] >= player2FirstTroop + player1SwordmanRange:
                    player1TroopStateList[player1NumTroop] = "attacking"



            # change state back to moving
            elif len(player2TroopHealthList) >= 1 :
                player1TroopStateList[player1NumTroop] = "moving"

            else:
                player1TroopStateList[player1NumTroop] = "moving"


            if player1TroopStateList[player1NumTroop] == "moving":
                #moving annimation
                player1TroopXList[player1NumTroop] += swordManSpeedX
                gameWindow.blit(swordManPic[frame% 3 + 3], (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
                letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX, swordManY))


            elif player1TroopStateList[player1NumTroop] == "attacking" and len(player2TroopHealthList) > 0:
                #attacking animation
                player2TroopHealthList[player2FirstTroopIndex] -= player1SwordmanDamage
                gameWindow.blit(swordManPic[frame % 3 ], (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
                letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX, swordManY))



        #bomb man
        if player1TroopTypeList[player1NumTroop] == "bombMan" and player1TroopHealthList[player1NumTroop] > 0:

            # changes state to moving when there are no enemies in front
            player1TroopStateList[player1NumTroop] = "moving"

            if len(player2TroopTypeList) > 1:

                # change state to attacking when enemy in front
                if player1TroopXList[player1NumTroop] >= player2FirstTroop + player1BombManRange:
                    player1TroopStateList[player1NumTroop] = "attacking"

            elif len(player2TroopTypeList) == 1:

                # changes state to attacking when tower in front
                if player1TroopXList[player1NumTroop] >= player2FirstTroop + player1BombManRange:
                    player1TroopStateList[player1NumTroop] = "attacking"


            if player1TroopStateList[player1NumTroop] == "moving":
                #moving animation
                player1TroopXList[player1NumTroop] += bombManSpeedX
                gameWindow.blit(bombManPic[frame% 3 + 3], (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
                letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX, bombManY))


            elif player1TroopStateList[player1NumTroop] == "attacking" and len(player2TroopHealthList) > 0:
                #attacking animation
                player2TroopHealthList[player2FirstTroopIndex] -= player1BombManDamage
                gameWindow.blit(bombManPic[frame % 3], (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
                letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX, bombManY))



        #dragon
        if player1TroopTypeList[player1NumTroop] == "dragon" and player1TroopHealthList[player1NumTroop] > 0:


            # changes state to moving when there are no enemies in front
            player1TroopStateList[player1NumTroop] = "moving"

            if len(player2TroopTypeList) > 1:

                # change state to attacking when enemy in front
                if player1TroopXList[player1NumTroop] >= player2FirstTroop + player1DragonRange:
                    player1TroopStateList[player1NumTroop] = "attacking"

            elif len(player2TroopTypeList) == 1:

                # changes state to attacking when tower in front
                if player1TroopXList[player1NumTroop] >= player2FirstTroop + player1DragonRange:
                    player1TroopStateList[player1NumTroop] = "attacking"


            if player1TroopStateList[player1NumTroop] == "moving":
                # moving animation
                player1TroopXList[player1NumTroop] += fireDragonSpeedX
                gameWindow.blit(fireDragonPic[frame % 3 + 3], (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
                letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX, fireDragonY))

            if player1TroopStateList[player1NumTroop] == "attacking" and len(player2TroopHealthList) > 0:
                # attacking animation
                player2TroopHealthList[player2FirstTroopIndex] -= player1DragonDamage
                gameWindow.blit(fireDragonPic[frame % 3], (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
                letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX, fireDragonY))




    #cycles through list of troops for player 2
    for player2NumTroop in range(len(player2TroopTypeList)):

        #sword man
        if player2TroopTypeList[player2NumTroop] == "swordMan" and player2TroopHealthList[player2NumTroop] > 0:

            #changes state to moving when there are no enemies in front
            player2TroopStateList[player2NumTroop] = "moving"

            if len(player1TroopTypeList) > 1:

                # change state to attacking when enemy in front
                if player2TroopXList[player2NumTroop] <= player1FirstTroop + player2SwordmanRange :
                    player2TroopStateList[player2NumTroop] = "attacking"

            elif len(player1TroopTypeList) == 1:

                #changes state to attacking when tower in front
                if player2TroopXList[player2NumTroop] <= player1FirstTroop + player2SwordmanRange :
                    player2TroopStateList[player2NumTroop] = "attacking"


            if player2TroopStateList[player2NumTroop] == "moving":
                #moving annimation
                player2TroopXList[player2NumTroop] -= swordManSpeedX
                gameWindow.blit(player2SwordManPic[frame% 3 + 3], (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
                letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX, swordManY))


            elif player2TroopStateList[player2NumTroop] == "attacking" and len(player1TroopHealthList) > 0:
                #attacking animation
                player1TroopHealthList[player1FirstTroopIndex] -= player2SwordmanDamage
                gameWindow.blit(player2SwordManPic[frame % 3 ], (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
                letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX, swordManY))



        # bomb man
        if player2TroopTypeList[player2NumTroop] == "bombMan" and player2TroopHealthList[player2NumTroop] > 0:

            # changes state to moving when there are no enemies in front
            player2TroopStateList[player2NumTroop] = "moving"


            if len(player1TroopTypeList) > 1:

                # change state to attacking
                if player2TroopXList[player2NumTroop] <= player1FirstTroop + player2BombManRange:
                    player2TroopStateList[player2NumTroop] = "attacking"

            elif len(player1TroopTypeList) == 1:

                #changes state to attacking when tower in front
                if player2TroopXList[player2NumTroop] <= player1FirstTroop + player2BombManRange :
                    player2TroopStateList[player2NumTroop] = "attacking"


            if player2TroopStateList[player2NumTroop] == "moving":
                # moving animation
                player2TroopXList[player2NumTroop] -= bombManSpeedX
                gameWindow.blit(player2BombManPic[frame % 3 + 3], (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
                letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX, bombManY))


            elif player2TroopStateList[player2NumTroop] == "attacking" and len(player1TroopHealthList) > 0:
                # attacking animation
                player1TroopHealthList[player1FirstTroopIndex] -= player2BombManDamage
                gameWindow.blit(player2BombManPic[frame % 3 ], (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
                letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX, bombManY))



        # dragon
        if player2TroopTypeList[player2NumTroop] == "dragon" and player2TroopHealthList[player2NumTroop] > 0:

            # changes state to moving when there are no enemies in front
            player2TroopStateList[player2NumTroop] = "moving"

            if len(player1TroopTypeList) > 1:

                # change state to attacking when enemy in front
                if player2TroopXList[player2NumTroop] <= player1FirstTroop + player2DragonRange:
                    player2TroopStateList[player2NumTroop] = "attacking"

            elif len(player1TroopTypeList) == 1:

                # changes state to attacking when tower in front
                if player2TroopXList[player2NumTroop] <= player1FirstTroop + player2DragonRange:
                    player2TroopStateList[player2NumTroop] = "attacking"


            if player2TroopStateList[player2NumTroop] == "moving":
                # moving animation
                player2TroopXList[player2NumTroop] -= fireDragonSpeedX
                gameWindow.blit(player2FireDragonPic[frame % 3 + 3],(player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
                letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX, fireDragonY))

            if player2TroopStateList[player2NumTroop] == "attacking" and len(player1TroopHealthList) > 0:
                # attacking animation
                player1TroopHealthList[player1FirstTroopIndex] -= player2DragonDamage
                gameWindow.blit(player2FireDragonPic[frame % 3 ], (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
                letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
                gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX, fireDragonY))

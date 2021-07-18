import sys
import math
import pandas as pd
import numpy as np
import random

# Carte
factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
carte = []
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    carte.append([factory_1, factory_2, distance])
df_carte = pd.DataFrame(carte, columns=['factory_1', 'factory_2', 'distance'])

# Ressources
bombs = 2
turn = 1

# game loop
while True:
    factories = []
    troops = []

    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])

        if entity_type == 'FACTORY':
            factories.append([entity_type,entity_id,arg_1,arg_2,arg_3])
        elif entity_type == 'TROOP':
            troops.append([entity_type,entity_id,arg_1,arg_2,arg_3,arg_4,arg_5])

    df_factories = pd.DataFrame(factories,columns=['type','id','player','cyborgs','prod'])
    df_troops = pd.DataFrame(troops,columns=['type','id','player','from_fct','to_fct','qty','turn_2_go'])

    #print(df_factories, file=sys.stderr)
    #print(df_troops, file=sys.stderr)

    # Game engine
    go = False
    go_bomb = False
    ordre = 'WAIT'
    tries = 0

    while not go:

        # Trouve la factory enemie avec le plus de cyborgs
        list_en_fact = list(df_factories[df_factories['player'] == -1].sort_values('cyborgs',ascending=False).index)
        if len(list_en_fact) >= 2 and bombs > 0:
            go_bomb = True
            bomb_1 = df_factories.iloc[list_en_fact[0]]['id']
            bomb_2 = df_factories.iloc[list_en_fact[1]]['id']
            print(bomb_1, bomb_2, file = sys.stderr)

        # Trouve une factory a moi
        list_from = list(df_factories[df_factories['player'] == 1].index)
        from_id = random.sample(list_from,1)[0]
        print('FROM',from_id, file=sys.stderr)

        FROM = df_factories.iloc[from_id]['id']
        cyborg_dispo = df_factories[df_factories['id'] == FROM]['cyborgs'].iloc[0]

        # Trouve une factory enemie ou neutre
        list_to = list(df_factories[df_factories['player'] != 1].index)

        # Envoie bomb
        if go_bomb:
            b1 = "BOMB {} {}".format(FROM,bomb_1)
            b2 = "BOMB {} {}".format(FROM,bomb_2)
            ordre = b1+';'+b2
            bombs = 0
            go=True

        # Envoie cyborg
        elif len(list_to) > 0:
            to_id = random.sample(list_to,1)[0]
            print('TO',to_id, file=sys.stderr)

            TO = df_factories.iloc[to_id]['id']
            cyborg_requis = df_factories[df_factories['id'] == TO]['cyborgs'].iloc[0]

            print(FROM, cyborg_dispo, TO, cyborg_requis, file = sys.stderr)

            # Si ma factory a au moins & cyborg de plus que l'enemie, on y envoie requis+1
            surplus = 2
            if cyborg_dispo >= cyborg_requis+surplus:
                go = True
                ordre = "MOVE {} {} {}".format(FROM,TO,cyborg_requis+surplus)
        tries+=1
        if tries > 5:
            go = True
    
    turn+=1

    # Execute order
    print(ordre)

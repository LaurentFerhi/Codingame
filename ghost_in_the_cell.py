import sys
import math
import pandas as pd
import numpy as np
import random

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
carte = []
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    carte.append([factory_1, factory_2, distance])
df_carte = pd.DataFrame(carte, columns=['factory_1', 'factory_2', 'distance'])

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
    ordre = 'WAIT'
    tries = 0

    while not go:

        # Trouve une factory a moi
        list_from = list(df_factories[df_factories['player'] == 1].index)
        from_id = random.sample(list_from,1)[0]
        print('FROM',from_id, file=sys.stderr)

        FROM = df_factories.iloc[from_id]['id']
        cyborg_dispo = df_factories[df_factories['id'] == FROM]['cyborgs'].iloc[0]

        # Trouve une factory enemie ou neutre
        list_to = list(df_factories[df_factories['player'] != 1].index)

        if len(list_to) > 0:
            to_id = random.sample(list_to,1)[0]
            print('TO',to_id, file=sys.stderr)

            TO = df_factories.iloc[to_id]['id']
            cyborg_requis = df_factories[df_factories['id'] == TO]['cyborgs'].iloc[0]

            print(FROM, cyborg_dispo, TO, cyborg_requis, file = sys.stderr)

            # Si ma factory a au moins & cyborg de plus que l'enemie, on y envoie requis+1
            surplus = 1
            if cyborg_dispo >= cyborg_requis+surplus:
                go = True
                ordre = "MOVE {} {} {}".format(FROM,TO,cyborg_requis+surplus)
        
        tries+=1

        if tries > 10:
            go = True

    print(ordre)


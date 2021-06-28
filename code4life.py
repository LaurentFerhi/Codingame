import sys
import math
import pandas as pd
import numpy as np

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

step = 0 # 0: doit aller au diagnostic, 1: doit aller aux molécules, 2: doit aller au labo
mission = 1 # 0: a faire, 1: faite

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

# game loop
while True:
    for i in range(2):
        inputs = input().split()
        target = inputs[0]
        eta = int(inputs[1])
        score = int(inputs[2])
        storage_a = int(inputs[3])
        storage_b = int(inputs[4])
        storage_c = int(inputs[5])
        storage_d = int(inputs[6])
        storage_e = int(inputs[7])
        expertise_a = int(inputs[8])
        expertise_b = int(inputs[9])
        expertise_c = int(inputs[10])
        expertise_d = int(inputs[11])
        expertise_e = int(inputs[12])
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]

    sample_data = []
    sample_count = int(input())
    for i in range(sample_count):
        inputs = input().split()
        sample_id = int(inputs[0])
        carried_by = int(inputs[1])
        rank = int(inputs[2])
        expertise_gain = inputs[3]
        health = int(inputs[4])
        cost_a = int(inputs[5])
        cost_b = int(inputs[6])
        cost_c = int(inputs[7])
        cost_d = int(inputs[8])
        cost_e = int(inputs[9])

        sample_data.append([sample_id, carried_by,health,cost_a,cost_b,cost_c,cost_d,cost_e])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # DIAGNOSIS
    if step == 0 and mission == 1: # sort du labo avec mission accomplie (ou 1er tour)
        print("GOTO DIAGNOSIS")
        mission = 0

    elif step == 0 and mission == 0: # est au diagno avec mission a faire
        df_sample = pd.DataFrame(sample_data, columns=['id', 'carried_by','health','a','b','c','d','e'])
        df_to_pick = df_sample[df_sample['carried_by'] == -1].sort_values('health', ascending=False)

        # On prend le premier choix
        best_id = df_to_pick.iloc[0]['id']
        num_A = df_to_pick.iloc[0]['a']
        num_B = df_to_pick.iloc[0]['b']
        num_C = df_to_pick.iloc[0]['c']
        num_D = df_to_pick.iloc[0]['d']
        num_E = df_to_pick.iloc[0]['e']
        print(num_A,num_B,num_C,num_D,num_E, file=sys.stderr)
        print("CONNECT {}".format(best_id))
        
        # Mission accomplie, next step
        mission = 1
        step = 1

    # MOLECULES
    elif step == 1 and mission == 1: # sort du diagno avec mission accomplie (ou 1er tour)
        print("GOTO MOLECULES")

        # initialise les compteurs
        compteur_a = 0
        compteur_b = 0
        compteur_c = 0
        compteur_d = 0
        compteur_e = 0

        mission = 0

    elif step == 1 and mission == 0: # est au molecules avec mission a faire

        if compteur_a != num_A:
            print("CONNECT A")
            compteur_a += 1
        elif compteur_b != num_B:
            print("CONNECT B")
            compteur_b += 1
        elif compteur_c != num_C:
            print("CONNECT C")
            compteur_c += 1
        elif compteur_d != num_D:
            print("CONNECT D")
            compteur_d += 1
        elif compteur_e != num_E:
            print("CONNECT E")
            compteur_e += 1
        else:
            # Mission accomplie, next step
            print("GOTO LABORATORY")
            mission = 0
            step = 2

    # LABORATORY
    elif step == 2 and mission == 1: # sort du molecules avec mission accomplie (ou 1er tour)
        print("GOTO LABORATORY")
        mission = 0

    elif step == 2 and mission == 0: # est au labo avec mission a faire
        # Connect l'id
        print("CONNECT {}".format(best_id))

        # Mission accomplie, next step
        mission = 1
        step = 0
    else:
        step == 0
        mission == 1
        print("GOTO DIAGNOSIS")

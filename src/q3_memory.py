from typing import List, Tuple
import json

"""
La función q3_memory optimiza la memoria al procesar los tweets para contar las menciones de usuarios. Almacena las
menciones contadas en el diccionario mentions_count, donde la clave es el ID del usuario mencionado y el valor es la
frecuencia de menciones. Además, mantiene un diccionario user_info que contiene la información del usuario mencionado,
como su nombre de usuario, utilizando el ID como clave.

La función solo mantiene en memoria los diccionarios mentions_count y user_info, lo que reduce
significativamente el uso de memoria.
"""


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    #Inicializamos dos diccionarios para el numero de menciones y la información del usuario
    mentions_count = {}
    user_info = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            #Revisamos que el tweet tenga menciones
            if 'mentionedUsers' in tweet and tweet['mentionedUsers']:
                for user in tweet['mentionedUsers']:
                    #Asumimos que id funciona como llave única en este dataset
                    user_id = user['id'] 
                    if user_id in mentions_count:
                        mentions_count[user_id] += 1
                    else:
                        mentions_count[user_id] = 1
                        user_info[user_id] = user['username']
    
    # Ordenar las menciones
    sorted_mentions = sorted(mentions_count.items(), key=lambda x: x[1], reverse=True)
    
    results = []
    for user_id, count in sorted_mentions[:10]:
        results.append((user_info[user_id], count))
    
    return results

from typing import List, Tuple
import json
from collections import Counter, defaultdict

"""
La función q3_time optimiza el tiempo de ejecución al procesar los tweets para contar las menciones de usuarios. Utiliza un
contador (Counter) para realizar un seguimiento de la frecuencia de las menciones y utiliza el método most_common del contador 
para encontrar las menciones más comunes, lo quees más eficiente que ordenar manualmente las menciones.
"""

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    #Inicializamos el contador
    mentions_count = Counter()
    user_info = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            #Nos aseguramos que el tweet tenga menciones
            if 'mentionedUsers' in tweet and tweet['mentionedUsers']:
                for user in tweet['mentionedUsers']:
                    #Asumimos que id es un identificador único para este dataset
                    user_id = user['id']
                    mentions_count[user_id] += 1
                    if user_id not in user_info:
                        user_info[user_id] = user['username']
    
    # Ordenar por menciones y encontrar los mas comunes
    top_mentions = mentions_count.most_common()
    
    results = []
    for user_id, count in top_mentions:
        results.append((user_info[user_id], count))
    
    return results[:10]

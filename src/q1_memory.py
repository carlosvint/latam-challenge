from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
import heapq

"""
La función q1_memory optimiza memoria de dos maneras:
1) Al procesar el archivo linea por linea
2) Utilizar heap para encontrar fechas con más tweets, así la complejidad en memoria pasa de ser O(n) a O(1).

En terminos generales la función guarda en un diccionario anidado el número de tweets por usuario y por fecha, 
y en otro diccionario el número total de tweets por fecha. Luego utilizamos un heap para encontrar las 10 
fechas con más tweets. De esta forma ahorramos tanto tiempo como memoria.
"""

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Guardamos el número de tweets de cada usuario por fecha
    user_tweet_counts = defaultdict(lambda: defaultdict(int))
    #Guardamos el número de tweets for fecha
    total_tweets_by_date = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'][:10], "%Y-%m-%d").date() #Necesario para obtener el output especificado.
            user = tweet['user']['username']
            user_tweet_counts[date][user] += 1
            total_tweets_by_date[date] += 1

    # Utilizamos un heap para encontrar las 10 fechas con más tweets
    top_dates_heap = [(count, date) for date, count in total_tweets_by_date.items()]
    heapq.heapify(top_dates_heap)
    top_dates = heapq.nlargest(10, top_dates_heap)
    
    result = []
    for _, date in top_dates:
        top_user = max(user_tweet_counts[date], key=user_tweet_counts[date].get)
        result.append((date, top_user))

    return result

from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
from datetime import datetime

"""
La función q1_time optimiza el tiempo de ejecución de dos maneras:
1) Utilizamos un diccionario anidado para guardar el número de tweets por usuario y por fecha
2) Procesa las fechas como si fuesen strings y luego las convierte en un objeto datetime.date 
    para cumplir con el formato de output solicitado.


"""


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Diccionario para guardar tweets por usuario y fecha.
    user_tweet_counts = defaultdict(lambda: defaultdict(int))
    #Diccionario para guardar tweets for fecha
    tweet_counts_by_date = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            # Podemos procesar las fechas como strings 
            date = tweet['date'][:10]  # Formato YYYY-MM-DD
            user = tweet['user']['username']
            user_tweet_counts[date][user] += 1
            tweet_counts_by_date[date] += 1

    # Encontramos las top 10 fechas con sort
    top_dates = sorted(tweet_counts_by_date.items(), key=lambda x: x[1], reverse=True)[:10]

    result = []
    for date_str, _ in top_dates:
        # Convertimos las fechas a objetos datetime.date solo para el output
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        top_user, _ = max(user_tweet_counts[date_str].items(), key=lambda x: x[1])
        result.append((date_obj, top_user))
    
    return result

from typing import List, Tuple
import json
from collections import Counter, defaultdict

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mentions_count = Counter()
    user_info = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            if 'mentionedUsers' in tweet and tweet['mentionedUsers']:
                for user in tweet['mentionedUsers']:
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
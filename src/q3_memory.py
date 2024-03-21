from typing import List, Tuple
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mentions_count = {}
    user_info = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            if 'mentionedUsers' in tweet and tweet['mentionedUsers']:
                for user in tweet['mentionedUsers']:
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

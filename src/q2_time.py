from typing import List, Tuple
import json
import re
from heapq import nlargest
from collections import defaultdict

# Este es el patron de emojis usualmente utilizado
EMOJI_PATTERN = re.compile(
    "(["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "])"
)

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = defaultdict(int)  # Utilizar un diccionario para contar

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            emojis = EMOJI_PATTERN.findall(content)
            for emoji in emojis:
                emoji_counts[emoji] += 1

    # Usamos nlargest porque internamente tiene una estructura heap y es mas eficiente
    top_emojis = nlargest(10, emoji_counts, key=emoji_counts.get)

    # Convertimos al output con el formato requerido
    top_emojis_with_counts = [(emoji, emoji_counts[emoji]) for emoji in top_emojis]

    return top_emojis_with_counts

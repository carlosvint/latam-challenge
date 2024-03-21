from typing import List, Tuple
import json
from collections import Counter
import re

"""
La función q2_memory cuenta la frecuencia de emojis en tweets utilizando expresiones regulares para identificarlos.
Esto permite optimizar la memoria al procesar el archivo línea por línea, reduciendo así la necesidad de almacenar grandes
cantidades de datos en memoria en un solo momento.

Para realizar esto, la función utiliza una expresión regular (EMOJI_PATTERN) para encontrar emojis en el contenido de los
tweets. Luego, actualiza un contador para mantener un registro de la frecuencia de cada emoji.

"""


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

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    #Inicializar el contador
    emoji_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            # Encontrar los emojis utilizando regex
            emojis = EMOJI_PATTERN.findall(content)
            # Actualizar el contador
            emoji_counter.update(emojis)

    #Utilizar el método most_common porque se basa en una estructura de datos heap.
    top_emojis = emoji_counter.most_common(10)

    return top_emojis

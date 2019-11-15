import spacy

"""
Game plan: 
    1. Generate seed sentence according to grammar rules
    2. Parse the seed sentence with Spacy, then convert to a NetworkX tree (possible alternative: NLTK tree?)
    3. Drop or add elements at random (as long as they fit the grammar rules)
    4. Make the generated sentence the new seed sentence, then repeat from step 2

Current problems:
    -WordNet isn't expansive enough for current purposes, alternatives? (Microsoft )
    -
"""

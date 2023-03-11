import requests as rq
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    pass

def search_pokemon(search_term):
    """ Gets information about a pokemon from the pokeapi and returns a dictionary with that information

    Args:
        search_term (str/int): pokemon name (str) OR pokedex number (int)

    Returns:
        dict: A dictionary of information about the pokemon
    """
    
    # Cleans the search term and prints live synopsis
    search_term = str(search_term).strip().lower()
    print(f'Retrieving information for {search_term.title()if search_term.isalpha() else "pokedex #"+search_term}...', end=' ') # Proper output if word or number
    
    # Gets information from pokeapi and checks if succesful
    response = rq.get(f"{POKE_API_URL}{search_term}")
    if response.ok:
        print('Success!')
        return response.json() # returns dict of pokemon info
    else:
        print('Failed!')
        print(f"Response code: {response.status_code} {response.reason}")
    
    return 
    
if __name__ == '__main__':
    main()
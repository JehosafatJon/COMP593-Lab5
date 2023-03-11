"""~~~ Jonathan Hughes COMP593 ~~~~~~
               __
              / _) < woohoo python!
     _.----._/ /
    /         /
 __/ (  | (  |
/__.-'|_|--|_|   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description:
    Accepts a pokemon name or pokedex 
    entry for a pokemon, retreives 
    information about that pokemon 
    from PokeApi, and writes a bullet 
    point list of their abilities to 
    pastebin.

Usage:
    python pokemon_paste.py <pokemon>

Parameters:
    pokemon (str or int) = A pokemon name (str) or pokedex number (int)

~~~~~~ Jonathan Hughes COMP086  ~~~"""

from sys import argv
from pastebin_api import create_new_paste
from poke_api import search_pokemon

def main():
    # Get the pokemon name from the command line
    search_term = get_search_term()

    # Fetch pokemon information from pokeapi
    pokemon_info = search_pokemon(search_term)

    # If information is fetched succesfully
    if pokemon_info:

        # Detemine the title and body of the paste
        title, body_text = get_paste_content(pokemon_info)
        
        # Print the URL of the new PasteBin paste
        new_paste = create_new_paste(title, body_text)
        if new_paste != None:
            print(f"URL of the paste is: {new_paste}")

    pass

def get_search_term():
    """ Gets the search term from the command line parameter.

    Returns:
        (str) : The search term
    """

    if len(argv) < 2:
        print('Error. Missing search term')
        exit(1)
    else:
        return argv[1]

def get_paste_content(pokemon_info):
    """ Creates the Title and Body of the new paste from the information of the pokemon

    Args:
        pokemon_info (dict): the dictionary of pokemon information

    Returns:
        title (str): The title of the pastebin paste
        body_text (str): The body of the pastebin paste
    """

    # Title of the paste
    title = f"{pokemon_info['name'].title()}'s Abilities"

    # Body of the paste
    body_text = ''
    for ability in pokemon_info['abilities']:
        body_text += "- " + ability['ability']['name'].title()
        body_text += '\n'
    
    return title, body_text.strip() # Strip to remove the unused new line

if __name__ == '__main__':
    main()
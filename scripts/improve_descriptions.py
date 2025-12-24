import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'src', 'data', 'games.json')

def improve_descriptions():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        games = json.load(f)
    
    updated_count = 0
    
    # Templates for generating richer descriptions
    templates = [
        "Play {name} online for free. {name} is an exciting {category} game that provides endless entertainment. Play directly in your browser without any downloads. Enjoy the best unblocked gaming experience and challenge your friends in {name} today!",
        "Experience the fun of {name} unblocked. This popular {category} game is available to play for free in your web browser. No installation required - just click and play {name} instantly on Modern Game Portal.",
        "Looking for {name}? Play it now online for free! {name} is a top-rated {category} game that offers smooth gameplay and addictive fun. Dive into the action without any downloads or ads blocking your way.",
        "Enjoy {name} unblocked directly in your browser. As one of the best {category} games available, {name} guarantees hours of fun. Play now for free and see why everyone loves this game!"
    ]
    
    for game in games:
        desc = game.get('description', '')
        name = game.get('name', '')
        category = game.get('category', 'Arcade')
        
        # Check for the short pattern or very short length
        # Pattern usually: "Play {name} unblocked."
        is_short = len(desc) < 60
        is_generic = desc.strip() == f"Play {name} unblocked."
        
        if is_short or is_generic:
            # Pick a random template
            template = random.choice(templates)
            new_desc = template.format(name=name, category=category)
            
            game['description'] = new_desc
            updated_count += 1
            # print(f"Updated: {name}")

    if updated_count > 0:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(games, f, indent=2)
        print(f"Successfully updated descriptions for {updated_count} games.")
    else:
        print("No descriptions needed updating.")

if __name__ == "__main__":
    improve_descriptions()

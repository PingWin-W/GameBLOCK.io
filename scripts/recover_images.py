import json
import os
import urllib.request
import urllib.error
import time

# Configuration
GAMES_JSON_PATH = 'src/data/games.json'
IMAGE_BASE_PATH = 'public/cache/data/image/game'
GD_BASE_URL = 'https://img.gamedistribution.com'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

def download_image(game_id, slug):
    """
    Attempts to download the image for a given game ID.
    Tries .jpeg first, then .jpg.
    Returns the partial local path (e.g., 'public/cache/...') if successful, None otherwise.
    """
    extensions = ['.jpeg', '.jpg']
    
    # Create target directory
    target_dir = os.path.join(IMAGE_BASE_PATH, slug)
    os.makedirs(target_dir, exist_ok=True)
    
    for ext in extensions:
        url = f"{GD_BASE_URL}/{game_id}-512x512{ext}"
        target_filename = f"{slug}{ext}" # Keep original extension from source
        target_path = os.path.join(target_dir, target_filename)
        
        print(f"Trying {url}...")
        
        try:
            req = urllib.request.Request(
                url, 
                data=None, 
                headers={'User-Agent': USER_AGENT}
            )
            
            with urllib.request.urlopen(req) as response:
                data = response.read()
                
                # Check if we got a valid image (simple size check)
                if len(data) < 1000:
                    print(f"  Skipping: File too small ({len(data)} bytes)")
                    continue
                    
                with open(target_path, 'wb') as f:
                    f.write(data)
                
                print(f"  Success! Saved to {target_path}")
                # Return the relative path consistent with how it's used in the app
                # The app expects path starting with public/ or ./public/
                # Based on previous existing paths loop: "./public/cache/data/image/game/..."
                return f"./public/cache/data/image/game/{slug}/{target_filename}"
                
        except urllib.error.HTTPError as e:
            print(f"  Failed: {e.code}")
        except Exception as e:
            print(f"  Error: {e}")
            
    return None

def main():
    print(f"Reading {GAMES_JSON_PATH}...")
    try:
        with open(GAMES_JSON_PATH, 'r') as f:
            games = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {GAMES_JSON_PATH}")
        return

    updated_count = 0
    
    for game in games:
        # We need the ID to construct the source URL
        # Assuming the 'id' field in json is the GameDistribution hash
        # If not, we might need to rely on the existing image URL to extract it, 
        # but let's assume 'id' is correct based on standard GD usage.
        
        # Check if 'id' looks like a GD hash (32 chars)
        game_id = game.get('id')
        slug = game.get('slug') # We use slug for folder structure
        
        if not game_id or not slug:
            print(f"Skipping game {game.get('title', 'Unknown')}: Missing id or slug")
            continue
            
        print(f"\nProcessing {game.get('title')} ({game_id})...")
        
        new_image_path = download_image(game_id, slug)
        
        if new_image_path:
            game['image'] = new_image_path
            updated_count += 1
        else:
            print(f"Could not recover image for {game.get('title')}")

    print(f"\nSummary: Updated {updated_count} games.")
    
    # Save updated JSON
    with open(GAMES_JSON_PATH, 'w') as f:
        json.dump(games, f, indent=2)
    print(f"Saved updates to {GAMES_JSON_PATH}")

if __name__ == "__main__":
    main()

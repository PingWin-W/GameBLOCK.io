import os

def update_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    # 1. Update branding in H1
                    # Handle both "Portal" and "unblocked" if present
                    content = content.replace('<h1>Portal</h1>', '<h1>ublocked games</h1>')
                    content = content.replace('<h1>unblocked</h1>', '<h1>ublocked games</h1>')
                    
                    # 2. Update Title
                    # "Modern Game Portal" -> "Modern ublocked games"
                    content = content.replace('Modern Game Portal', 'Modern ublocked games')
                    # Removing "Portal" from other titles if it exists as a standalone word might be risky, 
                    # but let's target specific known patterns
                    content = content.replace(' - Popular Games', ' - Popular ublocked games')

                    # 3. Update Meta Description and properties
                    # "Play the best free online games at Modern Game Portal."
                    content = content.replace('Modern Game Portal', 'Modern ublocked games')
                    
                    if content != original_content:
                        print(f"Updating {filepath}")
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    base_dir = '/Users/pingwin/Desktop/GAMEREPO'
    update_files(base_dir)
    print("Batch branding update complete.")

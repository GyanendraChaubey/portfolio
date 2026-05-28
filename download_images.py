import re
import os
import urllib.request
import hashlib

files = ['index.html', 'projects.html', 'publications.html']
img_dir = 'images'
os.makedirs(img_dir, exist_ok=True)

# Regex to find image sources
img_regex = re.compile(r'src="(https://lh3\.googleusercontent\.com/[^"]+)"')

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    matches = img_regex.findall(content)
    for url in set(matches):
        # Create a safe filename based on a hash of the URL
        hash_name = hashlib.md5(url.encode()).hexdigest()[:10]
        local_path = f"{img_dir}/image_{hash_name}.jpg"
        
        # Download the image
        print(f"Downloading {url[:50]}... to {local_path}")
        try:
            urllib.request.urlretrieve(url, local_path)
            # Replace the URL in the content
            content = content.replace(url, local_path)
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            
    with open(f, 'w') as file:
        file.write(content)
print("Finished downloading images and updating HTML.")

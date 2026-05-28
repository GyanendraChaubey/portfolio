import re
import os

files = ['index.html', 'projects.html', 'publications.html']

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Update navigation links
    # Home link
    content = re.sub(r'<a([^>]*?)href="#"(.*?)>Home</a>', r'<a\1href="index.html"\2>Home</a>', content)
    # Research link
    content = re.sub(r'<a([^>]*?)href="#"(.*?)>Research</a>', r'<a\1href="publications.html"\2>Research</a>', content)
    # Projects link
    content = re.sub(r'<a([^>]*?)href="#"(.*?)>Projects</a>', r'<a\1href="projects.html"\2>Projects</a>', content)
    # CV link
    content = re.sub(r'<a([^>]*?)href="#"(.*?)>CV</a>', r'<a\1href="https://drive.google.com/file/d/1scMp81pFI7d6a0qwLat-r0OSM8ZDXaCl/view?usp=sharing"\2>CV</a>', content)
    
    # Update Profile Image in index.html
    if f == 'index.html':
        content = re.sub(r'src="https://lh3.googleusercontent.com/aida/[^"]+"', r'src="images/profile.jpg"', content)
        
    with open(f, 'w') as file:
        file.write(content)

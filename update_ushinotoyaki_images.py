import os
import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('story_ushinotoyaki_somewake.jpg', 'ushinotoyaki_somewake.png')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update stories.html
with open('stories.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('story_ushinotoyaki_somewake.jpg', 'ushinotoyaki_somewake.png')
with open('stories.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update story-ushinotoyaki.html
with open('story-ushinotoyaki.html', 'r', encoding='utf-8') as f:
    html = f.read()
# Replace the hero background and the first image
html = html.replace('story_ushinotoyaki_somewake.jpg', 'ushinotoyaki_somewake.png')

# The prompt also asked to use the climbing kiln (登り窯). Let's replace the traditional_craft.jpg (which was used for the "current creators" section) with ushinotoyaki_kama.png.
html = html.replace('traditional_craft.jpg', 'ushinotoyaki_kama.png')
html = html.replace('作陶イメージ', '牛ノ戸焼 登り窯')

with open('story-ushinotoyaki.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Images updated successfully!")

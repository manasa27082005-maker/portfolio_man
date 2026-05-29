import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<section class="expertise-section" id="expertise">.*?</section>', re.DOTALL)
with open('patch.html', 'r', encoding='utf-8') as f:
    patch_content = f.read()

new_content = pattern.sub(patch_content, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

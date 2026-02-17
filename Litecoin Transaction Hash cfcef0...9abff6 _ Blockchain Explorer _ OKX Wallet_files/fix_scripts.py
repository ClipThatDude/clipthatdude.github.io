import re
from bs4 import BeautifulSoup

# HTML dosyasını oku
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# BeautifulSoup ile parse et
soup = BeautifulSoup(content, 'html.parser')

# Tüm script taglerini bul ve src'lerini düzelt
for script in soup.find_all('script'):
    if script.get('src'):
        src = script['src']
        # URL'leri local path'e çevir
        if src.startswith('http'):
            filename = src.split('/')[-1]
            script['src'] = './' + filename

# Tüm link taglerini bul ve href'lerini düzelt
for link in soup.find_all('link'):
    if link.get('href'):
        href = link['href']
        # URL'leri local path'e çevir
        if href.startswith('http'):
            filename = href.split('/')[-1]
            link['href'] = './' + filename

# Düzeltilmiş HTML'i kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup.prettify()))

print("Script ve CSS linkleri düzeltildi!")

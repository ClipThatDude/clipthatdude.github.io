import re

# HTML dosyasını oku
with open('saved_resource.html', 'r', encoding='utf-8') as f:
    html = f.read()

# transition-property stillerini kaldır
html = re.sub(r'\s*style="[^"]*transition-property[^"]*"', '', html)
html = re.sub(r'\s*transition-property:\s*none;?', '', html)

# Dark mode ve diğer eklenti stillerini kaldır
html = re.sub(r'<link[^>]*dark-mode[^>]*>', '', html)
html = re.sub(r'<style[^>]*dark-mode[^>]*>.*?</style>', '', html, flags=re.DOTALL)

# Temizlenmiş HTML'i kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML temizlendi ve index.html olarak kaydedildi!")

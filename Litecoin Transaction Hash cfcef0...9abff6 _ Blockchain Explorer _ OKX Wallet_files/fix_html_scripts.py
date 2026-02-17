import re

# HTML dosyasını oku
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# .download uzantılarını kaldır
html = html.replace('.js.download', '.js')
html = html.replace('.css.download', '.css')

# Düzeltilmiş HTML'i kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML dosyasındaki script referansları düzeltildi!")

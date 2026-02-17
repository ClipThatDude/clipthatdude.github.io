with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS linkini head'e ekle
css_link = '<link rel="stylesheet" href="fix_overlay.css">\n'
html = html.replace('</head>', css_link + '</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('CSS başarıyla eklendi!')

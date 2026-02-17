import re

# HTML dosyasını oku
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Rotation style'ı
rotation_style = '''
<style>
/* Script toggle animasyonu */
.index_arrow__a8ckA {
    transition: transform 0.3s ease;
    cursor: pointer;
}

.index_arrow__a8ckA.index_rotate__sjEdk {
    transform: rotate(180deg);
}

.index_script__9l20r .index_header__kXd22 {
    cursor: pointer;
}

/* Script içeriği için smooth transition */
.index_script__9l20r > div > div {
    transition: all 0.3s ease;
}
</style>
'''

# </head> etiketinden önce style'ı ekle
html = html.replace('</head>', rotation_style + '\n</head>')

# Düzeltilmiş HTML'i kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Rotation style başarıyla eklendi!")

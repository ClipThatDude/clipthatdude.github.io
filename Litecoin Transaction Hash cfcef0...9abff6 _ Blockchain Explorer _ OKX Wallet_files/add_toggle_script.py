import re

# HTML dosyasını oku
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Toggle script'i
toggle_script = '''
<script>
// Script toggle fonksiyonu
function toggleScript(icon) {
    const wrapper = icon.closest('.index_script__9l20r');
    if (!wrapper) return;
    
    const content = wrapper.querySelector('div > div');
    if (!content) return;
    
    if (icon.classList.contains('index_rotate__sjEdk')) {
        // Kapat
        content.style.display = 'none';
        icon.classList.remove('index_rotate__sjEdk');
        icon.setAttribute('aria-label', 'Show more');
    } else {
        // Aç
        content.style.display = 'block';
        icon.classList.add('index_rotate__sjEdk');
        icon.setAttribute('aria-label', 'Show less');
    }
}

// Sayfa yüklendiğinde tüm script ikonlarına event listener ekle
document.addEventListener('DOMContentLoaded', function() {
    const scriptIcons = document.querySelectorAll('.index_script__9l20r .index_arrow__a8ckA');
    
    scriptIcons.forEach(icon => {
        // Click event
        icon.addEventListener('click', function() {
            toggleScript(this);
        });
        
        // Klavye erişilebilirliği
        icon.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleScript(this);
            }
        });
    });
});
</script>
'''

# </body> etiketinden önce script'i ekle
html = html.replace('</body>', toggle_script + '\n</body>')

# Düzeltilmiş HTML'i kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Toggle script başarıyla eklendi!")

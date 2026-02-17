import os
import shutil

# Tüm .download uzantılı dosyaları bul ve yeniden adlandır
for filename in os.listdir('.'):
    if filename.endswith('.download'):
        new_name = filename.replace('.download', '')
        print(f"Renaming: {filename} -> {new_name}")
        
        # Eğer hedef dosya zaten varsa, üzerine yaz
        if os.path.exists(new_name):
            os.remove(new_name)
        
        shutil.move(filename, new_name)

print("\nTüm .download dosyaları yeniden adlandırıldı!")

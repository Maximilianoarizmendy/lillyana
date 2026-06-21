import os
import pypandoc

bitacoras_dir = r"c:\Users\maxig\Downloads\lillyana\lillyana\bitacoras"
downloads_dir = r"c:\Users\maxig\Downloads"

for f in os.listdir(bitacoras_dir):
    if f.endswith(".md"):
        md_path = os.path.join(bitacoras_dir, f)
        docx_path = os.path.join(downloads_dir, f.replace(".md", ".docx"))
        print(f"Convirtiendo {f} a docx...")
        pypandoc.convert_file(md_path, "docx", outputfile=docx_path)

print("¡Todas las bitácoras han sido convertidas exitosamente!")

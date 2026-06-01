import docx
import glob
import os

files = glob.glob('trimestre/*.docx')
# Filter out requirements.docx
files = [f for f in files if 'requirements.docx' not in f]
files.sort()

for i, f in enumerate(files):
    try:
        doc = docx.Document(f)
        text = []
        for p in doc.paragraphs:
            if p.text.strip():
                text.append(p.text)
        
        md_file = f'bitacoras/bitacora_{i+1}.md'
        with open(md_file, 'w', encoding='utf-8') as out:
            out.write(f'# Bitacora extraida de: {os.path.basename(f)}\n\n')
            out.write('\n\n'.join(text))
            
        print(f'Wrote {md_file}')
    except Exception as e:
        print(f'Error reading {f}: {e}')

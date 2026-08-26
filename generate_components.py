import os

# Helper to write files
def write_file(rel_path, content):
    full_path = os.path.join('d:/portfolio', rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f_out:
        f_out.write(content.strip() + '\n')
    print(f'Wrote {rel_path}')

print('Initialized generate_components.py')

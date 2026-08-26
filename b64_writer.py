import os, base64

def write_b64_file(rel_path, b64_content):
    full_path = os.path.join('d:/portfolio', rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'wb') as f:
        f.write(base64.b64decode(b64_content))
    print('Wrote ' + rel_path)

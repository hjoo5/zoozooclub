import json

def write_json(data, fname):
    with open(fname, 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent='\t')
        
def load_json(fname):
    with open(fname, encoding="utf-8") as f:
        json_obj = json.load(f)

    return json_obj

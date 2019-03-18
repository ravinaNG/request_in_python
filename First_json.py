book = { }
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 98989898
}
book['bob'] = {
    'name': 'tom',
    'address': '1 green street, NY',
    'phone': 1232344324
}

import json
s = json.dumps(book)
print (s)

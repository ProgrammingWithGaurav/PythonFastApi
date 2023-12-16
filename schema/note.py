def Note_Entity(item) -> dict: # item of type dictionary
    return {
        'id': str(item['_id']),
        "title": item['title'],
        "desc": item['desc'],
        "important": item['important']
    }

def NotesEntity(items) -> list:
    return [Note_Entity(item) for item in items]
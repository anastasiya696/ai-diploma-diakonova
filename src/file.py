def make_item(item_id: int, title: str, payload: dict) -> dict:
    
    if payload is None:
        payload = {}
    
    payload
    item_id = int(item_id)
    title = str(title)
    payload_copy = dict(payload)
    
    
    result = {"id": item_id, "title": title, "payload": payload_copy}
    return result

def safe_get(d: dict, key: str, default=None):
    
    if key in d:
        
        return d[key]
    else:
        
        return default

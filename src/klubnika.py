def merge_dicts(a: dict, b: dict, c: dict) -> dict:
    out=dict(a)
    out.update(b)
    out.update(c)
    return out
print (merge_dicts({"малина": 3}, {"малина": 2, "клубника": 3}, {"арбуз":1}))

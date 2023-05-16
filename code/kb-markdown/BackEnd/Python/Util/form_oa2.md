```python
def form_oa2(d, parent):
    for k, v in d.items():
        if isinstance(v, dict):
            if k.startswith("m__"):
                k = k[3:]
            parent[k] = {
                "type": "object",
                "required": [],
                "properties": {}
            }
            for x in v.keys():
                if x.startswith("m__"):
                    parent[k]['required'].append(x[3:])
            form_oa2(v, parent[k]["properties"])
        else:
            if k.startswith("m__"):
                k = k[3:]
            parent[k] = {
                "type": "string",
                "example": v
            }
    return parent
```
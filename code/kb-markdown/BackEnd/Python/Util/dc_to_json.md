```python
import json

def dc_to_json_file(dc, fn='data.json'):
    with open(fn, 'w') as outfile:
        # sort_keys = True
        j = json.dumps(dc, indent=4)
        outfile.write(j)

```
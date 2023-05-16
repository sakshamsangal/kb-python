```python

import json


def form_json(dc, ls):
    if ls:
        k = ls.pop(0)
        if len(ls) == 0:
            if k not in dc:
                dc[k] = ''
        else:
            if k not in dc:
                dc[k] = {}
            elif isinstance(dc[k], str):
                dc[k] = {}
            form_json(dc[k], ls)
    return dc

```
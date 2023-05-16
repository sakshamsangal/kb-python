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
                "description": "",
                "example": v
            }
    return parent


def dc_to_oa2(dc):
    return form_oa2(dc, {})


if __name__ == '__main__':
    njson = {
        "numbersMock": {
            "m__smallInt": -20,
            "m__stringsMock": {
                "m__stringTest": "Hello World"
            },
            "b1": {
                "m__b1c1": "Hello World"
            }
        }
    }
    oa2 = dc_to_oa2(njson)
    print(oa2)


def dc_to_json_file(dc, fn='data.json'):
    with open(fn, 'w') as outfile:
        # sort_keys = True
        j = json.dumps(dc, indent=4)
        outfile.write(j)


def dc_to_yml_file(dc, fn='data.yml'):
    with open(fn, 'w') as outfile:
        yaml.dump(dc, outfile, default_flow_style=False)

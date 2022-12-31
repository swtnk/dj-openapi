import yaml
import json

format_map = {"json": json, "yaml": yaml}


def yaml_json_converter(data, from_format="json", to_format="yaml"):
    if data:
        converted_data = format_map[to_format].dumps(
            format_map[from_format].loads(data)
        )
        print(converted_data)
        return converted_data
    else:
        return False

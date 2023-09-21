import json


class JsonUtils:
    data_model = {
        "{nome_id}": {
            "nome": str,
            "tipo": str,
            "importancia": str,
            "tipo_endereco": str,
            "lat": float,
            "lon": float,
        }
    }

    def add_citydata_json(self, path_file, data):
        with open(path_file, 'r') as f:
            data_content = json.loads(f.read())
            data_content.update(data)
        with open(path_file, 'w') as f:
            if all(
                    isinstance(data.get(key), tuple(self.data_model[key]))
                    if isinstance(self.data_model[key], tuple)
                    else True
                    for key in self.data_model
            ):
                json.dump(data_content, f)

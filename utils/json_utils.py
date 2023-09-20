import json


class JsonUtils:
    # not use, yet
    # if all(isinstance(data.get(key), self.data_model[key]) for key in self.data_model):

    data_model = {
        "{nome}": {
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
            json.dump(data_content, f)

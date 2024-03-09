INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Penguins having dinner"]
    },
    "num_inference_steps": {
        'datatype': 'INT8',
        'required': True,
        'shape': [1],
        'example': [40]
    },
    "height": {
        'datatype': 'INT8',
        'required': True,
        'shape': [1],
        'example': [1024]
    },
    "width": {
        'datatype': 'INT8',
        'required': True,
        'shape': [1],
        'example': [1024]
    }
}

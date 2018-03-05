from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

schema = {
    "type" : "object",
    "properties" : {
        "name" : {"type" : "string"},
        "description" : {"type" : "string"},
    }
}

class ProductInputs(Inputs):
    json = [JsonSchema(schema=schema)]

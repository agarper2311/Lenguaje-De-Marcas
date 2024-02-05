import json
from jsonschema import validate

# Definir el esquema
schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "concesionario": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "codigo_de_coche": {
            "type": "string",
            "pattern": "^[0-9]{8}$"
          },
          "marca": {
            "type": "string"
          },
          "modelo": {
            "type": "string"
          },
          "matricula": {
            "type": "string",
            "pattern": "^[0-9]{4}[A-Za-z]{3}$"
          },
          "potenciacv": {
            "type": "string",
            "pattern": "^[0-9]+cv$"
          },
          "plazas": {
            "type": "string",
            "pattern": "^[0-9]+$"
          },
          "num_puertas": {
            "type": "string",
            "pattern": "^[0-9]+$"
          }
        },
        "required": ["codigo_de_coche", "marca", "modelo", "matricula", "potenciacv", "plazas", "num_puertas"],
        "additionalProperties": False
      }
    }
  },
  "required": ["concesionario"],
  "additionalProperties": False
}


# Archivo JSON a validar
archivo_json = '''
{
    "concesionario": [
        {
            "codigo_de_coche": "12345678",
            "marca": "Ford",
            "modelo": "Mustang",
            "matricula": "1234htd",
            "potenciacv": "150cv",
            "plazas": "4",
            "num_puertas": "3"
        },
        {
            "codigo_de_coche": "23456789",
            "marca": "Audi",
            "modelo": "A3",
            "matricula": "2324NMZ",
            "potenciacv": "130cv",
            "plazas": "5",
            "num_puertas": "5"
        }
    ]
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
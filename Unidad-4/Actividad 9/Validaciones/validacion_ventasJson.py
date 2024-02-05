import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "titulo": {
      "type": "string"
    },
    "descripcion": {
      "type": "string"
    },
    "fecha": {
      "type": "string",
      "pattern": "^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
    },
    "ventas": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "nombre": {
            "type": "string"
          },
          "trimestres": {
            "type": "object",
            "properties": {
              "trimestre1": { "type": ["string", "null"], "pattern": "^[0-9]+|NO_INFO$" },
              "trimestre2": { "type": ["string", "null"], "pattern": "^[0-9]+|NO_INFO$" },
              "trimestre3": { "type": ["string", "null"], "pattern": "^[0-9]+|NO_INFO$" },
              "trimestre4": { "type": ["string", "null"], "pattern": "^[0-9]+|NO_INFO$" }
            },
            "required": ["trimestre1", "trimestre2", "trimestre3", "trimestre4"],
            "additionalProperties": False
          }
        },
        "required": ["nombre", "trimestres"],
        "additionalProperties": False
      }
    }
  },
  "required": ["titulo", "descripcion", "fecha", "ventas"],
  "additionalProperties": False
}

# Archivo JSON a validar
archivo_json = '''
{
    "titulo": "Informe regional de ventas",
    "descripcion": "informe de ventas para las regiones Norte, Centro y Sur",
    "fecha": "30/12/2009",
    "ventas": [
        {
            "nombre": "Norte",
            "trimestres": {
                "trimestre1": "24000",
                "trimestre2": "38600",
                "trimestre3": "NO_INFO",
                "trimestre4": "NO_INFO"
            }
        },
        {
            "nombre": "Centro",
            "trimestres": {
                "trimestre1": "NO_INFO",
                "trimestre2": "16080",
                "trimestre3": "25000",
                "trimestre4": "29000"
            }
        },
        {
            "nombre": "Sur",
            "trimestres": {
                "trimestre1": "27000",
                "trimestre2": "31400",
                "trimestre3": "40100",
                "trimestre4": "30000"
            }
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
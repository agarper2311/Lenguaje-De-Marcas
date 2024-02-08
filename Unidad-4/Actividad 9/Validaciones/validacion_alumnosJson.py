import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "alumnos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "nif": {
            "type": "string",
            "pattern": "^[0-9]{8}[A-Z]$"
          },
          "resultado": {
            "type": "string",
            "enum": ["apto", "No apto"]
          },
          "observaciones": {
            "type": "string"
          },
          "ip": {
            "type": "string",
            "format": "ipv4"
          },
          "mac": {
            "type": "string",
            "pattern": "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
          }
        },
        "required": ["nif", "resultado", "ip"],
        "additionalProperties": False
      }
    }
  },
  "required": ["alumnos"],
  "additionalProperties": False
}

# Archivo JSON a validar
archivo_json = '''
{
    "alumnos": [
        {
            "nif": "12345678A",
            "resultado": "apto",
            "observaciones": "Excelente rendimiento",
            "ip": "192.168.1.1"
        },
        {
            "nif": "23456789B",
            "resultado": "No apto",
            "mac": "00:1B:44:11:3A:B7",
            "ip": "192.168.1.3"
        },
        {
            "nif": "34567890C",
            "resultado": "apto",
            "ip": "192.168.1.2"
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
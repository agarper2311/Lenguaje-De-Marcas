import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "modulos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "nombre": {
            "type": "string"
          },
          "contenidos": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "tipo": {
                  "type": "string",
                  "enum": ["Teórica", "Práctica"]
                },
                "descripcion": {
                  "type": "string"
                }
              },
              "required": ["tipo", "descripcion"],
              "additionalProperties": False
            }
          }
        },
        "required": ["nombre", "contenidos"],
        "additionalProperties": False
      }
    }
  },
  "required": ["modulos"],
  "additionalProperties": False
}


# Archivo JSON a validar
archivo_json = '''
{
    "modulos": [
        {
            "nombre": "Programación",
            "contenidos": [
                {
                    "tipo": "Teórica",
                    "descripcion": "Introducción a la Programación"
                },
                {
                    "tipo": "Práctica",
                    "descripcion": "Programación Orientada a Objetos"
                }
            ]
        },
        {
            "nombre": "Base de Datos",
            "contenidos": [
                {
                    "tipo": "Teórica",
                    "descripcion": "Modelos de Datos"
                },
                {
                    "tipo": "Práctica",
                    "descripcion": "SQL Avanzado"
                }
            ]
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
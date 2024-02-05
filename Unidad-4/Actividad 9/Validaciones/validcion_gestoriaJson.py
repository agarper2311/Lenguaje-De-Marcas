import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "Gestoria": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Empleado": {
            "type": "string"
          },
          "Fecha": {
            "type": "string",
            "format": "date"
          },
          "Clientes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "codCliente": {
                  "type": "string",
                  "pattern": "^[A-Z]{3}-[0-9]{3}$"
                },
                "descCliente": {
                  "type": "string"
                },
                "vivienda": {
                  "type": "string",
                  "pattern": "^[0-9]+$"
                },
                "coste": {
                  "type": "string",
                  "pattern": "^[0-9]+$"
                },
                "resumen": {
                  "type": "string"
                },
                "plazo": {
                  "type": "string",
                  "pattern": "^[0-9]+$"
                }
              },
              "required": ["codCliente", "descCliente", "vivienda", "coste", "resumen", "plazo"],
              "additionalProperties": False
            }
          }
        },
        "required": ["Empleado", "Fecha", "Clientes"],
        "additionalProperties": False
      }
    }
  },
  "required": ["Gestoria"],
  "additionalProperties": False
}


# Archivo JSON a validar
archivo_json = '''
{
    "Gestoria": [
        {
            "Empleado": "Juan Perez",
            "Fecha": "2024-01-22",
            "Clientes": [
                {
                    "codCliente": "AAA-112",
                    "descCliente": "Insolvente",
                    "vivienda": "10",
                    "coste": "100",
                    "resumen": "Producto muy frágil",
                    "plazo": "10"
                },
                {
                    "codCliente": "BBB-113",
                    "descCliente": "Insolvente",
                    "vivienda": "10",
                    "coste": "100",
                    "resumen": "Producto no frágil",
                    "plazo": "17"
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
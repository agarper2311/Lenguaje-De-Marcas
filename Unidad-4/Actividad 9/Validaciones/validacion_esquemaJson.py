import json
from jsonschema import validate

# Definir el esquema
schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "biblioteca": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "autores": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "apellido1": { "type": ["string", "null"] },
                "apellido2": { "type": ["string", "null"] },
                "nombre": { "type": ["string", "null"] }
              },
              "additionalProperties": False
            }
          },
          "titulo": { "type": ["string", "null"] },
          "editorial": { "type": ["string", "null"] },
          "fecha_Publicacion": { "type": ["string", "null"] },
          "ISBN": { "type": ["string", "null"] }
        },
        "required": ["autores", "titulo", "editorial", "fecha_Publicacion", "ISBN"],
        "additionalProperties": False
      }
    }
  },
  "required": ["biblioteca"],
  "additionalProperties": False
}



# Archivo JSON a validar
archivo_json = '''
{
    "biblioteca": [
        {
            "autores": [
                {
                    "apellido1": null,
                    "apellido2": null,
                    "nombre": null
                }
            ],
            "titulo": null,
            "editorial": null,
            "fecha_Publicacion": null,
            "ISBN": null
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
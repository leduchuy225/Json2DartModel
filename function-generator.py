import sys
import json
from share import *
from pathlib import Path


def handle_content(content):
  json_object = json.loads(content)
  buffer = StringBuffer()

  buffer.writeInline('{')

  for key in json_object:
    keyName = snake_case_to_camel_case(key)

    if type(json_object[key]) is str:
      buffer.writeInline(f'String? {keyName},')
    elif type(json_object[key]) is int:
      buffer.writeInline(f'int? {keyName},')
    else:
      buffer.writeInline(f'dynamic? {keyName},')

  buffer.write('}')

  buffer.write(f'final Map<String, dynamic> payload = {{')

  for key in json_object:
    keyName = snake_case_to_camel_case(key)
    buffer.write(f"'{key}': {keyName},")
  buffer.write('};')

  return buffer.getvalue()


if __name__ == "__main__":
  argument = './source.json'
  file_name = 'hello_world'

  if len(sys.argv) == 2:
    file_name = sys.argv[1]

  path = Path(argument)
  parent_path = str(Path('resources', path).parents[0])

  file_content = open(path, "r").read()
  final_result = handle_content(file_content)

  f = open(parent_path + f"/{file_name}.dart", "a")
  f.truncate(0)
  f.write(final_result)
  f.close()

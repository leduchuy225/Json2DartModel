import sys
import json
from io import StringIO
from pathlib import Path


def handle_content(content, file_name):
  json_object = json.loads(content)
  class_name = snake_case_to_pascal_case(file_name) + "Model"

  buffer = StringBuffer()

  buffer.write("import 'package:json_annotation/json_annotation.dart';")
  buffer.addLine()

  buffer.write(f"part '{file_name}.g.dart';")
  buffer.addLine()

  buffer.write('@JsonSerializable()')
  buffer.write(f'class {class_name} {{')

  for x in json_object:
    buffer.write(f"@JsonKey(name: '{x}')")
    if type(json_object[x]) is str:
      buffer.write(f"final String? {snake_case_to_camel_case(x)};")
    elif type(json_object[x]) is int:
      buffer.write(f"final int? {snake_case_to_camel_case(x)};")
    elif type(json_object[x]) is list:
      if (len(json_object[x]) == 0):
        buffer.write(
            f"final List? {snake_case_to_camel_case(x)}; //Set type for this field")
      elif type(json_object[x][0]) is str:
        buffer.write(f"final List<String>? {snake_case_to_camel_case(x)};")
      elif type(json_object[x][0]) is int:
        buffer.write(f"final List<int>? {snake_case_to_camel_case(x)};")
      else:
        buffer.write(
            f"final List? {snake_case_to_camel_case(x)}; //Set type for this field")
    else:
      buffer.write(
          f"final dynamic {snake_case_to_camel_case(x)}; //Set type for this field")

  buffer.addLine()

  buffer.write(f'{class_name}({{')

  for x in json_object:
    buffer.write(f"this.{snake_case_to_camel_case(x)},")

  buffer.write('});')
  buffer.addLine()

  buffer.write(
      f"factory {class_name}.fromJson(Map<String, dynamic> json) => _${class_name}FromJson(json);")
  buffer.addLine()

  buffer.write(f"Map<String, dynamic> toJson() => _${class_name}ToJson(this);")
  buffer.write("}")

  return buffer.getvalue()


def snake_case_to_camel_case(content):
  words = content.split('_')
  return str(words[0] + ''.join(word.title() for word in words[1:]))


def snake_case_to_pascal_case(content):
  words = content.split('_')
  return str(''.join(word.capitalize() for word in words))


class StringBuffer(StringIO):
  def write(self, content):
    super().write(content)
    super().write('\n')

  def addLine(self):
    super().write('\n')


if __name__ == "__main__":
  argument = './source.json'
  file_name = 'hello_world'

  if len(sys.argv) == 2:
    file_name = sys.argv[1]

  path = Path(argument)
  parent_path = str(Path(path).parents[0])

  file_content = open(path, "r").read()
  final_result = handle_content(file_content, file_name)

  f = open(parent_path + f"/{file_name}.dart", "a")
  f.truncate(0)
  f.write(final_result)
  f.close()

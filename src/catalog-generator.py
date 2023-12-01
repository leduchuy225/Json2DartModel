

import sys
from pathlib import Path

from share import StringBuffer, snake_case_to_pascal_case


parentType = 'TraCuuCatalogType'
parentCatalog = 'TraCuuCatalogArgs'


def handle_content(content, f):
  for line in content:
    data = line.strip().split(',')
    className = data[0]
    name = snake_case_to_pascal_case(className) + 'CatalogArgs'

    buffer = StringBuffer()

    buffer.write(f"class {name} extends {parentCatalog} {{")
    buffer.addLine()

    for i in range(1, len(data)):
      buffer.write(f"final {data[i]};")

    buffer.writeInline(f"{name}({{bool forceUpdate = false,")

    for i in range(1, len(data)):
      buffer.writeInline(f"required this.{data[i].split(' ')[1]},")

    buffer.writeInline(
        f"}}) : super(type: {parentType}.{className},forceUpdate: forceUpdate,);")

    buffer.addLine()

    buffer.write('@override')
    buffer.writeInline('List<Object?> get props => [...super.props,')
    for i in range(1, len(data)):
      buffer.writeInline(f"{data[i].split(' ')[1]},")
    buffer.writeInline('];')

    buffer.addLine()

    buffer.write('@override')
    buffer.writeInline(
        f"{name} copyWith({{bool? forceUpdate,")

    for i in range(1, len(data)):
      buffer.writeInline(f"{data[i].split(' ')[0]}? {data[i].split(' ')[1]},")

    buffer.writeInline(
        f"}}) {{return {name}(forceUpdate: forceUpdate ?? this.forceUpdate,")

    for i in range(1, len(data)):
      buffer.writeInline(
          f"{data[i].split(' ')[1]}: {data[i].split(' ')[1]} ?? this.{data[i].split(' ')[1]},")

    buffer.writeInline(
        ");}")

    buffer.write('}')

    buffer.addLine()
    buffer.addLine()

    f.write(buffer.getvalue())


if __name__ == "__main__":
  argument = 'catalog.txt'
  file_name = 'hello_world'

  if len(sys.argv) == 2:
    file_name = sys.argv[1]

  path = Path(argument)
  parent_path = str(Path('resources', path).parents[0])

  f = open(parent_path + f"/{file_name}.dart", "a")
  f.truncate(0)

  file_content = open(path, "r").readlines()
  final_result = handle_content(file_content, f)

  f.close()

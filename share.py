from io import StringIO


def snake_case_to_camel_case(content):
  result = ''
  if (ord(content[0]) <= ord('Z')):
    result = chr(ord(content[0])+32)
    result += content[1:]
  else:
    result = content
  words = result.split('_')
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


def write_file(path, content):
  f = open(path, "a")
  f.truncate(0)
  f.write(content)
  f.close()

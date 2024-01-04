from io import StringIO


def snake_case_to_camel_case(content):
  words = content.split('_')
  if words[0].isupper():
    words[0] = words[0].lower()
  else:
    if (ord(words[0][0]) <= ord('Z')):
      result = chr(ord(words[0][0])+32)
      words[0] = result + words[0][1:]
  return str(words[0] + ''.join(word.title() for word in words[1:]))


def snake_case_to_pascal_case(content):
  words = content.split('_')
  return str(''.join(word.capitalize() for word in words))


class StringBuffer(StringIO):
  def write(self, content):
    super().write(content)
    super().write('\n')

  def addLine(self, count=1):
    for i in range(0, count):
      super().write('\n')

  def writeInline(self, content):
    super().write(content)


def write_file(path, content):
  f = open(path, "a")
  f.truncate(0)
  f.write(content)
  f.close()

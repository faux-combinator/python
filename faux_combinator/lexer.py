import re
base_regexp = "^(%s)" # regexp to capture the value

def lex(rules, code):
  tokens = []
  while code:
    code = code.lstrip(' \t')
    for rule in rules:
      pattern, type = rule
      result = re.search(base_regexp % pattern, code)
      if result:
        value = result.group(1)
        tokens.append({'type': type, 'value': value})
        code = code[len(value):]
        break
    else:
      raise LexerException("unable to match {0}".format(code[0:15]))

  return tokens

class LexerException(Exception):
  pass

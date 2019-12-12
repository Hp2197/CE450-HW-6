def prnt_lnk(s):
  res = '<'
  while s != empty:
    res += str(first(s)) + ' '
    s = rest(s)
  res += '>'
  return res

prnt_lnk(link(1, link(2, link(3, link(4, empty)))))
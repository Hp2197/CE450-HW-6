def insrt(l, elm, ind):
  result = empty
  i = 0
  tmp = len_link_recursive(l)
  while len_link_recursive(l) > 0:
    if i == ind:
      result = extend_link(result, link(elm, empty))
      i += 1
    else:
      result = extend_link(result, link(first(l), empty))
      l = rest(l)
    i += 1
  if ind > i:
    result = extend_link(result, link(elm, empty))
  return result

l = link(11, link(12, link(13, empty)))
n = insrt(l, 2019, 1)
n
m = insrt(n, 2020, 20)
m
def change(lnk, u, v):
  result = empty
  while len_link_recursive(lnk) > 0:
    if first(lnk) == u:
      result = extend_link(result, [v, []])
    else:
      result = extend_link(result, [first(lnk), []])
    lnk = rest(lnk)
  return  result

l = link(1, link(2, link(3, empty)))
n=change(l, 3, 1)
n
m=change(n, 1, 2)
m
change(m, 5, 1)
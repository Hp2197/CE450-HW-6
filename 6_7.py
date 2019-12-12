def apnd(lnk, m):
  return extend_link(lnk, [m, []])

l = link(1, link(2, (link(3, empty))))
n = apnd(l, 4)
first(rest(rest(rest(n))))
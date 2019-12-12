def sum_lnk(lnk, g):
  result = 0
  while len_link_recursive(lnk) > 0:
    result += g(first(lnk))
    lnk = rest(lnk)
  return result

sqr = lambda x: x * x
dbl = lambda y: 2 * y
lnk1 = link(1, link(2, link(3, link(4, empty))))
sum_lnk (lnk1, sqr)
lnk2 = link(3, link(5, link(4, link(6, empty))))
sum_lnk (lnk2, dbl)
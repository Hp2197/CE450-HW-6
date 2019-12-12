def rvrs_lnk(s):
  res = empty
  while len_link_recursive(s) > 0:
    res = extend_link(link(first(s), empty), res)
    s = rest(s)
  return res

s = [1, [2, [3, [4, [ ] ]]]]
s = extend_link(s, [5, []])
rvrs_lnk(s)
[4, [3, [2, [1, [ ] ]]]
def cntn_link(s, elm):
  if s == empty:
    return False
  elif first(s) == elm:
    return True
  else:
    return False or cntn_link(rest(s), elm)

cntn_link (link(1, link(2, link(3, empty))), 1)
cntn_link (link(1, link(2, link(3, empty))), 4)
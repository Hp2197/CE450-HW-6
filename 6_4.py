def srt(lnk):
  if len_link_recursive(lnk) <= 1:
    return True
  elif first(lnk) > first(rest(lnk)):
    return False
  else:
    return True and srt(rest(lnk))

lnk1 = link(1, link(2, link(3, link(4, empty))))
srt(lnk1)
lnk2 = link(1, link(3, link(2, link(4, link(5, empty)))))
srt(lnk2)
lnk3 = link(3, link(3, link(3, empty)))
srt(lnk3)
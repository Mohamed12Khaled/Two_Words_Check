def checkTwoString(string):
  first, second = string.split(" ")
  if first[0] == second[0]:
    return True
  else:
    return False

print(checkTwoString("Shishir Shishir"))
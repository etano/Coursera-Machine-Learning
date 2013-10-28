xs = [3,2,4,0]
ys = [4,1,3,1]
m = len(xs)

def h(x,t0,t1):
  return t0 + t1*x

def J(t0,t1):
  tot = 0.
  for (x,y) in zip(xs,ys):
    tot += (h(x,t0,t1) - y)**2
  return tot/(2*m)

# 1
print m

# 2
print J(0,1)

# 3
print h(6,-2,0.5)

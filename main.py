import sympy as sp

sp.init_printing()

def str_function(f):
  return str(f).replace("**", "^")

x = sp.symbols("x")

print("---INPUT---")
f = sp.sympify(input("f(x) = "))
g = sp.sympify(input("g(x) = "))
fg = f.subs(x, g).expand()
ff = f.subs(x, f).expand()
gg = g.subs(x, g).expand()
gf = g.subs(x, f).expand()

print("---RESULTADO---")
print("f(x) = ", str_function(f))
print("g(x) = ", str_function(g))
print("(g°f)(x) = ", str_function(gf))
print("(f°f)(x) = ", str_function(ff))
print("(g°g)(x) = ", str_function(gg))
print("(f°g)(x) = ", str_function(fg))


def str_float(n):
  return str(n).rstrip("0").rstrip(".")

def str_fx(f, x):
  return str_float(f.subs({"x": x}).evalf(chop=True))

for i in range(3):
  print(f"---TESTE {i + 1}---")
  x = float(input("x = "))
  print(f"(g°f)({str_float(x)}) = {str_fx(gf, x)}")
  print(f"(f°f)({str_float(x)}) = {str_fx(ff, x)}")
  print(f"(g°g)({str_float(x)}) = {str_fx(gg, x)}")
  print(f"(f°g)({str_float(x)}) = {str_fx(fg, x)}")
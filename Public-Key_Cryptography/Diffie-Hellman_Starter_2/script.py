# def is_primitive_element(g, p):
#     result=[]
#     for i in range(1, p-1):
#         tmp=pow(g,i,p)
#         if tmp==1:
#             return False
#     return True


# def find_primitive_element(p):
#     for g in range(2, p):
#         if is_primitive_element(g, p):
#             return g
#     return None

# p = 28151
# primitive_element = find_primitive_element(p)

# if primitive_element is not None:
#     print(f"The smallest primitive element in F{p} is {primitive_element}.")
# else:
#     print(f"No primitive element found in F{p}.")
from primefac import primefac

p = 28151
totient = p - 1 
totient_factors = set(primefac(totient))
print(totient_factors)
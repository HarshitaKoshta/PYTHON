a = int(input("Enter first term : "))
d = int(input("Enter common difference: "))
n = int(input("Enter n: "))

nth_term = a+(n-1)*d

sum_n_terms = n*(2*a+(n-1)*d) // 2 

print("nth term is ",nth_term)
print("Sum of n terms:", sum_n_terms)
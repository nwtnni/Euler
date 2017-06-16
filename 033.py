'''
033: Digit Canceling Fractions

Newton Ni
'''

if __name__ == "__main__":
    
    final_n = 1
    final_d = 1
    for d in range(10, 100):
        for n in range(10, d):

            proper = float(n) / float(d)

            n_ten = n / 10
            n_one = n % 10

            d_ten = d / 10
            d_one = d % 10

            if (n_ten == d_one and d_ten != 0 and float(n_one) / d_ten == proper):
                final_n *= n_one
                final_d *= d_ten 

            elif n_one == d_ten and d_one != 0 and float(n_ten) / d_one == proper:
                final_n *= n_ten
                final_d *= d_one
    
    print final_n, "/", final_d

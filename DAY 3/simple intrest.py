def calculate_sample_intrest(principal,time,rate=1)
    return(principal*rate*time)/100
intrest = calculate_sample_intrest(1000,2)
print(f"simple intrest:{intrest}")
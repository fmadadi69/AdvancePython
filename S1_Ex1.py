num_prime_dict = dict()


def prime_factors(factor):
    for f in range(2, int(factor ** 0.5) + 1):
        if factor % f == 0:
            return False
    else:
        return True


def prime_divisors(number):
    divisors = []
    for i in range(2, number):
        if number % i == 0 and prime_factors(i):
            divisors.append(i)
    # print(number, divisors)
    return len(divisors)


def max_prime_factors():
    for index in range(10):
        num = int(input())
        num_prime_dict[num] = prime_divisors(num)
    # print(max(num_prime_dict.values()))
    max_key = [key for key, value in num_prime_dict.items() if value == max(num_prime_dict.values())]
    if len(max_key) > 1:
        return f'{max(max_key)} {num_prime_dict[max(max_key)]}'
    else:
        return f'{max_key[0]} {num_prime_dict[max(max_key)]}'


print(max_prime_factors())

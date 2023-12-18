import sys

input = sys.stdin.readline


def mod_pow(base, exponent, modulus):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_pow = mod_pow(base, exponent // 2, modulus)
        return (half_pow * half_pow) % modulus
    else:
        half_pow = mod_pow(base, (exponent - 1) // 2, modulus)
        return (base * half_pow * half_pow) % modulus


k, p, n = map(int, input().split())
MOD = 10 ** 9 + 7
p_pow_10n = mod_pow(p, 10 * n, MOD)
result = (k * p_pow_10n) % MOD

print(result)
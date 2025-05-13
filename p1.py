def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m

def chinese_remainder_theorem(remainders, moduli):
    if len(remainders) != len(moduli):
        raise ValueError("Lists must be the same length")

    M = 1
    for m in moduli:
        M *= m

    result = 0
    for ai, mi in zip(remainders, moduli):
        Mi = M // mi
        inv = mod_inverse(Mi, mi)
        result += ai * Mi * inv

    return result % M
remainders = [2, 3, 2]
moduli = [3, 5, 7]

x = chinese_remainder_theorem(remainders, moduli)
print("x ≡", x)

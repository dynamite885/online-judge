for i in range(int(input())):
    a = input()
    b = input()
    t = {c for c in a} & {c for c in b}
    print(f"Case #{i + 1}:", len(a + b) - 2 * sum(min(a.count(c), b.count(c)) for c in t))
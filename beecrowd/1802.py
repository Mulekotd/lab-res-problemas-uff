# Leitura das listas
p, *port = map(int, input().split())
m, *math = map(int, input().split())
f, *phys = map(int, input().split())
q, *chem = map(int, input().split())
b, *bio  = map(int, input().split())
K = int(input())

# Gera todas as somas possíveis
sums = []
for a in port:
    for c in math:
        for d in phys:
            for e in chem:
                for g in bio:
                    sums.append(a + c + d + e + g)

# Ordena em ordem decrescente
sums.sort(reverse=True)

# Soma os K maiores
result = sum(sums[:K])

print(result)

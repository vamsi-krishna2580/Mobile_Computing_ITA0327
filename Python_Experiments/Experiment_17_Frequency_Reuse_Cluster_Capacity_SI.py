import math

S = 420  # total duplex channels available
M = 10   # number of times the cluster is replicated
n = 4    # path-loss exponent (urban)

valid = sorted({
    i * i + i * j + j * j
    for i in range(0, 5)
    for j in range(0, 5)
} - {0})[:8]

print(f"{'N':>3}{'D/R':>8}{'ch/cell':>9}{'Capacity C':>12}{'S/I (dB)':>10}")
for N in valid:
    Q = math.sqrt(3 * N)  # co-channel reuse ratio D/R
    k = S // N            # channels per cell
    C = M * k * N         # system capacity = M*k*N
    si = (Q ** n) / 6     # 6 first-tier interferers
    print(f"{N:>3}{Q:8.3f}{k:9d}{C:12d}{10 * math.log10(si):10.2f}")

req = 18.0  # AMPS requirement (dB)
for N in valid:
    if 10 * math.log10((math.sqrt(3 * N) ** n) / 6) >= req:
        print(f"\nSmallest cluster size meeting S/I >= {req} dB : N = {N}")
        break

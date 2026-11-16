import numpy as np

rng = np.random.default_rng(7)
D = 2000.0  # BS1 at x=0, BS2 at x=D (metres)
P0, n, sigma = -30.0, 3.5, 4.0  # dBm at 1 m, path-loss exponent, shadowing sd (dB)
x = np.arange(10, D, 5.0)  # mobile moves from BS1 to BS2


def rss(d, shadow):
    return P0 - 10 * n * np.log10(d) + shadow


r1 = rss(x, rng.normal(0, sigma, x.size))
r2 = rss(D - x, rng.normal(0, sigma, x.size))


def run(H):
    serving, handoffs, log = 1, 0, []
    for xi, a, b in zip(x, r1, r2):
        if serving == 1 and b > a + H:
            serving, handoffs = 2, handoffs + 1
            log.append((float(xi), "1->2"))
        elif serving == 2 and a > b + H:
            serving, handoffs = 1, handoffs + 1
            log.append((float(xi), "2->1"))
    return handoffs, log


print(f"{'H (dB)':>7}{'Handoffs':>10}{'Ping-pongs':>12}")
for H in (0, 2, 4, 6, 8, 10):
    h, log = run(H)
    print(f"{H:7d}{h:10d}{max(h - 1, 0):12d}")

h, log = run(6)
print("\nHandoff events with H = 6 dB (position in metres):", log)

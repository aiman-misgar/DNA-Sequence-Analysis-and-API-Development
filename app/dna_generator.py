from functools import lru_cache
import random as R

@lru_cache(maxsize=5000)
def generate_dna_sequence(id: str, region: str, age: int, dna_seed: str) -> str:
    R.seed(f"{id}+{region}+{age}")
    
    Q = {
        "apac": ["agtc", "agct", "actg", "atgc", "actg", "agtc"],
        "na": ["gtac", "gcat", "gcta"],
        "latam": ["cgta", "ctga", "catg"],
        "emea": ["aagt", "aatg", "aagc"],
    }

    def F(S):
        return list({
            S[i : i + 4]
            for i in range(0, len(S) - 3, 4)
            if S[i : i + 4] in {q for v in Q.values() for q in v}
        })

    L, T, C = [], 0, 5000  # << small length
    M = F(dna_seed)

    if not M:
        return "x"

    while T < C:
        Z = R.choice(M)
        N = R.randint(1, min(C - T, 5))  # small repeat count
        W = Z * N
        L.append(W)
        T += len(W)

    return "".join(L)[:C]

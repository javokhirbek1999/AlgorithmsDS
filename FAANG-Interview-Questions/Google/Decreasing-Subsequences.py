"""
Time: O(n^2)
Space: O(n)
"""

from typing import List


def solve(subsequences: List[int]) -> int:

    subseqs = []

    for number in subsequences:
        if not subseqs:
            subseqs.append([number])
        else:
            inserted = False
            for subseq in subseqs:
                if subseq[-1] > number:
                    subseq.append(number)
                    inserted = True
                    break
            
            if not inserted:
                subseqs.append([number])

    return len(subseqs)

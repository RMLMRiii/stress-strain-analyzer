# Stress-Strain Analyzer
# Calculates stress and strain from sample material test data

from typing import List, Tuple


def calculate_stress(force: float, area: float) -> float:
    return force / area


def calculate_strain(change_in_length: float, original_length: float) -> float:
    return change_in_length / original_length


def analyze_data(area: float, original_length: float, data: List[Tuple[float, float]]) -> List[Tuple[float, float, float, float]]:
    results = []

    for force, change_in_length in data:
        stress = calculate_stress(force, area)
        strain = calculate_strain(change_in_length, original_length)
        results.append((force, change_in_length, stress, strain))

    return results


def display_results(results: List[Tuple[float, float, float, float]]) -> None:
    print("\nSTRESS-STRAIN ANALYZER")
    print("-" * 70)
    print(f"{'Force (N)':>12} | {'ΔL (m)':>10} | {'Stress (Pa)':>15} | {'Strain':>12}")
    print("-" * 70)

    for force, change_in_length, stress, strain in results:
        print(f"{force:12.2f} | {change_in_length:10.6f} | {stress:15.2f} | {strain:12.6f}")


def main() -> None:
    area = 0.0005
    original_length = 2.0

    sample_data = [
        (1000.0, 0.0002),
        (2000.0, 0.0005),
        (3000.0, 0.0009),
        (4000.0, 0.0014),
    ]

    results = analyze_data(area, original_length, sample_data)
    display_results(results)


if __name__ == "__main__":
    main()

import csv

DATA_FILE = "material_test_data.csv"


def display_data() -> None:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No material test data found.")
                return

            print("\nMATERIAL TEST DATA")
            print("-" * 40)

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("Material test data file not found.")
    except OSError as error:
        print(f"Error reading material test data: {error}")


if __name__ == "__main__":
    display_data()

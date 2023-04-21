import json

from typing import Optional


def find_word(letters: str, positions: Optional[str] = None) -> list[str]:
    matches: list[str] = []
    letters = [letter for letter in letters]

    with open("words_dutch.json", "r") as f:
        word_mapping = json.load(f)

        for key, values in word_mapping.items():
            if all([letter in key for letter in letters]):
                if not positions:
                    matches += values
                    continue

                if len(positions) != 12:
                    raise ValueError("invalid positions, length should be 12")

                for value in values:
                    possible_match = True

                    for combination in zip(value, positions):
                        check, position = combination

                        if not position.isalpha():
                            continue

                        if check != position:
                            possible_match = False
                            break

                    if possible_match:
                        matches.append(value)

    return matches


def print_help() -> None:
    print("\n" + "tweevoortwaalf word helper".rjust(42, " ") + "\n")
    print(
        "Enter the known letters into the input, the order does not matter.\n"
        "If you already know the position of letters, you can add a comma (,)\n"
        "after the known letters and put in 12 positions. Positions for which you\n"
        "don't know a letter yet, you need to fill in a dot (.)\n"
        "For example: alspveld,v..s.pe.....\n\n"
    )


def main() -> None:
    print_help()

    try:
        while True:
            user_input = input("Enter the known letters and positions: ")
            known_letters, _, positions = user_input.partition(",")
            matches = find_word(known_letters, positions)
            print(matches)
            print(f"number of matches: {len(matches)}")
    except KeyboardInterrupt:
        print("\nDone guessing")
    except ValueError as e:
        print(f"Input error: {e}")


if __name__ == '__main__':
    main()

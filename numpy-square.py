import numpy as np
import sys

# 72 Names of God
NAMES_OF_GOD = [
    "Vav-Heh-Vav", "Yod-Lamed-Yod", "Samekh-Yod-Tet", "Ayin-Lamed-Mem", "Mem-Heh-Shin",
    "Lamed-Lamed-Heh", "Aleph-Kaf-Aleph", "Kaf-Heh-Tav", "Heh-Tet-Aleph", "Aleph-Lamed-Dalet",
    "Aleph-Lamed-Mem", "Heh-Heh-Aleph", "Yod-Lamed-Kaf", "Yod-Nun-Yod", "Nun-Mem-Lamed",
    "Heh-Kaf-Mem", "Vav-Yod-Vav", "Lamed-Kaf-Aleph", "Tet-Vav-Heh", "Nun-Lamed-Heh",
    "Mem-Yod-Kaf", "Nun-Yod-Tav", "Mem-Yod-Heh", "Vav-Kaf-Lamed", "Lamed-Yod-Tet",
    "Tet-Lamed-Kaf", "Heh-Vav-Heh", "Lamed-Yod-Yod", "Heh-Aleph-Heh", "Aleph-Kaf-Kaf",
    "Mem-Tet-Vav", "Nun-Tet-Heh", "Aleph-Yod-Tav", "Mem-Aleph-Vav", "Yod-Heh-Heh",
    "Yod-Heh-Tav", "Aleph-Heh-Yod", "Aleph-Kaf-Mem", "Yod-Heh-Heh", "Tet-Kaf-Nun",
    "Nun-Tav-Vav", "Aleph-Tet-Mem", "Heh-Tet-Yod", "Nun-Kaf-Heh", "Kaf-Yod-Kaf",
    "Heh-Tet-Yod", "Nun-Yod-Nun", "Heh-Yod-Heh", "Aleph-Mem-Tet", "Lamed-Aleph-Kaf",
    "Yod-Tet-Aleph", "Kaf-Tet-Yod", "Mem-Vav-Aleph", "Nun-Tav-Heh", "Heh-Yod-Yod",
    "Mem-Aleph-Lamed", "Aleph-Mem-Yod", "Tet-Lamed-Heh", "Nun-Aleph-Nun", "Mem-Heh-Nun",
    "Heh-Mem-Kaf", "Tet-Aleph-Kaf", "Lamed-Vav-Heh", "Vav-Aleph-Heh", "Aleph-Yod-Heh",
    "Tet-Yod-Kaf", "Nun-Kaf-Mem", "Aleph-Kaf-Aleph", "Vav-Mem-Tet", "Lamed-Tet-Heh",
    "Yod-Yod-Heh", "Nun-Heh-Mem"
]

# Music Notes for Numbers
MUSIC_NOTES = [
    "C", "D", "E", "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#", "C", "D", "E",
    "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#", "C"
]

# Planetary Correspondences
PLANETS = {
    3: "Saturn",
    4: "Jupiter",
    5: "Mars",
    6: "Sun",
    7: "Venus",
    8: "Mercury",
    9: "Moon"
}

def name_of_god(number):
    """Map a number to the corresponding Name of God."""
    index = (number - 1) % 72
    return NAMES_OF_GOD[index]

def music_note_for_number(number):
    """Map a number to its corresponding music note."""
    index = (number - 1) % len(MUSIC_NOTES)
    return MUSIC_NOTES[index]

def odd_magic_square(n):
    """Create an odd-order magic square using the Siamese method."""
    m = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        m[i, j] = num
        i, j = (i - 1) % n, (j + 1) % n
        if m[i, j]: 
            i = (i + 2) % n
            j = (j - 1) % n
    return m

def lux_magic_square(n):
    """Create a singly even-order magic square using the LUX method."""
    if n % 2 != 0 or n % 4 == 0:
        raise ValueError("LUX method works only for singly even-order (n = 4k + 2) magic squares.")

    half_n = n // 2
    odd_square = odd_magic_square(half_n)

    # Create the quadrants
    A = odd_square
    B = odd_square + half_n * half_n
    C = odd_square + 2 * half_n * half_n
    D = odd_square + 3 * half_n * half_n

    # Combine quadrants
    magic_square = np.zeros((n, n), dtype=int)
    magic_square[:half_n, :half_n] = A  # Top-left
    magic_square[:half_n, half_n:] = D  # Top-right
    magic_square[half_n:, :half_n] = C  # Bottom-left
    magic_square[half_n:, half_n:] = B  # Bottom-right

    # Columns to swap for left quadrants
    k = (half_n - 1) // 2
    cols_left = list(range(k))
    cols_right = list(range(n - k, n))

    # Swap left columns of A and C
    magic_square[:half_n, cols_left], magic_square[half_n:, cols_left] = (
        magic_square[half_n:, cols_left],
        magic_square[:half_n, cols_left],
    )

    # Swap right columns of B and D
    magic_square[:half_n, cols_right], magic_square[half_n:, cols_right] = (
        magic_square[half_n:, cols_right],
        magic_square[:half_n, cols_right],
    )

    # Center column adjustments
    magic_square[half_n - 1, k], magic_square[half_n, k] = (
        magic_square[half_n, k],
        magic_square[half_n - 1, k],
    )
    magic_square[half_n - 1, n - k - 1], magic_square[half_n, n - k - 1] = (
        magic_square[half_n, n - k - 1],
        magic_square[half_n - 1, n - k - 1],
    )

    return magic_square

def display_names_square(square):
    """Convert a magic square to Names of God."""
    return np.vectorize(name_of_god)(square)

def display_music_square(square):
    """Convert a magic square to music notes."""
    return np.vectorize(music_note_for_number)(square)

def calculate_magic_constant(n):
    """Calculate the magic constant for a given magic square size."""
    return n * (n**2 + 1) // 2

def format_matrix(matrix):
    """Format a 2D matrix for pretty printing."""
    return "\n".join(["\t".join(map(str, row)) for row in matrix])

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <size> --odd|--lux [--numbers|--gods|--notes|--all]")
        sys.exit(1)

    # Parse arguments
    n = int(sys.argv[1])
    flag = sys.argv[2]
    show_numbers = "--numbers" in sys.argv
    show_gods = "--gods" in sys.argv
    show_notes = "--notes" in sys.argv
    show_all = "--all" in sys.argv

    # Generate the appropriate magic square
    try:
        if flag == "--odd":
            if n % 2 == 0:
                raise ValueError("Odd-order magic squares require n to be odd.")
            result = odd_magic_square(n)
        elif flag == "--lux":
            result = lux_magic_square(n)
        else:
            raise ValueError("Unknown flag. Use --odd or --lux.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Calculate additional information
    magic_constant = calculate_magic_constant(n)
    total_sum = result.sum()
    names_square = display_names_square(result)
    music_square = display_music_square(result)
    planet = PLANETS.get(n, "Unknown")

    # Display results based on flags
    print(f"\nPlanetary Correspondence: {planet}")
    if show_numbers or show_all:
        print("\nMagic Square (Numbers):")
        print(format_matrix(result))
        print(f"\nMagic Constant: {magic_constant}")
        print(f"Sum of All Squares: {total_sum}")

    if show_gods or show_all:
        print("\nMagic Square (Names of God):")
        print(format_matrix(names_square))

    if show_notes or show_all:
        print("\nMagic Square (Music Notes):")
        print(format_matrix(music_square))

if __name__ == "__main__":
    main()
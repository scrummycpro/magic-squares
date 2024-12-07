# Magic Square Generator with Planetary Correspondence, Names of God, and Music Notes

## Overview
This Python script generates **magic squares** of various sizes and associates them with:
- **Planetary correspondences** (based on classical astrology and esoteric traditions).
- **72 Names of God** (using Kabbalistic mappings).
- **Musical notes** (derived from modular arithmetic).

The script allows for the exploration of mystical, mathematical, and musical properties of magic squares.

---

## What Are Magic Squares?
A magic square is a grid of distinct numbers arranged such that the sum of every row, column, and diagonal is the same. This sum is called the **magic constant**.

### Historical Context
Magic squares have a rich history spanning various cultures:
- **China**: The earliest known magic square, the Lo Shu, is a 3x3 square associated with cosmic balance.
- **India**: Used in yantras and astrological practices.
- **Islamic World**: Integrated into talismans for mystical purposes.
- **Europe**: Popularized during the Renaissance for use in alchemy, numerology, and art.

### Esoteric Associations
In Western esotericism, magic squares are linked to the classical planets. Each square’s size corresponds to a specific planet and is used for talismans and rituals:

| **Square Size** | **Planet**      | **Symbolism**                                                   |
|------------------|-----------------|-----------------------------------------------------------------|
| 3x3              | Saturn          | Discipline, limitation, and protection                         |
| 4x4              | Jupiter         | Abundance, expansion, and luck                                 |
| 5x5              | Mars            | Strength, courage, and assertiveness                          |
| 6x6              | Sun             | Vitality, success, and illumination                           |
| 7x7              | Venus           | Love, harmony, and creativity                                 |
| 8x8              | Mercury         | Communication, intellect, and adaptability                    |
| 9x9              | Moon            | Emotion, intuition, and cycles                                |

---

## Features
### 1. Planetary Correspondence
The script determines the associated planet for each magic square size (3x3 through 9x9). The planet is displayed in the output to highlight its esoteric meaning.

### 2. 72 Names of God
Each number in the magic square is mapped to one of the **72 Names of God**, derived from Kabbalistic traditions. These sacred names are believed to hold divine powers and are often used in meditation and mystical practices.

### 3. Musical Notes
The numbers are also mapped to **musical notes**, cycling through an octave using modular arithmetic. This allows for the exploration of the harmonic and vibrational aspects of the magic square.

### 4. Magic Constant and Total Sum
The script calculates:
- **Magic Constant**: The sum of any row, column, or diagonal.
- **Total Sum**: The sum of all numbers in the square.

### 5. Flexible Output
Users can customize the output using flags:
- `--numbers`: Displays the magic square with numbers.
- `--gods`: Displays the magic square with the 72 Names of God.
- `--notes`: Displays the magic square with musical notes.
- `--all`: Displays all outputs.

---

## Installation and Usage
### Prerequisites
- Python 3.x
- NumPy

### Installation
1. Clone this repository or download the script.
2. Install NumPy if not already installed:
   ```bash
   pip install numpy
   ```

### Usage
Run the script from the command line:
```bash
python script.py <size> --odd|--lux [--numbers|--gods|--notes|--all]
```

#### Positional Arguments
- `<size>`: The size of the magic square (e.g., 3, 4, 5, 6, etc.).
- `--odd` or `--lux`: Specify the method for generating the square:
  - `--odd`: For odd-sized squares (e.g., 3x3, 5x5).
  - `--lux`: For singly even-sized squares (e.g., 4x4, 6x6).

#### Optional Flags
- `--numbers`: Displays the magic square with numbers.
- `--gods`: Displays the magic square with the 72 Names of God.
- `--notes`: Displays the magic square with musical notes.
- `--all`: Displays all outputs.

#### Example Commands
1. Generate a 3x3 magic square with all outputs:
   ```bash
   python script.py 3 --odd --all
   ```

2. Generate a 6x6 magic square with only Names of God:
   ```bash
   python script.py 6 --lux --gods
   ```

---

## Output Examples
### Example: 3x3 Magic Square (Saturn)
**Command:**
```bash
python script.py 3 --odd --all
```

**Output:**
```
Planetary Correspondence: Saturn

Magic Square (Numbers):
4	9	2
3	5	7
8	1	6

Magic Constant: 15
Sum of All Squares: 45

Magic Square (Names of God):
Ayin-Lamed-Mem	Heh-Tet-Aleph	Yod-Lamed-Yod
Samekh-Yod-Tet	Mem-Heh-Shin	Kaf-Heh-Tav
Nun-Lamed-Heh	Vav-Heh-Vav	Heh-Vav-Heh

Magic Square (Music Notes):
E	A	D
C	F	G
B	C	E
```

---

## Behind the Scenes
### Magic Constant Formula
The magic constant is calculated as:
\[
\text{Magic Constant} = \frac{n(n^2 + 1)}{2}
\]
Where \(n\) is the size of the square.

### Mapping Numbers to Names of God
Numbers are mapped cyclically to the 72 Names of God using:
\[
\text{Index} = (\text{Number} - 1) \mod 72
\]

### Mapping Numbers to Music Notes
Numbers are mapped cyclically to an octave of musical notes using:
\[
\text{Index} = (\text{Number} - 1) \mod 12
\]

---

## Additional Notes
### Applications
1. **Esoteric Practices**:
   - Talismans: Inscribe the square on metal or paper to invoke planetary energies.
   - Meditations: Chant the corresponding Names of God while visualizing the square.

2. **Music Theory**:
   - Explore the harmonic relationships of numbers and notes within the square.

3. **Mathematics**:
   - Use the script to study the properties and symmetry of magic squares.

### Future Enhancements
- Add support for doubly even magic squares (e.g., 8x8).
- Include visualization options (e.g., plotting the square).

---

## License
This project is licensed under the MIT License. Feel free to use and modify it for personal or educational purposes.


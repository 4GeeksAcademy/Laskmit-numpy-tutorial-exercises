<!-- hide -->
<div align="center">

# Numpy Tutorial Exercises

[![Certified by 4Geeks](https://img.shields.io/badge/4Geeks-certified%20tutorial-2563eb)](https://4geeks.com)
[![Autograded with LearnPack](https://img.shields.io/badge/LearnPack-autograded-2563eb)](https://learnpack.co)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-fb5a1f)](https://codespaces.new/?repo=4GeeksAcademy/numpy-tutorial-exercises)

🇪🇸 [Leer en español](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/blob/HEAD/README.es.md) · 🇬🇧 [Read in English](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/blob/HEAD/README.md)

![Cover of the interactive NumPy tutorial, showing the words Learn Python Numpy interactive next to the blue and light blue NumPy cube logo on a black background](https://raw.githubusercontent.com/4GeeksAcademy/numpy-tutorial-exercises/master/.learn/assets/preview.jpeg)

</div>
<!-- endhide -->

This LearnPack tutorial teaches NumPy through 21 exercises: one welcome page plus 20 auto-graded challenges on array creation, indexing, slicing, reshaping and basic statistics. You write every answer in a single `app.py` file and 53 pytest checks grade it. It drills `zeros`, `ones`, `arange`, `reshape`, `eye`, `pad`, `diag`, `nonzero`, `random`, `max` and `mean`. Estimated time: 10 hours, intermediate level.

<!-- hide -->

## 📋 About this tutorial

- **Difficulty:** intermediate
- **Estimated duration:** 10 hours
- **Language:** Python 3
- **Technologies:** Python, NumPy 1.24.2, pytest, LearnPack
- **Exercises:** 21 folders — 1 welcome page + 20 with automatic grading
- **Grading:** `incremental` mode, powered by LearnPack and pytest (53 `@pytest.mark.it` checks)
- **Available in:** English (`README.md`) and Spanish (`README.es.md`) inside every exercise

<!-- endhide -->

## 🎯 What will you learn?

NumPy is the array library that Pandas, scikit-learn and almost every scientific Python package are built on top of. This tutorial does not explain the theory of vector spaces: it makes you type the API until it sticks. Each exercise is one or two lines of code, so in a single sitting you touch the functions you will use every day.

By the end you will be comfortable with:

- Importing the library the canonical way, `import numpy as np`, and inspecting the installed build with `np.__version__` and `np.show_config()`.
- Reading the documentation without leaving Python, using `np.info(np.add)`.
- Creating arrays from nothing: `np.zeros()`, `np.ones()`, `np.eye()`, `np.arange()` and `np.array()`.
- Measuring what an array costs in RAM by multiplying its `.itemsize` by its `.size` (a vector of 10 floats takes 80 bytes).
- Editing values by position and by slice: `arr[4] = 1`, `matrix[1:-1, 1:-1] = 0`, `arr[::-1]`, `matrix[1::2, ::2] = 1`.
- Changing the shape of an array with `reshape()`, turning a 9-element vector into a 3×3 matrix.
- Searching inside an array with `np.nonzero()` and reading the tuple of index arrays it gives you back.
- Generating random data with `np.random.random()` and summarising it with `.max()` and `.mean()`.
- Growing a matrix with `np.pad()` and pulling out its main diagonal with `np.diag()`.
- The edge cases that bite everyone: `np.nan == np.nan` is `False`, `np.nan in set([np.nan])` is `True`, and `0.3 == 3 * 0.1` is `False`.

The exercises really are that short. This is the kind of slicing the last one, an 8×8 checkerboard, is built out of:

```python
import numpy as np

matrix = np.zeros((6, 6))

matrix[::2, 1::2] = 1   # ones on the even rows, odd columns

print(matrix[0])        # [0. 1. 0. 1. 0. 1.]
```

## 👀 What will you build?

There is no final project. You build one file, `app.py`, created in the first exercise and rewritten in every step afterwards. These are the 21 folders inside `.learn/exercises`, in order:

1. **`000` Welcome** — reading only, with no test: what NumPy is, why it is used, plus links to the official docs and a video.
2. **`001` Create Entry File** — create `app.py` in the root of the project. The single test only checks that the file exists.
3. **`002` Import NumPy** — import the library under the alias `np`.
4. **`003` NumPy Version** — print the installed version through `np.__version__`.
5. **`004` Your First Vector** — print a null vector of size 10 built with `np.zeros()`.
6. **`005` Array Memory Size** — print `80`, the memory that vector occupies, obtained from `.itemsize` and `.size`.
7. **`006` NumPy Documentation** — print the documentation of `np.add()` with `np.info()`.
8. **`007` Change Vector Values** — a null vector of size 10 whose fifth element (index `4`) is `1`.
9. **`008` Vector Ranging Values** — a vector with every integer from 10 to 49, built with `np.arange()`.
10. **`009` Reverse Vector** — the integers from 0 to 9 printed backwards using `array[::-1]`.
11. **`010` Matrix with Ranging Values** — the numbers 0 to 8 turned into a 3×3 matrix with `reshape()`.
12. **`011` Find Indexes of Non Zero Elements** — `np.nonzero()` over `[1,2,0,0,4,0]`, printing `(array([0, 1, 4]),)`.
13. **`012` Identity Matrix** — a 3×3 identity matrix created with `np.eye()`.
14. **`013` Random Values Array** — a variable named `arr` holding an array of 3 random values.
15. **`014` Minimum and Maximum** — `arr` with 10 random values, printing the largest one with `.max()`.
16. **`015` Mean Value** — `arr` with 10 random values, printing its average with `.mean()`.
17. **`016` Array Border** — a 5×5 matrix of ones whose centre is set to zero with `matrix[1:-1, 1:-1]`.
18. **`017` Add Border to Array** — a 3×3 matrix of ones wrapped in a border of zeros with `np.pad()`.
19. **`018` Result of Expressions** — print the six results of the `nan` and `inf` comparisons: `nan`, `False`, `False`, `nan`, `True`, `False`.
20. **`019` Diagonal** — print `[0 4 8]`, the diagonal of a 3×3 matrix, using `np.diag()`.
21. **`020` Checkerboard Pattern** — an 8×8 matrix filled with a checkerboard of zeros and ones.

## 🎓 What do you need before starting?

The tutorial is registered as **intermediate**, and the reason is Python, not mathematics. There is nothing here beyond arithmetic: the "matrices" are grids of numbers. What you do need is:

- **Comfortable Python basics** — variables, `print()`, lists and, above all, slice notation. Half the exercises are solved with a slice like `[::-1]`, `[1:-1, 1:-1]` or `[1::2, ::2]`.
- **No previous NumPy at all.** Exercise `002` starts from `import numpy as np`, and every function is introduced with a hint and a link to its page on numpy.org.
- **A Python 3 environment with NumPy and pytest.** If you open the repository in Codespaces, the dev container installs Python 3.10, `numpy==1.24.2` and `pytest==6.2.5` for you. Working locally you install them yourself.
- **Node.js 22** only if you run the exercises on your own machine, because LearnPack is a Node command line tool.

## ✅ How does the automatic grading work?

20 of the 21 folders ship a `test.py` file, and together they hold 53 checks written with `@pytest.mark.it("...")`, so each failure tells you in plain English what was expected. Grading mode is `incremental`: the exercises build on one another and all of them read the same `app.py` sitting in the root of the repository, not inside the exercise folder.

There are four kinds of check, and knowing which one you are facing saves a lot of time:

- **Output checks** capture what your program prints using pytest's `capsys` fixture. Up to exercise `012` they only require the expected text to appear somewhere in your output, but from `015` to `020` they compare the whole console output with `==`, character by character.
- **Source checks** open `app.py` and search for the function you were told to use: `zeros(`, `ones(`, `arange(`, `reshape(`, `eye(`, `pad(`, `diag(`, `nonzero`, `array`, `random(`, `max(`, `mean(`, `info(`, `itemsize`, `size`.
- **Anti-hardcoding checks** run a regular expression that fails if the expected result is written literally in your file. Eight exercises have one.
- **Import checks** in `013`, `014` and `015` run `from app import arr`, so `arr` has to exist as a variable at the top level of the module.

Run the tests from the LearnPack interface after editing `app.py`, and read the description of the failing check before touching your code.

## 💡 What mistakes should you avoid?

These are the traps that make the grader fail even when your NumPy is correct:

- **Leaving the previous exercise's code in `app.py`.** Everything is written in that one file, and from exercise `015` onwards the test compares the entire console output with `==`. One leftover `print()` from exercise `012` and a perfectly correct answer fails. Delete or comment out what you no longer need.
- **Confusing printing with assigning.** Exercises `013` and `014` are graded by importing the variable (`from app import arr`), so computing the value inside a `print()` without storing it in `arr` fails. Exercise `015` wants both things: the variable *and* the printed mean.
- **Typing the expected result by hand.** Exercises `004`, `005`, `007`, `008`, `009`, `010`, `011` and `012` run a regex that rejects the literal answer in your source, so `print("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]")` or `print(80)` will never pass.
- **Counting from one.** The "fifth element" in exercise `007` is `arr[4]`. The expected output is `[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]`.
- **Reversing without the slice.** Exercise `009` requires the literal `::-1` in your code. `np.flip()` prints exactly the right vector and still fails the check.
- **Changing the import style.** The regex looks for `import numpy as np`. Neither `import numpy` nor `from numpy import *` passes exercises `002` and `003`.
- **Guessing the wrong size in `016` and `017`.** The instructions of `016` never say how big the matrix is — the `💻 Expected Output` block further down the same statement does: 5×5, ones on the border and a 3×3 block of zeros in the middle. In `017` you start from a 3×3 of ones and `np.pad()` turns it into a 5×5, printed right there too. Read that block before writing any code.
- **Unwrapping the result of `np.nonzero()` in `011`.** The expected output is the tuple `(array([0, 1, 4]),)`. Printing `np.nonzero(arr)[0]` gives `[0 1 4]` and fails.

## ❓ Frequently asked questions

### Do I need to know Python before learning NumPy?

Yes, the basics. The tutorial is classified as intermediate because it assumes you already write variables, lists, `print()` and, most importantly, slices such as `lista[2:5]` or `lista[::-1]`. It assumes zero NumPy: the second exercise is the `import`.

### Do all the exercises use the same file?

Yes. You create `app.py` in exercise `001`, in the root of the project, and every following exercise is solved by editing that same file. That is what `incremental` grading means here, and it is also why cleaning up the previous answer matters before running the tests again.

### Why does my exercise fail if the output looks correct?

Almost always for one of three reasons: there is an extra `print()` left over from a previous exercise and the test compares the full output with `==`; you wrote the expected result as a literal string and the anti-hardcoding regex caught it; or you solved it with a different function from the one the check looks for in the source, such as `np.flip()` instead of `[::-1]`.

### Which NumPy functions does the tutorial cover?

Array creation with `array()`, `zeros()`, `ones()`, `eye()`, `arange()` and `random.random()`; shape and structure with `reshape()`, `pad()`, `diag()` and `nonzero()`; statistics with `max()` and `mean()`; the `itemsize` and `size` attributes; introspection with `__version__`, `show_config()` and `info()`; and index and slice notation applied to vectors and matrices.

### Do I have to install NumPy and pytest myself?

Only if you work on your own machine. The repository ships a dev container that, when the Codespace is created, installs Python 3.10, Node.js 22, `numpy==1.24.2`, `pandas`, `pytest==6.2.5` and LearnPack with its Python plugin. Locally it is two commands: a `pip3 install` for the Python packages and an `npm i` for LearnPack and its Python plugin.

### Are the solutions included, and does the tutorial cost anything?

19 of the 21 folders include a `solution.hide.py` file with the reference answer; LearnPack keeps it out of the way while you work, but it lives in the repository if you get truly stuck. Opening and following the tutorial costs nothing, and the code you write in `app.py` is yours. Note that the repository does not include a `LICENSE` file, so the teaching material itself is not published under an open source license.

<!-- hide -->

## 📚 Related tutorials

If you are heading towards data analysis, these interactive tutorials sit well around this one:

- [Learn Python Interactively (beginner)](https://4geeks.com/en/interactive-exercise/python-beginner-exercises) — the previous step if variables and lists still feel new.
- [Learn Python Loops and lists Interactively](https://4geeks.com/en/interactive-exercise/python-loops-lists-exercises) — slicing practice, which is what this tutorial leans on hardest.
- [Linear Algebra in Python and NumPy](https://4geeks.com/en/interactive-exercise/linear-algebra-in-python-and-numpy) — the natural next step: dot products, determinants and eigenvalues with the same library.
- [Master Python by practice (interactive)](https://4geeks.com/en/interactive-exercise/master-python-exercises) — more general practice once you are done.

## 🚀 How to start

The fastest route needs no local installation at all: open the repository in [GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/numpy-tutorial-exercises) (recommended) or in [Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/numpy-tutorial-exercises.git).

> 💡 Once VSCode opens, the LearnPack exercises should start on their own. If they do not, type `learnpack start` in the terminal.

## 💻 Local installation

1. Install [LearnPack](https://learnpack.co) and its Python plugin. You need Node.js 22 and Python 3.10 or higher:

    ```bash
    npm i @learnpack/learnpack@5.0.348 -g && learnpack plugins:install @learnpack/python@1.0.3
    ```

2. Clone the repository and enter the folder:

    ```bash
    git clone https://github.com/4GeeksAcademy/numpy-tutorial-exercises.git
    cd numpy-tutorial-exercises
    ```

3. Install the Python dependencies and start the tutorial from the same level as `learn.json`:

    ```bash
    pip3 install pytest==6.2.5 mock pytest-testdox toml numpy==1.24.2 pandas
    learnpack start
    ```

## 📚 How the exercises are organized

Every exercise lives in its own folder inside [`.learn/exercises`](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/tree/HEAD/.learn/exercises) and contains only text and tests:

- **`README.md`** — the statement in English, with the instructions, hints and, in several exercises, the exact expected output.
- **`README.es.md`** — the same statement in Spanish.
- **`test.py`** — the pytest script that grades the exercise. Reading it is the fastest way to understand exactly what is expected of you.
- **`solution.hide.py`** — the reference solution, present in 19 of the 21 folders (every one except `000-welcome` and `001-create-entry-file`).

The file you actually edit, `app.py`, is not inside these folders: it lives in the root of the repository, next to [`learn.json`](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/blob/HEAD/learn.json), and it is shared by every exercise. The `000-welcome` folder is the exception to everything: reading only, with no test and no solution.

## 🤝 Contributors

Thanks to these people, who built, tested and translated the exercises: [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr), [Tomás Gonzáles (tommygonzaleza)](https://github.com/tommygonzaleza), [Paolo Lucano (plucodev)](https://github.com/plucodev) and [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo).

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. All contributions are welcome: if you spot a bug or a typo, open an issue or a pull request in the [repository](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/issues).

This and many other exercises are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by Alejandro Sánchez and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer) and our [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning). See the full list of people who have contributed code in the [contributors graph](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/graphs/contributors).

<!-- endhide -->

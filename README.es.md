<!-- hide -->
<div align="center">

# Tutorial Interactivo de Numpy

[![Certificado por 4Geeks](https://img.shields.io/badge/4Geeks-tutorial%20certificado-2563eb)](https://4geeks.com)
[![Autocorregido con LearnPack](https://img.shields.io/badge/LearnPack-autocorregido-2563eb)](https://learnpack.co)
[![Abrir en Codespaces](https://img.shields.io/badge/Abrir%20en-Codespaces-fb5a1f)](https://codespaces.new/?repo=4GeeksAcademy/numpy-tutorial-exercises)

🇪🇸 [Leer en español](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/blob/HEAD/README.es.md) · 🇬🇧 [Read in English](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/blob/HEAD/README.md)

![Portada del tutorial interactivo de NumPy, con el texto Learn Python Numpy interactive junto al logo del cubo de NumPy en azul y azul claro sobre fondo negro](https://raw.githubusercontent.com/4GeeksAcademy/numpy-tutorial-exercises/master/.learn/assets/preview.jpeg)

</div>
<!-- endhide -->

Este tutorial de LearnPack enseña NumPy con 21 ejercicios: una página de bienvenida y 20 retos autocorregidos sobre creación de arrays, indexado, slicing, cambio de forma y estadística básica. Todo se escribe en un único fichero `app.py` y lo corrigen 53 comprobaciones de pytest. Practicas `zeros`, `ones`, `arange`, `reshape`, `eye`, `pad`, `diag`, `nonzero`, `random`, `max` y `mean`. Duración estimada: 10 horas, nivel intermedio.

<!-- hide -->

## 📋 Ficha del tutorial

- **Dificultad:** intermedia
- **Duración estimada:** 10 horas
- **Lenguaje:** Python 3
- **Tecnologías:** Python, NumPy 1.24.2, pytest, LearnPack
- **Ejercicios:** 21 carpetas — 1 de bienvenida + 20 con corrección automática
- **Corrección:** modo `incremental`, con LearnPack y pytest (53 comprobaciones `@pytest.mark.it`)
- **Idiomas:** español (`README.es.md`) e inglés (`README.md`) dentro de cada ejercicio

<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

NumPy es la librería de arrays sobre la que están construidos Pandas, scikit-learn y casi todo el Python científico. Este tutorial no te explica la teoría de los espacios vectoriales: te hace teclear la API hasta que se te queda. Cada ejercicio son una o dos líneas de código, así que en una sola sesión tocas las funciones que vas a usar todos los días.

Al terminar vas a manejar con soltura:

- El import canónico, `import numpy as np`, y cómo mirar la instalación con `np.__version__` y `np.show_config()`.
- Cómo consultar la documentación sin salir de Python, con `np.info(np.add)`.
- La creación de arrays desde cero: `np.zeros()`, `np.ones()`, `np.eye()`, `np.arange()` y `np.array()`.
- El cálculo de lo que ocupa un array en memoria multiplicando `.itemsize` por `.size` (un vector de 10 decimales ocupa 80 bytes).
- La modificación de valores por posición y por rebanada: `arr[4] = 1`, `matrix[1:-1, 1:-1] = 0`, `arr[::-1]`, `matrix[1::2, ::2] = 1`.
- El cambio de forma con `reshape()`, para convertir un vector de 9 elementos en una matriz de 3×3.
- La búsqueda dentro de un array con `np.nonzero()` y cómo leer la tupla de índices que devuelve.
- La generación de datos aleatorios con `np.random.random()` y su resumen con `.max()` y `.mean()`.
- El crecimiento de una matriz con `np.pad()` y la extracción de su diagonal con `np.diag()`.
- Los casos raros que sorprenden a todo el mundo: `np.nan == np.nan` es `False`, `np.nan in set([np.nan])` es `True` y `0.3 == 3 * 0.1` es `False`.

Los ejercicios son así de cortos. Estas son las rebanadas con las que se construye el último, un tablero de ajedrez de 8×8:

```python
import numpy as np

matrix = np.zeros((6, 6))

matrix[::2, 1::2] = 1   # unos en las filas pares, columnas impares

print(matrix[0])        # [0. 1. 0. 1. 0. 1.]
```

## 👀 ¿Qué vas a construir?

Aquí no hay proyecto final. Construyes un solo fichero, `app.py`, que creas en el primer ejercicio y reescribes en cada paso siguiente. Estas son las 21 carpetas de `.learn/exercises`, en orden:

1. **`000` Welcome** — solo lectura y sin test: qué es NumPy, para qué se usa y enlaces a la documentación oficial y a un vídeo.
2. **`001` Create Entry File** — crear `app.py` en la raíz del proyecto. El único test comprueba que el fichero existe.
3. **`002` Import NumPy** — importar la librería con el alias `np`.
4. **`003` NumPy Version** — imprimir la versión instalada usando `np.__version__`.
5. **`004` Your First Vector** — imprimir un vector nulo de tamaño 10 creado con `np.zeros()`.
6. **`005` Array Memory Size** — imprimir `80`, la memoria que ocupa ese vector, a partir de `.itemsize` y `.size`.
7. **`006` NumPy Documentation** — imprimir la documentación de `np.add()` con `np.info()`.
8. **`007` Change Vector Values** — un vector nulo de tamaño 10 cuyo quinto elemento (índice `4`) vale `1`.
9. **`008` Vector Ranging Values** — un vector con todos los enteros del 10 al 49, creado con `np.arange()`.
10. **`009` Reverse Vector** — los enteros del 0 al 9 impresos al revés usando `array[::-1]`.
11. **`010` Matrix with Ranging Values** — los números del 0 al 8 convertidos en una matriz de 3×3 con `reshape()`.
12. **`011` Find Indexes of Non Zero Elements** — `np.nonzero()` sobre `[1,2,0,0,4,0]`, imprimiendo `(array([0, 1, 4]),)`.
13. **`012` Identity Matrix** — una matriz identidad de 3×3 creada con `np.eye()`.
14. **`013` Random Values Array** — una variable llamada `arr` con un array de 3 valores aleatorios.
15. **`014` Minimum and Maximum** — `arr` con 10 valores aleatorios, imprimiendo el mayor con `.max()`.
16. **`015` Mean Value** — `arr` con 10 valores aleatorios, imprimiendo su media con `.mean()`.
17. **`016` Array Border** — una matriz de 5×5 de unos con el centro puesto a cero mediante `matrix[1:-1, 1:-1]`.
18. **`017` Add Border to Array** — una matriz de 3×3 de unos rodeada por un borde de ceros con `np.pad()`.
19. **`018` Result of Expressions** — imprimir los seis resultados de las comparaciones con `nan` e `inf`: `nan`, `False`, `False`, `nan`, `True`, `False`.
20. **`019` Diagonal** — imprimir `[0 4 8]`, la diagonal de una matriz de 3×3, usando `np.diag()`.
21. **`020` Checkerboard Pattern** — una matriz de 8×8 rellena con un patrón de tablero de ajedrez de ceros y unos.

## 🎓 ¿Qué necesitas antes de empezar?

El tutorial está catalogado como **intermedio**, y el motivo es Python, no las matemáticas: aquí no hay nada más allá de la aritmética, las «matrices» son rejillas de números. Lo que sí necesitas es:

- **Python básico bien asentado** — variables, `print()`, listas y sobre todo la notación de rebanadas. La mitad de los ejercicios se resuelven con un slice del tipo `[::-1]`, `[1:-1, 1:-1]` o `[1::2, ::2]`.
- **Cero experiencia previa con NumPy.** El ejercicio `002` empieza por el `import numpy as np` y cada función llega con una pista y un enlace a su página en numpy.org.
- **Un entorno de Python 3 con NumPy y pytest.** Si abres el repositorio en Codespaces, el dev container instala por ti Python 3.10, `numpy==1.24.2` y `pytest==6.2.5`. En local los instalas tú.
- **Node.js 22**, únicamente si vas a correr los ejercicios en tu propia máquina, porque LearnPack es una herramienta de línea de comandos de Node.

## ✅ ¿Cómo funciona la corrección automática?

20 de las 21 carpetas traen un fichero `test.py` y entre todas suman 53 comprobaciones escritas con `@pytest.mark.it("...")`, así que cada fallo te dice en una frase qué se esperaba. El modo de corrección es `incremental`: los ejercicios se apoyan unos en otros y todos leen el mismo `app.py` que vive en la raíz del repositorio, no dentro de la carpeta del ejercicio.

Hay cuatro tipos de comprobación, y saber cuál tienes delante te ahorra mucho tiempo:

- **Comprobaciones de salida:** capturan lo que imprime tu programa con el fixture `capsys` de pytest. Hasta el ejercicio `012` solo exigen que el texto esperado aparezca en algún punto de tu salida, pero del `015` al `020` comparan la consola entera con `==`, carácter a carácter.
- **Comprobaciones del código fuente:** abren `app.py` y buscan la función que se te pidió usar: `zeros(`, `ones(`, `arange(`, `reshape(`, `eye(`, `pad(`, `diag(`, `nonzero`, `array`, `random(`, `max(`, `mean(`, `info(`, `itemsize`, `size`.
- **Comprobaciones anti-copia:** lanzan una expresión regular que falla si el resultado esperado está escrito tal cual en tu fichero. Ocho ejercicios llevan una.
- **Comprobaciones de importación:** en `013`, `014` y `015` ejecutan `from app import arr`, así que `arr` tiene que existir como variable en el nivel superior del módulo.

Lanza los tests desde la interfaz de LearnPack después de editar `app.py` y lee la descripción de la comprobación que falla antes de tocar nada.

## 💡 ¿Qué errores debes evitar?

Estas son las trampas que hacen fallar la corrección aunque tu NumPy sea correcto:

- **Dejar en `app.py` el código del ejercicio anterior.** Todo se escribe en ese mismo fichero y, a partir del `015`, el test compara la salida completa de la consola con `==`. Un `print()` olvidado del ejercicio `012` tumba una respuesta perfectamente válida. Borra o comenta lo que ya no necesites.
- **Confundir imprimir con asignar.** Los ejercicios `013` y `014` se corrigen importando la variable (`from app import arr`), así que calcular el valor dentro de un `print()` sin guardarlo en `arr` falla. El `015` quiere las dos cosas: la variable *y* la media impresa.
- **Escribir el resultado esperado a mano.** Los ejercicios `004`, `005`, `007`, `008`, `009`, `010`, `011` y `012` llevan una regex que rechaza la respuesta literal en tu código: `print("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]")` o `print(80)` no van a pasar nunca.
- **Contar desde uno.** El «quinto elemento» del ejercicio `007` es `arr[4]`. La salida esperada es `[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]`.
- **Invertir el vector sin la rebanada.** El ejercicio `009` exige el literal `::-1` en tu código. `np.flip()` imprime exactamente el vector correcto y aun así falla la comprobación.
- **Cambiar la forma del import.** La regex busca `import numpy as np`. Ni `import numpy` ni `from numpy import *` superan los ejercicios `002` y `003`.
- **Equivocarte de tamaño en el `016` y el `017`.** Las instrucciones del `016` no dicen de qué tamaño es la matriz, pero el bloque `💻 Expected Output` que viene justo debajo en el mismo enunciado sí: 5×5, con unos en el borde y un bloque de 3×3 de ceros en el centro. En el `017` partes de una de 3×3 de unos y `np.pad()` la convierte en una de 5×5, también impresa ahí. Lee ese bloque antes de escribir nada.
- **Desenvolver el resultado de `np.nonzero()` en el `011`.** La salida esperada es la tupla `(array([0, 1, 4]),)`. Imprimir `np.nonzero(arr)[0]` da `[0 1 4]` y falla.

## ❓ Preguntas frecuentes

### ¿Hace falta saber Python antes de aprender NumPy?

Sí, lo básico. El tutorial está clasificado como intermedio porque da por sabidas las variables, las listas, el `print()` y, sobre todo, las rebanadas del tipo `lista[2:5]` o `lista[::-1]`. De NumPy no da nada por sabido: el segundo ejercicio es precisamente el `import`.

### ¿Todos los ejercicios usan el mismo fichero?

Sí. Creas `app.py` en el ejercicio `001`, en la raíz del proyecto, y todos los ejercicios siguientes se resuelven editando ese mismo fichero. Eso es lo que significa aquí la corrección `incremental`, y también por eso conviene limpiar la respuesta anterior antes de volver a lanzar los tests.

### ¿Por qué falla mi ejercicio si la salida se ve bien?

Casi siempre por una de tres razones: te queda un `print()` suelto de un ejercicio anterior y el test compara la salida completa con `==`; escribiste el resultado esperado como texto literal y lo cazó la regex anti-copia; o lo resolviste con una función distinta a la que la comprobación busca en el código, como `np.flip()` en lugar de `[::-1]`.

### ¿Qué funciones de NumPy cubre el tutorial?

Creación de arrays con `array()`, `zeros()`, `ones()`, `eye()`, `arange()` y `random.random()`; forma y estructura con `reshape()`, `pad()`, `diag()` y `nonzero()`; estadística con `max()` y `mean()`; los atributos `itemsize` y `size`; introspección con `__version__`, `show_config()` e `info()`; y la notación de índices y rebanadas aplicada a vectores y matrices.

### ¿Tengo que instalar NumPy y pytest por mi cuenta?

Solo si trabajas en tu propia máquina. El repositorio incluye un dev container que, al crear el Codespace, instala Python 3.10, Node.js 22, `numpy==1.24.2`, `pandas`, `pytest==6.2.5` y LearnPack con su plugin de Python. En local son dos comandos: un `pip3 install` con los paquetes de Python y un `npm i` para LearnPack y su plugin de Python.

### ¿Vienen las soluciones y cuesta algo el tutorial?

19 de las 21 carpetas incluyen un fichero `solution.hide.py` con la solución de referencia; LearnPack lo mantiene apartado mientras trabajas, pero está en el repositorio por si te atascas de verdad. Abrir y seguir el tutorial no cuesta nada y el código que escribas en `app.py` es tuyo. Eso sí, el repositorio no incluye fichero `LICENSE`, así que el material didáctico no está publicado bajo una licencia de código abierto.

<!-- hide -->

## 📚 Tutoriales relacionados

Si vas camino del análisis de datos, estos tutoriales interactivos encajan bien alrededor de este:

- [Aprende Python Interactivamente (Principiante)](https://4geeks.com/es/interactive-exercise/python-beginner-exercises-es) — el paso anterior si las variables y las listas todavía se te resisten.
- [Aprende listas y bucles de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-loops-lists-exercises-es) — práctica de rebanadas, que es justo donde más se apoya este tutorial.
- [Aprende las funciones de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-function-exercises-es) — para dejar de escribir todo suelto en un fichero.
- [Domina Python Practicando (interactivo)](https://4geeks.com/es/interactive-exercise/master-python-exercises-es) — más práctica general cuando termines.

## 🚀 Cómo empezar

La vía rápida no necesita ninguna instalación local: abre el repositorio en [GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/numpy-tutorial-exercises) (recomendado) o en [Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/numpy-tutorial-exercises.git).

> 💡 Cuando se abra VSCode, los ejercicios de LearnPack deberían arrancar solos. Si no lo hacen, escribe `learnpack start` en la terminal.

## 💻 Instalación local

1. Instala [LearnPack](https://learnpack.co) y su plugin de Python. Necesitas Node.js 22 y Python 3.10 o superior:

    ```bash
    npm i @learnpack/learnpack@5.0.348 -g && learnpack plugins:install @learnpack/python@1.0.3
    ```

2. Clona el repositorio y entra en la carpeta:

    ```bash
    git clone https://github.com/4GeeksAcademy/numpy-tutorial-exercises.git
    cd numpy-tutorial-exercises
    ```

3. Instala las dependencias de Python y arranca el tutorial al mismo nivel que `learn.json`:

    ```bash
    pip3 install pytest==6.2.5 mock pytest-testdox toml numpy==1.24.2 pandas
    learnpack start
    ```

## 📚 Cómo están organizados los ejercicios

Cada ejercicio vive en su propia carpeta dentro de [`.learn/exercises`](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/tree/HEAD/.learn/exercises) y contiene solo texto y tests:

- **`README.es.md`** — el enunciado en español, con las instrucciones, las pistas y, en varios ejercicios, la salida exacta que se espera.
- **`README.md`** — el mismo enunciado en inglés.
- **`test.py`** — el script de pytest que corrige el ejercicio. Leerlo es la forma más rápida de entender qué se espera exactamente de ti.
- **`solution.hide.py`** — la solución de referencia, presente en 19 de las 21 carpetas (todas menos `000-welcome` y `001-create-entry-file`).

El fichero que de verdad editas, `app.py`, no está en esas carpetas: vive en la raíz del repositorio, junto a [`learn.json`](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/blob/HEAD/learn.json), y lo comparten todos los ejercicios. La carpeta `000-welcome` es la excepción a todo: es solo de lectura, sin test y sin solución.

## 🤝 Colaboradores

Gracias a estas personas, que construyeron, probaron y tradujeron los ejercicios: [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr), [Tomás Gonzáles (tommygonzaleza)](https://github.com/tommygonzaleza), [Paolo Lucano (plucodev)](https://github.com/plucodev) y [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo).

Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). Todas las contribuciones son bienvenidas: si encuentras un fallo o una errata, abre una issue o una pull request en el [repositorio](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/issues).

Este y otros ejercicios son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp), realizado por Alejandro Sánchez y muchos otros colaboradores. Conoce más sobre nuestros [cursos de programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack), o nuestro [Bootcamp de Data Science y Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning). Puedes ver a todas las personas que han aportado código en el [gráfico de contribuidores](https://github.com/4GeeksAcademy/numpy-tutorial-exercises/graphs/contributors).

<!-- endhide -->

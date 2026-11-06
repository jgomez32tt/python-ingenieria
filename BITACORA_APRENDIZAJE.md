# Bitácora de aprendizaje — Python, Codex y GitHub

**Alumno:** Ingeniero mecatrónico en transición hacia soluciones digitales e inteligencia artificial  
**Proyecto:** `python-ingenieria`  
**Repositorio:** https://github.com/jgomez32tt/python-ingenieria  
**Última actualización:** 2026-11-05 (Clase 2, paso 5.3 completado)  
**Modalidad:** 3–5 horas semanales; sesiones preferidas de 7:00 a 9:00 p. m. (Colombia)

> **Uso:** Este documento es una guía de consulta y una bitácora. Actualizar al finalizar una clase solo cuando el alumno lo solicite: presentar primero los cambios y esperar su aprobación antes de guardarlos. Conservar la información anterior. No hacer commits ni publicaciones en GitHub sin autorización explícita. No agregar contraseñas, tokens, datos confidenciales ni información interna de la empresa.

## 1. Resumen del progreso

| Clase / etapa | Tema | Estado |
|---|---|---|
| Clase 1 — pasos 1–3 | Python, variables, tipos de datos, operaciones y archivo `.py` | Completado |
| Clase 1 — pasos 4.2–4.6 | Codex, `input()`, `float()`, `if/else`, `try/except` y pruebas manuales | Completado |
| Clase 1 — pasos 4.7–4.10 | Repositorio Git, Homebrew, GitHub CLI, autenticación y primer `push` | Completado |
| Clase 2 — paso 4.11 | `git status`, `git log`, `git remote -v` | Completado |
| Clase 2 — pasos 5–5.2 | Funciones `def`, parámetros, `return`, refactorización y cinco pruebas de regresión | Completado |
| Clase 2 — paso 5.3 | Pruebas automatizadas con `unittest` y `if __name__ == '__main__'` | Completado |
| Próximos temas | Ampliar pruebas, pruebas unitarias e integración, `assertRaises()` y mejores prácticas | Pendiente |

**Resultados recientes:** Cinco pruebas manuales aprobadas; segundo commit y `push` reportados exitosamente (2026-11-05).  
**Primer commit conocido:** `f98e79a` — *Crear calculadora de combustible con validaciones*.  
**Segundo commit:** registrado anteriormente como creado y publicado; identificador pendiente de confirmar con `git log --oneline -3` cuando se autorice la consulta.

**Alcance de la revisión inicial del 2026-11-05 (anterior al paso 5.3):** se comprobó la refactorización leyendo el archivo. Los resultados de pruebas y los commits anteriores se conservan como antecedentes registrados; durante aquella revisión no se ejecutaron esas pruebas ni se verificaron el historial o GitHub. Las comprobaciones posteriores del paso 5.3 se documentan al final.

## 2. Ruta habitual del proyecto en el Mac

```bash
cd ~/Documents/python-ingenieria
pwd
ls -la
```

- `cd`: cambia de carpeta.
- `pwd`: muestra la carpeta actual.
- `ls -la`: muestra archivos y carpetas ocultas, incluida `.git`.
- **Si aparece `fatal: not a git repository`**, primero verifica `pwd` y entra a la carpeta correcta. No uses `git init` otra vez sobre el proyecto existente.

## 3. Chuleta de Git y GitHub

**Git** controla versiones del proyecto mediante un historial de commits. **GitHub** aloja el repositorio remoto y permite compartirlo y colaborar. Un commit local no se publica hasta enviarlo con `push`.

| Objetivo | Comando | Explicación |
|---|---|---|
| Ver estado | `git status` | Archivos modificados, pendientes o limpios |
| Ver cambios | `git diff -- calculadora_combustible.py` | Diferencias no preparadas del archivo |
| Ver historial | `git log --oneline -3` | Últimos 3 commits |
| Ver conexión | `git remote -v` | URLs de `origin` para `fetch` y `push` |
| Preparar archivo | `git add calculadora_combustible.py` | Agrega cambios al *staging area* |
| Preparar bitácora | `git add BITACORA_APRENDIZAJE.md` | Agrega cambios de la bitácora |
| Crear commit | `git commit -m "Describir cambio"` | Registra una versión local |
| Publicar | `git push origin main` | Envía commits a GitHub |
| Ver autenticación | `gh auth status` | Comprueba la sesión de GitHub CLI; no revela tokens |

**Flujo habitual de referencia (no ejecutarlo automáticamente; commit y publicación requieren autorización explícita):**

```bash
cd ~/Documents/python-ingenieria
git status
git diff
git add calculadora_combustible.py BITACORA_APRENDIZAJE.md
git commit -m "Describir lo aprendido y los cambios"
git push origin main
```

> Realiza `git add` solo de archivos que realmente hayas cambiado; revisa `git diff` y no subas claves, datos personales, archivos `.env` ni datos operativos confidenciales.

## 4. Conceptos de Python aprendidos

| Concepto | Ejemplo | Para qué sirve |
|---|---|---|
| Variable | `galones = 1250` | Asigna un valor a un nombre |
| Entero | `type(1250)` → `int` | Representa números enteros |
| Decimal | `type(50.0)` → `float` | Representa números decimales |
| Mostrar | `print(consumo)` | Muestra información |
| Entrada | `input("Galones: ")` | Recibe un texto del usuario |
| Conversión | `float(input("Galones: "))` | Convierte texto a decimal |
| Condición | `if horas > 0:` | Decide si ejecutar un bloque |
| Alternativa | `else:` | Se ejecuta si la condición es falsa |
| Dos condiciones | `galones >= 0 and horas > 0` | Exige ambas condiciones |
| Excepción | `try: ... except ValueError:` | Controla errores de conversión |
| Función | `def calcular_consumo(galones, horas):` | Define cálculo reutilizable |
| Parámetros | `galones` y `horas` en la definición | Nombres que reciben los valores para el cálculo |
| Argumentos | `calcular_consumo(1250, 25)` | Valores que se proporcionan al llamar la función |
| Retorno | `return galones / horas` | Entrega valor al llamador, no lo imprime |
| Comentario | `# Una explicación` | Documenta; Python no lo ejecuta |

**Importante:** `if/else` son condicionales; `try/except` maneja excepciones. No son ciclos. `for` y `while` sí son ciclos.

### Estructura de referencia de la calculadora — versión anterior al paso 5.3

```python
def calcular_consumo(galones, horas):
    return galones / horas

print("=== CALCULADORA DE COMBUSTIBLE ===")

try:
    galones = float(input("Ingrese los galones de combustible: "))
    horas = float(input("Ingrese las horas de operación: "))

    if galones >= 0 and horas > 0:
        consumo = calcular_consumo(galones, horas)
        print("Galones suministrados:", galones)
        print("Horas de operacion:", horas)
        print("Consumo promedio:", consumo, "gal/h")
    else:
        print("Los galones deben ser mayores o iguales a cero y las horas mayores que cero.")
except ValueError:
    print("Entrada inválida. Ingrese números y use punto para los decimales.")
```

**Atención:** referencia educativa; el archivo `calculadora_combustible.py` del proyecto es la versión fuente real. La razón `galones suministrados / horas` es un indicador simplificado, no necesariamente el consumo real. Para un tanque cerrado sin otras entradas/salidas: `consumo = inventario inicial + suministro − inventario final`.

## 5. Pruebas manuales realizadas

Los estados siguientes proceden del registro anterior, confirmado por el alumno. No se repitieron los cinco escenarios durante la revisión inicial; las comprobaciones posteriores del paso 5.3 se detallan al final.

| Galones | Horas | Resultado esperado | Última ejecución |
|---:|---:|---|---|
| 1250 | 25 | 50.0 gal/h | Aprobada |
| 2400 | 32 | 75.0 gal/h | Aprobada |
| 1000 | 0 | Error controlado (horas inválidas) | Aprobada |
| 1000 | -5 | Error controlado (horas inválidas) | Aprobada |
| ABC | — | Error de conversión controlado | Aprobada |

**Casos adicionales pendientes (aún no registrados como ejecutados):** galones negativos, cero galones con horas positivas y texto inválido en las horas.

Ejecución:

```bash
cd ~/Documents/python-ingenieria
python3 calculadora_combustible.py
```

## 6. Método de trabajo con Codex

1. Describir **objetivo, alcance y restricciones**.
2. Pedir primero una **propuesta sin modificar archivos**.
3. Leerla y explicar los cambios con tus palabras.
4. Autorizar solo el cambio definido y revisar el diff.
5. Ejecutar pruebas con datos válidos e inválidos.
6. Crear commit y publicar solo con autorización explícita del alumno y tras verificar los resultados.
7. Cuando el alumno solicite el cierre, proponer la actualización con fecha, número de clase, conceptos, comandos y su función, errores y soluciones, ejercicios, pruebas, pendientes y próximo paso. Guardarla solo después de su aprobación.

**Prompt de consulta:**

> Lee `BITACORA_APRENDIZAJE.md` y `calculadora_combustible.py`. Explica el estado actual y el siguiente ejercicio al nivel de principiante. No modifiques archivos hasta que lo autorice.

**Prompt para actualizar al terminar una clase:**

> Actualiza `BITACORA_APRENDIZAJE.md` con fecha, temas trabajados, comandos nuevos, ejemplos, resultados de pruebas, errores resueltos, commit realizado, dudas y próximo paso. No borres aprendizajes anteriores, no inventes resultados, evita datos sensibles y enséñame el diff antes de guardar los cambios. No hagas commit ni push sin mi autorización.

## 7. Dudas y preguntas para repasar

- ¿Qué diferencia existe entre `git add`, `git commit` y `git push`?
- ¿Cuál es la diferencia entre `print()` y `return`?
- ¿Por qué el bloque dentro de `def`, `if` o `try` debe llevar indentación?
- ¿Por qué validamos antes de llamar a `calcular_consumo()`?
- ¿Cómo se prueba un programa automáticamente sin ingresar datos cada vez?

## 8. Plan inicial de pruebas automatizadas — realizado en el paso 5.3

**Tema:** Pruebas automatizadas con Python estándar, sin instalar librerías adicionales.

- Entender por qué los cinco escenarios manuales pueden convertirse en pruebas repetibles.
- Separar la ejecución interactiva del código importable usando `if __name__ == "__main__":`.
- Crear pruebas con `unittest` para la función de cálculo.
- Revisar los cambios de Codex y ejecutar pruebas; crear un commit o publicar únicamente con autorización explícita después de confirmar resultados.

**Último punto completado:** Clase 2, paso 5.3 — primera prueba automatizada aprobada.  
**Próximos temas:** ampliar las pruebas, diferenciar pruebas unitarias e integración, aprender `assertRaises()` e incorporar mejores prácticas gradualmente.

---

## 9. Plantilla de cierre de clase

Copiar y completar al finalizar una sesión:

```markdown
### Clase [número] — [AAAA-MM-DD]
- Objetivo:
- Conceptos aprendidos:
- Comandos nuevos:
- Archivos modificados:
- Pruebas y resultados:
- Errores encontrados y cómo se resolvieron:
- Commit (identificador y mensaje, si se creó):
- Dudas pendientes:
- Próximo paso:
```


## 10. Registro por clase

Estos resúmenes recuperan la información existente sin inventar fechas ni resultados faltantes.

### Clase 1 — fecha pendiente de confirmar

- Objetivo: crear la calculadora de combustible y conocer el flujo de trabajo con Codex, Git y GitHub.
- Conceptos aprendidos: variables, tipos `int` y `float`, operaciones, `print()`, `input()`, conversión con `float()`, condiciones `if/else` y manejo de `ValueError` con `try/except`.
- Comandos de referencia: `cd` cambia de carpeta; `pwd` muestra la ubicación; `ls -la` lista archivos, incluidos los ocultos; `python3 calculadora_combustible.py` ejecuta el programa; `git add` prepara cambios; `git commit` registra una versión local; `git push` publica commits; `gh auth status` consulta la autenticación. La clase exacta de introducción de cada comando no consta en el registro anterior.
- Ejercicio y archivo: creación de `calculadora_combustible.py` con entradas y validaciones.
- Pruebas: el resumen anterior registra pruebas manuales; no detalla cuáles se ejecutaron específicamente en esta clase.
- Errores y soluciones: no hay incidentes confirmados por clase. La nota sobre `fatal: not a git repository` es una guía preventiva, no evidencia de que haya ocurrido.
- Git/GitHub: primer commit registrado como `f98e79a`; autenticación y primer `push` registrados como completados, sin nueva verificación en esta revisión.
- Siguiente paso histórico: revisar el estado, historial y remoto; introducir funciones.

### Clase 2 — 2026-11-05 (registro inicial, hasta el paso 5.2)

- Objetivo: revisar conceptos de Git y extraer el cálculo a una función.
- Conceptos aprendidos: `def`, parámetros, argumentos, `return` y refactorización conservando el comportamiento. `return` devuelve un valor; `print()` lo muestra.
- Comandos documentados en esta clase: `git status` consulta el estado; `git log --oneline -3` muestra los últimos tres commits; `git remote -v` muestra las direcciones de los remotos. No se ejecutaron durante esta revisión.
- Ejercicio: definir `calcular_consumo(galones, horas)` antes del programa principal con `return galones / horas`, y sustituir la división por `consumo = calcular_consumo(galones, horas)`.
- Archivo de código modificado: `calculadora_combustible.py`. Se conservaron `float(input())`, `if/else`, `try/except ValueError` y los mensajes existentes. La refactorización fue autorizada y comprobada por lectura en esta conversación.
- Pruebas: cinco escenarios registrados como aprobados en la sección 5; no se repitieron durante la revisión inicial.
- Errores y soluciones: no se documentaron errores de ejecución nuevos durante la refactorización. La revisión de la bitácora aclaró parámetros y argumentos, alineó el ejemplo con el código y distinguió antecedentes de resultados verificados.
- Git/GitHub: segundo commit y publicación registrados previamente; identificador pendiente de confirmar. No se hicieron commits ni publicaciones durante esta revisión.
- Pendientes: confirmar datos históricos cuando corresponda, practicar los casos adicionales de la sección 5 y resolver las preguntas de la sección 7.
- Próximo paso: continuar la Clase 2, paso 5.3, con pruebas automatizadas mediante `unittest` y separación del programa interactivo con `if __name__ == "__main__":`. En el momento de ese registro aún no se habían implementado; su realización se documenta en la ampliación siguiente.


### Ampliación de la Clase 2 — 2026-11-05

**Conceptos aprendidos**

- Git: `status`, `log --oneline -3`, `remote -v`, `add`, `commit` y `push`.
- Funciones: definición con `def`, parámetros, argumentos, `return` y reutilización.
- Refactorización: extraer un cálculo a una función sin cambiar el comportamiento esperado.
- Pruebas automatizadas con `unittest`, incluido en Python.
- Importación de funciones mediante `from ... import ...`.
- `if __name__ == "__main__":`: permite ejecutar el programa directamente e importarlo sin solicitar datos.
- `class`: agrupa las pruebas y permite heredar las herramientas de `unittest.TestCase`.
- `self`: representa la instancia que ejecuta la prueba.
- `assertEqual()`: comprueba que dos valores sean iguales.

**Ejercicios completados y resultados**

- Refactorización de `calculadora_combustible.py` utilizando `calcular_consumo(galones, horas)`.
- Cinco pruebas manuales aprobadas, según el registro anterior y la confirmación del alumno.
- Incorporación del bloque `if __name__ == "__main__":`, conservando las entradas, validaciones y mensajes.
- Creación de `test_calculadora.py`.
- Primera prueba automatizada aprobada: `calcular_consumo(2400, 32) == 75.0`. Resultado: **1 prueba ejecutada, `OK`**, con Python **3.9.6**.
- Importación de la calculadora comprobada sin mensajes ni solicitud de datos.
- Funcionamiento interactivo comprobado con `2400 / 32`, horas en cero y entrada no numérica. Estas tres comprobaciones complementan el registro previo de cinco pruebas.

**Errores y soluciones**

No se encontraron fallos en las comprobaciones realizadas. Para permitir la importación sin solicitar datos, se colocó el programa interactivo dentro de `if __name__ == "__main__":`.

**Consulta rápida de comandos**

| Comando | Función |
|---|---|
| `git status` | Consulta el estado de los archivos. |
| `git log --oneline -3` | Muestra los últimos tres commits de forma resumida. |
| `git remote -v` | Muestra los nombres y las direcciones de los repositorios remotos. |
| `git add archivo.py` | Prepara los cambios de un archivo para el próximo commit. |
| `git commit -m "Mensaje"` | Registra los cambios preparados en una versión local. |
| `git push origin main` | Envía los commits de la rama `main` al remoto `origin`. |
| `python3 calculadora_combustible.py` | Ejecuta la calculadora interactiva. |
| `python3 -m unittest -v test_calculadora` | Ejecuta las pruebas del módulo con resultados detallados. |
| `python3 -B -m unittest -v test_calculadora` | Ejecuta las mismas pruebas sin generar archivos de caché `.pyc`; fue el comando utilizado en esta sesión. |

Los comandos de Git se incluyen como consulta. No se ejecutaron durante la implementación de las pruebas.

**Próximos temas**

- Ampliar las pruebas automatizadas.
- Diferenciar pruebas unitarias de pruebas de integración.
- Aprender `assertRaises()` para verificar excepciones.
- Incorporar gradualmente mejores prácticas de programación.

**Commits y publicaciones**

No se realizaron nuevos commits ni publicaciones durante esta implementación.

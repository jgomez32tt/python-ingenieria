# Bitácora de aprendizaje — Python, Codex y GitHub

**Alumno:** Ingeniero mecatrónico en transición hacia soluciones digitales e inteligencia artificial  
**Proyecto:** `python-ingenieria`  
**Repositorio:** https://github.com/jgomez32tt/python-ingenieria  
**Última actualización:** 2026-11-05 (Clase 2, paso 5.2)  
**Modalidad:** 3–5 horas semanales; sesiones preferidas de 7:00 a 9:00 p. m. (Colombia)

> **Uso:** Este documento es una guía de consulta y una bitácora. Actualizar después de cada clase. No agregar contraseñas, tokens, datos confidenciales ni información interna de la empresa.

## 1. Resumen del progreso

| Clase / etapa | Tema | Estado |
|---|---|---|
| Clase 1 — pasos 1–3 | Python, variables, tipos de datos, operaciones y archivo `.py` | Completado |
| Clase 1 — pasos 4.2–4.6 | Codex, `input()`, `float()`, `if/else`, `try/except` y pruebas manuales | Completado |
| Clase 1 — pasos 4.7–4.10 | Repositorio Git, Homebrew, GitHub CLI, autenticación y primer `push` | Completado |
| Clase 2 — paso 4.11 | `git status`, `git log`, `git remote -v` | Completado |
| Clase 2 — pasos 5–5.2 | Funciones `def`, parámetros, `return`, refactorización y cinco pruebas de regresión | Completado |
| Siguiente clase | Pruebas automatizadas con `unittest` y `if __name__ == '__main__'` | Pendiente |

**Resultados recientes:** Cinco pruebas manuales aprobadas; segundo commit y `push` reportados exitosamente (2026-11-05).  
**Primer commit conocido:** `f98e79a` — *Crear calculadora de combustible con validaciones*.  
**Segundo commit:** creado y publicado; consultar su identificador con `git log --oneline -3`.

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

**Flujo habitual:**

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
| Retorno | `return galones / horas` | Entrega valor al llamador, no lo imprime |
| Comentario | `# Una explicación` | Documenta; Python no lo ejecuta |

**Importante:** `if/else` son condicionales; `try/except` maneja excepciones. No son ciclos. `for` y `while` sí son ciclos.

### Estructura de referencia de la calculadora

```python
def calcular_consumo(galones, horas):
    consumo = galones / horas
    return consumo

print("=== CALCULADORA DE COMBUSTIBLE ===")

try:
    galones = float(input("Ingrese los galones: "))
    horas = float(input("Ingrese las horas: "))

    if galones >= 0 and horas > 0:
        consumo = calcular_consumo(galones, horas)
        print("Consumo promedio:", consumo, "gal/h")
    else:
        print("Error: valores fuera de rango")
except ValueError:
    print("Error: ingrese solamente numeros")
```

**Atención:** referencia educativa; el archivo `calculadora_combustible.py` del proyecto es la versión fuente real. La razón `galones suministrados / horas` es un indicador simplificado, no necesariamente el consumo real. Para un tanque cerrado sin otras entradas/salidas: `consumo = inventario inicial + suministro − inventario final`.

## 5. Pruebas manuales realizadas

| Galones | Horas | Resultado esperado | Última ejecución |
|---:|---:|---|---|
| 1250 | 25 | 50.0 gal/h | Aprobada |
| 2400 | 32 | 75.0 gal/h | Aprobada |
| 1000 | 0 | Error controlado (horas inválidas) | Aprobada |
| 1000 | -5 | Error controlado (horas inválidas) | Aprobada |
| ABC | — | Error de conversión controlado | Aprobada |

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
6. Crear commit y publicar tras verificar los resultados.
7. Actualizar esta bitácora con conceptos, comandos, errores y próximos pasos.

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

## 8. Próxima sesión (plan)

**Tema:** Pruebas automatizadas con Python estándar, sin instalar librerías adicionales.

- Entender por qué los cinco escenarios manuales pueden convertirse en pruebas repetibles.
- Separar la ejecución interactiva del código importable usando `if __name__ == "__main__":`.
- Crear pruebas con `unittest` para la función de cálculo.
- Revisar los cambios de Codex, ejecutar pruebas y crear un commit después de confirmar resultados.

**Último punto completado:** Clase 2, paso 5.2.  
**Siguiente paso:** Clase 2, paso 5.3 — introducción a pruebas automatizadas.

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

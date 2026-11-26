# 1 VS 1

Juego de combate por turnos para dos jugadores, hecho en Python y ejecutado en la consola.

Proyecto presentado en la **Feria de Ingeniería** (27/11/2026) por estudiantes de **Ingeniería de Sistemas**. Además del juego final, el repositorio cuenta cómo evolucionó: de las reglas escritas en palabras, al pseudocódigo y, por último, al código.

## Reglas

- Cada jugador (A y B) empieza con **100 HP** y **3 pociones**.
- Los jugadores se turnan. En su turno, cada uno elige una acción:

| Opción | Acción | Efecto |
|--------|--------|--------|
| `1` | Atacar | Quita **15 HP** al rival |
| `2` | Curar | Recupera **25 HP** (máximo 100) y gasta **1 poción** |
| `3` | Rendirse | La victoria es para el rival |

- Gana quien deja al rival sin HP, o quien recibe la rendición del rival.

Así se ve el menú en la consola:

```
> Tu turno
[1] Atacar (-15 HP)
[2] Curar (+25 HP)
[3] Rendirse
```

## Cómo ejecutarlo

Requisitos: **Python 3** instalado.

```bash
git clone git@github.com:gianlucadmm/1v1.git
cd 1v1
python juego.py
```

## La historia del proyecto en 7 etapas

El juego se construyó por etapas, desde la idea hasta el código final:

1. [ETAPA 1]
2. [ETAPA 2]
3. [ETAPA 3]
4. [ETAPA 4]
5. [ETAPA 5]
6. [ETAPA 6]
7. [ETAPA 7]

## Un bug que nos enseñó algo

Creamos una lista vacía y le hicimos `append` a otras dos listas. Después, al ingresar datos e imprimir el resultado final, donde debían aparecer las acciones se mostraba la vida del jugador.

**Causa:** habíamos metido la misma lista dentro de dos listas distintas. En Python las listas se pasan por referencia, así que no se crearon dos copias: ambas apuntaban al mismo objeto, y un cambio hecho desde un lugar se veía en el otro.

**Solución:** crear una lista nueva e independiente para cada caso (por ejemplo, con `[]` en cada lugar, o con `.copy()` si se parte de una existente).

```python
# Problema: la misma lista queda dentro de dos listas
vacia = []
a = [vacia]
b = [vacia]
a[0].append("dato")
print(b[0])  # ['dato'], aunque solo se modificó a

# Solución: una lista independiente para cada una
a = [[]]
b = [[]]
a[0].append("dato")
print(b[0])  # []
```

## Autoría

- Carrera: Ingeniería de Sistemas
- GitHub: [gianlucadmm](https://github.com/gianlucadmm)

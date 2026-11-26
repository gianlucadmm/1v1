hp = []
pociones = []
nAtaque = []

VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
CYAN = "\033[96m"
NEGRITA = "\033[1m"
BLANCO = "\033[97m"
RESET = "\033[0m"

color_jugador = [ROJO, AZUL]
DANO_ATAQUE = 15
HP_CURA = 25
HP_MAX = 100
HP_MIN = 0
POC_INICIALES = 3

nRonda = 1
nJugador = 0 # Trabajamos con indices, Jugador 1 = 0, Jugador 2 = 1

for i in range(2): # Asignamos los valores iniciales
    hp.append(HP_MAX)
    pociones.append(POC_INICIALES)
    nAtaque.append(0)

acciones = []
hpRonda = []
nombres = []

nombre1 = input(f"{ROJO}Nombre del Jugador 1: {RESET}").strip()
if (nombre1 == ""):
    nombre1 = "Jugador 1"
nombres.append(nombre1)

nombre2 = input(f"{AZUL}Nombre del Jugador 2: {RESET}").strip()
if nombre2 == "":
    nombre2 = "Jugador 2"
nombres.append(nombre2)


print(f"{CYAN}{NEGRITA}")
print("╔═══════════════════════════════════════════════════════╗")
print("║                     ⚔️  1 VS 1  ⚔️                      ║")
print("║                 ¡EL COMBATE INICIARÁ!                 ║")
print("╚═══════════════════════════════════════════════════════╝")
print(f"{RESET}")
input(f"{AMARILLO}👉 Presiona [ENTER] para comenzar la batalla...{RESET}\n")
while ((hp[0] > HP_MIN) and (hp[1] > HP_MIN)):
    print("========================================")
    print(f"              ⚔️  Ronda {nRonda} ⚔️")
    print("========================================")
    for i in range(2):
        print(f"{color_jugador[i]}{NEGRITA}{nombres[i]}{RESET} -> ❤️  {hp[i]} HP | 🧪 {pociones[i]} pociones")
    print("---------------------------------------")

    nOponente = 1 - nJugador

    accion = 0
    while (((accion < 1) or (accion > 3)) or ((accion == 2) and (pociones[nJugador] == 0))):
        print(f"\n{color_jugador[nJugador]}{NEGRITA}{nombres[nJugador]}{RESET}, tu turno, elige una opción.")
        print(f"{CYAN}{NEGRITA}[1] ⚔️  Atacar  (-{DANO_ATAQUE} HP al rival){RESET}")
        print(f"{VERDE}{NEGRITA}[2] 🧪 Curar   (+{HP_CURA} HP){RESET}")
        print(f"{BLANCO}{NEGRITA}[3] 🏳️  Rendirse{RESET}")
        accion = input(f"\n{AMARILLO}🎮 Elige acción [1-3] > {RESET}").strip()

        if accion.isdigit(): # Verificamos si es digito
            accion = int(accion) # Si es un digito lo convertimos a entero

        else: # Si no es digito, lo hacemos 0 para que de error
            accion = 0

        if ((accion == 2) and (pociones[nJugador] == 0)):
            print(f"{nombres[nJugador]}, te quedaste sin pociones de curación, por favor, elige otra opción.")

        if ((accion < 1) or (accion > 3)):
            print("Error: opción no válida.")

    match accion:

        case 1:
            hp[nOponente] -= DANO_ATAQUE

            if (hp[nOponente] < HP_MIN):
                hp[nOponente] = HP_MIN

            print("\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n")
            print(f"{CYAN}{NEGRITA}     >>> ¡ATAQUE CRÍTICO! <<<{RESET}")
            print(f"{color_jugador[nJugador]}{NEGRITA}  {nombres[nJugador]}{RESET} inflige {CYAN}{NEGRITA}[{DANO_ATAQUE}]{RESET} de daño a {color_jugador[nOponente]}{NEGRITA}{nombres[nOponente]}{RESET}!")
            print("\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")


        case 2:
            hp[nJugador] += HP_CURA
            pociones[nJugador] -= 1

            if (hp[nJugador] > HP_MAX):
                hp[nJugador] = HP_MAX

            print("🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪\n")
            print(f"{VERDE}{NEGRITA}  >>> ¡RECUPERACIÓN EXITOSA! <<<{RESET}")
            print(f"{color_jugador[nJugador]}{NEGRITA}{nombres[nJugador]}{RESET} recupera {VERDE}{NEGRITA}+{HP_CURA} HP{RESET} (Pociones restantes: {pociones[nJugador]})")
            print("\n🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪")


        case 3:
            hp[nJugador] = HP_MIN

            print("\n🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ \n")
            print(f"{BLANCO}{NEGRITA}  >>> ¡RENDICIÓN! <<<{RESET}")
            print(f"  {color_jugador[nJugador]}{NEGRITA}{nombres[nJugador]}{RESET} ha izado la bandera blanca y abandona el combate.")
            print("\n🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️")

    input(f"\n{AMARILLO}👉 Presiona [ENTER] para continuar al siguiente turno...{RESET}")

    if (nJugador == 0):
        acciones.append([0,0])
        hpRonda.append([0,0])

    acciones[nRonda - 1][nJugador] = accion

    hpRonda[nRonda - 1][0] = hp[0]
    hpRonda[nRonda - 1][1] = hp[1]

    if ((hp[0] > HP_MIN) and (hp[1] > HP_MIN)):

        if (nJugador == 1):
            nRonda += 1

        nJugador = nOponente

print("\n👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑")
print(f"{AMARILLO}{NEGRITA}       🏆 ¡TENEMOS UN CAMPEÓN! 🏆{RESET}")
print("👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑👑")

if (accion == 3):
    print(f"\n  Ganador: {color_jugador[nOponente]}{NEGRITA}{nombres[nOponente]}{RESET} 🥇 (Por rendición del rival)")
    print(f"  Estado final: ❤️  {hp[nOponente]} HP | 🧪 {pociones[nOponente]} pociones")
else:
    print(f"\n  Ganador: {color_jugador[nJugador]}{NEGRITA}{nombres[nJugador]}{RESET} 🥇 (¡Victoria por K.O.!)")
    print(f"  Estado final: ❤️  {hp[nJugador]} HP | 🧪 {pociones[nJugador]} pociones")
print(f"\n  ⚔️  Rondas combatidas: {nRonda}")


input(f"\n{AMARILLO}👉 Presiona [ENTER] para desplegar los reportes finales...{RESET}")
print(f"\n{CYAN}{NEGRITA}╔═══════════════════════════════════════════════════════╗")
print("║             📊 REPORTES FINALES DEL JUEGO             ║")
print(f"╚═══════════════════════════════════════════════════════╝{RESET}")

print(f"\n{AMARILLO}{NEGRITA}📜 === BITÁCORA DETALLADA DEL COMBATE ==={RESET}")

for i in range(nRonda):
    print(f"\nRonda {i + 1}.")
    for j in range(2):

        if (acciones[i][j] == 0):
            if (hpRonda[i][j] != 0):
                print(f"{color_jugador[j]}{NEGRITA} - {nombres[j]}{RESET} no jugó | HP al finalizar la ronda: {hpRonda[i][j]} HP")
            else:
                print(f" - {nombres[j]} fue derrotado en combate (0 HP)")

        elif (acciones[i][j] == 3):
            print(f"{color_jugador[j]}{NEGRITA} - {nombres[j]}{RESET} eligió Acción [{acciones[i][j]}] | HP al finalizar la ronda: {hpRonda[i][j]} HP (Rendido)")

        else:
            print(f"{color_jugador[j]}{NEGRITA} - {nombres[j]}{RESET} eligió Acción [{acciones[i][j]}] | HP al finalizar la ronda: {hpRonda[i][j]} HP")

for i in range(nRonda):
    for j in range(2):
        if (acciones[i][j] == 1):
            nAtaque[j] += 1

print(f"\n{CYAN}{NEGRITA}╔═══════════════════════════════════════════════════════╗")
print("║              📈 ESTADÍSTICAS DEL COMBATE              ║")
print(f"╚═══════════════════════════════════════════════════════╝{RESET}")

for i in range(2):
    print(f"\n{color_jugador[i]}{NEGRITA}[{nombres[i]}]{RESET}")
    print(f"  ⚔️  Ataques realizados: {nAtaque[i]}")
    print(f"  🧪  Pociones consumidas: {POC_INICIALES - pociones[i]}")

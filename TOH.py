import shutil
import msvcrt
import time


class TOH:
    def __render():
        ...

    def Play(disks: int = 8):

        moves = 0

        towerL = [disks - x for x in range(disks)]
        target = [disks - x for x in range(disks)]
        towerM = []
        towerR = []
        towers = [towerL, towerM, towerR]

        selector = [0, 0]   # Let's say selector[0] = pos (0: L, 1: M, 2: R) and selector[1] = selected disk (0: none)

        # -------- RENDERING
        HEIGHT = shutil.get_terminal_size()[1]
        WIDTH = shutil.get_terminal_size()[0]
        for i in range(HEIGHT):
            print("\033[2K\033[F", end="")

        #print("\033[2J")
        print(f"TOWER OF HANOI: {disks} RINGS, {moves} MOVES MADE {' ' * (WIDTH-40-16 - 20)} PRESS 'Q' TO EXIT")    # 20 is extra, 40: start, 16: end
        #print(f"{(selector[0] * WIDTH // 3)*' '}V", end="")
        print(f"{(selector[0] * WIDTH // 3)*' '}", end="")
        print("V", end="")
        if HEIGHT > disks + 2:
            for i in range(HEIGHT - disks - 3):
                print()
        for i in range(disks):
            #print(f"{towers[0][disks - i - 1] if len(towers[0]) > disks - i - 1 else ' '}".center(WIDTH // 3), end="")
            print(f"{towers[0][disks - i - 1] if len(towers[0]) > disks - i - 1 else ' '}", end="")
            print(WIDTH // 3*' ', end="")
            #print(f"{towers[1][disks - i - 1] if len(towers[1]) > disks - i - 1 else ' '}".center(WIDTH // 3), end="")
            print(f"{towers[1][disks - i - 1] if len(towers[1]) > disks - i - 1 else ' '}", end="")
            print(WIDTH // 3*' ', end="")
            #print(f"{towers[2][disks - i - 1] if len(towers[2]) > disks - i - 1 else ' '}".center(WIDTH // 3))
            print(f"{towers[2][disks - i - 1] if len(towers[2]) > disks - i - 1 else ' '}")

        while True:
            if msvcrt.kbhit():

                    

                # -------- GAME LOGIC
                key = msvcrt.getch().decode("utf-8", errors="ignore")

                if key == "q":
                    print("Quitting...")
                    break

                #print(f"Pressed: {key}")

                if key == "w":
                    if selector[1] != 0:
                        print("Can't pick up two at a time", end="\033[F")
                    else:
                        if towers[selector[0]] == []:
                            print("Nothing to pick up", end="\033[F")
                        else:
                            selector[1] = towers[selector[0]].pop()

                elif key == "s":
                    if selector[1] == 0:
                        print("Nothing to put down", end="\033[F")
                    else:
                        if towers[selector[0]] == [] or selector[1] < towers[selector[0]][-1]:
                            towers[selector[0]].append(selector[1])
                            selector[1] = 0
                            moves += 1
                        else:
                            print("Larger disk must be below", end="\033[F")

                elif key == "a":
                    selector[0] = (selector[0] - 1) % 3

                elif key == "d":
                    selector[0] = (selector[0] + 1) % 3

                if towerR == target:
                    print(f"Congratulations! You solved the game in {moves} moves! The optimal solution was in {2**disks-1}.")
                    break

                # -------- RENDERING
                HEIGHT = shutil.get_terminal_size()[1]
                WIDTH = shutil.get_terminal_size()[0]
                for i in range(HEIGHT):
                    print("\033[2K\033[F", end="")

                #print("\033[2J")
                print(f"TOWER OF HANOI: {disks} RINGS, {moves} MOVES MADE {' ' * (WIDTH-40-16 - 20)} PRESS 'Q' TO EXIT")    # 20 is extra, 40: start, 16: end
                #print(f"{(selector[0] * WIDTH // 3)*' '}V", end="")
                print(f"{(selector[0] * WIDTH // 3)*' '}", end="")
                if selector[1] == 0:
                    print("V", end="")
                else:
                    print(selector[1], end="")
                if HEIGHT > disks + 2:
                    for i in range(HEIGHT - disks - 3):
                        print()
                for i in range(disks):
                    #print(f"{towers[0][disks - i - 1] if len(towers[0]) > disks - i - 1 else ' '}".center(WIDTH // 3), end="")
                    print(f"{towers[0][disks - i - 1] if len(towers[0]) > disks - i - 1 else ' '}", end="")
                    print(WIDTH // 3*' ', end="")
                    #print(f"{towers[1][disks - i - 1] if len(towers[1]) > disks - i - 1 else ' '}".center(WIDTH // 3), end="")
                    print(f"{towers[1][disks - i - 1] if len(towers[1]) > disks - i - 1 else ' '}", end="")
                    print(WIDTH // 3*' ', end="")
                    #print(f"{towers[2][disks - i - 1] if len(towers[2]) > disks - i - 1 else ' '}".center(WIDTH // 3))
                    print(f"{towers[2][disks - i - 1] if len(towers[2]) > disks - i - 1 else ' '}")

            time.sleep(0.1)  


if __name__ == "__main__":
    r = int(input("Rings?"))
    TOH.Play(r)

#   0: Take input, get dimensions, draw thing
#   1: Wait for input, (do static animations)
#   2: Redraw affected elements (or the entire thing if overhead is negligible)
#   3: Loop until Finished or given command q/Q/quit/exit/close/stop
#


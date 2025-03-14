def ClearScreen():
    import os
    import platform
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def PrintMainMune():
    print("Welcome To My X - O Game!")

def ReadNumber(Massage, From, To):  
        try:
            Number = int(input(Massage))
        except:
            print("Only Number")
            return ReadNumber(Massage, From, To)
        if Number < From or Number > To:
            print(f"Choose Number From {From} To {To}: ")
            return ReadNumber(Massage, From, To)
        return Number
def ChooseMainMune():
    print("1. Start Game.")
    print("2. Quit Game.")
    ChooseNumber = ReadNumber("Enter Yout Choice (1 Or 2): ", 1, 2)
    if ChooseNumber == 2:
        print("Thank You For Playing!")
        exit()

def MainMune():
    ClearScreen()
    PrintMainMune()
    ChooseMainMune()


def InfoPlayer():
    DictInfo = {}
    ListSingle = []
    i = 1
    while i < 3:
        ClearScreen()
        print(f"Player {i}, Enter Your Details:")
        NamePlayer = input("Enter Your Name (Letters Only): ")
        Single = input(f"{NamePlayer}, Choose Your Symbol (A Single Letter): ")
        if Single in ListSingle:
            continue
        ListSingle.append(Single)
        DictInfo[NamePlayer] = Single
        i += 1
    return DictInfo

def Patch(ListNumber):
    S = f"""
    {ListNumber[0]}  |  {ListNumber[1]}  | {ListNumber[2]}
  ----------------
    {ListNumber[3]}  |  {ListNumber[4]}  | {ListNumber[5]}
  ----------------
    {ListNumber[6]}  |  {ListNumber[7]}  | {ListNumber[8]}
    
    """
    print(S)

def CheckList(L, List):
    for i in L:
        if i not in List:
            return False
    return True

def CheckWin(List1, List2, i):
    # 1 2 3
    # 4 5 6
    # 7 8 9
    ListWin = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

    if i == 0:
        for L in ListWin:
            if CheckList(L, List1):
                return 1
    if i == 1:
        for L in ListWin:
            if CheckList(L, List2):
                return 1
    return 0

def ListWin(List1, List2, i):
    ListWin = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

    if i == 0:
        for L in ListWin:
            if CheckList(L, List1):
                return L
    if i == 1:
        for L in ListWin:
            if CheckList(L, List2):
                return L
            
def PrintListWin(List):
    ListNumber = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    ListNumber[List[0] - 1] = "*"
    ListNumber[List[1] - 1] = "*"
    ListNumber[List[2] - 1] = "*"
    return ListNumber

def GamePlay(DictInfo):
    ListNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ListMove = []
    ListMovePlayer1 = []
    ListMovePlayer2 = []
    Keys = dict(DictInfo).keys()
    Values = dict(DictInfo).values()
    i = 0
    while(i < 9):
        ClearScreen()
        Patch(ListNumber)
        print(f"{list(Keys)[i % 2]}'s Turn {list(Values)[i % 2]}")
        ChooseNumber = ReadNumber("Choose A Cell (1-9): ", 1, 9)
        if ChooseNumber in ListMove:
            continue
        ListMove.append(ChooseNumber)
        if i % 2 == 0:
            ListMovePlayer1.append(ChooseNumber)
        else:
            ListMovePlayer2.append(ChooseNumber)
        ListNumber[ChooseNumber - 1] = list(Values)[i % 2]
        if CheckWin(ListMovePlayer1, ListMovePlayer2, i % 2):
            ClearScreen()
            Patch(ListNumber)
            Patch(PrintListWin(ListWin(ListMovePlayer1, ListMovePlayer2, i % 2)))
            print(f"{list(Keys)[i % 2]} ({list(Values)[i % 2]}) Win!!\n\n")
            break
        i += 1
        ClearScreen()
        print("Drow\n\n")

def Again():
    print("     1. Restart Game.")
    print("     2. Quit Game.")
    ChooseNumber = ReadNumber("     Enter Yout Choice (1 Or 2): ", 1, 2)
    if ChooseNumber == 2:
        print("     Thank You For Playing!")
        exit()

def Game():
    MainMune()
    while True:
        GamePlay(InfoPlayer())
        Again()  

Game()
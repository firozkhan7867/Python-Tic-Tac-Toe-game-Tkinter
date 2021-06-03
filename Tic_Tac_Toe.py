from tkinter import *
from tkinter import messagebox


class game():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")
        self.root.title("Tic Tac Toe")

        #abfcaf
        self.f1 = Frame(self.root, bg="#abfcaf")
        self.f1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.player_1_lb = Label(
            self.f1, bg="#abfcaf", fg="red", text="Player_1", font=('Bold', 20))
        self.player_1_lb.place(x=50, y=50)

        self.player_2_lb = Label(
            self.f1, bg="#abfcaf", fg="red", text="Player_2", font=('Bold', 20))
        self.player_2_lb.place(x=300, y=50)

        self.f2 = Frame(self.f1, bg="light green",
                        relief=SUNKEN, borderwidth=2)
        self.f2.place(relx=0.02, rely=0.26, relwidth=0.96, relheight=0.73)

        self.dic = {1: None, 2: None, 3: None, 4: None,
                    5: None, 6: None, 7: None, 8: None, 9: None}

        self.count = 2

        self.t = 0

        def clik1(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but1.config(text="X")
                but1.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but1.config(text="O")
                but1.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but1.config(state=DISABLED)
            self.logic()

        def clik2(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but2.config(text="X")
                but2.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but2.config(text="O")
                but2.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but2.config(state=DISABLED)
            self.logic()

        def clik3(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but3.config(text="X")
                but3.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but3.config(text="O")
                but3.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but3.config(state=DISABLED)
            self.logic()

        def clik4(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but4.config(text="X")
                but4.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but4.config(text="O")
                but4.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but4.config(state=DISABLED)
            self.logic()

        def clik5(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but5.config(text="X")
                but5.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but5.config(text="O")
                but5.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but5.config(state=DISABLED)
            self.logic()

        def clik6(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but6.config(text="X")
                but6.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but6.config(text="O")
                but6.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but6.config(state=DISABLED)
            self.logic()

        def clik7(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but7.config(text="X")
                but7.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but7.config(text="O")
                but7.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but7.config(state=DISABLED)
            self.logic()

        def clik8(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but8.config(text="X")
                but8.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but8.config(text="O")
                but8.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but8.config(state=DISABLED)
            self.logic()

        def clik9(vr):
            self.t += 1
            if self.count % 2 == 0:
                self.count += 1
                but9.config(text="X")
                but9.config(bg="plum")
                self.dic[vr] = 1
            elif self.count % 2 == 1:
                but9.config(text="O")
                but9.config(bg="khaki")
                self.count += 1
                self.dic[vr] = 0
            but9.config(state=DISABLED)
            self.logic()

        but1 = Button(self.f2, text="-", font=('font', 30),
                      width=5, height=2, command=lambda: clik1(1))
        but1.grid(row=0, column=0, padx=20, pady=12)

        but2 = Button(self.f2, text="-", font=('font', 30),
                      width=5, height=2, command=lambda: clik2(2))
        but2.grid(row=0, column=1, padx=12, pady=12)

        but3 = Button(self.f2, text="-", font=(
            'font', 30), width=5, height=2, command=lambda: clik3(3))
        but3.grid(row=0, column=2, padx=12, pady=12)

        but4 = Button(self.f2, text="-", font=(
            'font', 30), width=5, height=2, command=lambda: clik4(4))
        but4.grid(row=1, column=0, padx=20, pady=12)

        but5 = Button(self.f2, text="-", font=('font', 30),
                      width=5, height=2, command=lambda: clik5(5))
        but5.grid(row=1, column=1, padx=12, pady=12)

        but6 = Button(self.f2, text="-", font=(
            'font', 30), width=5, height=2, command=lambda: clik6(6))
        but6.grid(row=1, column=2, padx=12, pady=12)

        but7 = Button(self.f2, text="-", font=('font', 30),
                      width=5, height=2, command=lambda: clik7(7))
        but7.grid(row=2, column=0, padx=20, pady=12)

        but8 = Button(self.f2, text="-", font=(
            'font', 30), width=5, height=2, command=lambda: clik8(8))
        but8.grid(row=2, column=1, padx=12, pady=12)

        but9 = Button(self.f2, text="-", font=('font', 30),
                      width=5, height=2, command=lambda: clik9(9))
        but9.grid(row=2, column=2, padx=12, pady=12)

        self.root.mainloop

    def logic1(self):
        print(self.dic)
        self.self.lst = []
        for i in self.dic.keys():
            self.self.lst.append(i)
        # print(self.self.lst)
        # c = self.self.lst[:3]
        # print("hellloooooooo    ",c)
        # if c == [1, 1, 1]:
        #     print("you won")

        self.self.lst.sort()
        print(self.self.lst)
        l1 = []

        for i in self.lst:
            l1.append(self.dic[i])
        print(l1)

    def logic(self):
        print(self.dic)
        
        self.lst = []
        for i in self.dic.values():
            self.lst.append(i)
        print(self.lst)

        self.cmp()

    def cmp(self):
        s = [1, 1, 1]
        zero = [0, 0, 0]

        if self.lst[:3] == s:
            messagebox.showinfo("Combo", " have been found")
            self.root.quit()

        elif self.lst[0::3] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[0::4] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[1::3] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[2::3] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[-3:] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[2:-2:2] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[1::3] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit()
        elif self.lst[3:6] == s:
            messagebox.showinfo(
                "Congratulation", "Player 'X' has won the game")
            self.root.quit() 

        #$$$$$$$$$$$$$$$$$$$$$$$$

        elif self.lst[:3] == zero :
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()

        elif self.lst[0::3] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[0::4] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[1::3] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[2::3] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[-3:] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[2:-2:2] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[1::3] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.lst[3:6] == zero:
            messagebox.showinfo(
                "Congratulation", "Player 'O' has won the game")
            self.root.quit()
        elif self.t == 9:
            messagebox.showinfo(
                "Tie....", "Its an tie match between 'X' and 'O'")
            self.root.quit()


        else:
            print('not an combo')


root = Tk()
s = game(root)
root.mainloop()

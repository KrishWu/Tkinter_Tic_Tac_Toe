import tkinter as tk

class Board(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        canvas_width = 600
        canvas_height = 600
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, background="grey")
        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)
        self.canvas.bind("<Button-1>", self.click)
        self.num0s = 10
        self.old_num0s = 10
        self.turn = 0
        self.board1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def checkWin(self):
        for y in range(3):
            if self.board1[0][y] == self.board1[1][y] and self.board1[1][y] == self.board1[2][y] and self.board1[0][y] != 0:
                return True
        for x in range(3):
            if self.board1[x][0] == self.board1[x][1] and self.board1[x][1] == self.board1[x][2] and self.board1[x][0] != 0:
                return True
        if self.board1[0][0] == self.board1[1][1] and self.board1[1][1] == self.board1[2][2] and self.board1[0][0] != 0:
            return True
        if self.board1[2][0] == self.board1[1][1] and self.board1[1][1] == self.board1[0][2] and self.board1[2][0] != 0:
            return True
        return False

    def draw_x(self, x, y):
        # self.canvas.create_text((x*200)+100, (y*200)+100, anchor=tk.W, font="Purisa", text="x")
        self.canvas.create_oval((x*200)+100, (y*200)+100, (x*200)+100+80, (y*200)+100+80, outline="#1f1", width=2)

    def draw_o(self, x, y):
        self.canvas.create_oval((x*200)+100, (y*200)+100, (x*200)+100+80, (y*200)+100+80, outline="#f11", width=2)

    def draw_board(self):
        self.old_num0s = self.num0s
        self.num0s = 0
        self.canvas.delete("all")
        for i in range(2):
            self.canvas.create_line(0, 200+(i*200), 600, 200+(i*200), width=10)
        for i in range(2):
            self.canvas.create_line(200+(i*200), 0, 200+(i*200), 600, width=10)
        for i in range(3):
            for w in range(3):
                if self.board1[i][w] == "x":
                    self.draw_x(i, w)
                if self.board1[i][w] == "y":
                    self.draw_o(i, w)
                if self.board1[i][w] == 0:
                    self.num0s += 1
        if self.checkWin():
            if self.turn%2 == 0:
                winner = "green"
            else:
                winner = "red"
            self.canvas.create_text(250, 300, anchor=tk.W, font="Purisa", text="The winner is " + winner + "!")
        if self.num0s == 0:
            self.canvas.create_text(250, 300, anchor=tk.W, font="Purisa", text="Its a tie!")
        if self.old_num0s-1 == self.num0s:
            self.turn += 1


    def click(self, event):
        print('x: {} y: {}'.format(event.x, event.y))
        list_x = event.x // 200
        list_y = event.y // 200
        if self.board1[list_x][list_y] == 0:
            if self.turn % 2 == 0:
                self.board1[list_x][list_y] = "x"
            if self.turn % 2 == 1:
                self.board1[list_x][list_y] = "y"
        self.draw_board()


game = True


root = tk.Tk()
root.title('Tic Tac Toe')
board = Board(root)
board.pack(side="top")
board.draw_board()
root.mainloop()

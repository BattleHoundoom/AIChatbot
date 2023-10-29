from tkinter import *
from Bot import get_response

BG = "#000000"
FG = "#16ECA2"
TC = "#FFFFFF"

class ChatBubble(Text):
    def __init__(self, parent, text, is_sent=True):
        super().__init__(parent)
        self.pack(anchor="w" if is_sent else "e", padx=10 if not is_sent else 5, pady=5)
        self.configure(bg="lightblue" if is_sent else "lightgreen")

        label = Label(self, text=text, wraplength=200, bg="lightblue" if is_sent else "lightgreen")
        label.pack(padx=10, pady=5)

class Chatbot:
    def __init__(self):
        self.window = Tk()
        self.setup()

    def run(self):
        self.window.mainloop()

    def setup(self):
        self.window.title("Chatbot (Powered by ChatGPT-3.5)")
        self.window.configure(width=600, height=800, bg=BG)

        title = Label(self.window, text="Chat with AI bot", pady=10, bg=BG, fg=FG, font=("Helvetica", 24, "bold"))
        title.place(relwidth=1)

        line = Label(self.window, width=450, bg=BG)
        line.place(relwidth=1, relheight=0.012, rely=0.07)

        self.text_widget = Text(self.window, width=20, height=0, padx=5, pady=5, bg=BG, fg=FG, wrap=WORD)
        self.text_widget.place(relwidth=0.95, rely=0.08, relheight=0.745)
        self.text_widget.configure(cursor="arrow")

        scrollbar = Scrollbar(self.window)
        scrollbar.place(relheight=0.745, relx=0.96, rely=0.08)

        self.text_widget.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.text_widget.yview)

        bottom = Label(self.window, height=80, bg=BG)
        bottom.place(relwidth=1, rely=0.85)

        self.text_box = Entry(bottom, bg=BG, fg=TC, insertbackground=TC)
        self.text_box.place(relwidth=0.74, relheight=0.06, relx=0.011, rely=0.008)
        self.text_box.focus()
        self.text_box.bind("<Return>", self.submit)

        send_btn = Button(bottom, text="Send", width=20, bg=FG, fg=TC, command=lambda: self.submit(None), font=("Helvetica", 18, "bold"))
        send_btn.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        self.text_widget.update_idletasks()
        self.DisplayResponse("Introduce Yourself")

    def submit(self, event):
        msg = self.text_box.get()
        self.InsertMsg(msg)

    def InsertMsg(self, msg):
        if not msg: return

        self.text_box.delete(0, END)

        #msg1 = f"You: {msg}\n\n"
        #self.text_widget.configure(state=NORMAL)
        bubble = ChatBubble(self.text_widget, msg, is_sent=False)
        #self.text_widget.insert(END, ChatBubble(self.text_widget, msg, is_sent=False))
        #self.text_widget.configure(state=DISABLED)
        self.text_widget.update_idletasks()
        self.text_widget.see("end")  # Scroll to the end of the Text widget

        self.DisplayResponse(msg)

    def DisplayResponse(self, msg):
        #msg2 = f"Bot: {get_response(msg)}\n\n"
        #self.text_widget.configure(state=NORMAL)
        bubble = ChatBubble(self.text_widget, get_response(msg), is_sent=True)
        #self.text_widget.insert(END, ChatBubble(self.text_widget, get_response(msg), is_sent=True))

        #self.text_widget.configure(state=DISABLED)
        self.text_widget.update_idletasks()
        self.text_widget.see("end")  # Scroll to the end of the Text widget


if __name__ == "__main__":
    app = Chatbot()
    app.run()
# 2 things left: chatgpt intial prompt, scrollable text_widget
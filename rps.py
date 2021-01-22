from tkinter import*
import random

root = Tk()
root.configure(bg="#000000")
root.geometry('+0+0')
root.iconbitmap("C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\rps.ico")
root.title("Rock-Paper-Scissor")
root.resizable(width=False,height=False)

#SOUND
roar = 'C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\roar.mp3'
laugh ='C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\sound\\laugh.mp3'

#IMAGES
rock= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\Rock.png")
paper= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\Paper.png")
scissor= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\Scissor.png")
win= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\WIN.png")
lose = PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\LOST.png")
tie= PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\DRAW.png")
startgame = PhotoImage(file="C:\\Users\\divya\\OneDrive\\Desktop\\CLG\\191270\\Project\\ZEUS\\pictures\\game.png")

rockHandButton = " "
paperHandButton = " "
scissorHandButton = " "
resultButton = Button(root,image=startgame)

click = True

def play():
    global rockHandButton,paperHandButton,scissorHandButton    
    #Set images and commands for buttons :
    rockHandButton = Button(root,image = rock, command=lambda:you_pick("Rock"))
    paperHandButton = Button(root,image = paper, command=lambda:you_pick("Paper"))
    scissorHandButton = Button(root,image = scissor, command=lambda:you_pick("Scissor"))


    #Place the buttons on window :
    rockHandButton.grid(row=0,column=0)
    paperHandButton.grid(row=0,column=1)
    scissorHandButton.grid(row=0,column=2)

    #Add space :
    root.grid_rowconfigure(1, minsize=50) 

    #Place result button on window : 
    resultButton.grid(row=2,column=0,columnspan=5)

def computer_pick():
    choice = random.choice(["Rock","Paper","Scissor"])
    return choice
# speak("choose among rock paper or scissor")
def you_pick(yourChoice):
    global click

    comp_pick = computer_pick()
    if click==True:
        if yourChoice == "Rock":
            rockHandButton.configure(image=rock)

            if comp_pick == "Rock":
                paperHandButton.configure(image=rock)
                resultButton.configure(image=tie)
                scissorHandButton.grid_forget()
                click = False
                print("draw!")

            elif comp_pick == "Paper":
                paperHandButton.configure(image=paper)
                scissorHandButton.grid_forget()
                resultButton.configure(image=lose)
                click = False
                print("You Lost!")


            else:
                paperHandButton.configure(image=scissor)
                scissorHandButton.grid_forget()
                resultButton.configure(image=win)
                click = False
                print("You Win!")

        elif yourChoice == "Paper":
            rockHandButton.configure(image=paper)

            if comp_pick == "Rock":
                paperHandButton.configure(image=rock)
                resultButton.configure(image=win)
                scissorHandButton.grid_forget()
                click = False
                print("You Win!")


            elif comp_pick == "Paper":
                paperHandButton.configure(image=paper)
                resultButton.configure(image=tie)
                scissorHandButton.grid_forget()
                click = False
                print("draw!")

            else:
                paperHandButton.configure(image=scissor)
                resultButton.configure(image=lose)
                scissorHandButton.grid_forget()
                click = False
                print("You Lost!")

        elif yourChoice=="Scissor":
            rockHandButton.configure(image=scissor)

            if comp_pick == "Rock":
                paperHandButton.configure(image=rock)
                resultButton.configure(image=lose)
                scissorHandButton.grid_forget()
                click = False
                print("You Lost!")

            elif comp_pick == "Paper":
                paperHandButton.configure(image=paper)
                resultButton.configure(image=win)
                scissorHandButton.grid_forget()
                click = False
                print("You Win!")
            

            else:
                paperHandButton.configure(image=scissor)
                resultButton.configure(image=tie)
                scissorHandButton.grid_forget()
                click = False
                print("draw!")
       
    else:
        #To reset the game :
        if yourChoice=="Rock" or yourChoice=="Paper" or yourChoice=="Scissor" or yourChoice=="Lizard" or yourChoice=="Spock":
            rockHandButton.configure(image=rock)
            paperHandButton.configure(image=paper)
            scissorHandButton.configure(image=scissor)
            resultButton.configure(image=startgame)
            
            #Get back the deleted buttons
            scissorHandButton.grid(row=0,column=2)
            click=True



play()
root.mainloop()
from tkinter import *
import random

root = Tk()
root.title('quick sort dan shell sort by apiw anak bu eli')
root.maxsize(1080,720)
root.config (bg='pink')

data1 = []
data2 = []

def quick_sort(data,drawArr,canvas,left,right):
    if left >= right:
        return
    index = left
    for j in range(left, right):
        if data[j] < data[right]:
            data[j], data[index] = data[index], data[j]
            drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
            index += 1
    data[index], data[right] = data[right], data[index]
    quick_sort(data,drawArr,canvas, index + 1, right)
    quick_sort(data,drawArr,canvas, left, index - 1)
    drawArr(data, ['green' for x in range(len(data))], canvas)    


def shell_sort(data,drawArr,canvas):   
    gap = len(data) // 2

    while gap > 0:
        for i in range(gap,len(data)):
            tmp = data[i]
            j = i
            while j >= gap and data[j-gap] > tmp:
                data[j] = data[j-gap]
                drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                j -= gap
            data[j] = tmp
        gap //= 2
    drawArr(data, ['green' for x in range(len(data))], canvas)

def drawArr(data, color, canvas):
    canvas.delete("all")
    c_width = 336
    c_height = 380
    x_width = c_width / (len(data) + 1)
    offset = 10
    space = 5
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 336
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], outline=color[i])

    root.update_idletasks()


def generateArr():
    global data1
    global data2
    data1 = []  
    data2 = []
    

    size = int(sizeInput.get())
    for _ in range(size):
        data1.append(random.randrange(5, 100))
    data2[:] = data1[:]
    drawArr(data1,['white' for x in range(len(data1))],canvas1)
    drawArr(data2,['white' for x in range(len(data2))],canvas2)

def startAlgo():
    global data1
    global data2

    shell_sort(data2, drawArr, canvas2)
    quick_sort(data1, drawArr, canvas1,left=0,right=len(data1)-1)


Label(root,text="quick Sort",bg='pink').grid(row=0,column=0)
Label(root,text="Shell Sort",bg='pink').grid(row=0,column=1)

canvas1 = Canvas(root, width=340, height=380, bg = 'magenta')
canvas1.grid(row=1, column=0, padx=10, pady=10)

canvas2 = Canvas(root, width=340, height=380, bg = 'magenta')
canvas2.grid(row=1, column=1, padx=10, pady=10)

buttonsFrame = Frame(root, width = 720, height = 50, bg ='pink')
buttonsFrame.grid(row = 3, column=0, padx =10, pady=10)

Label(buttonsFrame, text="masukan angka :", bg= 'white').grid(row=0, column=0, padx=5,pady=5)

sizeInput = Entry(buttonsFrame)
sizeInput.grid(row=1, column=0, padx=5,pady=5)

genButton =Button(buttonsFrame, text="buat array acak", command=generateArr)
genButton.grid(row=1, column=1, padx=5, pady=5)

startButton = Button(buttonsFrame, text="mulai sortir", command=startAlgo)
startButton.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()
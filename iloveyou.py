from tkinter import *
from tkinter import ttk
import time
import sys
from tkinter.ttk import Style


df_iloveyou = [ 
    '#Python\nprint(\'I love you!\')',
    '#Java\npublic class ILoveYou\n{\n    public static void main(String[] args)\n    {\n     System.out.println("I love you!");\n    }\n}',
    '#C\n#include <stdio.h>\n\nint main(void)\n{\n    printf("I love you!\\n");\n    return 0;\n}',
    '#C++\n#include <stdio.h>\n\nint main(void)\n{\n    std::cout << "I love you!" << std::endl;\n    return 0;\n}',
    '#JavaScipt\ndocument.write("I love you!");',
    '#Arduino\nvoid setup() {\nSerial.begin(9600);\nSerial.println("I love you!");\n}\n\nvoid loop() {\n}',
    '#Go\npackage main;\n\nimport "fmt"\n\nfunc main()\n{\n   fmt.Println("I love you!")\n]',
    '#MATLAB\ndisp(\'I love you!\')',
    '#Ruby\nputs "I love you!"',
    '#Dart\nvoid main() {\n   print(\'I love you!\');\n}',
    '#SQL\nCREATE TABLE iloveyou (phrase TEXT);\nINSERT INTO iloveyou VALUES ("I love you!");\nSELECT COUNT(*) FROM iloveyou;',
    '#PHP\n<?php\necho "I love you!";\n?>',
    '#Assembly\n   global  _main\n   extern  _printf\n\nsection .text\n_main:\n   push    message\n   call    _printf'
      '\n   add     esp, 4\n   ret\nmessage:\n   db  \'I love you!\', 10, 0',
    '#Scala\nobject Love {\n    def main(args: Array[String]) = {\n        println("I love you!")\n    }\n}',
    '#Kotlin\nfun main(args: Array<String>) {\n    println("I love you!")\n}',
    '#Julia\nprintln("I love you!")',
    '#Rust\nfn main() {\n    println!("I love you!");\n}',
    '#Shell\n#!/bin/sh\n\necho I love you!'
]

def resume_code():
    for code in df_iloveyou:
        canvas.delete('all')
        canvas.create_text((300,300), text=code, font=('Roboto', 20))
        time.sleep(2)
        window.update()


window = Tk()
window.title('Валентинка на всех языках программирования')
Button(window, text='Тыкни на меня :З', command=resume_code).pack()
Button(window, text='Выйти (не в окно)', command=lambda: sys.exit()).pack()
canvas = Canvas(window, width=600, height=600)
canvas.pack()



window.mainloop()
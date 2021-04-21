#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: José Rodolfo (JRIC2002)

#Modules

#External modules
import sys

#Internal modules
from modules import functions

class Color:
    """ Colores en código ANSI. """

    #Styles
    reset = "\033[0m"
    bold = "\033[1m"
    dark = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    hidden = "\033[8m"

    #Foreground
    black= "\033[30m"
    gray = "\033[1;30m"
    red= "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    #Background
    bgBlack = "\033[40m"
    bgRed = "\033[41m"
    bgGreen = "\033[42m"
    bgYellow = "\033[43m"
    bgBlue = "\033[44m"
    bgMagenta = "\033[45m"
    bgCyan = "\033[46m"
    bgWhite = "\033[47m"

#Instancia de la clase Color
color = Color()

class Start:
    """ Inicio de la herramienta MathCalc. """
    
    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta MathCalc. """

        print("{}".format(color.bold))
        print("         {} __  __       _   _        {}____      _".format(color.blue, color.green))
        print("         {}|  \/  | __ _| |_| |__    {}/ ___|__ _| | ___".format(color.blue, color.green))
        print("         {}| |\/| |/ _` | __| '_ \  {}| |   / _` | |/ __|".format(color.blue, color.green))
        print("         {}| |  | | (_| | |_| | | | {}| |__| (_| | | (__".format(color.blue, color.green))
        print("         {}|_|  |_|\__,_|\__|_| |_|  {}\____\__,_|_|\___| {}".format(color.blue, color.green, color.white))
        print("")
        print("               {}</> {}Tool coded by:{} JRIC2002 {}</>{}".format(color.gray, color.yellow, color.white, color.gray, color.white))
        print("          {}</> {}Description:{} Solve math operations {}</>{}".format(color.gray, color.yellow, color.white, color.gray, color.reset))
        print("")

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta MathCalc. """

        print("{}{}Usage: python3 MathCalc.py [options]".format(color.bold, color.white))
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.")
        print("")
        print("   Basic operations:")
        print("      At least one of these options must be provided to perform the mathematical operation.")
        print("")
        print("      -s, --sum               Perform the mathematical operation of 'SUM'")
        print("      -r, --subtract          Perform the mathematical operation of 'SUBTRACT'")
        print("      -m, --multiply          Perform the mathematical operation of 'MULTIPLY'")
        print("      -d, --divide            Perform the mathematical operation of 'DIVIDE'")
        print("      -p, --power             Perform the mathematical operation of 'POWER'")
        print("{}".format(color.reset))

    def version(self):
        """ Imprime la versión de la herramienta MathCalc. """

        print("{}{}#MathCalc version 1.3{}".format(color.bold, color.white, color.reset))

    def error1(self):
        """ Imprime un mensaje de error. """

        print("{}{}Usage: python3 MathCalc.py [options]".format(color.bold, color.white))
        print("")
        print("MathCalc.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.{}".format(color.reset))

    def error2(self):
        """ Imprime un mensaje de error de argumentos. """

        print("{}{}Usage: python3 MathCalc.py [options]".format(color.bold, color.white))
        print("")
        print("MathCalc.py: Error: Invalid option or arguments.")
        print("Use -h or --help to see the help menu.".format(color.reset))

#Instancia de la clase Start
start = Start()

#Start
if len(sys.argv) == 1:
    start.logo()
    start.help_menu()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        start.logo()
        start.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        start.version()
    else:
        start.logo()
        start.error1()
else:
    if sys.argv[1] == "-s" or sys.argv[1] == "--sum":
        functions.sum(sys.argv[2:])
    elif sys.argv[1] == "-r" or sys.argv[1] == "--subtract":
        functions.subtract(sys.argv[2:])
    elif sys.argv[1] == "-m" or sys.argv[1] == "--multiply":
        functions.multiply(sys.argv[2:])
    elif len(sys.argv) == 4:
        if sys.argv[1] == "-d" or sys.argv[1] == "--divide":
            functions.divide(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "-p" or sys.argv[1] == "--power":
            functions.power(sys.argv[2], sys.argv[3])
        else:
            start.logo()
            start.error1()
    else:
        start.logo()
        start.error2()

from PIL import Image

import sys
import getopt
from os import system, name, remove, path



def main(argv):

    # getting inputs from commandline and parsing them for errors
    try:
        opts, args = getopt.getopt(argv, "i", ["ifile="])
    except getopt.GetoptError:
        print("There was a problem parsing your input (error 1)")
        sys.exit()

    opt = opts[0][0]
    imagePath = args[0]

    if opt != "-i":
        print("There was a problem parsing your input (error 2)")
        sys.exit()

    # creating the ascii output path
    pathNameArr = imagePath.split(".")
    outputPath = ""
    x = 0
    while (x < len(pathNameArr) - 1):
        outputPath += f"{pathNameArr[x]}."
        x += 1
    outputPath += "txt"

    # attempting to open the picture
    try:
        image = Image.open(imagePath, 'r')
    except:
        print("There was a problem opening the picture (error 3)")

    blackAndWhite = []

    adderArr = []
    index = 0
    x = 0

    imageList = list(image.getdata())

    while index < len(imageList):
        currentPixelTuple = imageList[index]
        
        sum = 0
        sum += currentPixelTuple[0] * .299
        sum += currentPixelTuple[1] * .587
        sum += currentPixelTuple[2] * .114

        adjusted = (sum / 255.0) * 100.0

        adderArr.append(adjusted)
        #print(f"{currentPixelTuple} converted is {sum} and adjusted is {adjusted}")

        x += 1
        index += 1
        if x >= image.width:
            x = 0
            blackAndWhite.append(adderArr)
            adderArr = []

    if path.exists(outputPath):
            remove(outputPath)
            
    with open(outputPath, 'a') as f:
        print("┌", end="", file=f)
        for i in range((image.width * 2) + 1):
            print("─", end="", file=f)
        print("┐", file=f)

        for j in blackAndWhite:
            print("│ ", end="", file=f)
            for currentPixelValue in j:
                #currentPixelValue = blackAndWhite[j][i]
                #print(f"currentPixelValue is set to blackAndWhite[{j}][{i}] ({currentPixelValue})", end = "")
                printVal = ''
                if currentPixelValue > 95:
                    printVal = '█'
                elif currentPixelValue > 90:
                    printVal = '▓'
                elif currentPixelValue > 85:
                    printVal = '#'
                elif currentPixelValue > 80:
                    printVal = 'B'
                elif currentPixelValue > 75:
                    printVal = 'A'
                elif currentPixelValue > 70:
                    printVal = 'R'
                elif currentPixelValue > 60:
                    printVal = 'Q'
                elif currentPixelValue > 50:
                    printVal = 'G'
                elif currentPixelValue > 45:
                    printVal = 'U'
                elif currentPixelValue > 40:
                    printVal = 'O'
                elif currentPixelValue > 25:
                    printVal = '▒'
                elif currentPixelValue >= 0:
                    printVal = ' '
                else:
                    print("There was an error parsing the image on this specific pixel... (error 4)", file=f)
                print(f"{printVal} ", end="", file=f)
            print("│", file=f)

        
        print("└", end="", file=f)
        for i in range((image.width * 2) + 1):
            print("─", end="", file=f)
        print("┘", file=f)


if __name__ == "__main__":
    main(sys.argv[1:])

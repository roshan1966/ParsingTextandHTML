# Ask the user for file name
filename = input("Enter the name of a Text File: ")

def analyze_file(filename):
    try:
        with open (filename, "r", encoding="utf8") as txt_file:
            file_contents = txt_file.read()
    except FileNotFoundError:
        print ("Sorry, the file named '" + filename + "' was not found")
    else:
        num_lines = 0
        num_non_space = 0
        num_spaces = 0
        num_tabs = 0
        num_paragraph = 0
        potential_paragraph = 0

        for i in range(0, len(file_contents)):
            if (file_contents[i] == "\t"):
                num_tabs += 1
            
            if (file_contents[i] == ' '):
                num_spaces += 1
                if (potential_paragraph > 0):
                    potential_paragraph += 1
            else:
                num_non_space += 1
                potential_paragraph = 0
            
            if (file_contents[i] == '\n'):
                num_lines += 1
            
            if (file_contents[i] == '\r' and file_contents[i - 1] != '\n'):
                num_lines += 1
            
            if (file_contents[i - 1] == '\n' or file_contents[i - 1] == '\r'):
                potential_paragraph += 1
            
            if (potential_paragraph > 2):
                potential_paragraph = 0
                num_paragraph += 1
            
        print ("Number of words: " + str(len(file_contents.split())))
        print ("Number of lines: " + str(num_lines))
        print ("Number of non-space characters: " + str(num_non_space))
        print ("Number of spaces (excluding paragraph spaces): " + str(num_spaces - num_paragraph * 2))
        print ("Number of tabs: " + str(num_tabs))
        print ("Number of paragraphs: " + str(num_paragraph))
        print ("Number of spaces (including paragraph spaces): " + str(num_spaces))


analyze_file(filename)
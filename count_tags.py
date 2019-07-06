# Ask the user for file name
filename = input("Enter the name of a HTML File: ")

def analyze_file(filename):
    try:
        with open (filename, "r", encoding="utf8") as txt_file:
            file_contents = txt_file.read()
    except FileNotFoundError:
        print ("Sorry, the file named '" + filename + "' was not found")
    else:
        tags = []

        openings = file_contents.split('<')
        
        for opening in openings:
            if len(opening) > 1:
                if opening[0] != '/':
                    opening = opening.split('>')[0]
                    opening = opening.split(' ')[0]
                    tags.append('<' + opening + '>')

        print ("Number of tags: " + str(len(tags)))

        for i in range(len(tags)):
            print (str(i+1) + ". " + str(tags[i]))

analyze_file(filename)
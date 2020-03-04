url = ""

def main():
    x = '<img src="'
    y = '">\n'
    z = input("Type a URL: Type exit() to quit:")
    global url
###stips whitespace off url
    url = z.strip()
###opens test.txt, creates if it does't exist then appends file
    a = open("test.txt", "a")
    a.write(x + url + y)
    a.close()

###while loop to exit program if exit() is entered, jump back to main() otherwise
while url != "exit()":
    main()
    if url == "exit()":
       break


###read what was written to test.txt file
a = open ("test.txt", "r")
print(a.read())

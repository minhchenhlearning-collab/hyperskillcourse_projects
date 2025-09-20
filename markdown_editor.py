def basic_format():
    global output_passage
    text = input("Text: ")
    if format == "plain":
        output_passage += text
    elif format == "bold":
        output_passage += f"**{text}**"
    elif format == "italic":
        output_passage += f"*{text}*"
    elif format == "inline-code":
        output_passage += f"`{text}`"
    print(output_passage)

def headings():
    global output_passage
    while (level := int(input("Level: "))) > 6 or level < 1:
        print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    output_passage += f"{'#'*level} {text}\n"
    print(output_passage)

def new_line():
    global output_passage
    output_passage += "\n"
    print(output_passage)

def link():
    global output_passage
    label = input("Label: ")
    url = input("URL: ")
    text = f"[{label}]({url})"
    output_passage += text
    print(output_passage)

def list_():
    global output_passage
    while (rows := int(input("Number of rows: "))) < 1:
        print("The number of rows should be greater than zero")
    text = [input(f"Row #{i}: ") for i in range(1, rows+1)]
    if format == "ordered-list":
        for index, content in enumerate(text):
            output_passage += f"{index+1}. {content}\n"
    elif format == "unordered-list":
        for content in text:
            output_passage += f"* {content}\n"
    print(output_passage)

def save_file():
    if format == "!done":
        with open("Markdown\output.md", "w") as file:
            file.write(output_passage)


formatters = "plain bold italic header link inline-code ordered-list unordered-list new-line".split()
formatters_dict = {"plain":basic_format, "bold":basic_format, "italic":basic_format, "header":headings,
                   "link":link, "inline-code":basic_format, "ordered-list":list_, "unordered-list":list_, "new-line": new_line}
output_passage = ""
while True:
    if (format := input("Choose a formatter: ")) != "!done":
        if format == "!help":
            print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
            print("Special commands: !help !done")
            continue
        if format not in formatters:
            print("Unknown formatting type or command")
            continue
        else:
            formatters_dict.get(format)()
            continue
    else:
        save_file()
        break
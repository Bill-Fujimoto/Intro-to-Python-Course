def load_file(filename):
    input_file = open(filename, "r")
    value=input_file.readline()
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value

contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))

import sys
from os import getenv
def echo(args):
    print(" ".join(args))

def load_executables():
    paths = getenv('PATH')
    sys.stdout.write(paths)
    executables = {}
    if paths:
        for path in paths.split(';'):
            sys.stdout.write(path)
            executables[path.split('\\')[:-1]] = path.split('\\')[-1]
    return executables
            
def exit():
    sys.stdout.write("Goodbye!")
    sys.exit(0)

def clear():
    sys.stdout.write("\033c")

def type(args):
    sys.stdout.write(load_executables() + '\n')
    if args[0] in valid_commands:
        sys.stdout.write(f"{args[0]} is a built in command\n")
    else:
        sys.stdout.write(f"{args[0]}: Command not found\n")
def main():
    while True:
        global valid_commands
        valid_commands = ['exit', 'echo', 'type', 'clear']
        sys.stdout.write("$ ")
        command = input().split()
        if len(command) <= 0:
            continue
        args = command[1:]
        command = command[0]
        
        if command == "exit":
            exit()
        elif command == "echo":
            echo(args)
        elif command == "clear":
            clear()
        elif command == "type":
            type(args)
        elif not command in valid_commands:
            print(f"{command}: Command not found\n")

if __name__ == '__main__':
    main()
    sys.exit(0)
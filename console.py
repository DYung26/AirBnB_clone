#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle End-of-File (EOF) input"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + `ENTER` shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()    

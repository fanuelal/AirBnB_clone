#!/usr/bin/python3

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    making the console
    """
    all_classes = {'BaseModel' : BaseModel, 'User' : User, 'State' : State,
                   'City': City, 'Amenity' : Amenity, 'Place' : Place,
                   'Review' : Review}

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ exiting the program"""
        return True

    def do_EOF(self, arg):
        """ quit """
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ creates a new instance of BaseModel saves it to the json file
            and prints the id
        """
        if arg == '':
            print('** class name missing **')
            return
        elif arg not in HBNBCommand.all_classes.keys():
            print('** class doesn\'t exist **')
        else:
            B1 = HBNBCommand.all_classes[arg]()
            B1.save()
            print(B1.id)

    def do_show(self, arg):
        """ prints the str rep of an instance based on the
            class name and id
        """
        lst = arg.split(' ')
        if len(arg) == 0:
            print('** class name missing **')
            return

        elif lst[0] not in HBNBCommand.all_classes.keys():
            print('** class doesn\'t exist **')
            return

        elif len(lst) == 1:
            print('** instance id missing **')
            return

        else:
            key = lst[0] + '.' + lst[1]
            allInstances = storage.all()
            if key not in allInstances.keys():
                print('** no instance found **')
            else:
                obj = allInstances[key]
                print(obj)

    def do_destroy(self, arg):
        """
        deletes an instance based on the class name and id
        """
        lst = arg.split(' ')
        if len(arg) == 0:
            print('** class name missing **')
            return

        elif lst[0] not in HBNBCommand.all_classes.keys():
            print('** class doesn\'t exist **')
            return

        elif len(lst) == 1:
            print('** instance id missing **')
            return

        else:
            key = lst[0] + '.' + lst[1]
            allInstances = storage.all()
            if key not in allInstances.keys():
                print('** no instance found **')
            else:
                del(allInstances[key])
                storage.save()

    def do_all(self, arg):
        """
        prints all str rep of all instances based or not on the class name
        """
        objList = []
        obj = storage.all()
        try:
            if len(arg) != 0:
                eval(arg)
            else:
                pass
        except NameError:
            print('** class doesn\'t exist **')
            return
        arg.strip()
        for key, val in obj.items():
            if len(arg) != 0:
                if type(val) is eval(arg):
                    val = str(obj[key])
                    objList.append(val)
            else:
                val = str(obj[key])
                objList.append(val)
        print(objList)

    def do_update(self, arg):
        """
        updates an instance based on the class name and id by adding or updating attr
        """

        lst = arg.split(' ')
        if len(arg) == 0:
            print('** class name missing **')
            return

        elif lst[0] not in HBNBCommand.all_classes.keys():
            print('** class doesn\'t exist **')
            return

        elif len(lst) == 1:
            print('** instance id missing **')
            return

        elif len(lst) == 2:
            print('** attribute name missing **')

        elif len(lst) == 3:
            print('** value missing **')

        else:
            key = lst[0] + '.' + lst[1]
            allInstances = storage.all()
            if key not in allInstances.keys():
                print('** no instance found **')
            else:
                obj = allInstances[key]
                setattr(obj, lst[2], lst[3])
                storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()

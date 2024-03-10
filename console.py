#!/usr/bin/python3

import cmd
import json
from models import storage
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):

    """Simple Command Processor example."""

    prompt = "(hbnb) "

    def handle_unrec_cmd(self, cmd_text):
        """  """
        self._parse_line(cmd_text)




    def _parse_line(self, cmd_text):
        """  """
        # Split the line by '.' to separate classname from the rest
        parts = cmd_text.split('.', 1)
        if len(parts) < 2:
            return cmd_text
    
        classname, rest = parts
        if '(' not in rest or ')' not in rest:
            return cmd_text
        # Extract method name and arguments
        method, arguments = rest.split('(', 1)
        arguments = arguments.rstrip(')')
    
        # Process arguments further if necessary
        if method == "update" and arguments:
            if arguments.startswith('{') and arguments.endswith('}'):
                # Handle dictionary argument
                self.refresh_instance_data(classname, arguments[1:-1])
                return ""
            else:
                # Handle other arguments
                arg_parts = arguments.split(',', 1)
                uid = arg_parts[0].strip('"')
                attr_or_dict = arg_parts[1] if len(arg_parts) > 1 else ""
            
                attr_and_value = attr_or_dict
                command = f'{method} {classname} {uid} {attr_and_value}'
                self.onecmd(command)
                return command
        else:
            # Handle commands that are not 'update' or have no arguments
            command = f'{method} {classname} {arguments}'
            self.onecmd(command)
            return command
        

    def refresh_instance_data(self, classname, uid, s_dict):
        try:
            if not classname:
                raise ValueError("** class name missing **")
            if classname not in storage.classes():
                raise ValueError("** class doesn't exist **")
            if uid is None:
                raise ValueError("** instance id missing **")

            key = f"{classname}.{uid}"
            instance = storage.all().get(key)
            if instance is None:
                raise ValueError("** no instance found **")

            d = json.loads(s_dict.replace("'", '"'))
            attributes = storage.attributes().get(classname, {})

            for attribute, value in d.items():
                if attribute in attributes:
                    converted_value = attributes[attribute](value)
                    setattr(instance, attribute, converted_value)

            instance.save()
        except ValueError as e:
            print(e)

    def do_quit(self, cmd_text):
        """  """
        return True
    
    def emptyline(self):
        """  """
        pass

    def do_EOF(self, cmd_text):
        """  """
        print()
        return True
    

    def do_create(self, cmd_text):
        """  """
        if not cmd_text:
            return print("** class name missing **")
        if cmd_text not in storage.classes():
            return print("** class doesn't exist **")
    
        instance = storage.classes()[cmd_text]()
        instance.save()
        print(instance.id)


    def do_show(self, cmd_text):
        """  """
        if not cmd_text:
            print("** class name missing **")
            return
        words = cmd_text.split(' ')
        if words[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print("** instance id missing **")
            return

        key = f"{words[0]}.{words[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])



    def do_all(self, cmd_text):
        """  """
        if cmd_text and cmd_text not in storage.classes():
            print("** class doesn't exist **")
            return

        if cmd_text:
            instances = [str(obj) for obj in storage.all().values() if type(obj).__name__ == cmd_text]
        else:
            instances = [str(obj) for obj in storage.all().values()]
    
        print(instances)



    def do_destroy(self, cmd_text):
        """  """
        if not (cmd_text := cmd_text.strip()):
            print("** class name missing **")
            return

        words = cmd_text.split(' ')
        if not (class_name := words[0]) in storage.classes():
            print("** class doesn't exist **")
            return

        if len(words) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{words[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()



    def do_update(self, cmd_text):
        """   """
        if not cmd_text:
            print("** class name missing **")
            return

        parts = cmd_text.split()
        if len(parts) < 1:
            print("** class name missing **")
            return
        classname = parts[0]

        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(parts) < 2:
            print("** instance id missing **")
            return
        uid = parts[1]

        if len(parts) < 3:
            print("** attribute name missing **")
            return
        attribute = parts[2]

        if len(parts) < 4:
            print("** value missing **")
            return
        value = ' '.join(parts[3:]).strip('"')

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return

        cast = None
        if '.' in value:
            try:
                value = float(value)
            except ValueError:
                pass
        else:
            try:
                value = int(value)
            except ValueError:
                pass

        setattr(storage.all()[key], attribute, value)
        storage.all()[key].save()
        print(f"Attribute {attribute} updated to {value} in {classname} {uid}.")

    def do_count(self, cmd_text):
        """  """
        words = cmd_text.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
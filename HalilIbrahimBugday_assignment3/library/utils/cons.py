# CENG 487 Assignment3 by
# Halil İbrahim Buğday
# StudentId: 280201094
# 12 2023


message_type_of = "'{name}' invalid type: {class_names}"
message_one_of = "'{name}' invalid value {values}"
message_number = "'{name}' invalid name"

def type_of(o: object, name: str, types: list, message: str = message_type_of):
    if not type(o) in types:
        class_names = ", ".join(map(lambda cls: cls.__name__, types))
        raise TypeError(message.format(name=name, class_names=class_names))

def one_of(o: object, name: str, values: list, message: str = message_one_of):
    if not o in values:
        raise TypeError(message.format(name=name, values=values))

def number(o: object, name: str, message: str = message_number):
    type_of(o, name, [float, int], message)

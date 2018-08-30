def camel_to_snake(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(camel_to_snake('python_exercises'))


def print_arg(arguments):
 strlen = len(arguments)
 if strlen == 0:
     singular_plural = "arguments."
 elif strlen == 1:
    singular_plural = "argument:"
 elif strlen > 1:
    singular_plural = "arguments:"
 print("{} {} " .format(strlen, singular_plural))
 for i, arg in enumerate(arguments, start = 1):
    print("{}: {}" .format(i, arg))

if __name__ == "__main__":
 arguments = input().split()
 print_arg(arguments)
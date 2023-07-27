def print_args(arguments):
    num_arguments = len(arguments)
    if num_arguments == 0:
        singular_plural = "arguments."
    elif num_arguments == 1:
        singular_plural = "argument:"
    elif num_arguments > 1:
        singular_plural = "arguments:"

    print("{} {}".format(num_arguments, singular_plural))

    if num_arguments > 0:
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    arguments = [1, 2, 3]  # Example list of arguments
    print_args(arguments)


def main(argv):
  # Get the number of arguments
  number_of_arguments = len(argv)

  # Print the number of arguments
  print("Number of arguments:", number_of_arguments)

  # If there are no arguments, print a message and exit
  if number_of_arguments == 0:
    print("No arguments.")
    return

  # Print the list of arguments
  for index, argument in enumerate(argv):
    print(f"{index + 1}: {argument}")


if __name__ == "__main__":
  argv = input()
  main(argv)
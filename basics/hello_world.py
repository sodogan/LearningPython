print("Hello, World!")


def main():
    print("   /|")
    print("  / |")
    print(" /  |")
    print("/___|")



# Когда интерпретатор Python читает исходный файл, он исполняет весь найденный в нем код.
# Перед тем, как начать выполнять команды, он определяет несколько специальных переменных.
# Например, если интерпретатор запускает некоторый модуль (исходный файл) как основную программу,
# он присваивает специальной переменной __name__ значение "__main__". Если этот файл импортируется
# из другого модуля, переменной __name__ будет присвоено имя этого модуля.

# If python interpreter is running this code and it has assigned this file's variable __name__ to "__main__",
# then run this code (this program is executed as main program / not an included program)
if __name__ == "__main__":
    main()

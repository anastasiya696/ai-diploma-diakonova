from user_menu import show_menu, run_choice


def main():
    while True:
        show_menu()
        choice = input("👉 Введите номер действия: ")

        run_choice(choice)

        if choice == "0":
            break


if __name__ == "__main__":
    main()
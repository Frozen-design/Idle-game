from screens import *

def main():
    test_window = Window(1000, 1000)
    manager = ScreenManager(test_window)
    manager.run_current_screen()

if __name__ == "__main__":
    main()
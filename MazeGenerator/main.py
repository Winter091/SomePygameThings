try:
    from MazeGenerator.Core import Core
except ImportError:
    from Core import Core

if __name__ == '__main__':
    Core = Core()
    Core.main_loop()

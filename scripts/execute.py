import subprocess
import sys
import os


def execute(configuration: str) -> None:
    for file in os.listdir(f"./build/{configuration}/"):
        if file.endswith('.exe'):
            executable_name = file

    os.chdir(f"./build/{configuration}/")
    subprocess.run((executable_name))


def main():
    execute(sys.argv[1])


if __name__ == '__main__':
    main()

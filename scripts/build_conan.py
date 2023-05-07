import subprocess


def run_conan():
    subprocess.run((
        'conan', 'install', '.',
        '--output-folder=./build',
        '--build=missing'
    ))


def main():
    run_conan()


if __name__ == '__main__':
    main()

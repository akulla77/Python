import os

from pathlib import Path


def __build_ui_files_from(directory: Path):
    for path in directory.glob('*.ui'):
        basename = path.name.split('.')[0]
        ui_file = Path(f'Ui_{basename}_test.py')

        os.system(f'pyside6-uic {path} -o {directory.joinpath(ui_file)}')


if __name__ == '__main__':
    __build_ui_files_from(Path(__file__).parent)
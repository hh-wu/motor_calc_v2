import argparse
import sys

import toml
import pathlib
from loguru import logger


def load_model(filename):
    return toml.load(filename)


def calc(infile, model):
    infile_path = pathlib.Path(infile)
    infile_results_path = infile_path.parent / f'{infile_path.name}.results'
    infile_results_path.mkdir(parents=True, exist_ok=True)
    logger.debug('model content:')
    logger.debug(model)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)

    args = parser.parse_args()
    infile_path = pathlib.Path(args.infile.name)
    logger.info(f'Input model file is "{infile_path.absolute()}"')
    model = load_model(infile_path)
    calc(infile_path, model)

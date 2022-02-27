from dataclasses import dataclass
from enum import Enum


class Config:
    def __init__(self, image_dir: str, out_dir: str, verbose: bool):
        self.image_dir = image_dir
        self.out_dir = out_dir
        self.verbose = verbose

    def __repr__(self):
        return f'Config(image_dir={self.image_dir}, out_dir={self.out_dir}, verbose={self.verbose})'

    @classmethod
    def from_parsed_args(cls, p):
        """
        Builds a Config from the given parsed args
        :param p: The parsed args
        :return: Config
        """
        return Config(image_dir=p.image_dir, out_dir=p.out_dir, verbose=p.verbose)

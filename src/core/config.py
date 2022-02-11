from dataclasses import dataclass
from enum import Enum


class Config:
    def __init__(self, image, model, name, train, out='./out/', epochs=10):
        self.name = name
        self.out = out
        self.train = train
        self.epochs = epochs
        self.model = model
        self.image = image

        # Bool casts due to python short-circuiting None-types.
        self.is_image_mode = bool(self.image and not self.train)
        self.is_train_mode = bool(self.train and not self.image)
        if self.is_image_mode == self.is_train_mode:
            raise ValueError('Invalid config. Training mode and image mode must be opposite. '
                             f'Current configuration: Image Mode: {self.is_image_mode} | Train Mode: {self.is_train_mode}')

    def __repr__(self):
        return f'Config(image={self.image}, model={self.model}, name={self.name}, train={self.train}, ' \
               f'epochs={self.epochs}, out={self.out}) | [Image Mode: {self.is_image_mode}]'


    @classmethod
    def from_parsed_args(cls, p):
        """
        Builds a Config from the given parsed args
        :param p: The parsed args
        :return: Config
        """
        return Config(image=p.image, model=p.model, name=p.name, out=p.out, train=p.train, epochs=p.epochs)

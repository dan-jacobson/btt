"""
Contains the Game class, as well as various simple network architectures.
"""

import numpy as np

import torch
from torch import nn


class Game:
    def __init__(self, model, points, board):
        self.model = model
        self.STARTING_POINTS = points
        self.board = board

    
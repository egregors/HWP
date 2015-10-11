# -*- coding: utf-8 -*-
"""
    HWP Core module
    ~~~~~~~~~~~~~~~
    ver.: 0.0.1

    Docstring...
    todo: this
"""
from __future__ import unicode_literals, print_function
from config import ANGLE, NODES_IN_WHEEL, BEGIN_POSITION
import matplotlib.pyplot as plt
import warnings
import numpy as np
import os

warnings.filterwarnings("ignore")

__author__ = '@egregors'


class ChainLengthExeption(Exception):
    pass


class Protein(object):
    def __init__(self, name=None, amino_acids=None):
        self.name = name
        self.amino_acids = amino_acids

        super(Protein, self).__init__()

    def __repr__(self):
        return ' '.join(['[{}]: '.format(__name__),
                         self.name,
                         ':',
                         self.amino_acids])

    def show(self):
        print(self.__repr__())


class ProteinSequence(object):
    def __init__(self, file_name=None, save_to=os.path.join(os.getcwd(), 'output/out.png')):
        self.save_to = save_to
        self.file_name = file_name if file_name is not None else None
        if self.file_name is not None:
            self.seq = []
            with open(self.file_name) as f:
                for line in f.readlines():
                    protein = Protein(name=line.split()[0],
                                      amino_acids=line.split()[1])
                    protein.show()
                    self.seq.append(protein)
            print('* * *')
            print('[{}]: Loaded {} proteins'.format(__name__, len(self.seq)))
        else:
            self.seq = None
        self.variability = []
        self.create_variability_vector()
        self.make_plot()
        super(ProteinSequence, self).__init__()

    def print_seq(self):
        """ For debug
        :return: None
        """
        if self.seq:
            for protein in self.seq:
                print(protein)

    def create_variability_vector(self):
        if self.seq:
            chain_length = len(self.seq[0].amino_acids)
            for protein in self.seq:
                if len(protein.amino_acids) != chain_length:
                    raise ChainLengthExeption(
                        'Number of all position in amino acids should be equal each other')

            for idx in range(chain_length):
                self.variability.append(
                    len(
                        set([protein.amino_acids[idx] for protein in self.seq]) - set('-')
                    ) - 1
                )

            print('[{}]: Variability vector = {}'.format(__name__, self.variability))

    def make_plot(self):

        if len(self.variability) != 0:

            radius_list = []
            nodes = []
            radius = 5
            area = 1200
            color = 'y'  # yellow

            print('[{}]: Creating plot...'.format(__name__))
            plt.subplot(111, polar=True)
            plt.title('HWP - {}'.format(self.file_name))
            plt.axis('off')

            variability_wheel = [x * 0 for x in range(NODES_IN_WHEEL)]

            for position, node in enumerate(self.variability):

                if position % NODES_IN_WHEEL == 0:
                    radius += 3

                radius_list.append(radius)
                nodes.append(BEGIN_POSITION + ANGLE * position * -1)
                plt.text(BEGIN_POSITION + ANGLE * position * -1, radius, position + 1)

            wheels_in_seq = int(len(self.variability) / NODES_IN_WHEEL)

            for pos in range(wheels_in_seq + 1):
                if pos != wheels_in_seq - 1:
                    tail = self.variability[:NODES_IN_WHEEL]
                    for idx in range(len(tail)):
                        variability_wheel[idx] += tail[idx]
                else:
                    tail = self.variability[wheels_in_seq * NODES_IN_WHEEL:]
                    for idx in range(len(tail)):
                        variability_wheel[idx] += tail[idx]

            for position, node in enumerate(variability_wheel):
                plt.text(BEGIN_POSITION + ANGLE * position * -1, radius + 3, node)

            print('[{}]: AVG variability vector = {}'.format(__name__, variability_wheel))

            plt.scatter(x=nodes, y=radius_list, s=area, c=color)

            M = variability_wheel.index(max(variability_wheel))

            # TODO: Calc arrow
            plt.arrow(
                0, 0,
                BEGIN_POSITION + M * ANGLE * -1,  # angle
                5,  # length
            )

            desc = '''
            var: {variability}
            '''.format(variability=variability_wheel)
            plt.text(19 * np.pi / 16, 33, desc)

            plt.savefig(self.save_to)
            print('[{}]: Save image into {}'.format(__name__, self.save_to))

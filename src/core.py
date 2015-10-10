# -*- coding: utf-8 -*-
"""
    HWP Core module
    ~~~~~~~~~~~~~~~
    ver.: 0.0.1

    Docstring...
    todo: this
"""
from __future__ import unicode_literals, print_function

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
    def __init__(self, file_name=None):
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

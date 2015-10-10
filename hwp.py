# -*- coding: utf-8 -*-
"""
    [HWP] Helical Wheel Painter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ver.: 0.0.1

    Documentation...
"""
from __future__ import unicode_literals, print_function
from optparse import OptionParser

from src.core import ProteinSequence

__author__ = '@egregors'

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="...", metavar="FILE")

    (options, args) = parser.parse_args()

    if options.filename is not None:
        print('[{}]: Load sequence from: {}'.format(__name__, options.filename))
        print('* * *')
        protein_req = ProteinSequence(file_name=options.filename)

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
                      help="path to file with protein group", metavar="FILE")
    parser.add_option("-s", "--save", dest="path_to_save",
                      help="path to save image (default: ./output/out.png)", metavar="PATH")

    (options, args) = parser.parse_args()

    if options.filename is not None:
        print('[{}]: Load sequence from: {}'.format(__name__, options.filename))
        print('* * *')
        if options.path_to_save is not  None:
            protein_req = ProteinSequence(file_name=options.filename, save_to=options.path_to_save)
        else:
            protein_req = ProteinSequence(file_name=options.filename)
    else:
        print('python hwp.py -h')
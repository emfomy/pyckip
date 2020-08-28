#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

from _base import *

def test_classic_constituency_parser():
    obj = CkipPipeline(constituency_parser='classic')
    doc = CkipDocument(ws=SegParagraph.from_list(ws), pos=SegParagraph.from_list(pos))
    obj.get_conparse(doc)
    assert doc.conparse.to_list() == conparse

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Convert reduced frames into the standard GALAH FITS format. """

__author__ = "Andy Casey <arc@ast.cam.ac.uk>"

from .iraf import from_iraf
from .tdfdr import from_2dfdr

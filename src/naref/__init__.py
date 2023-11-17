#!/usr/bin/env python
# Copyright 2023 NAREF Development Team
#
# Unless required by applicable law or agreed to in writing, this software
# is on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.

"""A quantum & classical reservoir handler for Temporal Series Prediction."""

from naref.dataset import data
from naref.demo import fastest_hs
from naref.classical.crc import CRC
from naref.classical.hyper import HyperC
from naref.quantum.qrc import QRC
from naref.quantum.hyper import HyperQ
from naref.comp import Comparator

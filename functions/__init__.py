#!/usr/bin/env python
"""
    __init__.py - init for funnybot functions.
    Copyright (C) 2011-2013  The FunnyBot Team

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

import os

#define files imported by the '*' option.
__all__ = list(set([os.path.splitext(file)[0] for file in os.listdir(os.path.join(os.getcwd(),'functions')) if '__' not in os.path.splitext(file)[0] and ('.py' ==  os.path.splitext(file)[1].lower() or '.pyc' ==  os.path.splitext(file)[1].lower())]))

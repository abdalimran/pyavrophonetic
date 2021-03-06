#!/usr/bin/env python
"""Provides configurations for pyAvroPhonetic.

-----------------------------------------------------------------------

Copyright (C) 2013 Kaustav Das Modak <kaustav.dasmodak@yahoo.co.in.

This file is part of pyAvroPhonetic.

pyAvroPhonetic is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyAvroPhonetic is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyAvroPhonetic.  If not, see <http://www.gnu.org/licenses/>.

"""

# Imports
import json
import io
import pkgutil
 
# Constants
AVRO_DICT_FILE = pkgutil.get_data(__name__, "resources/avrodict.json")

# -- Loads json data from avrodict.json
AVRO_DICT = json.loads(AVRO_DICT_FILE)

# -- Shortcut to vowels
AVRO_VOWELS = set(AVRO_DICT['data']['vowel'])

# -- Shortcut to consonants
AVRO_CONSONANTS = set(AVRO_DICT['data']['consonant'])

# -- Shortcut to case-sensitives
AVRO_CASESENSITIVES = set(AVRO_DICT['data']['casesensitive'])

# -- Shortcut to number
AVRO_NUMBERS = set(AVRO_DICT['data']['number'])

#!/usr/bin/python
#
# Copyright (c) 2013-2014 Pavol Rusnak <stick@gk2.sk>
#
# This file is part of Coinmap
#
# Coinmap is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
import json
import json.encoder
from overpass import parser as overpass_parser

scriptdir = os.path.dirname(os.path.abspath(__file__))

coins = {
	'Bitcoin': 'XBT',
}

parsers = {
	'overpass': overpass_parser,
}

json.encoder.FLOAT_REPR = lambda x: str(x) # fix for 52.1989256 showing as 52.198925299999999

# update data/currencies
with open(scriptdir + '/coins.js', 'w') as f:
	f.write('function get_coins() { return ["%s"]; }\n' % '", "'.join(sorted(coins.keys())))

# call individual parsers
for name, parser in parsers.iteritems():
	for coin in coins:
		coinlower = coin.lower()
		pts = parser.get_points(coinlower, coins[coin])
		json.dump(pts, open(scriptdir + '/data-%s-%s.json' % (name, coinlower), 'w'), separators = (',', ':'))
		for split in range(10):
			pts_split = [ x for x in pts if int(x['lon']) % 10 == split ]
			json.dump(pts_split, open(scriptdir + '/data-%s-%s-%d.json' % (name, coinlower, split), 'w'), separators = (',', ':'))

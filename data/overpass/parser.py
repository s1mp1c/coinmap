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

import requests

icon_mapping = {
'aeroway:aerodrome': 'transport_airport',
'aeroway:gate': 'transport_airport_gate',
'aeroway:helipad': 'transport_helicopter_pad',
'aeroway:terminal': 'transport_airport_terminal',
'amenity:atm': 'money_atm',
'amenity:bank': 'money_bank',
'amenity:bar': 'food_bar',
'amenity:bbq': 'tourist_picnic',
'amenity:bench': 'amenity_bench',
'amenity:bicycle_parking': 'transport_parking_bicycle',
'amenity:bicycle_rental': 'transport_rental_bicycle',
'amenity:bus_station': 'transport_bus_station',
'amenity:cafe': 'food_cafe',
'amenity:car_rental': 'transport_rental_car',
'amenity:cinema': 'tourist_cinema',
'amenity:college': 'education_university',
'amenity:drinking_water': 'food_drinkingtap',
'amenity:fast_food': 'food_fastfood',
'amenity:ferry_terminal': 'transport_port',
'amenity:fire_station': 'amenity_firestation',
'amenity:fountain': 'amenity_fountain',
'amenity:fuel': 'transport_fuel',
'amenity:grave_yard': 'amenity_place_of_worship',
'amenity:hospital': 'health_hospital',
'amenity:hunting_stand': 'sport_shooting',
'amenity:kindergarten': 'education_nursery',
'amenity:library': 'amenity_library',
'amenity:marketplace': 'shopping_marketplace',
'amenity:nightclub': 'food_bar',
'amenity:parking': 'transport_parking_car',
'amenity:pharmacy': 'health_pharmacy',
'amenity:place_of_worship': 'amenity_place_of_worship',
'amenity:police': 'amenity_police',
'amenity:post_box': 'amenity_post_box',
'amenity:post_office': 'amenity_post_office',
'amenity:pub': 'food_pub',
'amenity:recycling': 'amenity_recycling',
'amenity:restaurant': 'food_restaurant',
'amenity:school': 'education_school',
'amenity:shelter': 'accommodation_shelter',
'amenity:swimming_pool': 'sport_swimming_outdoor',
'amenity:taxi': 'transport_taxi_rank',
'amenity:telephone': 'amenity_telephone',
'amenity:theatre': 'tourist_theatre',
'amenity:toilets': 'amenity_toilets',
'amenity:townhall': 'amenity_town_hall',
'amenity:university': 'education_university',
'amenity:vending_machine': 'shopping_vending_machine',
'amenity:veterinary': 'health_veterinary',
'amenity:waste_basket': 'amenity_waste_bin',
'amenity:waste_disposal': 'amenity_waste_bin',
'barrier:block': 'barrier_blocks',
'barrier:bollard': 'barrier_bollard',
'barrier:cattle_grid': 'barrier_cattle_grid',
'barrier:cycle_barrier': 'barrier_cycle_barrier',
'barrier:gate': 'barrier_gate',
'barrier:kissing_gate': 'barrier_kissing_gate',
'barrier:lift_gate': 'barrier_lift_gate',
'barrier:stile': 'barrier_stile',
'barrier:toll_booth': 'barrier_toll_booth',
'boundary:administrative': 'poi_boundary_administrative',
'highway:bus_stop': 'transport_bus_stop',
'highway:crossing': 'transport_zebra_crossing',
'highway:mini_roundabout': 'transport_miniroundabout_anticlockwise',
'highway:turning_circle': 'transport_turning_circle',
'highway:service': 'transport_fuel',
'historic:archaeological_site': 'tourist_archaeological',
'historic:battlefield': 'tourist_battlefield',
'historic:castle': 'tourist_castle',
'historic:memorial': 'tourist_memorial',
'historic:monument': 'tourist_monument',
'historic:ruins': 'tourist_ruin',
'landuse:cemetery': 'amenity_place_of_worship',
'landuse:farmland': 'landuse_grass',
'landuse:farm': 'landuse_grass',
'landuse:farmyard': 'landuse_grass',
'landuse:forest': 'landuse_coniferous',
'landuse:meadow': 'landuse_grass',
'landuse:military': 'poi_military_bunker',
'landuse:orchard': 'landuse_grass',
'landuse:quarry': 'poi_mine',
'landuse:vineyard': 'landuse_grass',
'leisure:golf_course': 'sport_golf',
'leisure:marina': 'transport_marina',
'leisure:pitch': 'sport_leisure_centre',
'leisure:playground': 'amenity_playground',
'leisure:recreation_ground': 'sport_leisure_centre',
'leisure:slipway': 'transport_slipway',
'leisure:sports_centre': 'sport_leisure_centre',
'leisure:stadium': 'sport_stadium',
'leisure:track': 'sport_leisure_centre',
'natural:wood': 'landuse_coniferous',
'place:city': 'poi_place_city',
'place:hamlet': 'poi_place_hamlet',
'place:neighbourhood': 'poi_place_suburb',
'place:suburb': 'poi_place_suburb',
'place:town': 'poi_place_town',
'place:village': 'poi_place_village',
'power:pole': 'power_tower_low',
'power:station': 'power_substation',
'power:sub_station': 'power_transformer',
'power:tower': 'power_tower_high',
'public_transport:station': 'transport_bus_station',
'railway:station': 'transport_train_station',
'railway:tram_stop': 'transport_tram_stop',
'shop:alcohol': 'shopping_alcohol',
'shop:bakery': 'shopping_bakery',
'shop:bicycle': 'shopping_bicycle',
'shop:books': 'shopping_book',
'shop:butcher': 'shopping_butcher',
'shop:car_repair': 'shopping_car_repair',
'shop:car': 'shopping_car',
'shop:clothes': 'shopping_clothes',
'shop:computer': 'shopping_computer',
'shop:confectionery': 'shopping_confectionery',
'shop:convenience': 'shopping_convenience',
'shop:department_store': 'shopping_department_store',
'shop:doityourself': 'shopping_diy',
'shop:fishmonger': 'shopping_fish',
'shop:florist': 'shopping_florist',
'shop:garden_centre': 'shopping_garden_centre',
'shop:general': 'shopping_convenience',
'shop:gift': 'shopping_gift',
'shop:greengrocer': 'shopping_greengrocer',
'shop:hairdresser': 'shopping_hairdresser',
'shop:hifi': 'shopping_hifi',
'shop:jewelry': 'shopping_jewelry',
'shop:kiosk': 'shopping_kiosk',
'shop:laundry': 'shopping_laundrette',
'shop:mall': 'shopping_department_store',
'shop:mobile_phone': 'shopping_mobile_phone',
'shop:motorcycle': 'shopping_motorcycle',
'shop:music': 'shopping_music',
'shop:pastry': 'shopping_confectionery',
'shop:newsagent': 'shopping_newspaper',
'shop:supermarket': 'shopping_supermarket',
'shop:toys': 'shopping_toys',
'tourism:alpine_hut': 'accommodation_alpinehut',
'tourism:artwork': 'tourist_art_gallery',
'tourism:attraction': 'tourist_attraction',
'tourism:camp_site': 'accommodation_camping',
'tourism:caravan_site': 'accommodation_caravan_park',
'tourism:chalet': 'accommodation_chalet',
'tourism:guest_house': 'accommodation_bed_and_breakfast',
'tourism:hostel': 'accommodation_youth_hostel',
'tourism:hotel': 'accommodation_hotel',
'tourism:motel': 'accommodation_motel',
'tourism:museum': 'tourist_museum',
'tourism:picnic_site': 'tourist_picnic',
'tourism:theme_park': 'tourist_theme_park',
'tourism:viewpoint': 'tourist_view_point',
'tourism:zoo': 'tourist_zoo',
'traffic_calming:yes': 'transport_speedbump',
}

nodes = {}
ways = {}

def determine_icon(tags, coin = 'bitcoin'):
	icon = '_' + coin
	for kv in icon_mapping:
		k,v = kv.split(':')
		t = tags.get(k)
		if not t:
			continue
		t = t.split(';')[0]
		if t == v:
			icon = icon_mapping[kv]
			break
	icon = icon.replace('-', '_')
	return icon

def get_points(coin = 'bitcoin', iso = 'XBT'):
	points = []
	resp = requests.get('http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];(node["payment:%s"=yes];>;way["payment:%s"=yes];>;relation["payment:%s"=yes];>;node["currency:%s"=yes];>;way["currency:%s"=yes];>;relation["currency:%s"=yes];);out;' % (coin, coin, coin, iso, iso, iso)).json()
	print len(resp['elements'])
	for e in resp['elements']:
		lat = e.get('lat', None)
		lon = e.get('lon', None)
		typ = e['type']
		tags = e.get('tags', {})
		ide = e['id']

		if typ == 'node':
			nodes[ide] = (lat, lon)
			if tags.get('payment:%s' % coin) != 'yes' and tags.get('currency:%s' % iso) != 'yes': # nodes that are part of way (i.e. not accepting coins)
				continue

		elif typ == 'way':
			try:
				lat, lon = nodes[e['nodes'][0]] # extract coordinate of first node
			except:
				continue
			ways[ide] = (lat, lon)
			if tags.get('payment:%s' % coin) != 'yes' and tags.get('currency:%s' % iso) != 'yes': # ways that are part of relation
				continue

		elif typ == 'relation':
			try:
				lat, lon = ways[e['members'][0]['ref']]
			except:
				continue

		if not lat or not lon:
			continue

		if 'name' in tags:
			name = tags['name']
		else:
			name = '%s %s' % (typ, ide)

		icon = determine_icon(tags, coin)
		point = {'lat': lat, 'lon': lon, 'title': name, 'id': ide, 'type': typ, 'icon': icon}

		if 'addr:street' in tags:
			point['addr'] = '%s %s' % (tags.get('addr:street', ''), tags.get('addr:housenumber', ''))
		if 'addr:city' in tags:
			point['city'] = '%s %s' % (tags.get('addr:postcode', ''), tags.get('addr:city', ''))
		if 'addr:country' in tags:
			point['country'] = tags.get('addr:country', '')
		if 'contact:website' in tags:
			w = tags['contact:website']
			if w.startswith('http://') or w.startswith('https://'):
				point['web'] = w
		elif 'website' in tags:
			w = tags['website']
			if w.startswith('http://') or w.startswith('https://'):
				point['web'] = w
		if 'contact:email' in tags:
			point['email'] = tags['contact:email']
		elif 'email' in tags:
			point['email'] = tags['email']
		if 'contact:phone' in tags:
			point['phone'] = tags['contact:phone']
		elif 'phone' in tags:
			point['phone'] = tags['phone']
		if 'description' in tags:
			point['desc'] = tags['description']

		points.append(point)

	return points

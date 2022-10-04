fish_avail_times = {
    # 4am - 9pm, aka 4:00 - 21:00
    '4 AM – 9 PM': list(range(4, 21)),

    # 9am - 4pm, aka 9:00 - 16:00
    '9 AM –\xa04 PM': list(range(9, 16)),

    # 4pm - 9am, aka 16:00 - 9:00
    '4 PM –\xa09 AM': list(range(16, 24)) + list(range(0, 9)),

    # 9pm - 4am, aka 21:00 - 4:00
    '9 PM –\xa04 AM': list(range(21, 24)) + list(range(0, 4)),

    # piranha: 9am - 4pm and 9pm - 4am
    '9 AM –\xa04 PM; 9 PM – 4 AM': list(range(9, 16)) + list(range(21, 24)) + list(range(0, 4)),

    # all day, functionally 0:00 - 24:00
    'All day': list(range(0, 24)),
}

fish_icon_dict = {
    'anchovy': 'Fish81',
    'angelfish': 'Fish30',
    'arapaima': 'Fish36',
    'arowana': 'Fish33',
    'barred knifejaw': 'Fish47',
    'barreleye': 'Fish84',
    'betta': 'Fish77',
    'bitterling': 'Fish0',
    'black bass': 'Fish19',
    'blowfish': 'Fish73',
    'blue marlin': 'Fish58',
    'bluegill': 'Fish17',
    'butterfly fish': 'Fish42',
    'carp': 'Fish5',
    'catfish': 'Fish14',
    'char': 'Fish24',
    'cherry salmon': 'Fish23',
    'clown fish': 'Fish40',
    'coelacanth': 'Fish63',
    'crawfish': 'Fish10',
    'crucian carp': 'Fish2',
    'dab': 'Fish50',
    'dace': 'Fish3',
    'dorado': 'Fish34',
    'football fish': 'Fish56',
    'freshwater goby': 'Fish12',
    'frog': 'Fish11',
    'gar': 'Fish35',
    'giant snakehead': 'Fish16',
    'giant trevally': 'Fish70',
    'golden trout': 'Fish79',
    'goldfish': 'Fish7',
    'great white shark': 'Fish62',
    'guppy': 'Fish29',
    'hammerhead shark': 'Fish61',
    'horse mackerel': 'Fish46',
    'killifish': 'Fish9',
    'king salmon': 'Fish28',
    'koi': 'Fish6',
    'loach': 'Fish13',
    'mahi-mahi': 'Fish82',
    'mitten crab': 'Fish66',
    'moray eel': 'Fish55',
    'Napoleonfish': 'Fish43',
    'neon tetra': 'Fish31',
    'nibble fish': 'Fish67',
    'oarfish': 'Fish69',
    'ocean sunfish': 'Fish60',
    'olive flounder': 'Fish51',
    'pale chub': 'Fish1',
    'pike': 'Fish20',
    'piranha': 'Fish32',
    'pond smelt': 'Fish21',
    'pop-eyed goldfish': 'Fish8',
    'puffer fish': 'Fish45',
    'rainbowfish': 'Fish80',
    'ranchu goldfish': 'Fish85',
    'ray': 'Fish59',
    'red snapper': 'Fish49',
    'ribbon eel': 'Fish71',
    'saddled bichir': 'Fish68',
    'salmon': 'Fish27',
    'saw shark': 'Fish74',
    'sea bass': 'Fish48',
    'sea butterfly': 'Fish37',
    'sea horse': 'Fish39',
    'snapping turtle': 'Fish78',
    'soft-shelled turtle': 'Fish65',
    'squid': 'Fish52',
    'stringfish': 'Fish26',
    'sturgeon': 'Fish75',
    'suckerfish': 'Fish83',
    'surgeonfish': 'Fish41',
    'sweetfish': 'Fish22',
    'tadpole': 'Fish64',
    'tilapia': 'Fish76',
    'tuna': 'Fish57',
    'whale shark': 'Fish72',
    'yellow perch': 'Fish18',
    'zebra turkeyfish': 'Fish44'
    }

bug_avail_times = {
    # all day, functionally 0:00 - 24:00
    'all': list(range(0, 24)),    
    
    # 4am - 5pm, aka 4:00 - 17:00
    '4a-5p': list(range(4, 17)),
    
    # 4am - 7pm, aka 4:00 - 19:00
    '4a-7p': list(range(4, 19)),
    
    # 8am - 4pm, aka 8:00 - 16:00
    '8a-4p': list(range(8, 16)),
    
    # 8am - 5pm, aka 8:00 - 17:00
    '8a-5p': list(range(8, 17)),
    
    # 8am - 7pm, aka 8:00 - 19:00
    '8a-7p': list(range(8, 19)),

    # 4pm - 11am, aka 16:00 - 11:00
    '4p-11a': list(range(16, 24)) + list(range(0, 11)),    
    
    # 5pm - 4am, aka 17:00 - 4:00
    '5p-4a': list(range(17, 24)) + list(range(0, 4)),
    
    # 5pm - 8am, aka 17:00 - 8:00
    '5p-8a': list(range(17, 24)) + list(range(0, 8)),
    
    # 7pm - 4am, aka 19:00 - 4:00
    '7p-4a': list(range(19, 24)) + list(range(0, 4)),
    
    # 7pm - 8am, aka 19:00 - 8:00
    '7p-8a': list(range(19, 24)) + list(range(0, 8)),

    # 11pm - 8am, aka 23:00 - 8:00
    '11p-8a': list(range(23, 24)) + list(range(0, 8)),

    # 11pm - 4pm, aka 23:00 - 16:00
    '11p-4p': list(range(23, 24)) + list(range(0, 16)),
    
    # evening cicada: 4am - 8am and 4pm - 7pm
    '4a-8a-4p-7p': list(range(4, 8)) + list(range(16, 19)),
    
    # walking stick: 4am - 8am and 5pm - 7pm
    '4a-8a-5p-7p': list(range(4, 8)) + list(range(17, 19)),
}

bug_icon_dict = {
    'Agrias Butterfly': 'Ins6',
    'Ant': 'Ins26',
    'Atlas Moth': 'Ins10',
    'Bagworm': 'Ins36',
    'Banded Dragonfly': 'Ins24',
    'Bell Cricket': 'Ins31',
    'Blue Weevil Beetle': 'Ins80',
    'Brown Cicada': 'Ins17',
    'Centipede': 'Ins60',
    'Cicada Shell': 'Ins69',
    'Citrus Long-horned Beetle': 'Ins39',
    'Common Bluebottle': 'Ins72',
    'Common Butterfly': 'Ins0',
    'Cricket': 'Ins30',
    'Cyclommatus Stag': 'Ins49',
    'Damselfly': 'Ins81',
    'Darner Dragonfly': 'Ins23',
    'Diving Beetle': 'Ins28',
    'Drone Beetle': 'Ins75',
    'Dung Beetle': 'Ins40',
    'Earth-boring Dung Beetle': 'Ins42',
    'Emperor Butterfly': 'Ins5',
    'Evening Cicada': 'Ins20',
    'Firefly': 'Ins41',
    'Flea': 'Ins56',
    'Fly': 'Ins59',
    'Giant Cicada': 'Ins65',
    'Giant Stag': 'Ins47',
    'Giant Water Bug': 'Ins76',
    'Giraffe Stag': 'Ins77',
    'Golden Stag': 'Ins50',
    'Goliath Beetle': 'Ins55',
    'Grasshopper': 'Ins32',
    'Great Purple Emperor': 'Ins74',
    'Hermit Crab': 'Ins66',
    'Honeybee': 'Ins11',
    'Horned Atlas': 'Ins52',
    'Horned Dynastid': 'Ins51',
    'Horned Elephant': 'Ins53',
    'Horned Hercules': 'Ins54',
    'Jewel Beetle': 'Ins44',
    'Ladybug': 'Ins37',
    'Long Locust': 'Ins13',
    'Madagascan Sunset Moth': 'Ins79',
    'Man-faced Stink Bug': 'Ins78',
    'Mantis': 'Ins15',
    'Migratory Locust': 'Ins14',
    'Miyama Stag': 'Ins46',
    'Mole Cricket': 'Ins33',
    'Monarch Butterfly': 'Ins4',
    'Mosquito': 'Ins58',
    'Moth': 'Ins9',
    'Orchid Mantis': 'Ins16',
    'Paper Kite Butterfly': 'Ins73',
    'Peacock Butterfly': 'Ins3',
    'Pill Bug': 'Ins57',
    'Pondskater': 'Ins27',
    "Queen Alexandra's Birdwing": 'Ins8',
    'Rainbow Stag': 'Ins48',
    "Rajah Brooke's Birdwing": 'Ins7',
    'Red Dragonfly': 'Ins22',
    'Rice Grasshopper': 'Ins67',
    'Robust Cicada': 'Ins18',
    'Rosalia Batesi Beetle': 'Ins82',
    'Saw Stag': 'Ins46',
    'Scarab Beetle': 'Ins43',
    'Scorpion': 'Ins63',
    'Snail': 'Ins29',
    'Spider': 'Ins61',
    'Stinkbug': 'Ins64',
    'Tarantula': 'Ins62',
    'Tiger Beetle': 'Ins70',
    'Tiger Butterfly': 'Ins2',
    'Violin Beetle': 'Ins38',
    'Walker Cicada': 'Ins19',
    'Walking Leaf': 'Ins34',
    'Walking Stick': 'Ins35',
    'Wasp': 'Ins12',
    'Wharf Roach': 'Ins71',
    'Yellow Butterfly': 'Ins1'
    }
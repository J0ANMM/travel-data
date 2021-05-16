"""Create list of dicts with time transfer between all hubs of one European city."""

transfers_raw_one_dir_DE = [
    {'city': 'DE-AAH', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-AAH', 'orig_hub': '01-1', 'dest_hub': '02-2', 'trip_duration': 14, 'freq': 15},
    {'city': 'DE-AAH', 'orig_hub': '01-1', 'dest_hub': '03-2', 'trip_duration': 16, 'freq': 15},
    {'city': 'DE-AAH', 'orig_hub': '02-2', 'dest_hub': '02-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-AAH', 'orig_hub': '02-2', 'dest_hub': '03-2', 'trip_duration': 21, 'freq': 20},
    {'city': 'DE-AAH', 'orig_hub': '03-2', 'dest_hub': '03-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-AGB', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-AGB', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 20, 'freq': 30},
    {'city': 'DE-AGB', 'orig_hub': '00-0', 'dest_hub': '02-2', 'trip_duration': 40, 'freq': 90},
    {'city': 'DE-AGB', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-AGB', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration': 20, 'freq': 60},
    {'city': 'DE-AGB', 'orig_hub': '02-2', 'dest_hub': '02-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BAB', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BAB', 'orig_hub': '00-0', 'dest_hub': '00-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BAB', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 31, 'freq': 60},
    {'city': 'DE-BAB', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 26, 'freq': 60},
    {'city': 'DE-BAB', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BAB', 'orig_hub': '01-1', 'dest_hub': '00-2', 'trip_duration': 31, 'freq': 60},
    {'city': 'DE-BAB', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BAB', 'orig_hub': '00-2', 'dest_hub': '00-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BAB', 'orig_hub': '00-2', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},

    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration': 15, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '00-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 30, 'freq':  7},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 25, 'freq':  7},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '02-0', 'trip_duration': 60, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '02-2', 'trip_duration': 50, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '03-1', 'trip_duration': 35, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '03-2', 'trip_duration': 35, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '04-2', 'trip_duration': 31, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '05-2', 'trip_duration': 16, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '06-2', 'trip_duration': 26, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '07-2', 'trip_duration': 18, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-0', 'dest_hub': '08-2', 'trip_duration': 16, 'freq': 25},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '00-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '01-1', 'trip_duration': 30, 'freq':  7},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '01-2', 'trip_duration': 25, 'freq':  7},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '02-0', 'trip_duration': 60, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '02-2', 'trip_duration': 50, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '03-1', 'trip_duration': 35, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '03-2', 'trip_duration': 35, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '04-2', 'trip_duration': 31, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '05-2', 'trip_duration': 16, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '06-2', 'trip_duration': 26, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '07-2', 'trip_duration': 18, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '00-2', 'dest_hub': '08-2', 'trip_duration': 16, 'freq': 25},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '02-0', 'trip_duration': 30, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '02-2', 'trip_duration': 30, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '03-1', 'trip_duration': 10, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '03-2', 'trip_duration': 10, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '04-2', 'trip_duration': 15, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '05-2', 'trip_duration': 25, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '06-2', 'trip_duration':  6, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '07-2', 'trip_duration':  7, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-1', 'dest_hub': '08-2', 'trip_duration': 22, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '02-0', 'trip_duration': 30, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '02-2', 'trip_duration': 30, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '03-1', 'trip_duration': 10, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '03-2', 'trip_duration': 10, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '04-2', 'trip_duration': 15, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '05-2', 'trip_duration': 25, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '06-2', 'trip_duration':  6, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '07-2', 'trip_duration':  7, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '01-2', 'dest_hub': '08-2', 'trip_duration': 22, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '02-0', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '02-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '03-1', 'trip_duration': 40, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '03-2', 'trip_duration': 40, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '04-2', 'trip_duration': 15, 'freq': 60},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '05-2', 'trip_duration': 30, 'freq': 60},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '06-2', 'trip_duration': 31, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '07-2', 'trip_duration': 36, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-0', 'dest_hub': '08-2', 'trip_duration': 46, 'freq': 40},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '02-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '03-1', 'trip_duration': 40, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '03-2', 'trip_duration': 40, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '04-2', 'trip_duration': 15, 'freq': 60},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '05-2', 'trip_duration': 30, 'freq': 60},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '06-2', 'trip_duration': 31, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '07-2', 'trip_duration': 36, 'freq': 30},
    {'city': 'DE-BER', 'orig_hub': '02-2', 'dest_hub': '08-2', 'trip_duration': 46, 'freq': 40},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '03-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '03-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '04-2', 'trip_duration': 16, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '05-2', 'trip_duration': 25, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '06-2', 'trip_duration': 10, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '07-2', 'trip_duration': 17, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '03-1', 'dest_hub': '08-2', 'trip_duration': 27, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '03-2', 'dest_hub': '03-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '03-2', 'dest_hub': '04-2', 'trip_duration': 16, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '03-2', 'dest_hub': '05-2', 'trip_duration': 25, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '03-2', 'dest_hub': '06-2', 'trip_duration': 10, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '03-2', 'dest_hub': '07-2', 'trip_duration': 17, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '03-2', 'dest_hub': '08-2', 'trip_duration': 27, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '04-2', 'dest_hub': '04-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '04-2', 'dest_hub': '05-2', 'trip_duration': 18, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '04-2', 'dest_hub': '06-2', 'trip_duration': 13, 'freq': 15},
    {'city': 'DE-BER', 'orig_hub': '04-2', 'dest_hub': '07-2', 'trip_duration': 22, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '04-2', 'dest_hub': '08-2', 'trip_duration': 43, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '05-2', 'dest_hub': '05-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '05-2', 'dest_hub': '06-2', 'trip_duration': 31, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '05-2', 'dest_hub': '07-2', 'trip_duration': 14, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '05-2', 'dest_hub': '08-2', 'trip_duration': 25, 'freq': 20},
    {'city': 'DE-BER', 'orig_hub': '06-2', 'dest_hub': '06-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '06-2', 'dest_hub': '07-2', 'trip_duration': 13, 'freq':  5},
    {'city': 'DE-BER', 'orig_hub': '06-2', 'dest_hub': '08-2', 'trip_duration': 24, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '07-2', 'dest_hub': '07-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BER', 'orig_hub': '07-2', 'dest_hub': '08-2', 'trip_duration': 21, 'freq': 10},
    {'city': 'DE-BER', 'orig_hub': '08-2', 'dest_hub': '08-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BFE', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BFE', 'orig_hub': '01-1', 'dest_hub': '02-2', 'trip_duration': 14, 'freq': 15},
    {'city': 'DE-BFE', 'orig_hub': '02-2', 'dest_hub': '02-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BOM', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BOM', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BOM', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BON', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BON', 'orig_hub': '01-1', 'dest_hub': '02-2', 'trip_duration': 13, 'freq':  5},
    {'city': 'DE-BON', 'orig_hub': '01-1', 'dest_hub': '03-2', 'trip_duration': 12, 'freq':  0},
    {'city': 'DE-BON', 'orig_hub': '02-2', 'dest_hub': '02-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BON', 'orig_hub': '02-2', 'dest_hub': '03-2', 'trip_duration': 22, 'freq': 10},
    {'city': 'DE-BON', 'orig_hub': '03-2', 'dest_hub': '03-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BWE', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BWE', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BWE', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BRE', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-BRE', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 23, 'freq': 10},
    {'city': 'DE-BRE', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 23, 'freq': 10},
    {'city': 'DE-BRE', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BRE', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BRE', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-BRV', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-BRV', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-BRV', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '00-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '00-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '02-1', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '02-2', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-0', 'dest_hub': '03-2', 'trip_duration': 42, 'freq': 30},
    {'city': 'DE-CGN', 'orig_hub': '00-1', 'dest_hub': '00-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '00-1', 'dest_hub': '00-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '00-1', 'dest_hub': '01-1', 'trip_duration': 15, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-1', 'dest_hub': '02-1', 'trip_duration': 15, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-1', 'dest_hub': '02-2', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-1', 'dest_hub': '03-2', 'trip_duration': 42, 'freq': 30},
    {'city': 'DE-CGN', 'orig_hub': '00-2', 'dest_hub': '00-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '00-2', 'dest_hub': '01-1', 'trip_duration': 15, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-2', 'dest_hub': '02-1', 'trip_duration': 15, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-2', 'dest_hub': '02-2', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '00-2', 'dest_hub': '03-2', 'trip_duration': 42, 'freq': 30},
    {'city': 'DE-CGN', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '01-1', 'dest_hub': '02-1', 'trip_duration':  5, 'freq':  5},
    {'city': 'DE-CGN', 'orig_hub': '01-1', 'dest_hub': '02-2', 'trip_duration':  5, 'freq':  5},
    {'city': 'DE-CGN', 'orig_hub': '01-1', 'dest_hub': '00-2', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '01-1', 'dest_hub': '03-2', 'trip_duration': 27, 'freq': 45},
    {'city': 'DE-CGN', 'orig_hub': '02-1', 'dest_hub': '02-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '02-1', 'dest_hub': '02-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '02-1', 'dest_hub': '00-2', 'trip_duration': 20, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '02-1', 'dest_hub': '03-2', 'trip_duration': 27, 'freq': 45},
    {'city': 'DE-CGN', 'orig_hub': '02-2', 'dest_hub': '02-2', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-CGN', 'orig_hub': '02-2', 'dest_hub': '03-2', 'trip_duration': 33, 'freq': 15},
    {'city': 'DE-CGN', 'orig_hub': '03-2', 'dest_hub': '03-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-DAR', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-DAR', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-DAR', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-DTM', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-DTM', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 27, 'freq': 60},
    {'city': 'DE-DTM', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 27, 'freq': 60},
    {'city': 'DE-DTM', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-DTM', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-DTM', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-DRS', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-DRS', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 21, 'freq': 30},
    {'city': 'DE-DRS', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 21, 'freq': 30},
    {'city': 'DE-DRS', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-DRS', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-DRS', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-DUI', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-DUI', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-DUI', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-DUS', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-DUS', 'orig_hub': '00-0', 'dest_hub': '00-1', 'trip_duration':  5, 'freq':  0},
    # {'city': 'DE-DUS', 'orig_hub': '00-0', 'dest_hub': '00-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-DUS', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 20, 'freq': 20},
    {'city': 'DE-DUS', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 20, 'freq': 20},
    {'city': 'DE-DUS', 'orig_hub': '00-1', 'dest_hub': '00-1', 'trip_duration':  0, 'freq':  0},
    # {'city': 'DE-DUS', 'orig_hub': '00-1', 'dest_hub': '00-2', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-DUS', 'orig_hub': '00-1', 'dest_hub': '01-1', 'trip_duration': 15, 'freq': 20},
    {'city': 'DE-DUS', 'orig_hub': '00-1', 'dest_hub': '01-2', 'trip_duration': 20, 'freq': 20},
    {'city': 'DE-DUS', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  0, 'freq':  0},
    {'city': 'DE-DUS', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration':  5, 'freq':  0},
    # {'city': 'DE-DUS', 'orig_hub': '01-1', 'dest_hub': '00-2', 'trip_duration': 20, 'freq': 20},
    # {'city': 'DE-DUS', 'orig_hub': '00-2', 'dest_hub': '00-2', 'trip_duration':  5, 'freq':  0},
    # {'city': 'DE-DUS', 'orig_hub': '00-2', 'dest_hub': '01-2', 'trip_duration': 20, 'freq':  0},

    {'city': 'DE-ERF', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-ERF', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 23, 'freq': 20},
    {'city': 'DE-ERF', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 23, 'freq': 20},
    {'city': 'DE-ERF', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-ERF', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-ERF', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-ERL', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-ERL', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-ERL', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-ESS', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-ESS', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-ESS', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    #taking worste case for Fraport (change of Terminal)
    {'city': 'DE-FRA', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  30, 'freq':  5}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-0', 'dest_hub': '00-1', 'trip_duration':  30, 'freq':  5}, #max. is between T2 and T1
    {'city': 'DE-FRA', 'orig_hub': '00-0', 'dest_hub': '00-2', 'trip_duration':  30, 'freq':  5}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration':  45, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration':  45, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-0', 'dest_hub': '02-1', 'trip_duration':  45, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-1', 'dest_hub': '00-2', 'trip_duration':  30, 'freq':  5}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-1', 'dest_hub': '01-1', 'trip_duration':  30, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-1', 'dest_hub': '01-2', 'trip_duration':  45, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-1', 'dest_hub': '02-1', 'trip_duration':  45, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-2', 'dest_hub': '01-1', 'trip_duration':  45, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-2', 'dest_hub': '01-2', 'trip_duration':  50, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '00-2', 'dest_hub': '02-1', 'trip_duration':  60, 'freq':  15}, #max. is between T1 and T2
    {'city': 'DE-FRA', 'orig_hub': '01-1', 'dest_hub': '02-1', 'trip_duration':  10, 'freq':  5},
    {'city': 'DE-FRA', 'orig_hub': '01-2', 'dest_hub': '02-1', 'trip_duration':  20, 'freq':  5},

    {'city': 'DE-HNH', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-HNH', 'orig_hub': '00-0', 'dest_hub': '00-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-HNH', 'orig_hub': '00-2', 'dest_hub': '00-2', 'trip_duration':  0, 'freq':  0},

    {'city': 'DE-FBG', 'orig_hub': '01-1', 'dest_hub': '01-1', 'trip_duration':  5, 'freq':  0},
    {'city': 'DE-FBG', 'orig_hub': '01-1', 'dest_hub': '01-2', 'trip_duration': 10, 'freq':  0},
    {'city': 'DE-FBG', 'orig_hub': '01-2', 'dest_hub': '01-2', 'trip_duration':  0, 'freq':  0},

    #AUTOMATIZE TIMES BETWEEN 01-1 AND 01-2



    {'city': 'DE-PAD', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration':  20, 'freq':  60},
    {'city': 'DE-PAD', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration':  20, 'freq':  60},

    {'city': 'DE-RSK', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration':  35, 'freq':  60*8}, #only 3 times per day: http://www.rebus.de/index.php?p=flughafen.htm
    {'city': 'DE-RSK', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration':  35, 'freq':  60*8},

    {'city': 'DE-STR', 'orig_hub': '00-0', 'dest_hub': '00-0', 'trip_duration':  10, 'freq':  0},

    {'city': 'DE-WZE', 'orig_hub': '00-0', 'dest_hub': '00-1', 'trip_duration':  5, 'freq': 0},
    {'city': 'DE-WZE', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration': 11, 'freq': 60},
    {'city': 'DE-WZE', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration': 11, 'freq': 60},
    {'city': 'DE-WZE', 'orig_hub': '00-0', 'dest_hub': '02-2', 'trip_duration': 25, 'freq': 60},
    {'city': 'DE-WZE', 'orig_hub': '00-1', 'dest_hub': '01-1', 'trip_duration': 11, 'freq': 60},
    {'city': 'DE-WZE', 'orig_hub': '00-1', 'dest_hub': '01-2', 'trip_duration': 11, 'freq': 60},
    {'city': 'DE-WZE', 'orig_hub': '00-1', 'dest_hub': '02-2', 'trip_duration': 25, 'freq': 60},
    {'city': 'DE-WZE', 'orig_hub': '01-1', 'dest_hub': '02-2', 'trip_duration':  6, 'freq': 30},
    {'city': 'DE-WZE', 'orig_hub': '01-2', 'dest_hub': '02-2', 'trip_duration':  6, 'freq': 30},

    ]


transfers_raw_one_dir_ES = [
    # {'city': 'ES-PMI', 'orig_hub': '01-3', 'dest_hub': '02-3', 'trip_duration':  100, 'freq':  90},

    # {'city': 'ES-MJV', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration':  70, 'freq':  60*3},
    # {'city': 'ES-MJV', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration':  70, 'freq':  60*3},

    {'city': 'ES-TCI', 'orig_hub': '00-0', 'dest_hub': '01-0', 'trip_duration':  55, 'freq':  60*2},

    {'city': 'ES-MJV', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration':  75, 'freq':  90},
    {'city': 'ES-MJV', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration':  75, 'freq':  90},

    {'city': 'ES-CAS', 'orig_hub': '00-0', 'dest_hub': '01-1', 'trip_duration':  40, 'freq':  60*5},
    {'city': 'ES-CAS', 'orig_hub': '00-0', 'dest_hub': '01-2', 'trip_duration':  40, 'freq':  60*5},
    {'city': 'ES-CAS', 'orig_hub': '00-0', 'dest_hub': '02-2', 'trip_duration':  60, 'freq':  60*5},
]


transfers_raw_one_dir_GB = [
    {'city': 'GB-LON', 'orig_hub': '00-0', 'dest_hub': '01-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '00-0', 'dest_hub': '02-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '00-0', 'dest_hub': '03-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '00-0', 'dest_hub': '04-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '00-0', 'dest_hub': '05-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '01-0', 'dest_hub': '02-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '01-0', 'dest_hub': '03-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '01-0', 'dest_hub': '04-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '01-0', 'dest_hub': '05-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '02-0', 'dest_hub': '03-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '02-0', 'dest_hub': '04-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '02-0', 'dest_hub': '05-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '03-0', 'dest_hub': '04-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '03-0', 'dest_hub': '05-0', 'trip_duration':  60*5, 'freq':  60*3},
    {'city': 'GB-LON', 'orig_hub': '04-0', 'dest_hub': '05-0', 'trip_duration':  60*5, 'freq':  60*3},
]

transfers_raw_one_dir_FR = [
    {'city': 'FR-PAR', 'orig_hub': '00-0', 'dest_hub': '01-0', 'trip_duration':  75*2, 'freq':  30},
]

transfers_raw_one_dir_IT = [
    {'city': 'IT-MIL', 'orig_hub': '00-0', 'dest_hub': '01-0', 'trip_duration':  75, 'freq':  30+20},

    {'city': 'IT-ROM', 'orig_hub': '00-0', 'dest_hub': '01-0', 'trip_duration':  130, 'freq':  60+30},
]

transfers_raw_one_dir_RU = [
    {'city': 'RU-MOW', 'orig_hub': '00-0', 'dest_hub': '01-0', 'trip_duration': 46+13+30, 'freq':  30+5+10},
    {'city': 'RU-MOW', 'orig_hub': '00-0', 'dest_hub': '02-0', 'trip_duration': 46+7+38, 'freq':  30+60+5},
    {'city': 'RU-MOW', 'orig_hub': '00-0', 'dest_hub': '03-0', 'trip_duration': 46+8+54+20, 'freq':  30+30+30+5},
    {'city': 'RU-MOW', 'orig_hub': '01-0', 'dest_hub': '02-0', 'trip_duration': 30+5+38, 'freq':  10+5+60},
    {'city': 'RU-MOW', 'orig_hub': '01-0', 'dest_hub': '03-0', 'trip_duration': 30+7+37+20, 'freq':  10+5+60+30},
    {'city': 'RU-MOW', 'orig_hub': '02-0', 'dest_hub': '03-0', 'trip_duration': 38+13+37+20, 'freq':  60+5+60+30},
]


transfers_raw_one_dir = (transfers_raw_one_dir_DE + transfers_raw_one_dir_ES + transfers_raw_one_dir_GB +
                        transfers_raw_one_dir_FR + transfers_raw_one_dir_IT + transfers_raw_one_dir_RU)

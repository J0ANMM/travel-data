    def hubs_dict(self):
        """Create list of dicts for hubs, including all hubs (airports, train stations, bus stations & ferry terminals) for all European cities with an Airport or with a population larger than 100.000 inhabitants.

            'point' digit is assigned manually and is specific for each hub.
            Each point can have more than one hub if different modes of transportation are possible in the same location. Example: airport with a train station.
        """

        flight = self.get_tm_id('flight')
        train = self.get_tm_id('train')
        bus = self.get_tm_id('bus')
        # ferry = self.get_tm_id('ferry')

        hubs_DE = [
            {'point': 1, 'city': 'DE-AAH', 'iata_code': 'XHJ', 'icao_code':  None, 'lat': 50.767920, 'lon': 6.091404, 'tm': train, 'name': 'Aachen Hbf'},
            {'point': 2, 'city': 'DE-AAH', 'iata_code':  None, 'icao_code':  None, 'lat': 50.782460, 'lon': 6.071465, 'tm': bus, 'name': 'Aachen Bf West'},
            {'point': 3, 'city': 'DE-AAH', 'iata_code':  None, 'icao_code':  None, 'lat': 50.786560, 'lon': 6.137619, 'tm': bus, 'name': 'Aachen Wilmersdorfer Strasse'},

            # {'point': 0, 'city': 'DE-AGB', 'iata_code': 'AGB', 'icao_code':'EDMA', 'lat': 48.424148, 'lon': 10.932442, 'tm': flight, 'name': 'Augsburg Airport'}, #no commercial flights since October 2017
            {'point': 1, 'city': 'DE-AGB', 'iata_code':  None, 'icao_code':  None, 'lat': 48.365444, 'lon': 10.885568, 'tm': train, 'name': 'Augsburg Hbf'},
            {'point': 2, 'city': 'DE-AGB', 'iata_code':  None, 'icao_code':  None, 'lat': 48.401731, 'lon': 10.877033, 'tm': bus, 'name': 'Augsburg Nord'},

            {'point': 0, 'city': 'DE-BAB', 'iata_code': 'FKB', 'icao_code':'EDSB', 'lat': 48.778996, 'lon': 8.090988, 'tm': flight, 'name': 'Karlsruhe Baden-Baden Airport'},
            {'point': 0, 'city': 'DE-BAB', 'iata_code':  None, 'icao_code':  None, 'lat': 48.778996, 'lon': 8.090988, 'tm': bus, 'name': 'Karlsruhe Baden-Baden Airport'},
            {'point': 1, 'city': 'DE-BAB', 'iata_code':  None, 'icao_code':  None, 'lat': 48.790201, 'lon': 8.191338, 'tm': train, 'name': 'Baden-Baden Station'},
            {'point': 1, 'city': 'DE-BAB', 'iata_code':  None, 'icao_code':  None, 'lat': 48.789501, 'lon': 8.191380, 'tm': bus, 'name': 'Baden-Baden Station'},

            {'point': 0, 'city': 'DE-BER', 'iata_code': 'TXL', 'icao_code':'EDDT', 'lat': 52.558794, 'lon': 13.288480, 'tm': flight, 'name': 'Berlin Tegel'},
            {'point': 0, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.553760, 'lon': 13.292310, 'tm': bus, 'name': 'Berlin Tegel'},
            {'point': 1, 'city': 'DE-BER', 'iata_code': 'QPP', 'icao_code':  None, 'lat': 52.525241, 'lon': 13.369423, 'tm': train, 'name': 'Berlin Hbf'},
            {'point': 1, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.526096, 'lon': 13.369155, 'tm': bus, 'name': 'Berlin Europaplatz am Hbf'},
            {'point': 2, 'city': 'DE-BER', 'iata_code': 'SXF', 'icao_code':'EDDB', 'lat': 52.385474, 'lon': 13.521389, 'tm': flight, 'name': 'Berlin Schönefeld'},
            {'point': 2, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.389326, 'lon': 13.519912, 'tm': bus, 'name': 'Berlin Schönefeld'},
            {'point': 3, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.510736, 'lon': 13.434995, 'tm': train, 'name': 'Berlin Ostbhf'},
            {'point': 3, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.510736, 'lon': 13.434995, 'tm': bus, 'name': 'Berlin Ostbhf Bus'},
            {'point': 4, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.475334, 'lon': 13.365847, 'tm': bus, 'name': 'Berlin Südkreuz'},
            {'point': 5, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.507613, 'lon': 13.279764, 'tm': bus, 'name': 'Berlin ZOB am Funkturm'},
            {'point': 6, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.523828, 'lon': 13.414381, 'tm': bus, 'name': 'Berlin Alexanderplatz'},
            {'point': 7, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.507328, 'lon': 13.332217, 'tm': train, 'name': 'Berlin Zoo'},
            {'point': 7, 'city': 'DE-BER', 'iata_code': 'QWC', 'icao_code':  None, 'lat': 52.507335, 'lon': 13.333408, 'tm': bus, 'name': 'Berlin Zoo'},
            {'point': 8, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.590618, 'lon': 13.282818, 'tm': bus, 'name': 'Berlin U Alt-Tegel'},
            {'point': 9, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.421542, 'lon': 13.177801, 'tm': bus, 'name': 'Berlin Wansee'},
            {'point':10, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.509309, 'lon': 13.497191, 'tm': train, 'name': 'Berlin Lichtenberg'},
            {'point':10, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.509309, 'lon': 13.497191, 'tm': bus, 'name': 'Berlin Lichtenberg'},
            {'point':11, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.535269, 'lon': 13.198093, 'tm': bus, 'name': 'Berlin Spandau'},
            {'point':12, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.491882, 'lon': 13.462671, 'tm': bus, 'name': 'Berlin S-Treptower Park'},
            {'point':13, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.5807  , 'lon': 13.431   , 'tm': bus, 'name': 'Berlin Am Feuchten Winkel'},
            {'point':14, 'city': 'DE-BER', 'iata_code': 'BER', 'icao_code':'EDDB', 'lat': 52.363986, 'lon': 13.508442, 'tm': flight, 'name': 'Berlin Brandenburg'},
            {'point':14, 'city': 'DE-BER', 'iata_code':  None, 'icao_code':  None, 'lat': 52.364399, 'lon': 13.509451, 'tm': train, 'name': 'Berlin Brandenburg Airport'},

            {'point': 1, 'city': 'DE-BFE', 'iata_code':  None, 'icao_code':  None, 'lat': 52.029325, 'lon': 8.533100, 'tm': train, 'name': 'Bielefeld Hbf'},
            {'point': 2, 'city': 'DE-BFE', 'iata_code':  None, 'icao_code':  None, 'lat': 51.998234, 'lon': 8.499708, 'tm': bus, 'name': 'Bielefeld Brackwede'},
            {'point': 3, 'city': 'DE-BFE', 'iata_code':  None, 'icao_code':  None, 'lat': 52.023115, 'lon': 8.533264, 'tm': bus, 'name': 'Bielefeld Jahnplatz'},

            {'point': 1, 'city': 'DE-BOM', 'iata_code':  None, 'icao_code':  None, 'lat': 51.478945, 'lon': 7.222630, 'tm': train, 'name': 'Bochum Hbf'},
            {'point': 1, 'city': 'DE-BOM', 'iata_code':  None, 'icao_code':  None, 'lat': 51.479244, 'lon': 7.224920, 'tm': bus, 'name': 'Bochum ZOB am Hbf'},

            {'point': 1, 'city': 'DE-BON', 'iata_code': 'BNJ', 'icao_code':  None, 'lat': 50.732474, 'lon': 7.096999, 'tm': train, 'name': 'Bonn Hbf'},
            {'point': 2, 'city': 'DE-BON', 'iata_code':  None, 'icao_code':  None, 'lat': 50.712839, 'lon': 7.120509, 'tm': bus, 'name': 'Bonn Museumsmeile'},
            {'point': 3, 'city': 'DE-BON', 'iata_code':  None, 'icao_code':  None, 'lat': 50.734823, 'lon': 7.088828, 'tm': bus, 'name': 'Bonn Thomastr.'},

            # {'point': 0, 'city': 'DE-BWE', 'iata_code': 'BVE', 'icao_code':'EDVE', 'lat': '', 'lon': '', 'tm': flight, 'name': 'Braunschweig-Wolfsburg Airpot'}, #no commercial flights
            {'point': 1, 'city': 'DE-BWE', 'iata_code':  None, 'icao_code':  None, 'lat': 52.252582, 'lon': 10.539373, 'tm': train, 'name': 'Braunschweig Hbf'},
            {'point': 1, 'city': 'DE-BWE', 'iata_code':  None, 'icao_code':  None, 'lat': 52.251205, 'lon': 10.536712, 'tm': bus, 'name': 'Braunschweig Hbf (Berliner Platz)'},

            {'point': 0, 'city': 'DE-BRE', 'iata_code': 'BRE', 'icao_code':'EDDW', 'lat': 53.048013, 'lon': 8.785836, 'tm': flight, 'name': 'Bremen Airport'},
            {'point': 1, 'city': 'DE-BRE', 'iata_code': 'HF8', 'icao_code':  None, 'lat': 53.083096, 'lon': 8.813414, 'tm': train, 'name': 'Bremen Hbf'},
            {'point': 1, 'city': 'DE-BRE', 'iata_code':  None, 'icao_code':  None, 'lat': 53.082179, 'lon': 8.810587, 'tm': bus, 'name': 'Bremen ZOB'},

            {'point': 1, 'city': 'DE-BRV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.534669, 'lon': 8.599653, 'tm': train, 'name': 'Bremerhaven Hbf'},
            {'point': 1, 'city': 'DE-BRV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.536706, 'lon': 8.599864, 'tm': bus, 'name': 'Bremerhaven Hbf (Bismarckstraße)'},
            {'point': 2, 'city': 'DE-BRV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.566323, 'lon': 8.599921, 'tm': train, 'name': 'Bremerhaven-Lehe'},

            {'point': 1, 'city': 'DE-CHE', 'iata_code':  None, 'icao_code':  None, 'lat': 50.839696, 'lon': 12.930877, 'tm': train, 'name': 'Chemnitz Hbf'},
            {'point': 1, 'city': 'DE-CHE', 'iata_code':  None, 'icao_code':  None, 'lat': 50.840937, 'lon': 12.926690, 'tm': bus, 'name': 'Chemnitz Omnibusbahnhof'},

            {'point': 0, 'city': 'DE-CGN', 'iata_code': 'CGN', 'icao_code':'EDDK', 'lat': 50.870717, 'lon': 7.140713, 'tm': flight, 'name': 'Cologne-Bonn Airport'},
            {'point': 0, 'city': 'DE-CGN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.878967, 'lon': 7.119270, 'tm': train, 'name': 'Cologne-Bonn Airport'},
            {'point': 0, 'city': 'DE-CGN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.881441, 'lon': 7.117078, 'tm': bus, 'name': 'Cologne-Bonn Airport'},
            {'point': 1, 'city': 'DE-CGN', 'iata_code': 'QKL', 'icao_code':  None, 'lat': 50.943213, 'lon': 6.958602, 'tm': train, 'name': 'Köln Hbf'},
            {'point': 2, 'city': 'DE-CGN', 'iata_code': 'QKU', 'icao_code':  None, 'lat': 50.940390, 'lon': 6.974360, 'tm': train, 'name': 'Köln Messe-Deutz'},
            {'point': 2, 'city': 'DE-CGN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.938547, 'lon': 6.988851, 'tm': bus, 'name': 'Köln Messe-Deutz'},
            {'point': 3, 'city': 'DE-CGN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.953861, 'lon': 7.116611, 'tm': bus, 'name': 'Cologne East - Refrath'},
            {'point': 4, 'city': 'DE-CGN', 'iata_code':  None, 'icao_code':  None, 'lat': 51.032181, 'lon': 6.990563, 'tm': bus, 'name': 'Cologne North - Leverkusen'},

            {'point': 1, 'city': 'DE-CUX', 'iata_code':  None, 'icao_code':  None, 'lat': 53.860895, 'lon': 8.703451, 'tm': train, 'name': 'Cuxhaven Bf'},
            {'point': 1, 'city': 'DE-CUX', 'iata_code':  None, 'icao_code':  None, 'lat': 53.861831, 'lon': 8.702464, 'tm': bus, 'name': 'Cuxhaven ZOB'},

            {'point': 1, 'city': 'DE-DAR', 'iata_code':  None, 'icao_code':  None, 'lat': 49.872598, 'lon': 8.629323, 'tm': train, 'name': 'Darmstadt Hbf'},
            {'point': 1, 'city': 'DE-DAR', 'iata_code':  None, 'icao_code':  None, 'lat': 49.870919, 'lon': 8.628610, 'tm': bus, 'name': 'Darmstadt Hbf Bus'},

            {'point': 0, 'city': 'DE-DTM', 'iata_code': 'DTM', 'icao_code':'EDLW', 'lat': 51.517318, 'lon': 7.612015, 'tm': flight, 'name': 'Dortmund Airport'},
            {'point': 1, 'city': 'DE-DTM', 'iata_code': 'DTZ', 'icao_code':  None, 'lat': 51.518048, 'lon': 7.458891, 'tm': train, 'name': 'Dortmund Hbf'},
            {'point': 1, 'city': 'DE-DTM', 'iata_code':  None, 'icao_code':  None, 'lat': 51.519955, 'lon': 7.459257, 'tm': bus, 'name': 'Dortmund Bus Station'},

            {'point': 0, 'city': 'DE-DRS', 'iata_code': 'DRS', 'icao_code':'EDDC', 'lat': 51.132152, 'lon': 13.767205, 'tm': flight, 'name': 'Dresden Airport'},
            {'point': 0, 'city': 'DE-DRS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.124827, 'lon': 13.766321, 'tm': bus, 'name': 'Dresden Airport'},
            {'point': 1, 'city': 'DE-DRS', 'iata_code': 'XIR', 'icao_code':  None, 'lat': 51.040503, 'lon': 13.731420, 'tm': train, 'name': 'Dresden Hbf'},
            {'point': 1, 'city': 'DE-DRS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.039925, 'lon': 13.730757, 'tm': bus, 'name': 'Dresden ZOB'},
            {'point': 2, 'city': 'DE-DRS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.065559, 'lon': 13.740895, 'tm': train, 'name': 'Dresden Neustadt'},
            {'point': 2, 'city': 'DE-DRS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.066378, 'lon': 13.739383, 'tm': bus, 'name': 'Dresden Neustadt'},
            {'point': 3, 'city': 'DE-DRS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.083731, 'lon': 13.686900, 'tm': bus, 'name': 'Dresden Riegelplatz'},

            {'point': 1, 'city': 'DE-DUI', 'iata_code':  None, 'icao_code':  None, 'lat': 51.429553, 'lon': 6.777101, 'tm': train, 'name': 'Duisburg Hbf'},
            {'point': 1, 'city': 'DE-DUI', 'iata_code':  None, 'icao_code':  None, 'lat': 51.428760, 'lon': 6.777217, 'tm': bus, 'name': 'Duisburg Hbf Bus'},

            {'point': 0, 'city': 'DE-DUS', 'iata_code': 'DUS', 'icao_code':'EDDL', 'lat': 51.287623, 'lon': 6.766796, 'tm': flight, 'name': 'Düsseldorf Airport'},
            {'point': 0, 'city': 'DE-DUS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.291591, 'lon': 6.786751, 'tm': train, 'name': 'Düsseldorf Airport'},
            # {'point': 0, 'city': 'DE-DUS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.276536, 'lon': 6.767046, 'tm': bus, 'name': 'Düsseldorf Airport Bus Station'}, #no buses to airport: only SAPS (italian)
            {'point': 1, 'city': 'DE-DUS', 'iata_code': 'QDU', 'icao_code':  None, 'lat': 51.220227, 'lon': 6.793007, 'tm': train, 'name': 'Düsseldorf Hbf'},
            {'point': 1, 'city': 'DE-DUS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.223022, 'lon': 6.795403, 'tm': bus, 'name': 'Düsseldorf Hbf'},
            {'point': 2, 'city': 'DE-DUS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.207045, 'lon': 6.828091, 'tm': bus, 'name': 'Düsseldorf Kuthsweg'},

            {'point': 0, 'city': 'DE-ERF', 'iata_code': 'ERF', 'icao_code': 'EDDE', 'lat': 50.979606, 'lon': 10.956902, 'tm': flight, 'name': 'Erfurt-Weimar Airport'},
            {'point': 1, 'city': 'DE-ERF', 'iata_code':  None, 'icao_code':  None, 'lat': 50.972507, 'lon': 11.038025, 'tm': train, 'name': 'Erfurt Hbf'},
            {'point': 1, 'city': 'DE-ERF', 'iata_code':  None, 'icao_code':  None, 'lat': 50.973747, 'lon': 11.040066, 'tm': bus, 'name': 'Erfurt Hbf'},
            {'point': 2, 'city': 'DE-ERF', 'iata_code':  None, 'icao_code':  None, 'lat': 50.950164, 'lon': 11.093406, 'tm': bus, 'name': 'Erfurt Urbicher Kreuz'},

            # {'point': 1, 'city': 'DE-ERL', 'iata_code':  None, 'icao_code':  None, 'lat': 49.596057, 'lon': 11.002100, 'tm': train, 'name': 'Erlangen Hbf'}, #near Nuremberg
            # {'point': 1, 'city': 'DE-ERL', 'iata_code':  None, 'icao_code':  None, 'lat': 49.596230, 'lon': 11.000150, 'tm': bus, 'name': 'Erlangen Hbf (Parkplatzstraße)'},

            {'point': 1, 'city': 'DE-ESS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.450764, 'lon': 7.013905, 'tm': train, 'name': 'Essen Hbf'},
            {'point': 1, 'city': 'DE-ESS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.450229, 'lon': 7.014956, 'tm': bus, 'name': 'Essen Hbf (Freiheit)'},

            {'point': 0, 'city': 'DE-FRA', 'iata_code': 'FRA', 'icao_code':'EDDF', 'lat': 50.037931, 'lon': 8.562152, 'tm': flight, 'name': 'Frankfurt Airport'},
            {'point': 0, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.052887, 'lon': 8.569872, 'tm': train, 'name': 'Frankfurt Airport Train Station'},
            {'point': 0, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.052539, 'lon': 8.588127, 'tm': bus, 'name': 'Frankfurt Airport Bus Station T2-E'},
            {'point': 1, 'city': 'DE-FRA', 'iata_code': 'ZRB', 'icao_code':  None, 'lat': 50.106525, 'lon': 8.662164, 'tm': train, 'name': 'Frankfurt Hbf'},
            {'point': 1, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.104331, 'lon': 8.662395, 'tm': bus, 'name': 'Frankfurt Hbf'},
            {'point': 2, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.099769, 'lon': 8.685971, 'tm': train, 'name': 'Frankfurt Süd'},
            # {'point': 2, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.099769, 'lon': 8.685971, 'tm': bus, 'name': 'Frankfurt Süd'}, #for Locomore through Busbud?
            {'point': 3, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.119259, 'lon': 8.639698, 'tm': train, 'name': 'Frankfurt West'},
            {'point': 4, 'city': 'DE-FRA', 'iata_code':  None, 'icao_code':  None, 'lat': 50.116745, 'lon': 8.683105, 'tm': bus, 'name': 'Frankfurt Stephanstr.'},

            {'point': 0, 'city': 'DE-HNH', 'iata_code': 'HHN', 'icao_code':'EDFH', 'lat': 49.945808, 'lon': 7.264198, 'tm': flight, 'name': 'Frankfurt Hahn Airport'},
            {'point': 0, 'city': 'DE-HNH', 'iata_code':  None, 'icao_code':  None, 'lat': 49.945522, 'lon': 7.269628, 'tm': bus, 'name': 'Frankfurt Hahn Airport'},

            {'point': 1, 'city': 'DE-FBG', 'iata_code': 'QFB', 'icao_code':  None, 'lat': 47.997626, 'lon': 7.842153, 'tm': train, 'name': 'Freiburg Hbf'},
            {'point': 1, 'city': 'DE-FBG', 'iata_code':  None, 'icao_code':  None, 'lat': 47.995688, 'lon': 7.840472, 'tm': bus, 'name': 'Freiburg ZOB am Hbf'},
            # {'point': 2, 'city': 'DE-FBG', 'iata_code':  None, 'icao_code':  None, 'lat': 47.985871, 'lon': 7.829558, 'tm': bus, 'name': 'Freiburg (Pressehaus / Am Radacker)'}, # no buses anymore

            {'point': 0, 'city': 'DE-FDH', 'iata_code': 'FDH', 'icao_code':'EDNY', 'lat': 47.672245, 'lon': 9.512185, 'tm': flight, 'name': 'Friedrichshafen Airport'},
            {'point': 0, 'city': 'DE-FDH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.672213, 'lon': 9.523715, 'tm': train, 'name': 'Friedrichshafen Airport Train Station'},
            {'point': 1, 'city': 'DE-FDH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.652963, 'lon': 9.473406, 'tm': train, 'name': 'Friedrichshafen Stadt'},
            {'point': 1, 'city': 'DE-FDH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.652731, 'lon': 9.473443, 'tm': bus, 'name': 'Friedrichshafen Central Bus Station'},
            # {'point': 2, 'city': 'DE-FDH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.651217, 'lon': 9.483031, 'tm': train, 'name': 'Friedrichshafen Hafen Bahnhof'},
            # {'point': 2, 'city': 'DE-FDH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.650353, 'lon': 9.483202, 'tm': ferry, 'name': 'Friedrichshafen Hafen'},

            # {'point': 1, 'city': 'DE-FUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.470072, 'lon': 10.990221, 'tm': train, 'name': 'Fürth Hbf'},
            # {'point': 1, 'city': 'DE-FUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.470301, 'lon': 10.991233, 'tm': bus, 'name': 'Fürth Hbf Bus'},

            {'point': 1, 'city': 'DE-GOE', 'iata_code': 'ZEU', 'icao_code':  None, 'lat': 51.536630, 'lon': 9.926782, 'tm': train, 'name': 'Göttingen Hbf'},
            {'point': 1, 'city': 'DE-GOE', 'iata_code':  None, 'icao_code':  None, 'lat': 51.535005, 'lon': 9.925737, 'tm': bus, 'name': 'Göttingen ZOB am Hbf'},

            {'point': 1, 'city': 'DE-HAL', 'iata_code':  None, 'icao_code':  None, 'lat': 51.477274, 'lon': 11.987551, 'tm': train, 'name': 'Halle Hbf'},
            {'point': 1, 'city': 'DE-HAL', 'iata_code':  None, 'icao_code':  None, 'lat': 51.477501, 'lon': 11.984600, 'tm': bus, 'name': 'Halle (Saale) ZOB'},

            {'point': 0, 'city': 'DE-HAM', 'iata_code': 'HAM', 'icao_code':'EDDH', 'lat': 53.633624, 'lon': 9.997415, 'tm': flight, 'name': 'Hamburg Airport'},
            {'point': 0, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': 53.632648, 'lon': 10.006495, 'tm': bus, 'name': 'Hamburg Airport'},
            {'point': 1, 'city': 'DE-HAM', 'iata_code': 'ZMB', 'icao_code':  None, 'lat': 53.552813, 'lon': 10.006978, 'tm': train, 'name': 'Hamburg Hbf'},
            {'point': 1, 'city': 'DE-HAM', 'iata_code': 'OBZ', 'icao_code':  None, 'lat': 53.551992, 'lon': 10.011593, 'tm': bus, 'name': 'Hamburg ZOB'},
            {'point': 2, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': 53.552210, 'lon': 9.934714, 'tm': train, 'name': 'Hamburg Altona'},
            {'point': 3, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': 53.456257, 'lon': 9.991637, 'tm': train, 'name': 'Hamburg-Harburg'},
            {'point': 3, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': 53.455884, 'lon': 9.990556, 'tm': bus, 'name': 'Hamburg-Harburg'},
            {'point': 4, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': 53.489958, 'lon': 10.205900, 'tm': train, 'name': 'Hamburg Bergedorf'},
            {'point': 5, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': 53.572639, 'lon': 10.070449, 'tm': bus, 'name': 'Hamburg Wandsbek'},
            # {'point': 3, 'city': 'DE-HAM', 'iata_code':  None, 'icao_code':  None, 'lat': '', 'lon': '', 'tm': ferry, 'name': 'Hamburg Hafen'},

            {'point': 1, 'city': 'DE-HMM', 'iata_code':  None, 'icao_code':  None, 'lat': 51.678419, 'lon': 7.809007, 'tm': train, 'name': 'Bahnhof Hamm (Westfalen)'},
            {'point': 1, 'city': 'DE-HMM', 'iata_code':  None, 'icao_code':  None, 'lat': 51.676470, 'lon': 7.806420, 'tm': bus, 'name': 'Hamm Bf (Unionstr)'},

            {'point': 0, 'city': 'DE-HAJ', 'iata_code': 'HAJ', 'icao_code':'EDDV', 'lat': 52.461847, 'lon': 9.688993, 'tm': flight, 'name': 'Hannover Airport'},
            {'point': 1, 'city': 'DE-HAJ', 'iata_code': 'ZVR', 'icao_code':  None, 'lat': 52.376485, 'lon': 9.741030, 'tm': train, 'name': 'Hannover Hbf'},
            {'point': 1, 'city': 'DE-HAJ', 'iata_code':  None, 'icao_code':  None, 'lat': 52.378525, 'lon': 9.741249, 'tm': bus, 'name': 'Hannover ZOB'},
            {'point': 2, 'city': 'DE-HAJ', 'iata_code':  None, 'icao_code':  None, 'lat': 52.317417, 'lon': 9.792669, 'tm': train, 'name': 'Hannover Messe/Laatzen'}, #Locomore used it during one week..
            {'point': 2, 'city': 'DE-HAJ', 'iata_code':  None, 'icao_code':  None, 'lat': 52.317724, 'lon': 9.792860, 'tm': bus, 'name': 'Hannover Messe/Laatzen'},
            # {'point': 3, 'city': 'DE-HAJ', 'iata_code':  None, 'icao_code':  None, 'lat': 52.376449, 'lon': 9.973442, 'tm': train, 'name': 'Hannover Lehrte'}, #Locomore used it during one week..

            {'point': 0, 'city': 'DE-HDF', 'iata_code': 'HDF', 'icao_code':'EDAH', 'lat': 53.877583, 'lon': 14.158086, 'tm': flight, 'name': 'Heringsdorf Airport'},
            {'point': 1, 'city': 'DE-HDF', 'iata_code':  None, 'icao_code':  None, 'lat': 53.949570, 'lon': 14.169126, 'tm': bus, 'name': 'Seebad Heringsdorf'},

            {'point': 1, 'city': 'DE-HEI', 'iata_code':  None, 'icao_code':  None, 'lat': 49.403917, 'lon': 8.675825, 'tm': train, 'name': 'Heidelberg Hbf'},
            {'point': 1, 'city': 'DE-HEI', 'iata_code': 'QHD', 'icao_code':  None, 'lat': 49.403843, 'lon': 8.676831, 'tm': bus, 'name': 'Heildelberg ZOB am Hbf'},

            {'point': 1, 'city': 'DE-HEN', 'iata_code':  None, 'icao_code':  None, 'lat': 49.142613, 'lon': 9.208513, 'tm': train, 'name': 'Heilbronn Hbf'},
            {'point': 1, 'city': 'DE-HEN', 'iata_code':  None, 'icao_code':  None, 'lat': 49.141628, 'lon': 9.205481, 'tm': bus, 'name': 'Heilbronn Hbf Bus'},
            {'point': 2, 'city': 'DE-HEN', 'iata_code':  None, 'icao_code':  None, 'lat': 49.188748, 'lon': 9.218717, 'tm': bus, 'name': 'Heilbronn/Neckarsulm Bf (Kanalstraße)'},

            # {'point': 0, 'city': 'DE-ING', 'iata_code': 'IGS', 'icao_code': 'ETSI', 'lat': '', 'lon': '', 'tm': flight, 'name': 'Ingolstadt Aiport'}, #no commercial flights
            {'point': 1, 'city': 'DE-ING', 'iata_code':  None, 'icao_code':  None, 'lat': 48.744299, 'lon': 11.436732, 'tm': train, 'name': 'Ingolstadt Hbf'},
            {'point': 1, 'city': 'DE-ING', 'iata_code':  None, 'icao_code':  None, 'lat': 48.744805, 'lon': 11.436181, 'tm': bus, 'name': 'Ingolstadt Hbf Bus'},
            {'point': 2, 'city': 'DE-ING', 'iata_code':  None, 'icao_code':  None, 'lat': 48.772333, 'lon': 11.432833, 'tm': bus, 'name': 'Ingolstadt Nordbahnhof'},

            {'point': 1, 'city': 'DE-JEN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.924952, 'lon': 11.587504, 'tm': train, 'name': 'Jena Bf Paradies'},
            {'point': 1, 'city': 'DE-JEN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.925500, 'lon': 11.587431, 'tm': bus, 'name': 'Jena Busbahnhof (Bf Paradies)'},
            {'point': 2, 'city': 'DE-JEN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.923188, 'lon': 11.578055, 'tm': train, 'name': 'Jena West'},
            {'point': 3, 'city': 'DE-JEN', 'iata_code':  None, 'icao_code':  None, 'lat': 50.884010, 'lon': 11.594967, 'tm': bus, 'name': 'Jena Göschwitz Bus'},

            {'point': 1, 'city': 'DE-KAE', 'iata_code': 'KJR', 'icao_code':  None, 'lat': 48.993560, 'lon': 8.401863, 'tm': train, 'name': 'Karlsruhe Hbf'},
            {'point': 1, 'city': 'DE-KAE', 'iata_code':  None, 'icao_code':  None, 'lat': 48.991675, 'lon': 8.401261, 'tm': bus, 'name': 'Karlsruhe Hbf Bus'},

            {'point': 1, 'city': 'DE-KLT', 'iata_code':  None, 'icao_code':  None, 'lat': 49.436253, 'lon': 7.768667, 'tm': train, 'name': 'Kaiserslautern Hbf'},
            {'point': 1, 'city': 'DE-KLT', 'iata_code':  None, 'icao_code':  None, 'lat': 49.436508, 'lon': 7.767771, 'tm': bus, 'name': 'Kaiserslautern Hbf Bus'},

            {'point': 0, 'city': 'DE-KAS', 'iata_code': 'KSF', 'icao_code':'EDVK', 'lat': 51.416529, 'lon': 9.386128, 'tm': flight, 'name': 'Kassel Airport'}, #only few seasonal flights in 2017
            {'point': 1, 'city': 'DE-KAS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.318276, 'lon': 9.489529, 'tm': train, 'name': 'Kassel Hbf'},
            {'point': 2, 'city': 'DE-KAS', 'iata_code': 'KWQ', 'icao_code':  None, 'lat': 51.312720, 'lon': 9.446979, 'tm': train, 'name': 'Kassel-Wilhelmshöhe'},
            {'point': 2, 'city': 'DE-KAS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.312271, 'lon': 9.448058, 'tm': bus, 'name': 'Bushaltestelle Kassel Bf (Wilhelmshöhe)'},
            {'point': 3, 'city': 'DE-KAS', 'iata_code':  None, 'icao_code':  None, 'lat': 51.291578, 'lon': 9.565720, 'tm': bus, 'name': 'Kassel (Kaufungen Papierfabrik)'},

            {'point': 1, 'city': 'DE-KEL', 'iata_code':  None, 'icao_code':  None, 'lat': 54.315453, 'lon': 10.132143, 'tm': train, 'name': 'Kiel Hbf'},
            {'point': 1, 'city': 'DE-KEL', 'iata_code':  None, 'icao_code':  None, 'lat': 54.310865, 'lon': 10.130618, 'tm': bus, 'name': 'Kiel ZOB'},

            {'point': 1, 'city': 'DE-KOB', 'iata_code':  None, 'icao_code':  None, 'lat': 50.350758, 'lon': 7.589257, 'tm': train, 'name': 'Koblenz Hbf'},
            {'point': 1, 'city': 'DE-KOB', 'iata_code':  None, 'icao_code':  None, 'lat': 50.349459, 'lon': 7.589674, 'tm': bus, 'name': 'Koblenz Hbf (Neversstraße)'},

            {'point': 1, 'city': 'DE-KON', 'iata_code':  None, 'icao_code':  None, 'lat': 47.658948, 'lon': 9.177163, 'tm': train, 'name': 'Konstanz Bahnhof'},
            {'point': 2, 'city': 'DE-KON', 'iata_code':  None, 'icao_code':  None, 'lat': 47.658164, 'lon': 9.169120, 'tm': bus, 'name': 'Konstanz Döbeleplatz'},
            {'point': 3, 'city': 'DE-KON', 'iata_code':  None, 'icao_code':  None, 'lat': 47.682203, 'lon': 9.202649, 'tm': bus, 'name': 'Konstanz Allmannsdorf'},
            {'point': 4, 'city': 'DE-KON', 'iata_code':  None, 'icao_code':  None, 'lat': 47.701082, 'lon': 9.183882, 'tm': bus, 'name': 'Konstanz-Mainau (Bodensee)'},

            {'point': 0, 'city': 'DE-LEJ', 'iata_code': 'LEJ', 'icao_code':'EDDP', 'lat': 51.422080, 'lon': 12.220382, 'tm': flight, 'name': 'Leipzig Airport'},
            {'point': 0, 'city': 'DE-LEJ', 'iata_code':  None, 'icao_code':  None, 'lat': 51.423346, 'lon': 12.223174, 'tm': train, 'name': 'Leipzig Airport Train'},
            {'point': 0, 'city': 'DE-LEJ', 'iata_code':  None, 'icao_code':  None, 'lat': 51.420478, 'lon': 12.220334, 'tm': bus, 'name': 'Leipzig Airport Bus'},
            {'point': 1, 'city': 'DE-LEJ', 'iata_code': 'XIT', 'icao_code':  None, 'lat': 51.345472, 'lon': 12.381574, 'tm': train, 'name': 'Leipzig Hbf'},
            {'point': 1, 'city': 'DE-LEJ', 'iata_code':  None, 'icao_code':  None, 'lat': 51.342253, 'lon': 12.381169, 'tm': bus, 'name': 'Leipzig Hbf Bus Station'},
            {'point': 2, 'city': 'DE-LEJ', 'iata_code':  None, 'icao_code':  None, 'lat': 51.396924, 'lon': 12.396223, 'tm': bus, 'name': 'Leipzig Messe'},

            {'point': 1, 'city': 'DE-LBC', 'iata_code':  None, 'icao_code':  None, 'lat': 53.867092, 'lon': 10.670480, 'tm': train, 'name': 'Lübeck Hbf'},
            {'point': 1, 'city': 'DE-LBC', 'iata_code':  None, 'icao_code':  None, 'lat': 53.866211, 'lon': 10.669225, 'tm': bus, 'name': 'Lübeck ZOB'},

            # {'point': 0, 'city': 'DE-MAG', 'iata_code': 'CSO', 'icao_code':'EDBC', 'lat': '', 'lon': '', 'tm': flight, 'name': 'Magdeburg Airport'}, #no commercial flights
            {'point': 1, 'city': 'DE-MAG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.130689, 'lon': 11.626817, 'tm': train, 'name': 'Magdeburg Hbf'},
            {'point': 1, 'city': 'DE-MAG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.131617, 'lon': 11.624750, 'tm': bus, 'name': 'Magdeburg ZOB'},

            # {'point': 0, 'city': 'DE-MHG', 'iata_code': 'MHG', 'icao_code':'EDFM', 'lat': 49.474955, 'lon': 8.518483, 'tm': flight, 'name': 'Mannheim City Airport'},
            {'point': 1, 'city': 'DE-MHG', 'iata_code': 'MHJ', 'icao_code':  None, 'lat': 49.479714, 'lon': 8.469880, 'tm': train, 'name': 'Mannheim Hbf'},
            {'point': 1, 'city': 'DE-MHG', 'iata_code':  None, 'icao_code':  None, 'lat': 49.478061, 'lon': 8.472898, 'tm': bus, 'name': 'Mannheim ZOB am Hbf'},

            {'point': 0, 'city': 'DE-MMN', 'iata_code': 'FMM', 'icao_code':'EDJA', 'lat': 47.987918, 'lon': 10.232517, 'tm': flight, 'name': 'Memmingen Airport'},
            {'point': 0, 'city': 'DE-MMN', 'iata_code':  None, 'icao_code':  None, 'lat': 47.989719, 'lon': 10.232263, 'tm': bus, 'name': 'Memmingen Airport Bus Station'},
            {'point': 1, 'city': 'DE-MMN', 'iata_code':  None, 'icao_code':  None, 'lat': 47.985716, 'lon': 10.186608, 'tm': train, 'name': 'Memmingen Hbf'},
            {'point': 1, 'city': 'DE-MMN', 'iata_code':  None, 'icao_code':  None, 'lat': 47.984488, 'lon': 10.186433, 'tm': bus, 'name': 'Memmingen ZOB'},

            {'point': 0, 'city': 'DE-MUC', 'iata_code': 'MUC', 'icao_code':'EDDM', 'lat': 48.353655, 'lon': 11.774964, 'tm': flight, 'name': 'Munich Airport'},
            {'point': 0, 'city': 'DE-MUC', 'iata_code':  None, 'icao_code':  None, 'lat': 48.355978, 'lon': 11.790023, 'tm': bus, 'name': 'Munich Airport T2'},
            {'point': 1, 'city': 'DE-MUC', 'iata_code': 'ZMU', 'icao_code':  None, 'lat': 48.140457, 'lon': 11.557768, 'tm': train, 'name': 'Munich Hbf'},
            {'point': 2, 'city': 'DE-MUC', 'iata_code':  None, 'icao_code':  None, 'lat': 48.142304, 'lon': 11.549874, 'tm': bus, 'name': 'Munich ZOB Hackerbrücke'},
            {'point': 3, 'city': 'DE-MUC', 'iata_code':  None, 'icao_code':  None, 'lat': 48.210819, 'lon': 11.618642, 'tm': bus, 'name': 'München Froettmaning'},
            {'point': 4, 'city': 'DE-MUC', 'iata_code':  None, 'icao_code':  None, 'lat': 48.135093, 'lon': 11.705079, 'tm': bus, 'name': 'München Messe'},
            {'point': 5, 'city': 'DE-MUC', 'iata_code':  None, 'icao_code':  None, 'lat': 48.127827, 'lon': 11.604467, 'tm': train, 'name': 'München Ost'},

            {'point': 0, 'city': 'DE-MSR', 'iata_code': 'FMO', 'icao_code':'EDDG', 'lat': 52.133871, 'lon': 7.685282, 'tm': flight, 'name': 'Münster-Osnabrück Airport'},
            {'point': 0, 'city': 'DE-MSR', 'iata_code':  None, 'icao_code':  None, 'lat': 52.130720, 'lon': 7.695332, 'tm': bus, 'name': 'Münster-Osnabrück Airport'},
            {'point': 1, 'city': 'DE-MSR', 'iata_code': 'G7D', 'icao_code':  None, 'lat': 51.956656, 'lon': 7.634637, 'tm': train, 'name': 'Münster Hbf'},
            {'point': 1, 'city': 'DE-MSR', 'iata_code':  None, 'icao_code':  None, 'lat': 51.953559, 'lon': 7.631869, 'tm': bus, 'name': 'Münster Hbf (Hafenstraße)'},

            {'point': 0, 'city': 'DE-NUE', 'iata_code': 'NUE', 'icao_code':'EDDN', 'lat': 49.497141, 'lon': 11.079808, 'tm': flight, 'name': 'Nuremberg Airport'},
            {'point': 1, 'city': 'DE-NUE', 'iata_code': 'ZAQ', 'icao_code':  None, 'lat': 49.446228, 'lon': 11.081943, 'tm': train, 'name': 'Nuremberg Hbf'},
            {'point': 1, 'city': 'DE-NUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.447698, 'lon': 11.085549, 'tm': bus, 'name': 'Nuremberg Hbf Bus Station'},
            {'point': 2, 'city': 'DE-NUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.448578, 'lon': 11.096899, 'tm': bus, 'name': 'Nuremberg Bahnhofstr.'},
            {'point': 3, 'city': 'DE-NUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.447899, 'lon': 11.067922, 'tm': bus, 'name': 'Nuremberg Frauentormauer'},

            {'point': 1, 'city': 'DE-OLO', 'iata_code':  None, 'icao_code':  None, 'lat': 53.143593, 'lon': 8.222465, 'tm': train, 'name': 'Oldenburg Hbf'},
            {'point': 1, 'city': 'DE-OLO', 'iata_code':  None, 'icao_code':  None, 'lat': 53.145062, 'lon': 8.223458, 'tm': bus, 'name': 'Oldenburg Hbf ZOB'},

            {'point': 1, 'city': 'DE-OSN', 'iata_code':  None, 'icao_code':  None, 'lat': 52.272756, 'lon': 8.060897, 'tm': train, 'name': 'Osnabrück Hbf'},
            {'point': 1, 'city': 'DE-OSN', 'iata_code':  None, 'icao_code':  None, 'lat': 52.273949, 'lon': 8.057831, 'tm': bus, 'name': 'Osnabrück Hbf (Eisenbahnstraße)'},

            {'point': 0, 'city': 'DE-PAD', 'iata_code': 'PAD', 'icao_code':'EDLP', 'lat': 51.610781, 'lon': 8.619811, 'tm': flight, 'name': 'Paderborn-Lippstadt Airport'},
            {'point': 1, 'city': 'DE-PAD', 'iata_code':  None, 'icao_code':  None, 'lat': 51.713240, 'lon': 8.740664, 'tm': train, 'name': 'Paderborn Hbf'},
            {'point': 1, 'city': 'DE-PAD', 'iata_code':  None, 'icao_code':  None, 'lat': 51.712965, 'lon': 8.739679, 'tm': bus, 'name': 'Paderborn ZOB am Hbf'},
            {'point': 2, 'city': 'DE-PAD', 'iata_code':  None, 'icao_code':  None, 'lat': 51.723047, 'lon': 8.753845, 'tm': bus, 'name': 'Paderborn Maspernplatz-West'},

            {'point': 1, 'city': 'DE-REG', 'iata_code':  None, 'icao_code':  None, 'lat': 49.012231, 'lon': 12.099671, 'tm': train, 'name': 'Regensburg Hbf'},
            {'point': 1, 'city': 'DE-REG', 'iata_code':  None, 'icao_code':  None, 'lat': 49.012489, 'lon': 12.097517, 'tm': bus, 'name': 'Regensburg Hbf Bus'},

            {'point': 1, 'city': 'DE-REU', 'iata_code':  None, 'icao_code':  None, 'lat': 48.495936, 'lon': 9.209369, 'tm': train, 'name': 'Reutlingen Hbf'},
            {'point': 1, 'city': 'DE-REU', 'iata_code':  None, 'icao_code':  None, 'lat': 48.496279, 'lon': 9.211161, 'tm': bus, 'name': 'Reutlingen Hbf Bus'},

            {'point': 0, 'city': 'DE-RSK', 'iata_code': 'RLG', 'icao_code':'ETNL', 'lat': 53.914007, 'lon': 12.286308, 'tm': flight, 'name': 'Rostock-Laage Airport'},
            {'point': 1, 'city': 'DE-RSK', 'iata_code':  None, 'icao_code':  None, 'lat': 54.078424, 'lon': 12.131820, 'tm': train, 'name': 'Rostock Hbf'},
            {'point': 1, 'city': 'DE-RSK', 'iata_code':  None, 'icao_code':  None, 'lat': 54.076457, 'lon': 12.130253, 'tm': bus, 'name': 'Rostock ZOB'},
            {'point': 2, 'city': 'DE-RSK', 'iata_code':  None, 'icao_code':  None, 'lat': 54.143956, 'lon': 12.101821, 'tm': bus, 'name': 'Rostock Ferry Terminal'},
            {'point': 3, 'city': 'DE-RSK', 'iata_code':  None, 'icao_code':  None, 'lat': 54.168996, 'lon': 12.084030, 'tm': bus, 'name': 'Rostock Warnemünde Werft'},
            {'point': 4, 'city': 'DE-RSK', 'iata_code':  None, 'icao_code':  None, 'lat': 54.175620, 'lon': 12.058230, 'tm': bus, 'name': 'Rostock Warnemünde Strand'},

            {'point': 0, 'city': 'DE-SCN', 'iata_code': 'SCN', 'icao_code':'EDDR', 'lat': 49.216477, 'lon': 7.111602, 'tm': flight, 'name': 'Saarbrücken Airport'},
            {'point': 1, 'city': 'DE-SCN', 'iata_code':  None, 'icao_code':  None, 'lat': 49.240760, 'lon': 6.990701, 'tm': train, 'name': 'Saarbrücken Hbf'},
            {'point': 1, 'city': 'DE-SCN', 'iata_code':  None, 'icao_code':  None, 'lat': 49.241950, 'lon': 7.000194, 'tm': bus, 'name': 'Saarbrücken Bus Station'},

            {'point': 1, 'city': 'DE-SGE', 'iata_code':  None, 'icao_code':  None, 'lat': 50.875862, 'lon': 8.016884, 'tm': train, 'name': 'Siegen Hbf'},
            {'point': 2, 'city': 'DE-SGE', 'iata_code':  None, 'icao_code':  None, 'lat': 50.872372, 'lon': 8.016939, 'tm': bus, 'name': 'Siegen (Koblenzer Str)'},

            {'point': 0, 'city': 'DE-STR', 'iata_code': 'STR', 'icao_code':'EDDS', 'lat': 48.687622, 'lon': 9.205544, 'tm': flight, 'name': 'Stuttgart Airport'},
            {'point': 0, 'city': 'DE-STR', 'iata_code':  None, 'icao_code':  None, 'lat': 48.691655, 'lon': 9.196775, 'tm': bus, 'name': 'Stuttgart Airport SAB'},
            {'point': 1, 'city': 'DE-STR', 'iata_code': 'ZWS', 'icao_code':  None, 'lat': 48.783213, 'lon': 9.182269, 'tm': train, 'name': 'Stuttgart Hbf'},
            {'point': 2, 'city': 'DE-STR', 'iata_code':  None, 'icao_code':  None, 'lat': 48.726840, 'lon': 9.111615, 'tm': bus, 'name': 'Stuttgart Vaihingen'},
            {'point': 3, 'city': 'DE-STR', 'iata_code':  None, 'icao_code':  None, 'lat': 48.862463, 'lon': 9.179332, 'tm': bus, 'name': 'Stuttgart-Nord Kornwestheim'},
            {'point': 4, 'city': 'DE-STR', 'iata_code':  None, 'icao_code':  None, 'lat': 48.686504, 'lon': 9.003186, 'tm': bus, 'name': 'Stuttgart Boeblingen'},
            {'point': 5, 'city': 'DE-STR', 'iata_code':  None, 'icao_code':  None, 'lat': 48.645328, 'lon': 9.443840, 'tm': bus, 'name': 'Stuttgart-East Kirchheim unter Teck'},
            {'point': 6, 'city': 'DE-STR', 'iata_code':  None, 'icao_code':  None, 'lat': 48.761782, 'lon': 9.266871, 'tm': bus, 'name': 'Stuttgart Obertürkheim'},

            {'point': 0, 'city': 'DE-SYT', 'iata_code': 'GWT', 'icao_code':'EDXW', 'lat': 54.913887, 'lon': 8.330131, 'tm': flight, 'name': 'Sylt Airport'},
            {'point': 1, 'city': 'DE-SYT', 'iata_code':  None, 'icao_code':  None, 'lat': 54.907322, 'lon': 8.309921, 'tm': train, 'name': 'Westerland Sylt Bf'},

            {'point': 1, 'city': 'DE-TRI', 'iata_code':  None, 'icao_code':  None, 'lat': 49.756981, 'lon': 6.651882, 'tm': train, 'name': 'Trier Hbf'},
            {'point': 1, 'city': 'DE-TRI', 'iata_code':  None, 'icao_code':  None, 'lat': 49.757635, 'lon': 6.651916, 'tm': bus, 'name': 'Trier Hbf Bus'},

            {'point': 1, 'city': 'DE-ULM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.399370, 'lon': 9.983187, 'tm': train, 'name': 'Ulm Hbf'},
            {'point': 2, 'city': 'DE-ULM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.425855, 'lon': 10.010422, 'tm': bus, 'name': 'Ulm (Eberhard-Finckh-Str)'},
            {'point': 3, 'city': 'DE-ULM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.392655, 'lon': 10.004257, 'tm': train, 'name': 'Neu-Ulm'},
            {'point': 3, 'city': 'DE-ULM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.392306, 'lon': 10.003549, 'tm': bus, 'name': 'Neu-Ulm'},

            # {'point': 1, 'city': 'DE-UEL', 'iata_code':  None, 'icao_code':  None, 'lat': 52.969947, 'lon': 10.553308, 'tm': train, 'name': 'Uelzen Bf'},
            # {'point': 1, 'city': 'DE-UEL', 'iata_code':  None, 'icao_code':  None, 'lat': 52.969186, 'lon': 10.554799, 'tm': bus, 'name': 'Uelzen ZOB'},

            {'point': 0, 'city': 'DE-WZE', 'iata_code': 'NRN', 'icao_code':'EDLV', 'lat': 51.599579, 'lon': 6.150396, 'tm': flight, 'name': 'Weeze Airport'},
            {'point': 0, 'city': 'DE-WZE', 'iata_code':  None, 'icao_code':  None, 'lat': 51.599041, 'lon': 6.150191, 'tm': bus, 'name': 'Weeze Airport Bus Station'},
            {'point': 1, 'city': 'DE-WZE', 'iata_code':  None, 'icao_code':  None, 'lat': 51.624331, 'lon': 6.197869, 'tm': train, 'name': 'Weeze Bahnhof'},
            {'point': 1, 'city': 'DE-WZE', 'iata_code':  None, 'icao_code':  None, 'lat': 51.624444, 'lon': 6.197179, 'tm': bus, 'name': 'Weeze Bahnhof (Holtumsweg)'}, #Flixbus
            {'point': 2, 'city': 'DE-WZE', 'iata_code':  None, 'icao_code':  None, 'lat': 51.682000, 'lon': 6.159861, 'tm': bus, 'name': 'Klever Str 8, Goch'}, #Flixbus

            {'point': 1, 'city': 'DE-WIB', 'iata_code':  None, 'icao_code':  None, 'lat': 50.070933, 'lon': 8.243395, 'tm': train, 'name': 'Wiesbaden Hbf'},
            {'point': 1, 'city': 'DE-WIB', 'iata_code':  None, 'icao_code':  None, 'lat': 50.070866, 'lon': 8.246164, 'tm': bus, 'name': 'Wiesbaden Hbf Bus'},

            {'point': 1, 'city': 'DE-WOB', 'iata_code':  None, 'icao_code':  None, 'lat': 52.429109, 'lon': 10.787721, 'tm': train, 'name': 'Wolfsburg Hbf'},
            {'point': 2, 'city': 'DE-WOB', 'iata_code':  None, 'icao_code':  None, 'lat': 52.431697, 'lon': 10.795854, 'tm': bus, 'name': 'Wolfsburg Autostadt'},

            {'point': 1, 'city': 'DE-WUP', 'iata_code':  None, 'icao_code':  None, 'lat': 51.254437, 'lon': 7.149535, 'tm': train, 'name': 'Wuppertal Hbf'},
            {'point': 2, 'city': 'DE-WUP', 'iata_code':  None, 'icao_code':  None, 'lat': 51.275005, 'lon': 7.224602, 'tm': bus, 'name': 'Wuppertal-Oberbarmen Bf (Berliner Str)'},

            # {'point': 0, 'city': 'DE-WUE', 'iata_code': 'QWU', 'icao_code':'EDFW', 'lat': 49.819191, 'lon': 9.900378, 'tm': flight, 'name': 'Würzburg-Schenkenturm Airport'}, #no flights but EKBR gave it. Added in out-of-scope
            {'point': 1, 'city': 'DE-WUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.801596, 'lon': 9.935751, 'tm': train, 'name': 'Würzburg Hbf'},
            {'point': 1, 'city': 'DE-WUE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.800858, 'lon': 9.937604, 'tm': bus, 'name': 'Würzburg Hbf'},
        ]

        hubs_ES = [
            {'point': 0, 'city': 'ES-LCG', 'iata_code': 'LCG', 'icao_code': 'LECO', 'lat': 43.302322, 'lon': -8.381990, 'tm': flight, 'name': 'A Coruña Airport'},
            {'point': 1, 'city': 'ES-LCG', 'iata_code':  None, 'icao_code':   None, 'lat': 43.352593, 'lon': -8.409875, 'tm': train, 'name': 'A Coruña train station'},
            {'point': 1, 'city': 'ES-LCG', 'iata_code':  None, 'icao_code':   None, 'lat': 43.353658, 'lon': -8.403919, 'tm': bus, 'name': 'A Coruña bus station'},

            # {'point': 0, 'city': 'ES-ALB', 'iata_code': 'ABC', 'icao_code': 'LEAB', 'lat': 38.945414, 'lon': -1.880318, 'tm': flight, 'name': 'Albacete Airport'}, #no commercial flights
            {'point': 1, 'city': 'ES-ALB', 'iata_code':  None, 'icao_code':   None, 'lat': 38.999836, 'lon': -1.848366, 'tm': train, 'name': 'Albacete train station'},
            {'point': 1, 'city': 'ES-ALB', 'iata_code': 'XJJ', 'icao_code':   None, 'lat': 38.997786, 'lon': -1.846610, 'tm': bus, 'name': 'Albacete bus station'},

            {'point': 1, 'city': 'ES-ALG', 'iata_code':  None, 'icao_code':  None, 'lat': 36.126437, 'lon': -5.448973, 'tm': train, 'name': 'Algeciras'},
            {'point': 1, 'city': 'ES-ALG', 'iata_code':  None, 'icao_code':  None, 'lat': 36.126270, 'lon': -5.447921, 'tm': bus, 'name': 'Algeciras San Bernardo'},
            {'point': 2, 'city': 'ES-ALG', 'iata_code':  None, 'icao_code':  None, 'lat': 36.128168, 'lon': -5.443764, 'tm': bus, 'name': 'Puerto de Algeciras'},
            # {'point': 1, 'city': 'ES-ALG', 'iata_code':  None, 'icao_code':  None, 'lat': 36.130778, 'lon': -5.438017, 'tm': bus, 'name': 'Algeciras Ferry Terminal'},

            {'point': 0, 'city': 'ES-ALC', 'iata_code': 'ALC', 'icao_code': 'LEAL', 'lat': 38.285482, 'lon': -0.560062, 'tm': flight, 'name': "Alicante Airport"},
            {'point': 0, 'city': 'ES-ALC', 'iata_code':  None, 'icao_code':   None, 'lat': 38.287360, 'lon': -0.559911, 'tm': bus, 'name': "Alicante Airport Bus Station"},
            {'point': 1, 'city': 'ES-ALC', 'iata_code': 'YJE', 'icao_code':   None, 'lat': 38.344583, 'lon': -0.495517, 'tm': train, 'name': "Alicante central station"},
            {'point': 2, 'city': 'ES-ALC', 'iata_code':  None, 'icao_code':   None, 'lat': 38.337468, 'lon': -0.491562, 'tm': bus, 'name': "Estación de autobuses de Alicante"},
            # {'point': 3, 'city': 'ES-ALC', 'iata_code':  None, 'icao_code':   None, 'lat': 38.332155, 'lon': -0.498943, 'tm': ferry, 'name': "Alicante Ferry Terminal"},

            {'point': 0, 'city': 'ES-LEI', 'iata_code': 'LEI', 'icao_code': 'LEAM', 'lat': 36.844949, 'lon': -2.370782, 'tm': flight, 'name': "Almería Airport"},
            {'point': 1, 'city': 'ES-LEI', 'iata_code': 'AMR', 'icao_code':   None, 'lat': 36.834986, 'lon': -2.455530, 'tm': train, 'name': "Almería Train Station"},
            {'point': 1, 'city': 'ES-LEI', 'iata_code':  None, 'icao_code':   None, 'lat': 36.835567, 'lon': -2.454490, 'tm': bus, 'name': "Almería Bus Station"},
            # {'point': 2, 'city': 'ES-LEI', 'iata_code':  None, 'icao_code':   None, 'lat': 36.834743, 'lon': -2.467440, 'tm': ferry, 'name': "Almería Ferry Terminal"},
            {'point': 2, 'city': 'ES-LEI', 'iata_code':  None, 'icao_code':   None, 'lat': 36.835527, 'lon': -2.467737, 'tm': bus, 'name': "Almería Puerto"},

            {'point': 1, 'city': 'ES-AVI', 'iata_code':  None, 'icao_code':  None, 'lat': 40.657251, 'lon': -4.683305, 'tm': train, 'name': 'Avila train station'},
            {'point': 1, 'city': 'ES-AVI', 'iata_code':  None, 'icao_code':  None, 'lat': 40.659094, 'lon': -4.682245, 'tm': bus, 'name': 'Avila bus station'},
            {'point': 2, 'city': 'ES-AVI', 'iata_code':  None, 'icao_code':  None, 'lat': 40.668639, 'lon': -4.657167, 'tm': bus, 'name': 'Avila Av. Juan Carlos I'},

            {'point': 0, 'city': 'ES-AVS', 'iata_code': 'OVD', 'icao_code':'LEAS', 'lat': 43.562118, 'lon': -6.032686, 'tm': flight, 'name': 'Asturias Airport'},
            {'point': 0, 'city': 'ES-AVS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.559231, 'lon': -6.033914, 'tm': bus, 'name': 'Asturias Airport'},
            {'point': 1, 'city': 'ES-AVS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.560957, 'lon': -5.922560, 'tm': train, 'name': 'Avilés train station'},
            {'point': 1, 'city': 'ES-AVS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.562277, 'lon': -5.923754, 'tm': bus, 'name': 'Avilés bus station'},
            {'point': 2, 'city': 'ES-AVS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.536537, 'lon': -5.897147, 'tm': bus, 'name': 'Avilés Las Vegas'},

            {'point': 0, 'city': 'ES-BJZ', 'iata_code': 'BJZ', 'icao_code':'LEBZ', 'lat': 38.893949, 'lon': -6.818828, 'tm': flight, 'name': 'Badajoz Airport'},
            {'point': 1, 'city': 'ES-BJZ', 'iata_code':  None, 'icao_code':  None, 'lat': 38.890696, 'lon': -6.981750, 'tm': train, 'name': 'Badajoz train station'},
            {'point': 2, 'city': 'ES-BJZ', 'iata_code':  None, 'icao_code':  None, 'lat': 38.866877, 'lon': -6.974549, 'tm': bus, 'name': 'Badajoz bus station'},

            {'point': 0, 'city': 'ES-BCN', 'iata_code': 'BCN', 'icao_code': 'LEBL', 'lat': 41.297469, 'lon': 2.083230, 'tm': flight, 'name': "Barcelona Airport"},
            {'point': 0, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':  None, 'lat': 41.287792, 'lon': 2.072997, 'tm': bus, 'name': "Barcelona Airport Terminal 1"},
            {'point': 10, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code': None, 'lat': 41.304315, 'lon': 2.079729, 'tm': bus, 'name': "Barcelona Airport T2C"}, #how to solve this??
            {'point': 1, 'city': 'ES-BCN', 'iata_code': 'YJB', 'icao_code': 'BSNT', 'lat': 41.379084, 'lon': 2.140142, 'tm': train, 'name': "Barcelona-Sants"},
            {'point': 1, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.379681, 'lon': 2.138959, 'tm': bus, 'name': "Barcelona-Sants"},
            {'point': 2, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.394691, 'lon': 2.182597, 'tm': bus, 'name': "Barcelona Estacio del Nord"},
            # {'point': 3, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.392246, 'lon': 2.165045, 'tm': train, 'name': "Barcelona Passeig de Gracia Train Station"},
            {'point': 4, 'city': 'ES-BCN', 'iata_code': 'YJD', 'icao_code':   None, 'lat': 41.383967, 'lon': 2.186484, 'tm': train, 'name': "Estacio de França"},
            # # {'point': 5, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.371907, 'lon': 2.176569, 'tm': ferry, 'name': "Barcelona Ferry Terminal"},
            {'point': 6, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.358256, 'lon': 2.179327, 'tm': bus, 'name': "Barcelona Cruise Terminal"},
            # {'point': 7, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.421884, 'lon': 2.186931, 'tm': train, 'name': "Barcelona La Sagrera Train Station"},
            {'point': 8, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.382558, 'lon': 2.159294, 'tm': bus, 'name': "Barcelona Urgell"},
            {'point': 9, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.386002, 'lon': 2.117819, 'tm': bus, 'name': "Barcelona Palau Reial"},
            {'point':11, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat':   41.4315, 'lon':  2.18329, 'tm': bus, 'name': "Barcelona Sant Andreu"},
            {'point':12, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.409287, 'lon': 2.187202, 'tm': train, 'name': "Barcelona Clot-Aragó"},
            {'point':13, 'city': 'ES-BCN', 'iata_code':  None, 'icao_code':   None, 'lat': 41.38756, 'lon': 2.170538, 'tm': bus, 'name': "Barcelona Plaça Catalunya"},

            {'point': 0, 'city': 'ES-BIO', 'iata_code': 'BIO', 'icao_code': 'LEBB', 'lat': 43.302485, 'lon': -2.911108, 'tm': flight, 'name': "Bilbao Airport"},
            {'point': 1, 'city': 'ES-BIO', 'iata_code': 'YJI', 'icao_code':   None, 'lat': 43.260227, 'lon': -2.928216, 'tm': train, 'name': "Bilbao Abando"},
            {'point': 2, 'city': 'ES-BIO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.261330, 'lon': -2.950192, 'tm': bus, 'name': "Bilbao San Mamés"},
            {'point': 3, 'city': 'ES-BIO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.262485, 'lon': -2.934953, 'tm': bus, 'name': "Bilbao Plaza Moyua"},
            {'point': 4, 'city': 'ES-BIO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.255128, 'lon': -2.972486, 'tm': bus, 'name': "Bilbao Castrejana"},
            {'point': 5, 'city': 'ES-BIO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.275976, 'lon': -2.971608, 'tm': bus, 'name': "Bilbao Zorrotza"},
            {'point': 6, 'city': 'ES-BIO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.260149, 'lon': -2.921806, 'tm': train, 'name': "Bilbao Zazpikaleak Casco Viejo"},

            {'point': 0, 'city': 'ES-BUR', 'iata_code': 'RGS', 'icao_code': 'LEBG', 'lat': 42.354817, 'lon': -3.622761, 'tm': flight, 'name': "Burgos Airport"},
            {'point': 1, 'city': 'ES-BUR', 'iata_code': 'UGR', 'icao_code':   None, 'lat': 42.371192, 'lon': -3.666305, 'tm': train, 'name': "Burgos Rosa de Lima"},
            {'point': 2, 'city': 'ES-BUR', 'iata_code': 'XJU', 'icao_code':   None, 'lat': 42.338264, 'lon': -3.701270, 'tm': bus, 'name': "Estación central de Burgos"},
            {'point': 3, 'city': 'ES-BUR', 'iata_code':  None, 'icao_code':   None, 'lat': 42.351137, 'lon': -3.672709, 'tm': bus, 'name': "Burgos Gamonal"},

            {'point': 1, 'city': 'ES-CCS', 'iata_code':  None, 'icao_code':   None, 'lat': 39.461131, 'lon': -6.385680, 'tm': train, 'name': "Caceres Train Station"},
            {'point': 1, 'city': 'ES-CCS', 'iata_code':  None, 'icao_code':   None, 'lat': 39.460173, 'lon': -6.382434, 'tm': bus, 'name': "Caceres Bus Station"},
            {'point': 2, 'city': 'ES-CCS', 'iata_code':  None, 'icao_code':   None, 'lat': 39.443017, 'lon': -6.393464, 'tm': bus, 'name': "Caceres Aldea Moret"}, #seems to be really in the middle of nowhere

            {'point': 1, 'city': 'ES-CAD', 'iata_code':  None, 'icao_code':   None, 'lat': 36.529449, 'lon': -6.289348, 'tm': train, 'name': "Cadiz Train Station"},
            {'point': 1, 'city': 'ES-CAD', 'iata_code':  None, 'icao_code':   None, 'lat': 36.528572, 'lon': -6.288639, 'tm': bus, 'name': "Cadiz Bus Station"},
            # {'point': 1, 'city': 'ES-CAD', 'iata_code':  None, 'icao_code':   None, 'lat': 36.530961, 'lon': -6.289483, 'tm': ferry, 'name': "Cadiz Ferry Terminal"},

            {'point': 1, 'city': 'ES-CAR', 'iata_code':  None, 'icao_code':   None, 'lat': 37.605036, 'lon': -0.975009, 'tm': train, 'name': "Cartagena Train Station"},
            {'point': 1, 'city': 'ES-CAR', 'iata_code':  None, 'icao_code':   None, 'lat': 37.603321, 'lon': -0.976917, 'tm': bus, 'name': "Cartagena Bus Station"},

            {'point': 0, 'city': 'ES-CAS', 'iata_code': 'CDT', 'icao_code': 'LECH', 'lat': 40.205404, 'lon': 0.066974, 'tm': flight, 'name': "Castellon Airport"},
            {'point': 1, 'city': 'ES-CAS', 'iata_code': 'CPJ', 'icao_code':   None, 'lat': 39.988010, 'lon': -0.052548, 'tm': train, 'name': "Castellon Estació Intermodal"},
            {'point': 1, 'city': 'ES-CAS', 'iata_code':  None, 'icao_code':   None, 'lat': 39.988010, 'lon': -0.052548, 'tm': bus, 'name': "Castellon Estació Intermodal"},
            {'point': 2, 'city': 'ES-CAS', 'iata_code':  None, 'icao_code':   None, 'lat': 39.980605, 'lon': -0.041765, 'tm': bus, 'name': "Castellon Plaza País Valenciano"},

            # {'point': 0, 'city': 'ES-CEU', 'iata_code':  None, 'icao_code':  'GECE', 'lat': 35.891964, 'lon': -5.306204, 'tm': flight, 'name': "Ceuta heliport"}, #currently not used
            # {'point': 1, 'city': 'ES-CEU', 'iata_code':  None, 'icao_code':   None, 'lat': 35.895042, 'lon': -5.321667, 'tm': ferry, 'name': "Ceuta Ferry Terminal"},

            {'point': 1, 'city': 'ES-CIR', 'iata_code': 'XJI', 'icao_code':   None, 'lat': 38.985300, 'lon': -3.913632, 'tm': train, 'name': "Ciudad Real Train Station"},
            {'point': 2, 'city': 'ES-CIR', 'iata_code':  None, 'icao_code':   None, 'lat': 38.979291, 'lon': -3.929890, 'tm': bus, 'name': "Ciudad Real Bus Station"},

            # {'point': 0, 'city': 'ES-ODB', 'iata_code':  None, 'icao_code':   None, 'lat': 37.844513, 'lon': -4.843771, 'tm': flight, 'name': "Cordoba Airport"}, #currently not used
            {'point': 1, 'city': 'ES-ODB', 'iata_code': 'XOJ', 'icao_code':   None, 'lat': 37.888492, 'lon': -4.789542, 'tm': train, 'name': "Cordoba Train Station"},
            {'point': 1, 'city': 'ES-ODB', 'iata_code':  None, 'icao_code':   None, 'lat': 37.889347, 'lon': -4.790148, 'tm': bus, 'name': "Cordoba Bus Station"},

            {'point': 1, 'city': 'ES-CUE', 'iata_code':  None, 'icao_code':   None, 'lat': 40.067343, 'lon': -2.136480, 'tm': train, 'name': "Estación de Cuenca"},
            {'point': 1, 'city': 'ES-CUE', 'iata_code':  None, 'icao_code':   None, 'lat': 40.066792, 'lon': -2.134982, 'tm': bus, 'name': "Estación de Cuenca"},
            {'point': 2, 'city': 'ES-CUE', 'iata_code': 'CEJ', 'icao_code':   None, 'lat': 40.035185, 'lon': -2.144407, 'tm': train, 'name': "Cuenca Fernando Zobel"},

            # {'point': 1, 'city': 'ES-DNA', 'iata_code':  None, 'icao_code':   None, 'lat': 38.839541, 'lon': 0.112699, 'tm': train, 'name': "Denia Train Station"}, #tren ligero a Benidorn
            {'point': 2, 'city': 'ES-DNA', 'iata_code':  None, 'icao_code':   None, 'lat': 38.837620, 'lon': 0.105670, 'tm': bus, 'name': "Estación de autobuses de Denia"},
            {'point': 3, 'city': 'ES-DNA', 'iata_code':  None, 'icao_code':   None, 'lat': 38.832933, 'lon': 0.059978, 'tm': bus, 'name': "Denia Hospital"},
            # {'point': 3, 'city': 'ES-DNA', 'iata_code':  None, 'icao_code':   None, 'lat': 38.840987, 'lon': 0.114308, 'tm': ferry, 'name': "Denia Ferry Terminal"},

            {'point': 0, 'city': 'ES-NST', 'iata_code': 'EAS', 'icao_code': 'LESO', 'lat': 43.356413, 'lon': -1.793058, 'tm': flight, 'name': "San Sebastian Airport"},
            {'point': 1, 'city': 'ES-NST', 'iata_code': 'YJH', 'icao_code':   None, 'lat': 43.317666, 'lon': -1.976700, 'tm': train, 'name': "San Sebastian Donostia Train Station"},
            {'point': 1, 'city': 'ES-NST', 'iata_code':  None, 'icao_code':   None, 'lat': 43.316928, 'lon': -1.977429, 'tm': bus, 'name': "San Sebastian Donosti Nueva Estación"},
            {'point': 2, 'city': 'ES-NST', 'iata_code':  None, 'icao_code':   None, 'lat': 43.308209, 'lon': -2.009688, 'tm': bus, 'name': "San Sebastian Donosti Universidad"},
            {'point': 3, 'city': 'ES-NST', 'iata_code':  None, 'icao_code':   None, 'lat': 43.313099, 'lon': -1.981636, 'tm': train, 'name': "Amara Donostia San Sebastian"},
            # {'point': 3, 'city': 'ES-NST', 'iata_code':  None, 'icao_code':   None, 'lat': '', 'lon': '', 'tm': train, 'name': "San Sebastian-Amara Bus Station"}, #not in use
            # {'point': 4, 'city': 'ES-NST', 'iata_code':  None, 'icao_code':   None, 'lat': '', 'lon': '', 'tm': bus, 'name': "San Sebastian PIO XII Bus Station"}, #old, not in use

            {'point': 1, 'city': 'ES-ECE', 'iata_code':  None, 'icao_code':   None, 'lat': 38.271793, 'lon': -0.695109, 'tm': train, 'name': "Elche Parque"},
            {'point': 1, 'city': 'ES-ECE', 'iata_code':  None, 'icao_code':   None, 'lat': 38.272269, 'lon': -0.691570, 'tm': bus, 'name': "Elche Parque"},
            {'point': 2, 'city': 'ES-ECE', 'iata_code':  None, 'icao_code':   None, 'lat': 38.268485, 'lon': -0.708103, 'tm': bus, 'name': "Elche Carrus"},

            {'point': 0, 'city': 'ES-VDH', 'iata_code': 'VDE', 'icao_code': 'GCHI', 'lat': 27.814299, 'lon': -17.886344, 'tm': flight, 'name': "El Hierro Airport"},
            # {'point': 1, 'city': 'ES-VDH', 'iata_code':  None, 'icao_code':   None, 'lat': 27.780484, 'lon': -17.901168, 'tm': ferry, 'name': "El Hierro Puerto de La Estaca Ferry Terminal"},
            # {'point': 2, 'city': 'ES-VDH', 'iata_code':  None, 'icao_code':   None, 'lat': 27.639650, 'lon': -17.979717, 'tm': ferry, 'name': "El Hierro La Restinga Ferry Terminal"},

            {'point': 0, 'city': 'ES-FUE', 'iata_code': 'FUE', 'icao_code': 'GCFV', 'lat': 28.452618, 'lon': -13.869435, 'tm': flight, 'name': "Fuerteventura Airport"},
            # {'point': 1, 'city': 'ES-FUE', 'iata_code':  None, 'icao_code':   None, 'lat': 28.495518, 'lon': -13.853953, 'tm': ferry, 'name': "Fuerteventura Puerto del Rosario Ferry Terminal"},

            {'point': 1, 'city': 'ES-GIJ', 'iata_code': 'QIJ', 'icao_code':   None, 'lat': 43.537709, 'lon': -5.675302, 'tm': train, 'name': "Gijón Train Station"},
            {'point': 2, 'city': 'ES-GIJ', 'iata_code':  None, 'icao_code':   None, 'lat': 43.538935, 'lon': -5.667261, 'tm': bus, 'name': "Gijón Bus Station"},
            {'point': 3, 'city': 'ES-GIJ', 'iata_code':  None, 'icao_code':   None, 'lat': 43.535377, 'lon': -5.652528, 'tm': bus, 'name': "Gijón Ramón y Cajal"},
            # {'point': 6, 'city': 'ES-GIJ', 'iata_code':  None, 'icao_code':   None, 'lat': 43.547730, 'lon': -5.667167, 'tm': ferry, 'name': "Gijón Ferry Terminal"},

            {'point': 0, 'city': 'ES-GRO', 'iata_code': 'GRO', 'icao_code': 'LEGE', 'lat': 41.897536, 'lon': 2.766242, 'tm': flight, 'name': "Girona Airport"},
            {'point': 0, 'city': 'ES-GRO', 'iata_code': None, 'icao_code': None, 'lat': 41.896680, 'lon': 2.765706, 'tm': bus, 'name': "Girona Airport Bus Station"},
            {'point': 1, 'city': 'ES-GRO', 'iata_code':  None, 'icao_code':   None, 'lat': 41.979345, 'lon': 2.816921, 'tm': train, 'name': "Girona Train Station"},
            {'point': 1, 'city': 'ES-GRO', 'iata_code':  None, 'icao_code':   None, 'lat': 41.978917, 'lon': 2.817314, 'tm': bus, 'name': "Girona Bus Station"},

            {'point': 0, 'city': 'ES-LPA', 'iata_code': 'LPA', 'icao_code': 'GCLP', 'lat': 27.933177, 'lon': -15.387707, 'tm': flight, 'name': "Las Palmas de Gran Canaria Airport"},
            # {'point': 1, 'city': 'ES-LPA', 'iata_code':  None, 'icao_code':   None, 'lat': 28.141363, 'lon': -15.425121, 'tm': ferry, 'name': "Las Palmas de Gran Canaria Ferry Terminal"},

            {'point': 0, 'city': 'ES-GRX', 'iata_code': 'GRX', 'icao_code':  'LEGR', 'lat': 37.187457, 'lon': -3.776546, 'tm': flight, 'name': "Granada Airport"},
            {'point': 0, 'city': 'ES-GRX', 'iata_code':  None, 'icao_code':   None, 'lat': 37.185180, 'lon': -3.778921, 'tm': bus, 'name': "Granada Airport Bus station"},
            {'point': 1, 'city': 'ES-GRX', 'iata_code':  None, 'icao_code':   None, 'lat': 37.184041, 'lon': -3.609195, 'tm': train, 'name': "Granada Train Station"},
            {'point': 2, 'city': 'ES-GRX', 'iata_code':  None, 'icao_code':   None, 'lat': 37.199716, 'lon': -3.613663, 'tm': bus, 'name': "Granada Bus Station"},

            {'point': 1, 'city': 'ES-GUA', 'iata_code':  None, 'icao_code':   None, 'lat': 40.586550, 'lon': -3.126471, 'tm': train, 'name': "Guadalajara-Yebes Train Station"},
            {'point': 2, 'city': 'ES-GUA', 'iata_code':  None, 'icao_code':   None, 'lat': 40.644224, 'lon': -3.182270, 'tm': train, 'name': "Guadalajara Train Station"},
            {'point': 3, 'city': 'ES-GUA', 'iata_code':  None, 'icao_code':   None, 'lat': 40.636368, 'lon': -3.173209, 'tm': bus, 'name': "Guadalajara Bus Station"},

            {'point': 1, 'city': 'ES-HUV', 'iata_code':  None, 'icao_code':   None, 'lat': 37.253079, 'lon': -6.950969, 'tm': train, 'name': "Huelva-Termino Train Station"},
            {'point': 2, 'city': 'ES-HUV', 'iata_code':  None, 'icao_code':   None, 'lat': 37.257466, 'lon': -6.957569, 'tm': bus, 'name': "Huelva Bus Station"},

            # {'point': 0, 'city': 'ES-HUC', 'iata_code': 'HSK', 'icao_code':  'LEHC', 'lat': 42.082428, 'lon': -0.322663, 'tm': flight, 'name': "Huesca Airport"}, currently not used
            {'point': 1, 'city': 'ES-HUC', 'iata_code':  None, 'icao_code':   None, 'lat': 42.133344, 'lon': -0.409788, 'tm': train, 'name': "Huesca Train Station"},
            {'point': 1, 'city': 'ES-HUC', 'iata_code':  None, 'icao_code':   None, 'lat': 42.133430, 'lon': -0.409495, 'tm': bus, 'name': "Huesca Bus Station"},

            {'point': 0, 'city': 'ES-IBZ', 'iata_code': 'IBZ', 'icao_code': 'LEIB', 'lat': 38.874847, 'lon': 1.371215, 'tm': flight, 'name': "Ibiza Airport"},
            # {'point': 1, 'city': 'ES-IBZ', 'iata_code':  None, 'icao_code':   None, 'lat': 38.877064, 'lon': 1.368732, 'tm': bus, 'name': "Ibiza Airport Bus Station"}, # Alsa
            # {'point': 1, 'city': 'ES-IBZ', 'iata_code':  None, 'icao_code':   None, 'lat': 38.911736, 'lon': 1.442105, 'tm': ferry, 'name': "Ibiza Ferry Terminal"},
            # {'point': 2, 'city': 'ES-IBZ', 'iata_code':  None, 'icao_code':   None, 'lat': 38.976584, 'lon': 1.298160, 'tm': ferry, 'name': "Ibiza-Sant Antoni Ferry Terminal"},

            {'point': 1, 'city': 'ES-JAE', 'iata_code':  None, 'icao_code':   None, 'lat': 37.779827, 'lon': -3.790797, 'tm': train, 'name': "Jaen Train Station"},
            {'point': 2, 'city': 'ES-JAE', 'iata_code':  None, 'icao_code':   None, 'lat': 37.771786, 'lon': -3.786447, 'tm': bus, 'name': "Jaen Bus Station"},

            {'point': 0, 'city': 'ES-JRZ', 'iata_code': 'XRY', 'icao_code': 'LEJR', 'lat': 36.745293, 'lon': -6.060876, 'tm': flight, 'name': "Jerez Airport"},
            {'point': 0, 'city': 'ES-JRZ', 'iata_code':  None, 'icao_code':   None, 'lat': 36.751606, 'lon': -6.065878, 'tm': train, 'name': "Jerez Airport"},
            {'point': 0, 'city': 'ES-JRZ', 'iata_code':  None, 'icao_code':   None, 'lat': 36.750180, 'lon': -6.064611, 'tm': bus, 'name': "Jerez Airport"},
            {'point': 1, 'city': 'ES-JRZ', 'iata_code': 'YJW', 'icao_code':   None, 'lat': 36.679929, 'lon': -6.126850, 'tm': train, 'name': "Jerez Train Station"},
            {'point': 1, 'city': 'ES-JRZ', 'iata_code':  None, 'icao_code':   None, 'lat': 36.679660, 'lon': -6.126418, 'tm': bus, 'name': "Jerez Bus Station"},
            {'point': 2, 'city': 'ES-JRZ', 'iata_code':  None, 'icao_code':   None, 'lat': 36.685467, 'lon': -6.117414, 'tm': bus, 'name': "Jerez Campus Universitario"},

            {'point': 0, 'city': 'ES-ACE', 'iata_code': 'ACE', 'icao_code': 'GCRR', 'lat': 28.950430, 'lon': -13.605782, 'tm': flight, 'name': "Lanzarote Airport"},
            # {'point': 1, 'city': 'ES-ACE', 'iata_code':  None, 'icao_code':   None, 'lat': 28.971241, 'lon': -13.526333, 'tm': ferry, 'name': "Lanzarote Ferry Terminal"},

            {'point': 0, 'city': 'ES-PPS', 'iata_code': 'GMZ', 'icao_code': 'GCGM', 'lat': 28.031613, 'lon': -17.211985, 'tm': flight, 'name': "La Gomera Airport"},
            # {'point': 1, 'city': 'ES-PPS', 'iata_code':  None, 'icao_code':   None, 'lat': 28.087608, 'lon': -17.107735, 'tm': ferry, 'name': "La Gomera Ferry Terminal"},

            {'point': 0, 'city': 'ES-SPC', 'iata_code': 'SPC', 'icao_code': 'GCLA', 'lat': 28.621816, 'lon': -17.752667, 'tm': flight, 'name': "La Palma Airport"},
            # {'point': 1, 'city': 'ES-SPC', 'iata_code':  None, 'icao_code':   None, 'lat': 28.677739, 'lon': -17.766804, 'tm': ferry, 'name': "Santa Cruz de La Palma Ferry Terminal"},

            {'point': 0, 'city': 'ES-LEN', 'iata_code': 'LEN', 'icao_code':  'LELN', 'lat': 42.590362, 'lon': -5.643220, 'tm': flight, 'name': "Leon Airport"},
            {'point': 1, 'city': 'ES-LEN', 'iata_code': 'EEU', 'icao_code':   None, 'lat': 42.596049, 'lon': -5.582429, 'tm': train, 'name': "Estación de León"},
            {'point': 1, 'city': 'ES-LEN', 'iata_code':  None, 'icao_code':   None, 'lat': 42.593447, 'lon': -5.579198, 'tm': bus, 'name': "Estación de León"},

            {'point': 0, 'city': 'ES-LLE', 'iata_code': 'ILD', 'icao_code': 'LEDA', 'lat': 41.728468, 'lon': 0.543491, 'tm': flight, 'name': "Lleida-Alguaire Airport"},
            {'point': 1, 'city': 'ES-LLE', 'iata_code': 'QLQ', 'icao_code':   None, 'lat': 41.620774, 'lon': 0.632803, 'tm': train, 'name': "Lleida-Pirineus Station"},
            {'point': 1, 'city': 'ES-LLE', 'iata_code':  None, 'icao_code':   None, 'lat': 41.619747, 'lon': 0.633305, 'tm': bus, 'name': "Lleida – Renfe Bus Station"}, #http://www.checkmybus.es/lleida
            {'point': 2, 'city': 'ES-LLE', 'iata_code':  None, 'icao_code':   None, 'lat': 41.611693, 'lon': 0.623124, 'tm': bus, 'name': "Lleida-Saracibar Bus Station"},

            {'point': 0, 'city': 'ES-LGR', 'iata_code': 'RJL', 'icao_code':  'LERJ', 'lat': 42.455967, 'lon': -2.314769, 'tm': flight, 'name': "Logroño Airport"},
            {'point': 1, 'city': 'ES-LGR', 'iata_code':  None, 'icao_code':   None, 'lat': 42.457650, 'lon': -2.440749, 'tm': train, 'name': "Estación de Logroño"},
            {'point': 1, 'city': 'ES-LGR', 'iata_code':  None, 'icao_code':   None, 'lat': 42.459933, 'lon': -2.444209, 'tm': bus, 'name': "Estación de Logroño"},

            {'point': 1, 'city': 'ES-LGO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.015220, 'lon': -7.552176, 'tm': train, 'name': "Lugo Train Station"},
            {'point': 2, 'city': 'ES-LGO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.008249, 'lon': -7.553830, 'tm': bus, 'name': "Lugo Bus Station"},

            {'point': 0, 'city': 'ES-MAD', 'iata_code': 'MAD', 'icao_code': 'LEMD', 'lat': 40.483936, 'lon': -3.567952, 'tm': flight, 'name': "Madrid Airport"},
            {'point': 0, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.492332, 'lon': -3.593857, 'tm': bus, 'name': "Madrid Barajas T4"},
            {'point': 10, 'city': 'ES-MAD', 'iata_code': None, 'icao_code':   None, 'lat': 40.461101, 'lon': -3.575940, 'tm': bus, 'name': "Madrid Barajas T1"}, #how to deal with 2 different stations of same tm in one point?
            {'point': 1, 'city': 'ES-MAD', 'iata_code': 'XOC', 'icao_code': 'MDAT', 'lat': 40.407052, 'lon': -3.691350, 'tm': train, 'name': "Madrid Atocha"},
            {'point': 1, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.406700, 'lon': -3.683730, 'tm': bus, 'name': "Madrid Atocha"},
            {'point': 2, 'city': 'ES-MAD', 'iata_code': 'XTI', 'icao_code': 'MADC', 'lat': 40.472446, 'lon': -3.682222, 'tm': train, 'name': "Madrid Chamartin"},
            {'point': 3, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.438064, 'lon': -3.676684, 'tm': bus, 'name': "Madrid Av. America "},
            {'point': 4, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.395268, 'lon': -3.678179, 'tm': bus, 'name': "Madrid Estación Sur"},
            {'point': 5, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.434520, 'lon': -3.719064, 'tm': bus, 'name': "Madrid Moncloa"},
            {'point': 6, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.384536, 'lon': -3.718287, 'tm': bus, 'name': "Madrid Plaza Eliptica"},
            {'point': 7, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat': 40.388200, 'lon': -3.627310, 'tm': bus, 'name': "Madrid Universidad Politécnica"},
            {'point': 8, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat':   40.4493, 'lon':  -3.72727, 'tm': bus, 'name': "Madrid Universidad Complutense"},
            {'point': 9, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat':   40.5465, 'lon':  -3.69359, 'tm': bus, 'name': "Madrid Universidad Autonoma"},
            {'point':11, 'city': 'ES-MAD', 'iata_code':  None, 'icao_code':   None, 'lat':   40.4309, 'lon':  -3.79083, 'tm': bus, 'name': "Madrid Campus de Somosaguas"},

            {'point': 0, 'city': 'ES-AGP', 'iata_code': 'AGP', 'icao_code': 'LEMG', 'lat': 36.679415, 'lon': -4.495004, 'tm': flight, 'name': "Malaga Airport"},
            {'point': 0, 'city': 'ES-AGP', 'iata_code':  None, 'icao_code':   None, 'lat': 36.676912, 'lon': -4.490334, 'tm': bus, 'name': "Malaga Airport"},
            {'point': 0, 'city': 'ES-AGP', 'iata_code':  None, 'icao_code':   None, 'lat': 36.677736, 'lon': -4.490127, 'tm': train, 'name': "Malaga Airport"},
            {'point': 1, 'city': 'ES-AGP', 'iata_code': 'YJM', 'icao_code':   None, 'lat': 36.711971, 'lon': -4.431804, 'tm': train, 'name': "Malaga Maria-Zambrano"},
            {'point': 1, 'city': 'ES-AGP', 'iata_code':  None, 'icao_code':   None, 'lat': 36.712925, 'lon': -4.434053, 'tm': bus, 'name': "Malaga Maria-Zambrano"},
            {'point': 2, 'city': 'ES-AGP', 'iata_code':  None, 'icao_code':   None, 'lat': 36.716278, 'lon': -4.420740, 'tm': bus, 'name': "Malaga Puerto"},
            # # {'point': 3, 'city': 'ES-AGP', 'iata_code':  None, 'icao_code':   None, 'lat': 36.715182, 'lon': -4.417918, 'tm': ferry, 'name': "Malaga Ferry Terminal"},

            {'point': 0, 'city': 'ES-PMI', 'iata_code': 'PMI', 'icao_code': 'LEPA', 'lat': 39.551739, 'lon': 2.736162, 'tm': flight, 'name': "Mallorca Airport"},
            # {'point': 1, 'city': 'ES-PMI', 'iata_code':  None, 'icao_code':   None, 'lat': 39.576342, 'lon': 2.654197, 'tm': train, 'name': "Palma-Estació Intermodal Train Station"},
            # {'point': 2, 'city': 'ES-PMI', 'iata_code':  None, 'icao_code':   None, 'lat': 39.576678, 'lon': 2.653834, 'tm': train, 'name': "Palma-Ferrocarril Sóller Train Station"},
            # {'point': 3, 'city': 'ES-PMI', 'iata_code':  None, 'icao_code':   None, 'lat': 39.552298, 'lon': 2.625993, 'tm': ferry, 'name': "Palma Ferry Terminal"},
            # {'point': 4, 'city': 'ES-PMI', 'iata_code':  None, 'icao_code':   None, 'lat': 39.835581, 'lon': 3.139811, 'tm': ferry, 'name': "Alcudia Ferry Terminal"},

            {'point': 1, 'city': 'ES-MQE', 'iata_code':  None, 'icao_code':   None, 'lat': 36.519545, 'lon': -4.892542, 'tm': bus, 'name': "Marbella Bus Station"},

            {'point': 0, 'city': 'ES-MLN', 'iata_code':  'MLN', 'icao_code':   None, 'lat': 35.278751, 'lon': -2.956326, 'tm': flight, 'name': "Melilla Airport"},
            # {'point': 1, 'city': 'ES-MLN', 'iata_code': 'MLN', 'icao_code':  'GEML', 'lat': 35.291733, 'lon': -2.928966, 'tm': ferry, 'name': "Melilla Ferry Terminal"},

            {'point': 1, 'city': 'ES-MEA', 'iata_code':  None, 'icao_code':   None, 'lat': 38.921502, 'lon': -6.343794, 'tm': train, 'name': "Mérida Train Station"},
            {'point': 2, 'city': 'ES-MEA', 'iata_code':  None, 'icao_code':   None, 'lat': 38.914757, 'lon': -6.357839, 'tm': bus, 'name': "Mérida Bus Station"},

            {'point': 0, 'city': 'ES-MAH', 'iata_code': 'MAH', 'icao_code': 'LEMH', 'lat': 39.864606, 'lon': 4.225670, 'tm': flight, 'name': "Menorca Airport"},
            # {'point': 1, 'city': 'ES-MAH', 'iata_code':  None, 'icao_code':   None, 'lat': 39.889998, 'lon': 4.267384, 'tm': ferry, 'name': "Mahón Ferry Terminal"},
            # {'point': 2, 'city': 'ES-MAH', 'iata_code':  None, 'icao_code':   None, 'lat': 39.988392, 'lon': 3.826936, 'tm': ferry, 'name': "Ciutadella Ferry Terminal"},

            {'point': 0, 'city': 'ES-MJV', 'iata_code': 'MJV', 'icao_code': 'LELC', 'lat': 37.775330, 'lon': -0.818128, 'tm': flight, 'name': "Murcia-San Javier Airport"},
            {'point': 1, 'city': 'ES-MJV', 'iata_code': 'XUT', 'icao_code':   None, 'lat': 37.974789, 'lon': -1.131521, 'tm': train, 'name': "Murcia Train Station"},
            {'point': 1, 'city': 'ES-MJV', 'iata_code':  None, 'icao_code':   None, 'lat': 37.986148, 'lon': -1.139506, 'tm': bus, 'name': "Murcia Bus Station"},
            # {'point': 2, 'city': 'ES-MJV', 'iata_code': 'RMU', 'icao_code': 'LEMI', 'lat': 37.804579, 'lon': -1.131442, 'tm': flight, 'name': "Región de Murcia Airport"},

            {'point': 1, 'city': 'ES-ORE', 'iata_code':  None, 'icao_code':   None, 'lat': 42.350393, 'lon': -7.872774, 'tm': train, 'name': "Ourense Train Station"}, #cambiado nombre de Orense por Ourense
            {'point': 2, 'city': 'ES-ORE', 'iata_code':  None, 'icao_code':   None, 'lat': 42.352409, 'lon': -7.879200, 'tm': bus, 'name': "Ourense Bus Station"},

            {'point': 1, 'city': 'ES-OVO', 'iata_code': 'OVI', 'icao_code':   None, 'lat': 43.366361, 'lon': -5.854861, 'tm': train, 'name': "Oviedo Train Station"},
            {'point': 2, 'city': 'ES-OVO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.369174, 'lon': -5.850884, 'tm': bus, 'name': "Oviedo Bus Station"},
            {'point': 3, 'city': 'ES-OVO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.375144, 'lon': -5.830167, 'tm': bus, 'name': "Oviedo Huca"},
            {'point': 4, 'city': 'ES-OVO', 'iata_code':  None, 'icao_code':   None, 'lat': 43.353768, 'lon': -5.871729, 'tm': bus, 'name': "Oviedo Facultades"},

            {'point': 1, 'city': 'ES-PAC', 'iata_code': 'PCI', 'icao_code':   None, 'lat': 42.015709, 'lon': -4.534135, 'tm': train, 'name': "Palencia Train Station"},
            {'point': 1, 'city': 'ES-PAC', 'iata_code':  None, 'icao_code':   None, 'lat': 42.016396, 'lon': -4.536837, 'tm': bus, 'name': "Palencia Bus Station"},

            {'point': 0, 'city': 'ES-PNA', 'iata_code': 'PNA', 'icao_code':  'LEPP', 'lat': 42.769390, 'lon': -1.643352, 'tm': flight, 'name': "Pamplona Airport"},
            {'point': 1, 'city': 'ES-PNA', 'iata_code': 'EEP', 'icao_code':   None, 'lat': 42.824981, 'lon': -1.661432, 'tm': train, 'name': "Pamplona Train Station"},
            {'point': 2, 'city': 'ES-PNA', 'iata_code':  None, 'icao_code':   None, 'lat': 42.811177, 'lon': -1.645215, 'tm': bus, 'name': "Pamplona Bus Station"},
            {'point': 3, 'city': 'ES-PNA', 'iata_code':  None, 'icao_code':   None, 'lat': 42.805163, 'lon': -1.663026, 'tm': bus, 'name': "Pamplona Av. de Pío XII"},

            {'point': 1, 'city': 'ES-PON', 'iata_code':  None, 'icao_code':   None, 'lat': 42.545432, 'lon': -6.602360, 'tm': train, 'name': "Ponferrada Train Station"},
            {'point': 2, 'city': 'ES-PON', 'iata_code':  None, 'icao_code':   None, 'lat': 42.553082, 'lon': -6.601381, 'tm': bus, 'name': "Ponferrada Bus Station"},

            {'point': 1, 'city': 'ES-PEV', 'iata_code':  None, 'icao_code':   None, 'lat': 42.421765, 'lon': -8.635828, 'tm': train, 'name': "Pontevedra Train Station"},
            {'point': 1, 'city': 'ES-PEV', 'iata_code':  None, 'icao_code':   None, 'lat': 42.421108, 'lon': -8.637263, 'tm': bus, 'name': "Pontevedra Bus Station"},
            {'point': 2, 'city': 'ES-PEV', 'iata_code':  None, 'icao_code':   None, 'lat':    42.428, 'lon':  -8.65163, 'tm': bus, 'name': "Pontevedra Av. Marín"},

            {'point': 0, 'city': 'ES-REU', 'iata_code': 'REU', 'icao_code': 'LERS', 'lat': 41.146986, 'lon': 1.153716, 'tm': flight, 'name': "Reus Airport"},
            {'point': 1, 'city': 'ES-REU', 'iata_code':  None, 'icao_code':   None, 'lat': 41.160492, 'lon': 1.100055, 'tm': train, 'name': "Reus Train Station"},
            {'point': 1, 'city': 'ES-REU', 'iata_code':  None, 'icao_code':   None, 'lat': 41.147479, 'lon': 1.111940, 'tm': bus, 'name': "Reus Bus Station"},

            {'point': 1, 'city': 'ES-RNA', 'iata_code':  None, 'icao_code':   None, 'lat': 36.748392, 'lon': -5.161970, 'tm': train, 'name': "Ronda Train Station"},
            {'point': 2, 'city': 'ES-RNA', 'iata_code':  None, 'icao_code':   None, 'lat': 36.746835, 'lon': -5.165696, 'tm': bus, 'name': "Ronda Bus Station"},

            {'point': 0, 'city': 'ES-SLM', 'iata_code': 'SLM', 'icao_code': 'LESA', 'lat': 40.949515, 'lon': -5.497535, 'tm': flight, 'name': "Salamanca Airport"},
            {'point': 1, 'city': 'ES-SLM', 'iata_code':  None, 'icao_code':   None, 'lat': 40.972125, 'lon': -5.648571, 'tm': train, 'name': "Salamanca Train Station"},
            {'point': 2, 'city': 'ES-SLM', 'iata_code':  None, 'icao_code':   None, 'lat': 40.970396, 'lon': -5.674963, 'tm': bus, 'name': "Salamanca Bus Station"},

            {'point': 0, 'city': 'ES-SDR', 'iata_code': 'SDR', 'icao_code': 'LEXJ', 'lat': 43.423292, 'lon': -3.824253, 'tm': flight, 'name': "Santander Airport"},
            {'point': 0, 'city': 'ES-SDR', 'iata_code':  None, 'icao_code':   None, 'lat': 43.422953, 'lon': -3.824349, 'tm': bus, 'name': "Santander Airport Bus Station"},
            {'point': 1, 'city': 'ES-SDR', 'iata_code': 'YJL', 'icao_code':   None, 'lat': 43.458560, 'lon': -3.811078, 'tm': train, 'name': "Santander Train Station"},
            {'point': 1, 'city': 'ES-SDR', 'iata_code':  None, 'icao_code':   None, 'lat': 43.459506, 'lon': -3.809675, 'tm': bus, 'name': "Santander Bus Station"},

            {'point': 0, 'city': 'ES-SCQ', 'iata_code': 'SCQ', 'icao_code': 'LEST', 'lat': 42.895253, 'lon': -8.422116, 'tm': flight, 'name': "Santiago de Compostela Airport"},
            {'point': 0, 'city': 'ES-SCQ', 'iata_code':  None, 'icao_code':   None, 'lat': 42.892020, 'lon': -8.421367, 'tm': train, 'name': "Santiago de Compostela Airport Bus Station"},
            {'point': 1, 'city': 'ES-SCQ', 'iata_code':  None, 'icao_code':   None, 'lat': 42.870841, 'lon': -8.544695, 'tm': train, 'name': "Santiago de Compostela Train Station"},
            {'point': 1, 'city': 'ES-SCQ', 'iata_code':  None, 'icao_code':   None, 'lat': 42.887520, 'lon': -8.533618, 'tm': bus, 'name': "Santiago de Compostela Bus Station"},

            {'point': 1, 'city': 'ES-SEG', 'iata_code':  None, 'icao_code':   None, 'lat': 40.910198, 'lon': -4.094818, 'tm': train, 'name': "Segovia-Av Train Station"},
            {'point': 2, 'city': 'ES-SEG', 'iata_code':  None, 'icao_code':   None, 'lat': 40.944755, 'lon': -4.121614, 'tm': bus, 'name': "Segovia Bus Station"},
            {'point': 3, 'city': 'ES-SEG', 'iata_code':  None, 'icao_code':   None, 'lat': 40.934245, 'lon': -4.113536, 'tm': train, 'name': "Segovia Train Station"},

            {'point': 0, 'city': 'ES-SVQ', 'iata_code': 'SVQ', 'icao_code': 'LEZL', 'lat': 37.420167, 'lon': -5.893048, 'tm': flight, 'name': "Sevilla Airport"},
            {'point': 0, 'city': 'ES-SVQ', 'iata_code':  None, 'icao_code':   None, 'lat': 37.423594, 'lon': -5.901126, 'tm': bus, 'name': "Sevilla Airport"},
            {'point': 1, 'city': 'ES-SVQ', 'iata_code': 'XQA', 'icao_code':   None, 'lat': 37.391863, 'lon': -5.975338, 'tm': train, 'name': "Sevilla Santa Justa"},
            {'point': 1, 'city': 'ES-SVQ', 'iata_code':  None, 'icao_code':   None, 'lat': 37.391400, 'lon': -5.972930, 'tm': bus, 'name': "Sevilla Santa Justa"},
            {'point': 2, 'city': 'ES-SVQ', 'iata_code':  None, 'icao_code':   None, 'lat': 37.391868, 'lon': -6.003950, 'tm': bus, 'name': "Sevilla Plaza de Armas"},
            {'point': 3, 'city': 'ES-SVQ', 'iata_code':  None, 'icao_code':   None, 'lat': 37.381143, 'lon': -5.984962, 'tm': bus, 'name': "Sevilla Prado de San Sebastián"},
            {'point': 4, 'city': 'ES-SVQ', 'iata_code':  None, 'icao_code':   None, 'lat': 37.287376, 'lon': -5.923646, 'tm': train, 'name': "Sevilla Dos Hermanas"},

            {'point': 1, 'city': 'ES-SOR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.754754, 'lon': -2.476536, 'tm': train, 'name': "Soria Train Station"},
            {'point': 2, 'city': 'ES-SOR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.767069, 'lon': -2.479309, 'tm': bus, 'name': "Soria Bus Station"},

            {'point': 1, 'city': 'ES-TAR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.111624, 'lon': 1.253216, 'tm': train, 'name': "Tarragona Estació de Tren"},
            {'point': 1, 'city': 'ES-TAR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.111493, 'lon': 1.252895, 'tm': bus, 'name': "Tarragona Estació de Tren"},
            {'point': 2, 'city': 'ES-TAR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.192291, 'lon': 1.273246, 'tm': train, 'name': "Camp de Tarragona"},
            {'point': 3, 'city': 'ES-TAR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.118249, 'lon': 1.244296, 'tm': bus, 'name': "Tarragona Estació d'Autobusos"},

            {'point': 0, 'city': 'ES-TCI', 'iata_code': 'TFS', 'icao_code': 'LETS', 'lat': 28.045771, 'lon': -16.576219, 'tm': flight, 'name': "Tenerife South Airport"},
            {'point': 1, 'city': 'ES-TCI', 'iata_code': 'TFN', 'icao_code': 'GCXO', 'lat': 28.484504, 'lon': -16.343422, 'tm': flight, 'name': "Tenerife North Airport"},
            # {'point': 2, 'city': 'ES-TCI', 'iata_code':  None, 'icao_code':   None, 'lat': 28.477329, 'lon': -16.241673, 'tm': ferry, 'name': "Tenerife Ferry Terminal"},

            # {'point': 0, 'city': 'ES-TER', 'iata_code': 'TEV', 'icao_code': 'LETL', 'lat': 40.409912, 'lon': -1.219571, 'tm': flight, 'name': "Teruel Airport"}, currently not used
            {'point': 1, 'city': 'ES-TER', 'iata_code':  None, 'icao_code':   None, 'lat': 40.341028, 'lon': -1.110283, 'tm': train, 'name': "Teruel Train Station"},
            {'point': 2, 'city': 'ES-TER', 'iata_code':  None, 'icao_code':   None, 'lat': 40.341838, 'lon': -1.104477, 'tm': bus, 'name': "Teruel Bus Station"},

            {'point': 1, 'city': 'ES-TOL', 'iata_code':  None, 'icao_code':   None, 'lat': 39.862272, 'lon': -4.011242, 'tm': train, 'name': "Toledo Train Station"},
            {'point': 2, 'city': 'ES-TOL', 'iata_code':  None, 'icao_code':   None, 'lat': 39.865828, 'lon': -4.020383, 'tm': bus, 'name': "Toledo Bus Station"},

            {'point': 0, 'city': 'ES-VLC', 'iata_code': 'VLC', 'icao_code': 'LEVC', 'lat': 39.489224, 'lon': -0.478023, 'tm': flight, 'name': "Valencia Airport"}, #cambiado de sitio y colocado por orden alfabético
            {'point': 0, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.491780, 'lon': -0.473472, 'tm': bus, 'name': "Valencia Airport Bus Station"},
            {'point': 1, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.460040, 'lon': -0.381677, 'tm': train, 'name': "Valencia Joaquín Sorolla"},
            {'point': 1, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.458930, 'lon': -0.382800, 'tm': bus, 'name': "Valencia Joaquín Sorolla"},
            {'point': 2, 'city': 'ES-VLC', 'iata_code': 'YJV', 'icao_code':   None, 'lat': 39.465962, 'lon': -0.377464, 'tm': train, 'name': "Valencia Nord"},
            {'point': 3, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.480407, 'lon': -0.387905, 'tm': bus, 'name': "Valencia Bus Station"},
            # {'point': 4, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.453360, 'lon': -0.323539, 'tm': ferry, 'name': "Valencia Ferry Terminal"},
            {'point': 4, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.435796, 'lon': -0.331562, 'tm': bus, 'name': "Valencia Moll de Ponent"},
            {'point': 5, 'city': 'ES-VLC', 'iata_code':  None, 'icao_code':   None, 'lat': 39.450117, 'lon': -0.403962, 'tm': train, 'name': "Valencia Sant Isidre"},

            {'point': 0, 'city': 'ES-VLL', 'iata_code': 'VLL', 'icao_code': 'LEVD', 'lat': 41.709917, 'lon': -4.855052, 'tm': flight, 'name': "Valladolid Airport"},
            {'point': 0, 'city': 'ES-VLL', 'iata_code':  None, 'icao_code':   None, 'lat': 41.706041, 'lon': -4.844599, 'tm': bus, 'name': "Valladolid Airport Bus Station"},
            {'point': 1, 'city': 'ES-VLL', 'iata_code': 'XIV', 'icao_code':   None, 'lat': 41.642166, 'lon': -4.726979, 'tm': train, 'name': "Valladolid-Campo Grande"},
            {'point': 1, 'city': 'ES-VLL', 'iata_code': 'XJN', 'icao_code':   None, 'lat': 41.641396, 'lon': -4.732192, 'tm': bus, 'name': "Valladolid-Campo Grande"},

            {'point': 0, 'city': 'ES-VGO', 'iata_code': 'VGO', 'icao_code': 'LEVX', 'lat': 42.225373, 'lon': -8.632597, 'tm': flight, 'name': "Vigo Airport"},
            {'point': 0, 'city': 'ES-VGO', 'iata_code':  None, 'icao_code':   None, 'lat': 42.224935, 'lon': -8.633313, 'tm': bus, 'name': "Vigo Airport"},
            {'point': 1, 'city': 'ES-VGO', 'iata_code': 'YJR', 'icao_code':   None, 'lat': 42.239738, 'lon': -8.711656, 'tm': train, 'name': "Vigo-Guixar"},
            {'point': 1, 'city': 'ES-VGO', 'iata_code':  None, 'icao_code':   None, 'lat': 42.224255, 'lon': -8.709298, 'tm': bus, 'name': "Vigo Bus Station"},
            {'point': 2, 'city': 'ES-VGO', 'iata_code':  None, 'icao_code':   None, 'lat': 42.234205, 'lon': -8.713723, 'tm': train, 'name': "Vigo-Urzáiz"},

            {'point': 0, 'city': 'ES-VIT', 'iata_code': 'VIT', 'icao_code': 'LEVT', 'lat': 42.883389, 'lon': -2.731344, 'tm': flight, 'name': "Vitoria Airport"},
            {'point': 1, 'city': 'ES-VIT', 'iata_code':  None, 'icao_code':   None, 'lat': 42.841518, 'lon': -2.672601, 'tm': train, 'name': "Vitoria-Gasteiz Train Station"},
            {'point': 2, 'city': 'ES-VIT', 'iata_code': 'VTI', 'icao_code':   None, 'lat': 42.859114, 'lon': -2.684405, 'tm': bus, 'name': "Vitoria-Gasteiz Bus Station"},

            {'point': 1, 'city': 'ES-ZMR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.515891, 'lon': -5.739674, 'tm': train, 'name': "Zamora Train Station"},
            {'point': 1, 'city': 'ES-ZMR', 'iata_code':  None, 'icao_code':   None, 'lat': 41.513891, 'lon': -5.739675, 'tm': bus, 'name': "Zamora Bus Station"},

            {'point': 0, 'city': 'ES-ZAZ', 'iata_code': 'ZAZ', 'icao_code': 'LEZG', 'lat': 41.663508, 'lon': -1.007926, 'tm': flight, 'name': "Zaragoza Airport"},
            {'point': 0, 'city': 'ES-ZAZ', 'iata_code':  None, 'icao_code':   None, 'lat': 41.663118, 'lon': -1.007702, 'tm': bus, 'name': "Zaragoza Airport"},
            {'point': 1, 'city': 'ES-ZAZ', 'iata_code': 'XZZ', 'icao_code':   None, 'lat': 41.658693, 'lon': -0.911225, 'tm': train, 'name': "Zaragoza-Delicias"},
            {'point': 1, 'city': 'ES-ZAZ', 'iata_code': 'RZG', 'icao_code':   None, 'lat': 41.659406, 'lon': -0.911230, 'tm': bus, 'name': "Zaragoza-Delicias"},
            {'point': 2, 'city': 'ES-ZAZ', 'iata_code':  None, 'icao_code':   None, 'lat': 41.650361, 'lon': -0.887395, 'tm': bus, 'name': "Zaragoza Puerta del Carmen"},
            {'point': 3, 'city': 'ES-ZAZ', 'iata_code':  None, 'icao_code':   None, 'lat': 41.633601, 'lon': -0.868221, 'tm': train, 'name': "Zaragoza Miraflores"},
        ]

        hubs_PT = [
            {'point': 1, 'city': 'PT-ALM', 'iata_code':  None, 'icao_code':  None, 'lat': 38.666323, 'lon': -9.179880, 'tm': train, 'name': "Almada Pragal"},
            {'point': 2, 'city': 'PT-ALM', 'iata_code':  None, 'icao_code':  None, 'lat': 38.667595, 'lon': -9.163809, 'tm': bus, 'name': "Almada Centro Sul"},

            # {'point': 1, 'city': 'PT-AMA', 'iata_code':  None, 'icao_code':  None, 'lat': 38.759691, 'lon': -9.235858, 'tm': train, 'name': "Amadora Avenida de Gago Coutinho"},
            # {'point': 2, 'city': 'PT-AMA', 'iata_code':  None, 'icao_code':  None, 'lat': 38.752624, 'lon': -9.209529, 'tm': bus, 'name': "Amadora Portas de Benfica"},

            {'point': 1, 'city': 'PT-AVE', 'iata_code':  None, 'icao_code':  None, 'lat': 40.643462, 'lon': -8.640545, 'tm': train, 'name': "Estação de Aveiro"},
            {'point': 1, 'city': 'PT-AVE', 'iata_code':  None, 'icao_code':  None, 'lat': 40.643991, 'lon': -8.638292, 'tm': bus, 'name': "Estação de Aveiro"},

            # {'point': 0, 'city': 'PT-BGZ', 'iata_code': 'BGZ', 'icao_code': 'LPBR', 'lat': 41.586944, 'lon': -8.445000, 'tm': flight, 'name': "Braga Airport"}, #no flights
            {'point': 1, 'city': 'PT-BGZ', 'iata_code': None, 'icao_code': None, 'lat': 41.548730, 'lon': -8.434128, 'tm': train, 'name': "Braga Rua Nova da Estação"},
            {'point': 2, 'city': 'PT-BGZ', 'iata_code': None, 'icao_code': None, 'lat': 41.555628, 'lon': -8.425205, 'tm': bus, 'name': "Braga General Norton de Matos "},

            {"point": 0, "city": "PT-BGC", "iata_code": "BGC", "icao_code": "LPBG", "lat": 41.856667, "lon": -6.707500, "tm": flight, "name": "Bragança Airport"},
            {"point": 1, "city": "PT-BGC", "iata_code": None, "icao_code": None, "lat": 41.809430, "lon": -6.760859, "tm": bus, "name": "Estaçao de Bragança"},

            {"point": 0, "city": "PT-CAS", "iata_code": "LCT", "icao_code": "LPCS", "lat": 38.725556, "lon": -9.355278, "tm": flight, "name": "Cascais Aerodrome"},
            {"point": 1, "city": "PT-CAS", "iata_code": None, "icao_code": None, "lat": 38.700714, "lon": -9.418576, "tm": train, "name": "Cascais Largo Estação"},
            {"point": 2, "city": "PT-CAS", "iata_code": None, "icao_code": None, "lat": 38.701524, "lon": -9.419938, "tm": bus, "name": "Cascais Costa Pinto"},

            # {'point': 0, 'city': 'PT-CBP', 'iata_code': 'CBP', 'icao_code': 'LPCO', 'lat': 40.156111, 'lon': -8.470000, 'tm': flight, 'name': "Coimbra Bissaya Barreto Aerodrome"},
            {'point': 1, 'city': 'PT-CBP', 'iata_code': None, 'icao_code': None, 'lat': 40.224365, 'lon': -8.440467, 'tm': train, 'name': "Coimbra-B"},
            {'point': 2, 'city': 'PT-CBP', 'iata_code': None, 'icao_code': None, 'lat': 40.216418, 'lon': -8.437256, 'tm': bus, 'name': "Coimbra Central Bus Station"},

            {'point': 0, 'city': 'PT-CVU', 'iata_code': 'CVU', 'icao_code': 'LPCR', 'lat': 39.670833, 'lon': -31.112778, 'tm': flight, 'name': "Corvo Airport"},
           # {'point': 1, 'city': 'PT-CVU', 'iata_code': None, 'icao_code': None, 'lat': 39.671870, 'lon': -31.109778, 'tm': ferry, 'name': "Vila Nova de Corvo"},

            {'point': 1, 'city': 'PT-ENT', 'iata_code': None, 'icao_code': None, 'lat': 39.461562, 'lon': -8.474166, 'tm': train, 'name': 'Entroncamento'},
            # {'point': 1, 'city': 'PT-ENT', 'iata_code': None, 'icao_code': None, 'lat': 39.461562, 'lon': -8.474166, 'tm': bus, 'name': 'Entroncamento'}, #no buses in busbud

            {"point": 0, "city": "PT-HOR", "iata_code": "HOR", "icao_code": "LPHR", "lat": 38.520000, "lon": -28.716389, "tm": flight, "name": "Horta Airport"},
            # {"point": 1, "city": "PT-HOR", "iata_code": None, "icao_code": None, "lat": 38.537779, "lon": -28.622050, "tm": ferry, "name": "Horta Terminal"},

            {'point': 0, 'city': 'PT-FAO', 'iata_code': 'FAO', 'icao_code':'LPFR', 'lat': 37.0144, 'lon': -7.96583, 'tm': flight, 'name': "Faro Airport"},
            {'point': 0, 'city': 'PT-FAO', 'iata_code':  None, 'icao_code':  None, 'lat': 37.021098, 'lon': -7.969147, 'tm': bus, 'name': "Faro Airport"},
            {'point': 1, 'city': 'PT-FAO', 'iata_code':  None, 'icao_code':  None, 'lat': 37.018547, 'lon': -7.939754, 'tm': train, 'name': "Faro Station"},
            {'point': 2, 'city': 'PT-FAO', 'iata_code':  None, 'icao_code':  None, 'lat': 37.017258, 'lon': -7.937888, 'tm': bus, 'name': "Faro Rodoviario"},

            {"point": 0, "city": "PT-SCF", "iata_code": "FLW", "icao_code": "LPFL", "lat": 39.45856, "lon": -31.132222, "tm": flight, "name": "Flores Airport"},
            # {"point": 1, "city": "PT-SCF", "iata_code": None, "icao_code": None, "lat": 39.378439, "lon": -31.167323, "tm": ferry, "name": "Flores Lajes"},

            {'point': 0, 'city': 'PT-LIS', 'iata_code': 'LIS', 'icao_code':'LPPT', 'lat': 38.774167, 'lon': -9.134167, 'tm': flight, 'name': "Lisbon Airport"},
            {'point': 0, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.769710, 'lon': -9.128072, 'tm': bus, 'name': "Lisbon Airport"},
            {'point': 1, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.767834, 'lon': -9.099356, 'tm': train, 'name': "Lisbon Oriente"},
            {'point': 1, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.767834, 'lon': -9.101154, 'tm': bus, 'name': "Lisbon Oriente"},
            {'point': 2, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.713649, 'lon': -9.123213, 'tm': train, 'name': "Lisbon Santa Apolónia"},
            {'point': 3, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.739689, 'lon': -9.167625, 'tm': bus, 'name': "Lisbon Sete Rios"},
            {'point': 4, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.744569, 'lon': -9.148638, 'tm': train, 'name': "Lisbon Entrecampos"},
            # {'point': 5, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.705096, 'lon': -9.144978, 'tm': ferry, 'name': "Lisbon Cais do Sodré"},
            # {'point': 6, 'city': 'PT-LIS', 'iata_code':  None, 'icao_code':  None, 'lat': 38.695038, 'lon': -9.198707, 'tm': ferry, 'name': "Lisbon Belem"},

            {"point": 0, "city": "PT-M6E", "iata_code": "FNC", "icao_code": "LPMA", "lat": 32.694167, "lon": -16.778056, "tm": flight, "name": "Madeira Airport"},
            # {"point": 1, "city": "PT-FNC", "iata_code": None, "icao_code": None, "lat": 32.647331, "lon": -16.902707, "tm": bus, "name": "Funchal Teleférico-Término"}, #bus in island not useful
            # {"point": 2, "city": "PT-FNC", "iata_code": None, "icao_code": None, "lat": 32.647322, "lon": -16.914312, "tm": bus, "name": "Funchal La vie"}, #bus in island not useful
            # # {"point": 3, "city": "PT-FNC", "iata_code": None, "icao_code": None, "lat": 32.641142, "lon": -16.915807, "tm": ferry, "name": "Funchal Santo Line"},

            {"point": 0, "city": "PT-MAD", "iata_code": "PIX", "icao_code": "LPPI", "lat": 38.5544, "lon": -28.4414, "tm": flight, "name": "Pico Airport"},
            # {"point": 1, "city": "PT-MAD", "iata_code": None, "icao_code": Nini, "lat": 38.535398, "lon": -28.529571, "tm": ferry, "name": "Pico João Quaresma"},
            # {"point": 2, "city": "PT-MAD", "iata_code": None, "icao_code": Nini, "lat": 38.530871, "lon": -28.319077, "tm": ferry, "name": "Pico Sao Roque"},

            {"point": 0, "city": "PT-PRM", "iata_code": "PRM", "icao_code": "LPPM", "lat": 37.147500, "lon": -8.579722, "tm": flight, "name": "Portimão Airport"},
            {"point": 1, "city": "PT-PRM", "iata_code": None, "icao_code": None, "lat": 37.144568, "lon": -8.537556, "tm": train, "name": "Portimão Largo Gil Eanes"},
            {"point": 2, "city": "PT-PRM", "iata_code": None, "icao_code": None, "lat": 37.136649, "lon": -8.535514, "tm": bus, "name": "Portimão Largo do Dique"},
            {"point": 3, "city": "PT-PRM", "iata_code": None, "icao_code": None, "lat": 37.146863, "lon": -8.535733, "tm": bus, "name": "Rodoviária Portimao"},
            {"point": 4, "city": "PT-PRM", "iata_code": None, "icao_code": None, "lat": 37.121667, "lon": -8.537833, "tm": bus, "name": "Portimão Av. das Comunidades Lusíadas"},

            {"point": 0, "city": "PT-PXO", "iata_code": "PXO", "icao_code": "LPPS", "lat": 33.070833, "lon": -16.349722, "tm": flight, "name": "Porto Santo Airport"},
            {"point": 1, "city": "PT-PXO", "iata_code": None, "icao_code": None, "lat": 33.059038, "lon": -16.334045, "tm": bus, "name": "Porto Santo ER111"}, # No estic segura
            # {"point": 1, "city": "PT-PXO", "iata_code": None, "icao_code": None, "lat": 33.058723, "lon": -16.312020, "tm": ferry, "name": "Porto Santo"},

            {'point': 0, 'city': 'PT-OPO', 'iata_code': 'OPO', 'icao_code':'LPPR', 'lat': 41.235556, 'lon': -8.678056, 'tm': flight, 'name': "Porto Airport"},
            {'point': 0, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.236416, 'lon': -8.669942, 'tm': bus, 'name': "Porto Airport"},
            {'point': 1, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.145659, 'lon': -8.610526, 'tm': train, 'name': "Porto Sao Bento"},
            {'point': 1, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.144306, 'lon': -8.605690, 'tm': bus, 'name': "Porto Sao Bento"}, #iata = ZYJ?
            {'point': 2, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.149620, 'lon': -8.585521, 'tm': train, 'name': "Porto-Campanhã"},
            {'point': 2, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.148959, 'lon': -8.585723, 'tm': bus, 'name': "Porto-Campanhã"},
            {'point': 3, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.161117, 'lon': -8.629924, 'tm': bus, 'name': "Porto Casa da Musica"},
            {'point': 4, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.129677, 'lon': -8.620197, 'tm': train, 'name': "Vila Nova de Gaia"},
            {'point': 5, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.145060, 'lon': -8.616355, 'tm': bus, 'name': "Porto Campo Martires de Patria"},
            {'point': 6, 'city': 'PT-OPO', 'iata_code':  None, 'icao_code':  None, 'lat': 41.144148, 'lon': -8.605622, 'tm': bus, 'name': "Porto Garagem Atlântico"},

            {"point": 0, "city": "PT-VDP", "iata_code": "SMA", "icao_code": "LPAZ", "lat": 36.973889, "lon": -25.171111, "tm": flight, "name": "Santa Maria Airport"},
            # {"point": 1, "city": "PT-VDP", "iata_code": None, "icao_code": None, "lat": 36.941477, "lon": -25.148567, "tm": ferry, "name": "Santa Maria Vila do Porto"},

            {'point': 0, 'city': 'PT-PDL', 'iata_code': 'PDL', 'icao_code': 'LPPD', 'lat': 37.741944, 'lon': -25.697778, 'tm': flight, 'name': "Ponta Delgada Airport"},
            # {'point': 1, 'city': 'PT-PDL', 'iata_code': None, 'icao_code': None, 'lat': 37.897724, 'lon': -25.756627, 'tm': bus, 'name': "Ponta Delgada EN1-1A"}, #bus in island not useful
            # {'point': 2, 'city': 'PT-PDL', 'iata_code': None, 'icao_code': None, 'lat': 37.736271, 'lon': -25.656255, 'tm': ferry, 'name': "Ponta Delgada Molhe do Porto"},

            {'point': 0, 'city': 'PT-LDP', 'iata_code': 'TER', 'icao_code':'LPLA', 'lat': 38.761944, 'lon': -27.090833, 'tm': flight, 'name': "Lajes Airport"},
            {'point': 1, 'city': 'PT-LDP', 'iata_code': None, 'icao_code': None, 'lat': 38.731689, 'lon': -27.065568, 'tm': bus, 'name': "Praia da Vitória Comendador Francisco José B. Barcelos"},
            # {'point': 2, 'city': 'PT-LDP', 'iata_code': None, 'icao_code': None, 'lat': 38.711692, 'lon': -27.052456, 'tm': ferry, 'name': "Praia da Vitória"},

            {"point": 0, "city": "PT-VRL", "iata_code": "VRL", "icao_code": "LPVR", "lat": 41.277500, "lon": -7.719722, "tm": flight, "name": "Vila Real Airport"},
            {"point": 1, "city": "PT-VRL", "iata_code": None, "icao_code": None, "lat": 41.294191, "lon": -7.738659, "tm": train, "name": "Vila Real Monsenhor Jerónimo de Amaral"},
            {"point": 2, "city": "PT-VRL", "iata_code": None, "icao_code": None, "lat": 41.299665, "lon": -7.750154, "tm": bus, "name": "Vila Real Dom António Valente da Fonseca"},

            {"point": 0, "city": "PT-VSE", "iata_code": "VSE", "icao_code": "LPVZ", "lat": 40.727778, "lon": -7.889167, "tm": flight, "name": "Viseu Airport"},
            {"point": 1, "city": "PT-VSE", "iata_code": None, "icao_code": None, "lat": 40.661188, "lon": -7.915810, "tm": bus, "name": "Viseu R. Bombeiros Voluntários"},
        ]

        hubs_FR = [
            {'point': 0, 'city': 'FR-AGF', 'iata_code':'AGF', 'icao_code':'LFBA', 'lat': 44.176230, 'lon': 0.594481, 'tm': flight, 'name': "Agen Airport"},
            {'point': 1, 'city': 'FR-AGF', 'iata_code': None, 'icao_code':  None, 'lat': 44.208175, 'lon': 0.620893, 'tm': train, 'name': "Gare d'Agen"},
            {'point': 1, 'city': 'FR-AGF', 'iata_code': None, 'icao_code':  None, 'lat': 44.208288, 'lon': 0.619743, 'tm': bus, 'name': "Gare d'Agen"},
            {'point': 2, 'city': 'FR-AGF', 'iata_code': None, 'icao_code':  None, 'lat': 44.166440, 'lon': 0.606315, 'tm': bus, 'name': "Agen Le Passage"},

            {'point': 1, 'city': 'FR-QXB', 'iata_code': None, 'icao_code': None, 'lat': 43.455132, 'lon': 5.317243, 'tm': train, 'name': "Aix-en-Provence TGV Train Station"},
            {'point': 1, 'city': 'FR-QXB', 'iata_code': None, 'icao_code': None, 'lat': 43.455521, 'lon': 5.316610, 'tm': bus, 'name': "Aix-en-Provence TGV Bus Station"},
            {'point': 2, 'city': 'FR-QXB', 'iata_code': None, 'icao_code': None, 'lat': 43.522876, 'lon': 5.445321, 'tm': train, 'name': "Aix-en-Provence Train Station"},
            {'point': 2, 'city': 'FR-QXB', 'iata_code': None, 'icao_code': None, 'lat': 43.523533, 'lon': 5.440484, 'tm': bus, 'name': "Aix-en-Provence Routière Bus Station"},

           {'point': 0, 'city': 'FR-AJA', 'iata_code':'AJA', 'icao_code':'LFKJ', 'lat': 41.919777, 'lon': 8.794267, 'tm': flight, 'name': "Ajaccio Airport"},
           {'point': 1, 'city': 'FR-AJA', 'iata_code': None, 'icao_code':  None, 'lat': 41.927329, 'lon': 8.739036, 'tm': train, 'name': "Ajaccio Train Station"},
           {'point': 1, 'city': 'FR-AJA', 'iata_code': None, 'icao_code':  None, 'lat': 41.927340, 'lon': 8.738349, 'tm': bus, 'name': "Ajaccio TCA Bus Station"},
           # {'point': 2, 'city': 'FR-AJA', 'iata_code': None, 'icao_code': None, 'lat': 41.922094, 'lon': 8.742659, 'tm': ferry, 'name': "Ajaccio Ferry Terminal"},

           {'point': 1, 'city': 'FR-AMI', 'iata_code': None, 'icao_code': None, 'lat': 49.890536, 'lon': 2.308135, 'tm': train, 'name': "Amiens Train Station"}, #name it Amiens Routière?
           {'point': 1, 'city': 'FR-AMI', 'iata_code': None, 'icao_code': None, 'lat': 49.891107, 'lon': 2.308390, 'tm': bus, 'name': "Amiens Bus Station"},
           # {'point': 2, 'city': 'FR-AMI', 'iata_code': None, 'icao_code': None, 'lat': 49.890539, 'lon': 2.308134, 'tm': train, 'name': "Amiens Routière Train Station"},
           # {'point': 2, 'city': 'FR-AMI', 'iata_code': None, 'icao_code': None, 'lat': 49.891102, 'lon': 2.308385, 'tm': bus, 'name': "Amiens Routière Bus Station"},

           {'point': 1, 'city': 'FR-ANE', 'iata_code': None, 'icao_code': None, 'lat': 47.464602, 'lon': -0.556217, 'tm': train, 'name': "Gare d'Angers Saint-Laud"},
           {'point': 1, 'city': 'FR-ANE', 'iata_code': None, 'icao_code': None, 'lat': 47.464963, 'lon': -0.559301, 'tm': bus, 'name': "Gare d'Angers Saint-Laud"},

            {'point': 0, 'city': 'FR-AUR', 'iata_code':'AUR', 'icao_code':'LFLW', 'lat': 44.897808, 'lon': 2.420641, 'tm': flight, 'name': "Aurillac Airport"},
            {'point': 1, 'city': 'FR-AUR', 'iata_code': None, 'icao_code':  None, 'lat': 44.921111, 'lon': 2.435780, 'tm': train, 'name': "Aurillac Train Station"},

            {'point': 0, 'city': 'FR-BIA', 'iata_code':'BIA', 'icao_code':'LFKB', 'lat': 42.552418, 'lon': 9.482551, 'tm': flight, 'name': "Bastia Airport"},
            {'point': 1, 'city': 'FR-BIA', 'iata_code': None, 'icao_code':  None, 'lat': 42.702196, 'lon': 9.447682, 'tm': train, 'name': "Bastia Train Station"},
            {'point': 1, 'city': 'FR-BIA', 'iata_code': None, 'icao_code':  None, 'lat': 42.702430, 'lon': 9.451493, 'tm': bus, 'name': "Bastia Bus Station"},
            # # {'point': 2, 'city': 'FR-BIA', 'iata_code': None, 'icao_code': None, 'lat': 42.701354, 'lon': 9.453319, 'tm': ferry, 'name': "Bastia Ferry Terminal"},

            {'point': 0, 'city': 'FR-BVA', 'iata_code':'BVA', 'icao_code':'LFOB', 'lat': 49.454468, 'lon': 2.111509, 'tm': flight, 'name': "Beauvais Airport"},
            {'point': 0, 'city': 'FR-BVA', 'iata_code': None, 'icao_code':  None, 'lat': 49.459469, 'lon': 2.110795, 'tm': bus, 'name': "Beauvais Airport"},
            {'point': 1, 'city': 'FR-BVA', 'iata_code': None, 'icao_code':  None, 'lat': 49.426391, 'lon': 2.088749, 'tm': train, 'name': "Beauvais Train Station"},
            {'point': 1, 'city': 'FR-BVA', 'iata_code': None, 'icao_code':  None, 'lat': 49.426403, 'lon': 2.088542, 'tm': bus, 'name': "Beauvais Bus Station"},

            {'point': 0, 'city': 'FR-EGC', 'iata_code': 'EGC', 'icao_code':'LFBE', 'lat': 44.823671, 'lon': 0.518692, 'tm': flight, 'name': "Bergerac Airport"},
            {'point': 1, 'city': 'FR-EGC', 'iata_code': None, 'icao_code': None, 'lat': 44.857248, 'lon': 0.489307, 'tm': train, 'name': "Bergerac Train Station"},
            {'point': 1, 'city': 'FR-EGC', 'iata_code': None, 'icao_code': None, 'lat': 44.856932, 'lon': 0.488803, 'tm': bus, 'name': "Bergerac Bus Station"},

            {'point': 1, 'city': 'FR-BSN', 'iata_code': None, 'icao_code': None, 'lat': 47.247051, 'lon': 6.021939, 'tm': train, 'name': "Besançon-Viotte"},
            {'point': 1, 'city': 'FR-BSN', 'iata_code': None, 'icao_code': None, 'lat': 47.246913, 'lon': 6.022411, 'tm': bus, 'name': "Besançon-Viotte"},
            {'point': 2, 'city': 'FR-BSN', 'iata_code': None, 'icao_code': None, 'lat': 47.307236, 'lon': 5.953348, 'tm': train, 'name': "Besançon Franche-Comté"},
            {'point': 3, 'city': 'FR-BSN', 'iata_code': None, 'icao_code': None, 'lat':   47.2777, 'lon':  5.99394, 'tm': bus, 'name': "Besançon Rue de Châtillon"},

            {'point': 0, 'city': 'FR-BZR', 'iata_code': 'BZR', 'icao_code':'LFMU', 'lat': 43.322207, 'lon': 3.354857, 'tm': flight, 'name': "Béziers Airport"},
            {'point': 1, 'city': 'FR-BZR', 'iata_code': None, 'icao_code': None, 'lat': 43.336286, 'lon': 3.218893, 'tm': train, 'name': "Gare de Béziers"},
            {'point': 1, 'city': 'FR-BZR', 'iata_code': None, 'icao_code': None, 'lat': 43.336312, 'lon': 3.219256, 'tm': bus, 'name': "Gare de Béziers"},
            {'point': 2, 'city': 'FR-BZR', 'iata_code': None, 'icao_code': None, 'lat': 43.345309, 'lon': 3.217999, 'tm': bus, 'name': "Béziers De Gaulle"},

            {'point': 0, 'city': 'FR-BIQ', 'iata_code': 'BIQ', 'icao_code': 'LFBZ', 'lat': 43.469193, 'lon':-1.530287, 'tm': flight, 'name': "Biarritz Airport"},
            {'point': 0, 'city': 'FR-BIQ', 'iata_code':  None, 'icao_code': None, 'lat': 43.472378, 'lon':-1.530947, 'tm': bus, 'name': "Biarritz Airport"},
            {'point': 1, 'city': 'FR-BIQ', 'iata_code':  None, 'icao_code': None, 'lat': 43.459360, 'lon': -1.545929, 'tm': train, 'name': "Gare de Biarritz"},
            {'point': 1, 'city': 'FR-BIQ', 'iata_code':  None, 'icao_code': None, 'lat': 43.459460, 'lon': -1.545567, 'tm': bus, 'name': "Gare de Biarritz"},
            {'point': 2, 'city': 'FR-BIQ', 'iata_code':  None, 'icao_code': None, 'lat': 43.477162, 'lon': -1.552869, 'tm': bus, 'name': "Biarritz Av. Charles Floquet"},

            {'point': 0, 'city': 'FR-BOD', 'iata_code': 'BOD', 'icao_code': 'LFBD', 'lat': 44.830593, 'lon': -0.710306, 'tm': flight, 'name': "Bordeaux Airport"},
            {'point': 1, 'city': 'FR-BOD', 'iata_code': 'ZFQ', 'icao_code': None, 'lat': 44.826432, 'lon': -0.556231, 'tm': train, 'name': "Bordeaux St-Jean"},
            {'point': 1, 'city': 'FR-BOD', 'iata_code':  None, 'icao_code': None, 'lat': 44.829828, 'lon': -0.555214, 'tm': bus, 'name': "Bordeaux St-Jean"},
            {'point': 2, 'city': 'FR-BOD', 'iata_code':  None, 'icao_code': None, 'lat': 44.795873, 'lon': -0.602145, 'tm': train, 'name': "Bordeaux Talence Université"},
            {'point': 3, 'city': 'FR-BOD', 'iata_code':  None, 'icao_code': None, 'lat': 44.856744, 'lon': -0.533629, 'tm': train, 'name': "Bordeaux Cenon"},
            # {'point': 4, 'city': 'FR-BOD', 'iata_code':  None, 'icao_code': None, 'lat': 44.796676, 'lon': -0.602545, 'tm': train, 'name': "Bordeaux Cours de la Libération"},
            {'point': 4, 'city': 'FR-BOD', 'iata_code':  None, 'icao_code': None, 'lat': 44.796676, 'lon': -0.602545, 'tm': bus, 'name': "Bordeaux Cours de la Libération"},

            {'point': 0, 'city': 'FR-BES', 'iata_code': 'BES', 'icao_code': 'LFRB', 'lat': 48.447638, 'lon': -4.417835, 'tm': flight, 'name': "Brest Airport"},
            {'point': 1, 'city': 'FR-BES', 'iata_code': None, 'icao_code': None, 'lat': 48.387717, 'lon': -4.480156, 'tm': train, 'name': "Brest Train Station"},
            {'point': 1, 'city': 'FR-BES', 'iata_code': None, 'icao_code': None, 'lat': 48.387712, 'lon': -4.482231, 'tm': bus, 'name': "Brest Bus Station"},

            {'point': 0, 'city': 'FR-BVE', 'iata_code': 'BVE', 'icao_code': 'LFSL', 'lat': 45.041371, 'lon': 1.490299, 'tm': flight, 'name': "Brive Airport"},
            {'point': 1, 'city': 'FR-BVE', 'iata_code': None, 'icao_code': None, 'lat': 45.152404, 'lon': 1.528640, 'tm': train, 'name': "Gare de Brive-la-Gaillarde"},
            {'point': 1, 'city': 'FR-BVE', 'iata_code': None, 'icao_code': None, 'lat': 45.152869, 'lon': 1.528455, 'tm': bus, 'name': "Gare de Brive-la-Gaillarde"},
            {'point': 2, 'city': 'FR-BVE', 'iata_code': None, 'icao_code': None, 'lat': 45.145928, 'lon': 1.482687, 'tm': bus, 'name': "Brive-la-Gaillarde Ouest"},

            {'point': 0, 'city': 'FR-CFR', 'iata_code': 'CFR', 'icao_code': 'LFRK', 'lat': 49.183274, 'lon':-0.459190, 'tm': flight, 'name': "Caen Airport"},
            {'point': 1, 'city': 'FR-CFR', 'iata_code': None, 'icao_code': None, 'lat': 49.176392, 'lon':-0.347589, 'tm': train, 'name': "Gare de Caen"},
            {'point': 1, 'city': 'FR-CFR', 'iata_code': None, 'icao_code': None, 'lat': 49.176486, 'lon': -0.346798, 'tm': bus, 'name': "Gare de Caen"},
            {'point': 2, 'city': 'FR-CFR', 'iata_code': None, 'icao_code': None, 'lat': 49.184017, 'lon': -0.356190, 'tm': bus, 'name': "Caen Port de Plaisance"},

            # {'point': 1, 'city': 'FR-CQF', 'iata_code': None, 'icao_code': None, 'lat': 50.966709, 'lon': 1.861798, 'tm': ferry, 'name': "Calais Ferry Terminal"},

            {'point': 0, 'city': 'FR-CLY', 'iata_code': 'CLY', 'icao_code': 'LFKC', 'lat': 42.525280, 'lon': 8.790033, 'tm': flight, 'name': "Calvi Airport"},
            {'point': 1, 'city': 'FR-CLY', 'iata_code': None, 'icao_code': None, 'lat': 42.564763, 'lon': 8.755946, 'tm': train, 'name': "Calvi Train Station"},
            # # {'point': 2, 'city': 'FR-CLY', 'iata_code': None, 'icao_code': None, 'lat': 42.566592, 'lon': 8.762425, 'tm': ferry, 'name': "Calvi Ferry Terminal"},

            {'point': 0, 'city': 'FR-CCF', 'iata_code': 'CCF', 'icao_code': 'LFMK', 'lat': 43.215752, 'lon': 2.306172, 'tm': flight, 'name': "Carcassonne Airport"},
            {'point': 0, 'city': 'FR-CCF', 'iata_code':  None, 'icao_code':   None, 'lat': 43.213784, 'lon': 2.309436, 'tm': bus, 'name': "Carcassonne Airport"},
            {'point': 1, 'city': 'FR-CCF', 'iata_code': None, 'icao_code': None, 'lat': 43.218127, 'lon': 2.351806, 'tm': train, 'name': "Gare de Carcassonne"},
            {'point': 1, 'city': 'FR-CCF', 'iata_code': None, 'icao_code': None, 'lat': 43.217774, 'lon': 2.352032, 'tm': bus, 'name': "Gare de Carcassonne"},
            {'point': 2, 'city': 'FR-CCF', 'iata_code': None, 'icao_code': None, 'lat': 43.215446, 'lon': 2.347796, 'tm': bus, 'name': "Carcassonne Boulevard de Varsovie"},

            {'point': 0, 'city': 'FR-CAS', 'iata_code': 'DCM', 'icao_code': 'LFCK', 'lat': 43.555142, 'lon': 2.290466, 'tm': flight, 'name': "Castres-Mazamet Airport"},
            {'point': 1, 'city': 'FR-CAS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.598990, 'lon': 2.231046, 'tm': train, 'name': "Castres Train Station"},

            {'point': 0, 'city': 'FR-CSM', 'iata_code': 'XCR', 'icao_code':'LFOK', 'lat': 48.780951, 'lon': 4.189309, 'tm': flight, 'name': "Châlons Airport"},
            {'point': 1, 'city': 'FR-CSM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.955227, 'lon': 4.348721, 'tm': train, 'name': "Gare de Châlons-en-Champagne"},
            {'point': 1, 'city': 'FR-CSM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.955019, 'lon': 4.348485, 'tm': bus, 'name': "Gare de Châlons-en-Champagne"},
            {'point': 2, 'city': 'FR-CSM', 'iata_code':  None, 'icao_code':  None, 'lat': 48.962758, 'lon': 4.365465, 'tm': bus, 'name': "Châlons-en-Champagne Centre"},

            {'point': 0, 'city': 'FR-CMF', 'iata_code': 'CMF', 'icao_code':'LFLB', 'lat': 45.638012, 'lon': 5.883715, 'tm': flight, 'name': "Chambéry Airport"},
            {'point': 1, 'city': 'FR-CMF', 'iata_code': None, 'icao_code': None, 'lat': 45.571320, 'lon': 5.919553, 'tm': train, 'name': "Chambéry-Challes-les-Eaux"},
            {'point': 1, 'city': 'FR-CMF', 'iata_code': None, 'icao_code': None, 'lat': 45.571035, 'lon': 5.919907, 'tm': bus, 'name': "Chambéry-Challes-les-Eaux"},
            {'point': 2, 'city': 'FR-CMF', 'iata_code': None, 'icao_code': None, 'lat': 45.569979, 'lon': 5.917416, 'tm': bus, 'name': "Chambéry Post Office"},

            # {'point': 1, 'city': 'FR-CER', 'iata_code': None, 'icao_code': None, 'lat': 49.646380, 'lon': -1.612697, 'tm': ferry, 'name': "Cherbourg Ferry Terminal"},

            {'point': 0, 'city': 'FR-CFE', 'iata_code': 'CFE', 'icao_code':'LFLC', 'lat': 45.786768, 'lon': 3.160265, 'tm': flight, 'name': "Clermont-Ferrand Airport"},
            {'point': 0, 'city': 'FR-CFE', 'iata_code': None, 'icao_code': None, 'lat': 45.792145, 'lon': 3.161264, 'tm': train, 'name': "Aulnat-Aéroport"},
            {'point': 1, 'city': 'FR-CFE', 'iata_code': None, 'icao_code': None, 'lat': 45.778865, 'lon': 3.100643, 'tm': train, 'name': "Clermont-Ferrand"},
            {'point': 2, 'city': 'FR-CFE', 'iata_code': None, 'icao_code': None, 'lat': 45.770515, 'lon': 3.082959, 'tm': bus, 'name': "Clermont-Ferrand Les Salins"},
            {'point': 3, 'city': 'FR-CFE', 'iata_code': None, 'icao_code': None, 'lat': 45.766990, 'lon': 3.134184, 'tm': train, 'name': "Clermont-la-Pardieu"},

            {'point': 0, 'city': 'FR-DOL', 'iata_code': 'DOL', 'icao_code':'LFRG', 'lat': 49.363942, 'lon': 0.159198, 'tm': flight, 'name': "Deauville Airport"},
            {'point': 1, 'city': 'FR-DOL', 'iata_code':  None, 'icao_code':  None, 'lat': 49.360031, 'lon': 0.084222, 'tm': train, 'name': "Deauville Trouville Train Station"},
            {'point': 1, 'city': 'FR-DOL', 'iata_code':  None, 'icao_code':  None, 'lat': 49.359267, 'lon': 0.083888, 'tm': bus, 'name': "Deauville Bus Station"},

            # {'point': 1, 'city': 'FR-DPE', 'iata_code': None, 'icao_code': None, 'lat': 49.933985, 'lon': 1.089666, 'tm': ferry, 'name': "Dieppe Ferry Terminal"},

            {'point': 1, 'city': 'FR-DIJ', 'iata_code':  None, 'icao_code':  None, 'lat': 47.323505, 'lon': 5.027135, 'tm': train, 'name': "Gare de Dijon"},
            {'point': 1, 'city': 'FR-DIJ', 'iata_code':  None, 'icao_code':  None, 'lat': 47.323541, 'lon': 5.027889, 'tm': bus, 'name': "Gare de Dijon"},
            {'point': 2, 'city': 'FR-DIJ', 'iata_code':  None, 'icao_code':  None, 'lat': 47.322824, 'lon': 5.054942, 'tm': train, 'name': "Dijon-Porte-Neuve"},

            {'point': 0, 'city': 'FR-DNR', 'iata_code': 'DNR', 'icao_code':'LFRD', 'lat': 48.587895, 'lon':-2.079286, 'tm': flight, 'name': "Dinard Airport"},
            {'point': 1, 'city': 'FR-DNR', 'iata_code': None, 'icao_code': None, 'lat': 48.630651, 'lon': -2.064256, 'tm': bus, 'name': "Dinard Bus Station"},

            {'point': 0, 'city': 'FR-DLE', 'iata_code': 'DLE', 'icao_code':'LFGJ', 'lat': 47.043689, 'lon': 5.424571, 'tm': flight, 'name': "Dole Airport"},
            {'point': 1, 'city': 'FR-DLE', 'iata_code': None, 'icao_code': None, 'lat': 47.096193, 'lon': 5.487996, 'tm': train, 'name': "Dole Train Station"},
            {'point': 2, 'city': 'FR-DLE', 'iata_code': None, 'icao_code': None, 'lat': 47.064090, 'lon': 5.447247, 'tm': bus, 'name': "Dole Bus Station"},

            # {'point': 1, 'city': 'FR-DKK', 'iata_code': None, 'icao_code': None, 'lat': 51.019640, 'lon': 2.189558, 'tm': ferry, 'name': "Dunkerque Ferry Terminal"},

            # {'point': 1, 'city': 'FR-GFR', 'iata_code': None, 'icao_code': None, 'lat': 48.833186, 'lon': -1.602958, 'tm': ferry, 'name': "Granville Ferry Terminal"},

            {'point': 0, 'city': 'FR-GNB', 'iata_code': 'GNB', 'icao_code':'LFLS', 'lat': 45.362157, 'lon': 5.330173, 'tm': flight, 'name': "Grenoble Airport"},
            {'point': 1, 'city': 'FR-GNB', 'iata_code': None, 'icao_code': None, 'lat': 45.191498, 'lon': 5.714482, 'tm': train, 'name': "Gare de Grenoble"},
            {'point': 1, 'city': 'FR-GNB', 'iata_code': None, 'icao_code': None, 'lat': 45.192783, 'lon': 5.713989, 'tm': bus, 'name': "Gare de Grenoble"},
            {'point': 2, 'city': 'FR-GNB', 'iata_code': None, 'icao_code': None, 'lat': 45.204469, 'lon': 5.701215, 'tm': bus, 'name': "Grenoble Presqu'île"},
            {'point': 3, 'city': 'FR-GNB', 'iata_code': None, 'icao_code': None, 'lat': 45.189308, 'lon': 5.774501, 'tm': bus, 'name': "Grenoble Condillac-Universités"},

            {'point': 1, 'city': 'FR-HEN', 'iata_code': None, 'icao_code': None, 'lat': 43.353054, 'lon': -1.781828, 'tm': train, 'name': 'Gare de Hendaye'},
            {'point': 1, 'city': 'FR-HEN', 'iata_code': None, 'icao_code': None, 'lat': 43.350975, 'lon': -1.783305, 'tm': bus, 'name': 'Hendaye'},

            {'point': 0, 'city': 'FR-LRH', 'iata_code': 'LRH', 'icao_code':'LFBH', 'lat': 46.176438, 'lon':-1.194980, 'tm': flight, 'name': "La Rochelle Airport"},
            {'point': 1, 'city': 'FR-LRH', 'iata_code': None, 'icao_code': None, 'lat': 46.152632, 'lon':-1.145300, 'tm': train, 'name': "La Rochelle Train Station"},
            {'point': 1, 'city': 'FR-LRH', 'iata_code': None, 'icao_code': None, 'lat': 46.152821, 'lon': -1.146476, 'tm': bus, 'name': "La Rochelle Bus Station"},

            {'point': 0, 'city': 'FR-LAI', 'iata_code': 'LAI', 'icao_code':'LFRO', 'lat': 48.756842, 'lon':-3.471037, 'tm': flight, 'name': "Lannion Airport"},
            {'point': 1, 'city': 'FR-LAI', 'iata_code': None, 'icao_code': None, 'lat': 48.727374, 'lon': -3.460334, 'tm': train, 'name': "Lannion train station"},
            {'point': 2, 'city': 'FR-LAI', 'iata_code': None, 'icao_code': None, 'lat': 48.726763, 'lon': -3.455955, 'tm': bus, 'name': "Lannion bus station"},

            {'point': 1, 'city': 'FR-LEH', 'iata_code': None, 'icao_code': None, 'lat': 49.492671, 'lon': 0.124743, 'tm': train, 'name': "Le Havre Train Station"},
            {'point': 1, 'city': 'FR-LEH', 'iata_code': None, 'icao_code': None, 'lat': 49.492107, 'lon': 0.125339, 'tm': bus, 'name': "Le Havre Bus Station"},
            # {'point': 2, 'city': 'FR-LEH', 'iata_code': None, 'icao_code': None, 'lat': 49.485063, 'lon': 0.116638, 'tm': ferry, 'name': "Le Havre Ferry Terminal"},

            {'point': 1, 'city': 'FR-LME', 'iata_code': None, 'icao_code': None, 'lat': 47.995616, 'lon': 0.192438, 'tm': train, 'name': "Le Mans Train Station"},
            {'point': 2, 'city': 'FR-LME', 'iata_code': None, 'icao_code': None, 'lat': 48.017419, 'lon': 0.149394, 'tm': bus, 'name': "Le Mans Bus Station"},

            # {'point': 1, 'city': 'FR-LP2', 'iata_code': None, 'icao_code': None, 'lat': 47.346396, 'lon': -3.152820, 'tm': ferry, 'name': "Le Palais Ferry Terminal"},

            # {'point': 1, 'city': 'FR-???', 'iata_code': None, 'icao_code': None, 'lat': 47.606056, 'lon': -2.792833, 'tm': ferry, 'name': "L’Île d'Artz Ferry Terminal"},

            # {'point': 1, 'city': 'FR-ILR', 'iata_code': None, 'icao_code': None, 'lat': 42.641525, 'lon': 8.936950, 'tm': ferry, 'name': "L’Île-Rousse Ferry Terminal"},

            {'point': 0, 'city': 'FR-LLE', 'iata_code': 'LIL', 'icao_code':'LFQQ', 'lat': 50.566992, 'lon': 3.103728, 'tm': flight, 'name': "Lille Airport"},
            {'point': 1, 'city': 'FR-LLE', 'iata_code': 'XDB', 'icao_code': None, 'lat': 50.639193, 'lon': 3.075447, 'tm': train, 'name': "Gare de Lille Europe"},
            {'point': 1, 'city': 'FR-LLE', 'iata_code': None, 'icao_code': None, 'lat': 50.638774, 'lon': 3.076652, 'tm': bus, 'name': "Gare de Lille Europe"},
            {'point': 2, 'city': 'FR-LLE', 'iata_code': None, 'icao_code': None, 'lat': 50.636174, 'lon': 3.071282, 'tm': train, 'name': "Lille Flandres"},
            {'point': 3, 'city': 'FR-LLE', 'iata_code': None, 'icao_code': None, 'lat': 50.624256, 'lon': 3.128062, 'tm': train, 'name': "Lille Pont de Bois"},

            {'point': 0, 'city': 'FR-LIG', 'iata_code': 'LIG', 'icao_code':'LFBL', 'lat': 45.860932, 'lon': 1.178761, 'tm': flight, 'name': "Limoges Airport"},
            {'point': 1, 'city': 'FR-LIG', 'iata_code': None, 'icao_code': None, 'lat': 45.836268, 'lon': 1.267524, 'tm': train, 'name': "Limoges-Bénédictins Train Station"},
            {'point': 1, 'city': 'FR-LIG', 'iata_code': None, 'icao_code': None, 'lat': 45.835898, 'lon': 1.268351, 'tm': bus, 'name': "Limoges Bus Station"},

            {'point': 0, 'city': 'FR-LRT', 'iata_code': 'LRT', 'icao_code':'LFRH', 'lat': 47.754124, 'lon':-3.437363, 'tm': flight, 'name': "Lorient Airport"},
            {'point': 1, 'city': 'FR-LRT', 'iata_code': None, 'icao_code': None, 'lat': 47.754831, 'lon': -3.367102, 'tm': train, 'name': "Gare de Lorient"},
            {'point': 1, 'city': 'FR-LRT', 'iata_code': None, 'icao_code': None, 'lat': 47.754261, 'lon': -3.367102, 'tm': bus, 'name': "Gare de Lorient"},
            {'point': 2, 'city': 'FR-LRT', 'iata_code': None, 'icao_code': None, 'lat': 47.7779, 'lon': -3.34207, 'tm': bus, 'name': "Lorient Lanester"},
            # # {'point': 2, 'city': 'FR-LRT', 'iata_code': None, 'icao_code': None, 'lat': 47.741406, 'lon': -3.352224, 'tm': ferry, 'name': "Lorient Ferry Terminal"},

            {'point': 0, 'city': 'FR-LDE', 'iata_code': 'LDE', 'icao_code':'LFBT', 'lat': 43.179677, 'lon':-0.004629, 'tm': flight, 'name': "Tarbes-Lourdes Airport"},
            {'point': 1, 'city': 'FR-LDE', 'iata_code': None, 'icao_code': None, 'lat': 43.100375, 'lon':-0.042194, 'tm': train, 'name': " Lourdes Train Station"},
            {'point': 1, 'city': 'FR-LDE', 'iata_code': None, 'icao_code': None, 'lat': 43.100182, 'lon':-0.041550, 'tm': bus, 'name': " Lourdes Bus Station"},

            {'point': 0, 'city': 'FR-LIO', 'iata_code':'LYS', 'icao_code':'LFLL', 'lat': 45.723417, 'lon': 5.088775, 'tm': flight, 'name': "Lyon Saint Exupéry Airport"},
            {'point': 0, 'city': 'FR-LIO', 'iata_code': None, 'icao_code':  None, 'lat': 45.720904, 'lon': 5.075829, 'tm': train, 'name': "Lyon Airport"},
            {'point': 0, 'city': 'FR-LIO', 'iata_code': None, 'icao_code':  None, 'lat': 45.721440, 'lon': 5.074812, 'tm': bus, 'name': "Lyon Airport"},
            {'point': 1, 'city': 'FR-LIO', 'iata_code':'XYD', 'icao_code': None, 'lat': 45.760545, 'lon': 4.861122, 'tm': train, 'name': "Lyon Part-Dieu"},
            {'point': 1, 'city': 'FR-LIO', 'iata_code': None, 'icao_code': None, 'lat': 45.760441, 'lon': 4.862300, 'tm': bus, 'name': "Lyon Part-Dieu"},
            {'point': 2, 'city': 'FR-LIO', 'iata_code': None, 'icao_code': None, 'lat': 45.748511, 'lon': 4.825708, 'tm': train, 'name': "Lyon Perrache"},
            {'point': 2, 'city': 'FR-LIO', 'iata_code': None, 'icao_code': None, 'lat': 45.748800, 'lon': 4.825924, 'tm': bus, 'name': "Lyon Perrache"},
            {'point': 3, 'city': 'FR-LIO', 'iata_code': None, 'icao_code': None, 'lat': 45.745202, 'lon': 4.841513, 'tm': train, 'name': "Lyon Jean Mace"},

            {'point': 0, 'city': 'FR-MRS', 'iata_code': 'MRS', 'icao_code':'LFML', 'lat': 43.438425, 'lon': 5.214412, 'tm': flight, 'name': "Marseille Airport"},
            {'point': 0, 'city': 'FR-MRS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.442237, 'lon': 5.221817, 'tm': bus, 'name': "Marseille Airport"},
            {'point': 1, 'city': 'FR-MRS', 'iata_code': 'XRF', 'icao_code':  None, 'lat': 43.302662, 'lon': 5.380519, 'tm': train, 'name': "Marseille Saint-Charles"},
            {'point': 1, 'city': 'FR-MRS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.303663, 'lon': 5.379959, 'tm': bus, 'name': "Marseille Saint-Charles"},
            {'point': 2, 'city': 'FR-MRS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.314210, 'lon': 5.368822, 'tm': bus, 'name': "Marseille Arenc"},
            {'point': 3, 'city': 'FR-MRS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.296216, 'lon': 5.406643, 'tm': train, 'name': "Marseille Blancarde"},
            {'point': 4, 'city': 'FR-MRS', 'iata_code':  None, 'icao_code':  None, 'lat':   43.2998, 'lon':  5.36377, 'tm': bus, 'name': "Marseille Port"},
            # # {'point': 4, 'city': 'FR-MRS', 'iata_code': None, 'icao_code': None, 'lat': 43.294327, 'lon': 5.373701, 'tm': ferry, 'name': "Marseille Ferry Terminal"},

            {'point': 0, 'city': 'FR-MZM', 'iata_code': 'ETZ', 'icao_code':'LFJL', 'lat': 48.981150, 'lon': 6.243926, 'tm': flight, 'name': "Metz-Nancy Airport"},
            {'point': 1, 'city': 'FR-MZM', 'iata_code': None, 'icao_code': None, 'lat': 49.109857, 'lon': 6.177127, 'tm': train, 'name': "Metz Central Station"},
            {'point': 1, 'city': 'FR-MZM', 'iata_code': None, 'icao_code': None, 'lat': 49.110523, 'lon': 6.183441, 'tm': bus, 'name': "Metz Central Station"},
            {'point': 3, 'city': 'FR-MZM', 'iata_code': 'XZI', 'icao_code': None, 'lat': 48.947767, 'lon': 6.169791, 'tm': train, 'name': "Gare de Lorraine TGV"},

            {'point': 0, 'city': 'FR-MPL', 'iata_code': 'MPL', 'icao_code':'LFMT', 'lat': 43.581030, 'lon': 3.962666, 'tm': flight, 'name': "Montpellier Airport"},
            {'point': 0, 'city': 'FR-MPL', 'iata_code':  None, 'icao_code':  None, 'lat': 43.579293, 'lon': 3.957732, 'tm': bus, 'name': "Montpellier Airport"},
            {'point': 1, 'city': 'FR-MPL', 'iata_code': 'XPJ', 'icao_code':  None, 'lat': 43.604895, 'lon': 3.880854, 'tm': train, 'name': "Montpellier-Saint-Roch"},
            {'point': 2, 'city': 'FR-MPL', 'iata_code':  None, 'icao_code':  None, 'lat': 43.583831, 'lon': 3.860397, 'tm': bus, 'name': "Montpellier Sabines"},
            {'point': 3, 'city': 'FR-MPL', 'iata_code':  None, 'icao_code':  None, 'lat': 43.604459, 'lon': 3.918320, 'tm': bus, 'name': "Montpellier Place de France"},

            {'point': 0, 'city': 'FR-MLH', 'iata_code': 'MLH', 'icao_code':'LFSB', 'lat': 47.598165, 'lon': 7.525359, 'tm': flight, 'name': "Mulhouse Airport"},
            {'point': 0, 'city': 'FR-MLH', 'iata_code':  None, 'icao_code':  None, 'lat':   47.6024, 'lon': 7.53106 , 'tm': bus, 'name': "Mulhouse Airport"},
            {'point': 1, 'city': 'FR-MLH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.742445, 'lon': 7.349204, 'tm': train, 'name': "Gare de Mulhouse"},
            {'point': 1, 'city': 'FR-MLH', 'iata_code':  None, 'icao_code':  None, 'lat': 47.742092, 'lon': 7.341935, 'tm': bus, 'name': "Gare de Mulhouse"},

            {'point': 1, 'city': 'FR-ENC', 'iata_code': None, 'icao_code': None, 'lat': 48.689835, 'lon': 6.174446, 'tm': train, 'name': "Nancy Train Station"},
            {'point': 2, 'city': 'FR-ENC', 'iata_code': None, 'icao_code': None, 'lat': 48.695488, 'lon': 6.190645, 'tm': bus, 'name': "Nancy Bus Station"},
            {'point': 3, 'city': 'FR-ENC', 'iata_code': None, 'icao_code': None, 'lat': 48.65    , 'lon': 6.14524 , 'tm': bus, 'name': "Nancy Brabois"},

            {'point': 0, 'city': 'FR-NTE', 'iata_code': 'NTE', 'icao_code':'LFRS', 'lat': 47.157417, 'lon':-1.606234, 'tm': flight, 'name': "Nantes Airport"},
            {'point': 0, 'city': 'FR-NTE', 'iata_code': None, 'icao_code': None, 'lat': 47.157392, 'lon':-1.596665, 'tm': bus, 'name': "Nantes Airport"},
            {'point': 1, 'city': 'FR-NTE', 'iata_code': 'QJZ', 'icao_code': None, 'lat': 47.217484, 'lon':-1.541958, 'tm': train, 'name': "Gare de Nantes"},
            {'point': 2, 'city': 'FR-NTE', 'iata_code': None, 'icao_code': None, 'lat': 47.248930, 'lon':-1.520805, 'tm': bus, 'name': "Nantes Bus Station"},
            {'point': 3, 'city': 'FR-NTE', 'iata_code': None, 'icao_code': None, 'lat': 47.212805, 'lon':-1.552189, 'tm': bus, 'name': "Nantes Hotel Dieu"},

            {'point': 0, 'city': 'FR-NCE', 'iata_code': 'NCE', 'icao_code':'LFMN', 'lat': 43.659768, 'lon': 7.214813, 'tm': flight, 'name': "Nice Airport"},
            {'point': 0, 'city': 'FR-NCE', 'iata_code': None, 'icao_code': None, 'lat': 43.665103, 'lon': 7.210946, 'tm': bus, 'name': "Nice Airport"},
            {'point': 1, 'city': 'FR-NCE', 'iata_code': None, 'icao_code': None, 'lat': 43.704601, 'lon': 7.261927, 'tm': train, 'name': "Gare de Nice Ville"},
            {'point': 2, 'city': 'FR-NCE', 'iata_code': None, 'icao_code': None, 'lat': 43.667735, 'lon': 7.209536, 'tm': bus, 'name': "Nice Boulevard René Cassin"},
            {'point': 3, 'city': 'FR-NCE', 'iata_code': None, 'icao_code': None, 'lat': 43.708686, 'lon': 7.286131, 'tm': bus, 'name': "Nice Gare Routière"},
            # # {'point': 3, 'city': 'FR-NCE', 'iata_code': None, 'icao_code': None, 'lat': 43.693469, 'lon': 7.283299, 'tm': ferry, 'name': "Nice Ferry Terminal"},

            {'point': 0, 'city': 'FR-FNI', 'iata_code': 'FNI', 'icao_code':'LFTW', 'lat': 43.760339, 'lon': 4.421846, 'tm': flight, 'name': "Nîmes Airport"},
            {'point': 1, 'city': 'FR-FNI', 'iata_code':'ZYN', 'icao_code': None, 'lat': 43.832500, 'lon': 4.366236, 'tm': train, 'name': "Nîmes Gare Routière"},
            {'point': 1, 'city': 'FR-FNI', 'iata_code': None, 'icao_code': None, 'lat': 43.832659, 'lon': 4.367475, 'tm': bus, 'name': "Nîmes Gare Routière"},
            {'point': 2, 'city': 'FR-FNI', 'iata_code': None, 'icao_code': None, 'lat': 43.817454, 'lon': 4.362138, 'tm': bus, 'name': "Nîmes Av Languedoc"},

            {'point': 1, 'city': 'FR-ORR', 'iata_code':  None, 'icao_code':  None, 'lat': 47.907804, 'lon': 1.904722, 'tm': train, 'name': "Gare d'Orléans"},
            {'point': 2, 'city': 'FR-ORR', 'iata_code':  None, 'icao_code':  None, 'lat': 47.919527, 'lon': 1.903487, 'tm': bus, 'name': "Orleans Libération"},
            {'point': 3, 'city': 'FR-ORR', 'iata_code':  None, 'icao_code':  None, 'lat': 47.926714, 'lon': 1.906678, 'tm': train, 'name': "Orleans Aubrais"},
            {'point': 4, 'city': 'FR-ORR', 'iata_code':  None, 'icao_code':  None, 'lat': 47.845541, 'lon': 1.915902, 'tm': bus, 'name': "Orleans South University"},

            {'point': 0, 'city': 'FR-PAR', 'iata_code': 'CDG', 'icao_code':'LFPG', 'lat': 49.009691, 'lon': 2.547921, 'tm': flight, 'name': "Paris Charles de Gaulle"},
            {'point': 0, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 49.003676, 'lon': 2.570924, 'tm': train, 'name': "Paris Charles de Gaulle"},
            {'point': 0, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 49.010545, 'lon': 2.558737, 'tm': bus, 'name': "Paris Charles de Gaulle T3"},
            {'point':25, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 49.004216, 'lon': 2.571150, 'tm': bus, 'name': "Paris Charles de Gaulle T2"},
            {'point': 1, 'city': 'FR-PAR', 'iata_code':'ORY', 'icao_code':'LFPO', 'lat': 48.726241, 'lon': 2.365241, 'tm': flight, 'name': "Paris Orly"},
            {'point': 1, 'city': 'FR-PAR', 'iata_code': None, 'icao_code':  None, 'lat': 48.728729, 'lon': 2.369017, 'tm': bus, 'name': "Paris Orly Sud"},
            {'point': 2, 'city': 'FR-PAR', 'iata_code': None, 'icao_code':  None, 'lat': 48.865262, 'lon': 2.414761, 'tm': bus, 'name': "Paris-Gallieni"},
            {'point': 3, 'city': 'FR-PAR', 'iata_code': 'XPG', 'icao_code': None, 'lat': 48.880957, 'lon': 2.355296, 'tm': train, 'name': "Paris-Nord"},
            {'point': 4, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.876793, 'lon': 2.359289, 'tm': train, 'name': "Paris-Est"},
            {'point': 4, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.881809, 'lon': 2.363098, 'tm': bus, 'name': "Paris Gare de l'Est"},
            {'point': 5, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.844325, 'lon': 2.374382, 'tm': train, 'name': "Paris Gare de Lyon"},
            {'point': 6, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.839189, 'lon': 2.382709, 'tm': train, 'name': "Paris Bercy"},
            {'point': 7,  'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.838213, 'lon': 2.382802, 'tm': bus, 'name': "Paris Bercy"},
            {'point': 8,  'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.841752, 'lon': 2.366102, 'tm': train, 'name': "Paris Austerlitz"},
            {'point': 9,  'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.841030, 'lon': 2.320331, 'tm': train, 'name': "Paris Montparnasse"},
            {'point': 10, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.875931, 'lon': 2.324320, 'tm': train, 'name': "Paris Saint-Lazare"},
            {'point': 11, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.879969, 'lon': 2.282243, 'tm': bus, 'name': "Paris Porte Maillot"},
            {'point': 12, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.821285, 'lon': 2.325754, 'tm': bus, 'name': "Paris Porte d’Orléans"},
            {'point': 13, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.891459, 'lon': 2.242060, 'tm': bus, 'name': "Paris Jules Verne"},
            {'point': 14, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.946779, 'lon': 2.257139, 'tm': train, 'name': "Paris Argenteuil"},
            {'point': 14, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.946822, 'lon': 2.257105, 'tm': bus, 'name': "Paris Argenteuil"},
            {'point': 15, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.917856, 'lon': 2.351087, 'tm': train, 'name': "Paris Saint-Denis"},
            {'point': 16, 'city': 'FR-PAR', 'iata_code':'XJY', 'icao_code': None, 'lat': 48.725860, 'lon': 2.261355, 'tm': train, 'name': "Paris Gare de Massy"},
            {'point': 16, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.727659, 'lon': 2.264631, 'tm': bus, 'name': "Paris Gare de Massy"},
            {'point': 17, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.891890, 'lon': 2.316459, 'tm': bus, 'name': "Paris Clichy Batignolles"},
            {'point': 18, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.946408, 'lon': 2.365189, 'tm': bus, 'name': "Paris Nord Saint-Denis - Université"},
            {'point': 19, 'city': 'FR-PAR', 'iata_code': 'XED', 'icao_code': None, 'lat': 48.870479, 'lon': 2.782824, 'tm': train, 'name': "Paris Disneyland - Gare de Marne la Vallée Chessy"},
            {'point': 19, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.874793, 'lon': 2.785437, 'tm': bus, 'name': "Paris Disneyland"},
            {'point': 20, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.795715, 'lon': 2.135966, 'tm': bus, 'name': "Paris Versailles Chantiers"},
            {'point': 21, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.930510, 'lon': 2.283899, 'tm': bus, 'name': "Paris Asnières - Gennevilliers"},
            {'point': 22, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.831359, 'lon': 2.398416, 'tm': bus, 'name': "Paris Porte de Charenton"},
            {'point': 23, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.883660, 'lon': 2.327115, 'tm': bus, 'name': "Paris Place de Clichy"},
            {'point': 24, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.795332, 'lon': 2.417241, 'tm': bus, 'name': "Paris Quai Jules Guesde"},
            # {'point':25, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 49.004216, 'lon': 2.571150, 'tm': bus, 'name': "Paris Charles de Gaulle T2"}, #see at point 0 with airport. Here also written so next station is not point 25 and duplicated
            {'point': 26, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat':   48.8977, 'lon':  2.28126, 'tm': bus, 'name': "Paris Rue Thierry le Luron"},
            {'point': 27, 'city': 'FR-PAR', 'iata_code': None, 'icao_code': None, 'lat': 48.901090, 'lon': 2.331797, 'tm': bus, 'name': "Paris Pte de St Ouen"},

            {'point': 0, 'city': 'FR-PUF', 'iata_code': 'PUF', 'icao_code':'LFBP', 'lat': 43.380972, 'lon':-0.418245, 'tm': flight, 'name': "Pau Airport"},
            {'point': 1, 'city': 'FR-PUF', 'iata_code': None, 'icao_code': None, 'lat': 43.291690, 'lon':-0.369675, 'tm': train, 'name': "Pau Train Station"},
            {'point': 1, 'city': 'FR-PUF', 'iata_code': None, 'icao_code': None, 'lat': 43.292196, 'lon':-0.368687, 'tm': bus, 'name': "Pau SNCF Bus Station"},
            {'point': 2, 'city': 'FR-PUF', 'iata_code': None, 'icao_code': None, 'lat': 43.311305, 'lon':-0.365066, 'tm': bus, 'name': "Pau Bus Station"},

            {'point': 0, 'city': 'FR-PGX', 'iata_code': 'PGX', 'icao_code':'LFBX', 'lat': 45.196379, 'lon': 0.812674, 'tm': flight, 'name': "Périgueux Airport"},
            {'point': 1, 'city': 'FR-PGX', 'iata_code': None, 'icao_code': None, 'lat': 45.187347, 'lon': 0.707743, 'tm': train, 'name': "Gare de Périgueux"},
            {'point': 2, 'city': 'FR-PGX', 'iata_code': None, 'icao_code': None, 'lat': 45.143155, 'lon': 0.698513, 'tm': bus, 'name': "Périgueux Créavallée Nord"},
            {'point': 3, 'city': 'FR-PGX', 'iata_code': None, 'icao_code': None, 'lat': 45.150082, 'lon': 0.799343, 'tm': bus, 'name': "Périgueux Restaurant Aire du Manoire"},

            {'point': 0, 'city': 'FR-PGF', 'iata_code': 'PGF', 'icao_code':'LFMP', 'lat': 42.740277, 'lon': 2.871176, 'tm': flight, 'name': "Perpignan Airport"},
            {'point': 0, 'city': 'FR-PGF', 'iata_code': None, 'icao_code': None, 'lat': 42.740916, 'lon': 2.867246, 'tm': bus, 'name': "Perpignan Airport"},
            {'point': 1, 'city': 'FR-PGF', 'iata_code': None, 'icao_code': None, 'lat': 42.696262, 'lon': 2.879685, 'tm': train, 'name': "Gare de Perpignan"},
            {'point': 1, 'city': 'FR-PGF', 'iata_code': None, 'icao_code': None, 'lat': 42.695019, 'lon': 2.879053, 'tm': bus, 'name': "Gare de Perpignan"},

            {'point': 0, 'city': 'FR-PIS', 'iata_code': 'PIS', 'icao_code':'LFBI', 'lat': 46.585936, 'lon': 0.311346, 'tm': flight, 'name': "Poitiers Airport"},
            {'point': 1, 'city': 'FR-PIS', 'iata_code': 'XOP', 'icao_code':  None, 'lat': 46.582397, 'lon': 0.333188, 'tm': train, 'name': "Gare de Poitiers"},
            {'point': 1, 'city': 'FR-PIS', 'iata_code':  None, 'icao_code':  None, 'lat': 46.584512, 'lon': 0.335625, 'tm': bus, 'name': "Gare de Poitiers"},

            {'point': 0, 'city': 'FR-PVO', 'iata_code': 'FSC', 'icao_code':'LFKF', 'lat': 41.502336, 'lon': 9.098378, 'tm': flight, 'name': "Figari Sud Corse Airport"},
            # {'point': 1, 'city': 'FR-PVO', 'iata_code': None, 'icao_code': None, 'lat': 41.591828, 'lon': 9.283785, 'tm': bus, 'name': "Porto-Vecchio Bus Station"},
            # {'point': 2, 'city': 'FR-PVO', 'iata_code': None, 'icao_code': None, 'lat': 41.587476, 'lon': 9.292396, 'tm': ferry, 'name': "Porto-Vecchio Ferry Terminal"},

            # {'point': 1, 'city': 'FR-QUI', 'iata_code': None, 'icao_code': None, 'lat': 47.477489, 'lon': -3.123558, 'tm': ferry, 'name': "Quiberon Ferry Terminal"},

            {'point': 0, 'city': 'FR-UIP', 'iata_code': 'UIP', 'icao_code':'LFRQ', 'lat': 47.975073, 'lon':-4.174163, 'tm': flight, 'name': "Quimper Airport"},
            {'point': 1, 'city': 'FR-UIP', 'iata_code': None, 'icao_code': None, 'lat': 47.994507, 'lon':-4.092194, 'tm': train, 'name': "Quimper Train Station"},
            {'point': 1, 'city': 'FR-UIP', 'iata_code': None, 'icao_code': None, 'lat': 47.994697, 'lon':-4.093793, 'tm': bus, 'name': "Quimper Bus Station"},

            {'point': 1, 'city': 'FR-RHE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.258987, 'lon': 4.024393, 'tm': train, 'name': "Reims SNCF Train Station"},
            {'point': 2, 'city': 'FR-RHE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.214729, 'lon': 3.994616, 'tm': train, 'name': "Reims Champagne-Ardenne TGV Train Station"},
            {'point': 2, 'city': 'FR-RHE', 'iata_code':  None, 'icao_code':  None, 'lat': 49.214879, 'lon': 3.994720, 'tm': bus, 'name': "Reims Champagne-Ardenne TGV Bus Station"},

            {'point': 0, 'city': 'FR-RNS', 'iata_code': 'RNS', 'icao_code':'LFRN', 'lat': 48.069783, 'lon':-1.734368, 'tm': flight, 'name': "Rennes Airport"},
            {'point': 1, 'city': 'FR-RNS', 'iata_code': 'ZFJ', 'icao_code': None, 'lat': 48.103492, 'lon':-1.672292, 'tm': train, 'name': "Rennes Train Station"},
            {'point': 1, 'city': 'FR-RNS', 'iata_code': None, 'icao_code': None, 'lat': 48.103905, 'lon':-1.670618, 'tm': bus, 'name': "Rennes Bus Station"},

            {'point': 0, 'city': 'FR-RDZ', 'iata_code': 'RDZ', 'icao_code':'LFCR', 'lat': 44.410816, 'lon': 2.483209, 'tm': flight, 'name': "Rodez Airport"},
            {'point': 1, 'city': 'FR-RDZ', 'iata_code': None, 'icao_code': None, 'lat': 44.362675, 'lon': 2.580538, 'tm': train, 'name': "Rodez Train Station"},
            {'point': 1, 'city': 'FR-RDZ', 'iata_code': None, 'icao_code': None, 'lat': 44.362645, 'lon': 2.580241, 'tm': bus, 'name': "Rodez Bus Station"},

            # {'point': 1, 'city': 'FR-ROS', 'iata_code': None, 'icao_code': None, 'lat': 48.721937, 'lon': -3.964465, 'tm': ferry, 'name': "Roscoff Ferry Terminal"},

            {'point': 1, 'city': 'FR-URO', 'iata_code':  None, 'icao_code':  None, 'lat': 49.448855, 'lon': 1.094122, 'tm': train, 'name': "Rouen Train Station"},
            {'point': 2, 'city': 'FR-URO', 'iata_code':  None, 'icao_code':  None, 'lat': 49.434190, 'lon': 1.092678, 'tm': bus, 'name': "Rouen Bus Station"},

            {'point': 0, 'city': 'FR-EBU', 'iata_code': 'EBU', 'icao_code':'LFMH', 'lat': 45.531806, 'lon': 4.294071, 'tm': flight, 'name': "Saint-Étienne Airport"},
            {'point': 1, 'city': 'FR-EBU', 'iata_code': None, 'icao_code': None, 'lat': 45.443436, 'lon': 4.399419, 'tm': train, 'name': "Saint-Étienne Train Station"},
            {'point': 1, 'city': 'FR-EBU', 'iata_code': None, 'icao_code': None, 'lat': 45.442447, 'lon': 4.402893, 'tm': bus, 'name': "Saint-Étienne Bus Station"},

            # {'point': 1, 'city': 'FR-SML', 'iata_code': None, 'icao_code': None, 'lat': 48.642530, 'lon': -2.025577, 'tm': ferry, 'name': "Saint-Malo Ferry Terminal"},

            # {'point': 1, 'city': 'FR-SNR', 'iata_code': None, 'icao_code': None, 'lat': 47.270798, 'lon': -2.203049, 'tm': ferry, 'name': "Saint-Nazaire Ferry Terminal"},

            # {'point': 1, 'city': 'FR-STP', 'iata_code': None, 'icao_code': None, 'lat': 43.272162, 'lon': 6.633230, 'tm': ferry, 'name': "Saint-Tropez Ferry Terminal"},

            # {'point': 1, 'city': 'FR-SET', 'iata_code': None, 'icao_code': None, 'lat': 43.404975, 'lon': 3.704324, 'tm': ferry, 'name': "Sete Ferry Terminal"},

            {'point': 0, 'city': 'FR-CRO', 'iata_code': 'SXB', 'icao_code':'LFST', 'lat': 48.544726, 'lon': 7.628131, 'tm': flight, 'name': "Strasbourg Airport"},
            {'point': 1, 'city': 'FR-CRO', 'iata_code': 'XWG', 'icao_code':  None, 'lat': 48.585186, 'lon': 7.734289, 'tm': train, 'name': "Gare de Strasbourg"},
            {'point': 1, 'city': 'FR-CRO', 'iata_code': 'XER', 'icao_code':  None, 'lat': 48.585082, 'lon': 7.735417, 'tm': bus, 'name': "Gare de Strasbourg"},
            {'point': 2, 'city': 'FR-CRO', 'iata_code':  None, 'icao_code':  None, 'lat': 48.574188, 'lon': 7.754199, 'tm': bus, 'name': "Strasbourg Place de L'Etoile"},

            {'point': 0, 'city': 'FR-TLN', 'iata_code': 'TLN', 'icao_code':'LFTH', 'lat': 43.091031, 'lon': 6.159226, 'tm': flight, 'name': "Toulon Airport"},
            {'point': 1, 'city': 'FR-TLN', 'iata_code': 'XZV', 'icao_code': None, 'lat': 43.128347, 'lon': 5.929435, 'tm': train, 'name': "Toulon Train Station"},
            {'point': 1, 'city': 'FR-TLN', 'iata_code': None, 'icao_code': None, 'lat': 43.127811, 'lon': 5.930725, 'tm': bus, 'name': "Toulon Bus Station"},
            # # {'point': 2, 'city': 'FR-TLN', 'iata_code': None, 'icao_code': None, 'lat': 43.117021, 'lon': 5.932108, 'tm': ferry, 'name': "Toulon Ferry Terminal"},

            {'point': 0, 'city': 'FR-TLS', 'iata_code': 'TLS', 'icao_code':'LFBO', 'lat': 43.629385, 'lon': 1.367682, 'tm': flight, 'name': "Toulouse Airport"},
            {'point': 0, 'city': 'FR-TLS', 'iata_code':  None, 'icao_code':  None, 'lat': 43.630440, 'lon': 1.374501, 'tm': bus, 'name': "Toulouse Airport Bus Station"},
            {'point': 1, 'city': 'FR-TLS', 'iata_code': None, 'icao_code': None, 'lat': 43.611236, 'lon': 1.453743, 'tm': train, 'name': "Toulouse-Matabiau Train Station"},
            {'point': 2, 'city': 'FR-TLS', 'iata_code': None, 'icao_code': None, 'lat': 43.613292, 'lon': 1.452230, 'tm': bus, 'name': "Toulouse Pierre Sémard Bus Station"},

            {'point': 0, 'city': 'FR-TUF', 'iata_code':'TUF', 'icao_code':'LFOT', 'lat': 47.431795, 'lon': 0.725314, 'tm': flight, 'name': "Tours Airport"},
            {'point': 1, 'city': 'FR-TUF', 'iata_code': None, 'icao_code': None, 'lat': 47.389212, 'lon': 0.694281, 'tm': train, 'name': "Tours Train Station"},
            {'point': 1, 'city': 'FR-TUF', 'iata_code': None, 'icao_code': None, 'lat': 47.383380, 'lon': 0.702632, 'tm': bus, 'name': "Tours Bus Station"},
            {'point': 2, 'city': 'FR-TUF', 'iata_code':'XSH', 'icao_code': None, 'lat': 47.386114, 'lon': 0.723614, 'tm': train, 'name': "Tours St-Pierre-des-Corps"},
            {'point': 3, 'city': 'FR-TUF', 'iata_code': None, 'icao_code': None, 'lat':   47.3912, 'lon': 0.693666, 'tm': bus, 'name': "Tours Parking des Peupliers"},

            # {'point': 1, 'city': 'FR-VNE', 'iata_code': None, 'icao_code': None, 'lat': 47.640143, 'lon': -2.761820, 'tm': ferry, 'name': "Vannes Ferry Terminal"},
        ]

        hubs_CH = [
            {'point': 0, 'city': "CH-ATR", 'iata_code': 'ACH', 'icao_code': 'LSZR', 'lat': 47.485859, 'lon': 9.559911, 'tm': flight, 'name': "St.Gallen-Altenrhein Airport"},
            # {'point': 1, 'city': "CH-ATR", 'iata_code':  None, 'icao_code':   None, 'lat': 47.480853, 'lon': 9.536564, 'tm': train, 'name': "Altenrhein Staad Train"},

            {'point': 0, 'city': "CH-BSL", 'iata_code': 'BSL', 'icao_code': 'LSZM', 'lat': 47.598123, 'lon': 7.524509, 'tm': flight, 'name': " Basel-Mulhouse-Freiburg Euroairport"},
            {'point': 0, 'city': "CH-BSL", 'iata_code':  None, 'icao_code':   None, 'lat': 47.600718, 'lon': 7.531720, 'tm': bus, 'name': "Basel-Mulhouse-Freiburg Euroairport"},
            {'point': 1, 'city': "CH-BSL", 'iata_code': 'ZDH', 'icao_code':   None, 'lat': 47.547586, 'lon': 7.589696, 'tm': train, 'name': "Basel SBB"},
            {'point': 1, 'city': "CH-BSL", 'iata_code':  None, 'icao_code':   None, 'lat': 47.546313, 'lon': 7.587760, 'tm': bus, 'name': "Basel SBB"},
            {'point': 2, 'city': "CH-BSL", 'iata_code': 'ZBA', 'icao_code':   None, 'lat': 47.567271, 'lon': 7.607024, 'tm': train, 'name': "Basel Badischer Train"},
            {'point': 2, 'city': "CH-BSL", 'iata_code':  None, 'icao_code':   None, 'lat': 47.567271, 'lon': 7.607024, 'tm': bus, 'name': "Basel Badischer Bus"},
            # {'point': 3, 'city': "CH-BSL", 'iata_code':  None, 'icao_code':   None, 'lat': 47.546313, 'lon': 7.587760, 'tm': bus, 'name': "Basel SBB (Meret Oppenheim-Straße)"}, #SBB bus duplicated
            {'point': 4, 'city': "CH-BSL", 'iata_code':  None, 'icao_code':   None, 'lat': 47.557248, 'lon': 7.570585, 'tm': bus, 'name': "Basel Allschwilerplatz"},

            {'point': 0, 'city': "CH-BRN", 'iata_code': 'BRN', 'icao_code': 'LSZB', 'lat': 46.912297, 'lon': 7.499080, 'tm': flight, 'name': "Bern-Belp Airport"},
            {'point': 1, 'city': "CH-BRN", 'iata_code': 'ZDJ', 'icao_code':   None, 'lat': 46.949146, 'lon': 7.438785, 'tm': bus, 'name': "Bern Central Bus Station"},
            {'point': 1, 'city': "CH-BRN", 'iata_code':  None, 'icao_code':   None, 'lat': 46.949146, 'lon': 7.438785, 'tm': train, 'name': "Bern Central Train Station"},
            {'point': 2, 'city': "CH-BRN", 'iata_code':  None, 'icao_code':   None, 'lat': 46.963003, 'lon': 7.432063, 'tm': bus, 'name': "Bern PR Neufeld Bus Station"},
            # {'point': 2, 'city': "CH-BRN", 'iata_code':  None, 'icao_code':   None, 'lat': 46.963003, 'lon': 7.432063, 'tm': train, 'name': "Bern PR Neufeld Train"},
            # {'point': 3, 'city': "CH-BRN", 'iata_code':  None, 'icao_code':   None, 'lat': 46.948878, 'lon': 7.438934, 'tm': bus, 'name': "Postautostation 1 Bus"}, #repeated == Hbf

            {'point': 0, 'city': "CH-GVA", 'iata_code': 'GVA', 'icao_code': 'LSGG', 'lat': 46.238333, 'lon': 6.109444, 'tm': flight, 'name': "Geneva Airport"},
            {'point': 0, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.232500, 'lon': 6.111944, 'tm': train, 'name': "Geneva Airport"},
            {'point': 0, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.230125, 'lon': 6.109287, 'tm': bus, 'name': "Geneva Airport"},
            {'point': 1, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.210498, 'lon': 6.143042, 'tm': train, 'name': "Geneva Cornavin"},
            {'point': 1, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.210498, 'lon': 6.143042, 'tm': bus, 'name': "Geneva Cornavin"},
            {'point': 2, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.223493, 'lon': 6.144720, 'tm': bus, 'name': "Geneva Rigot"},
            {'point': 3, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.188926, 'lon': 6.125516, 'tm': train, 'name': "Geneva Lancy-Pons-Rouge"},
            {'point': 4, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.187628, 'lon': 6.127126, 'tm': bus, 'name': "Geneva P+R Etoile"},
            {'point': 5, 'city': "CH-GVA", 'iata_code':  None, 'icao_code':   None, 'lat': 46.208316, 'lon': 6.146667, 'tm': bus, 'name': "Gare Routiere"},

            # {'point': 0, 'city': "CH-ZHI", 'iata_code':  None, 'icao_code': 'LSZG', 'lat': 47.181389, 'lon': 7.416944, 'tm': flight, 'name': "Grenchen Airport"}, #airport with no flights
            # {'point': 1, 'city': "CH-ZHI", 'iata_code':  None, 'icao_code':   None, 'lat': 47.191689, 'lon': 7.389718, 'tm': train, 'name': "Grenchen Nord train"},
            # {'point': 2, 'city': "CH-ZHI", 'iata_code':  None, 'icao_code':   None, 'lat': 47.191803, 'lon': 7.389375, 'tm': bus, 'name': "Bahnhof Nord"},
            # {'point': 3, 'city': "CH-ZHI", 'iata_code':  None, 'icao_code':   None, 'lat': 47.188848, 'lon': 7.398289, 'tm': train, 'name': "Grenchen Sud"},

            {'point': 1, 'city': "CH-LAU", 'iata_code': 'AJF', 'icao_code':   None, 'lat': 46.517017, 'lon': 6.629240, 'tm': train, 'name': "Lausanne Central Station"},
            {'point': 1, 'city': "CH-LAU", 'iata_code':  None, 'icao_code':   None, 'lat': 46.517261, 'lon': 6.630085, 'tm': bus, 'name': "Lausanne Central Station"},
            {'point': 2, 'city': "CH-LAU", 'iata_code':  None, 'icao_code':   None, 'lat': 46.520749, 'lon': 6.630289, 'tm': train, 'name': "Lausanne Flon"},
            {'point': 2, 'city': "CH-LAU", 'iata_code':  None, 'icao_code':   None, 'lat': 46.520461, 'lon': 6.630976, 'tm': bus, 'name': "Lausanne Flon"},
            {'point': 3, 'city': "CH-LAU", 'iata_code':  None, 'icao_code':   None, 'lat': 46.536371, 'lon': 6.623311, 'tm': bus, 'name': "Lausanne Parc Vélodrome"},

            {'point': 0, 'city': "CH-LUG", 'iata_code': 'LUG', 'icao_code': 'LSZA', 'lat': 46.003611, 'lon': 8.910278, 'tm': flight, 'name': "Lugano-Agno Airport"},
            {'point': 1, 'city': "CH-LUG", 'iata_code':  None, 'icao_code':   None, 'lat': 46.004430, 'lon': 8.947656, 'tm': train, 'name': "Lugano Main Station"},
            {'point': 1, 'city': "CH-LUG", 'iata_code':  None, 'icao_code':   None, 'lat': 46.005361, 'lon': 8.947270, 'tm': bus, 'name': "Lugano Main Station"},
            {'point': 2, 'city': "CH-LUG", 'iata_code':  None, 'icao_code':   None, 'lat': 46.023239, 'lon': 8.963925, 'tm': bus, 'name': "Lugano Via Giacomo E Filippo Ciani"},
            {'point': 3, 'city': "CH-LUG", 'iata_code':  None, 'icao_code':   None, 'lat': 45.985376, 'lon': 8.932591, 'tm': bus, 'name': "Lugano Pambio-Noranco Posta"},
            {'point': 4, 'city': "CH-LUG", 'iata_code':  None, 'icao_code':   None, 'lat': 46.0101, 'lon': 8.96004, 'tm': bus, 'name': "Lugano Via Pietro"},

            {'point': 0, 'city': "CH-SAM", 'iata_code': 'SMV', 'icao_code': 'LSZS', 'lat': 46.533889, 'lon': 9.883889, 'tm': flight, 'name': "Samedan Airport"},
            {'point': 1, 'city': "CH-SAM", 'iata_code':  None, 'icao_code':   None, 'lat': 46.533838, 'lon': 9.873580, 'tm': train, 'name': "Samedan Train Station"},
            {'point': 1, 'city': "CH-SAM", 'iata_code':  None, 'icao_code':   None, 'lat': 46.533748, 'lon': 9.872872, 'tm': bus, 'name': "Samedan Bus Station am Bahnhof"},
            # {'point': 2, 'city': "CH-SAM", 'iata_code':  None, 'icao_code':   None, 'lat': 46.533046, 'lon': 9.869358, 'tm': bus, 'name': "Samedan Central Bus Station"},

            {'point': 0, 'city': "CH-SIR", 'iata_code': 'SIR', 'icao_code': 'LSGS', 'lat': 46.219592, 'lon': 7.326764, 'tm': flight, 'name': "Sion-Sitten Airport"},
            {'point': 1, 'city': "CH-SIR", 'iata_code':  None, 'icao_code':   None, 'lat': 46.227447, 'lon': 7.359148, 'tm': train, 'name': "Sion Train Station"},
            {'point': 1, 'city': "CH-SIR", 'iata_code':  None, 'icao_code':   None, 'lat': 46.227807, 'lon': 7.359529, 'tm': bus, 'name': "Sion Bus Station"},
            # {'point': 2, 'city': "CH-SIR", 'iata_code':  None, 'icao_code':   None, 'lat': 46.229247, 'lon': 7.363696, 'tm': bus, 'name': "Tourbillon Bus Station"}, #close to the main station

            {'point': 1, 'city': "CH-WIN", 'iata_code':  None, 'icao_code':   None, 'lat': 47.500973, 'lon': 8.723730, 'tm': train, 'name': "Winterthur Central Train Station"},
            {'point': 1, 'city': "CH-WIN", 'iata_code':  None, 'icao_code':   None, 'lat': 47.500385, 'lon': 8.723952, 'tm': bus, 'name': "Winterthur Central Bus Station"},

            {'point': 0, 'city': "CH-ZRH", 'iata_code': 'ZRH', 'icao_code': 'LSZH', 'lat': 47.464722, 'lon': 8.549167, 'tm': flight, 'name': "Zurich Airport"},
            {'point': 0, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.450158, 'lon': 8.563512, 'tm': train, 'name': "Zurich Airport Train Station"},
            {'point': 0, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.450158, 'lon': 8.563512, 'tm': bus, 'name': "Zurich Airport Bus Station"},
            {'point': 1, 'city': "CH-ZRH", 'iata_code': 'ZLP', 'icao_code':   None, 'lat': 47.377916, 'lon': 8.540211, 'tm': train, 'name': "Zurich Main Station"},
            {'point': 1, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.380717, 'lon': 8.537089, 'tm': bus, 'name': "Zurich Main Station Bus"},
            {'point': 2, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.385132, 'lon': 8.517510, 'tm': train, 'name': "Zürich Hardbrücke Train Station"},
            {'point': 2, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.385132, 'lon': 8.517510, 'tm': bus, 'name': "Zurich Hardbrücke Bus Station"},
            {'point': 3, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.391477, 'lon': 8.488881, 'tm': train, 'name': "Zurich Altstetten Train Station"},
            {'point': 4, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.366563, 'lon': 8.548457, 'tm': train, 'name': "Zurich Stadelhofen Train Station"},
            {'point': 4, 'city': "CH-ZRH", 'iata_code':  None, 'icao_code':   None, 'lat': 47.366563, 'lon': 8.548457, 'tm': bus, 'name': "Zurich Stadelhofen Bus Station"},
        ]

        hubs_NL = [
            {'point': 1, 'city': "NL-ALK", 'iata_code':  None, 'icao_code':   None, 'lat': 52.637778, 'lon': 4.740556, 'tm': train, 'name': "Alkmaar Train Station"},
            {'point': 1, 'city': "NL-ALK", 'iata_code':  None, 'icao_code':   None, 'lat': 52.637778, 'lon': 4.740556, 'tm': bus, 'name': "Alkmaar Bus Station"},
            {'point': 2, 'city': "NL-ALK", 'iata_code':  None, 'icao_code':   None, 'lat': 52.643889, 'lon': 4.764722, 'tm': train, 'name': "Alkmaar Noord Train Station"},
            {'point': 2, 'city': "NL-ALK", 'iata_code':  None, 'icao_code':   None, 'lat': 52.643889, 'lon': 4.764722, 'tm': bus, 'name': "Alkmaar Noord Bus Station"},

            {'point': 1, 'city': "NL-AER", 'iata_code':  None, 'icao_code':   None, 'lat': 52.375302, 'lon': 5.215609, 'tm': train, 'name': "Almere Centrum Train Station"},
            {'point': 1, 'city': "NL-AER", 'iata_code':  None, 'icao_code':   None, 'lat': 52.375302, 'lon': 5.215609, 'tm': bus, 'name': "Almere Centrum Bus Station"},
            {'point': 2, 'city': "NL-AER", 'iata_code':  None, 'icao_code':   None, 'lat': 52.376667, 'lon': 5.244444, 'tm': train, 'name': "Almere Parkwijk Train"},
            {'point': 2, 'city': "NL-AER", 'iata_code':  None, 'icao_code':   None, 'lat': 52.376667, 'lon': 5.244444, 'tm': bus, 'name': "Almere Parkwijk Bus Station"},
        	{'point': 3, 'city': "NL-AER", 'iata_code':  None, 'icao_code':   None, 'lat': 52.367738, 'lon': 5.190772, 'tm': train, 'name': "Almere Muziekwijk Train Station"},
            {'point': 3, 'city': "NL-AER", 'iata_code':  None, 'icao_code':   None, 'lat': 52.367500, 'lon': 5.190278, 'tm': bus, 'name': " Almere Muziekwijk Bus Station"},

            {'point': 1, 'city': "NL-APN", 'iata_code':  None, 'icao_code':   None, 'lat': 52.124741, 'lon': 4.657528, 'tm': train, 'name': "Alphen a/d Rijn Train Station"},
            {'point': 1, 'city': "NL-APN", 'iata_code':  None, 'icao_code':   None, 'lat': 52.124741, 'lon': 4.657528, 'tm': bus, 'name': "Alphen a/d Rijn Bus Station"},

            {'point': 1, 'city': "NL-AME", 'iata_code':  None, 'icao_code':   None, 'lat': 52.153389, 'lon': 5.373994, 'tm': train, 'name': "Amersfoort Train Station"},
            {'point': 1, 'city': "NL-AME", 'iata_code':  None, 'icao_code':   None, 'lat': 52.153389, 'lon': 5.373994, 'tm': bus, 'name': "Amersfoort Bus Station"},
            {'point': 2, 'city': "NL-AME", 'iata_code':  None, 'icao_code':   None, 'lat': 52.174750, 'lon': 5.403997, 'tm': train, 'name': "Amersfoort Schothorst Train Station"},
            {'point': 2, 'city': "NL-AME", 'iata_code':  None, 'icao_code':   None, 'lat': 52.174750, 'lon': 5.403997, 'tm': bus, 'name': "Amersfoort Schothorst Bus Station"},
            {'point': 3, 'city': "NL-AME", 'iata_code':  None, 'icao_code':   None, 'lat': 52.192197, 'lon': 5.433416, 'tm': train, 'name': "Amersfoort Vathorst Train Station"},
            {'point': 3, 'city': "NL-AME", 'iata_code':  None, 'icao_code':   None, 'lat': 52.192197, 'lon': 5.433416, 'tm': bus, 'name': "Amersfoort Vathorst Bus Station"},

            {'point': 0, 'city': "NL-AMS", 'iata_code': 'AMS', 'icao_code': 'EHAM', 'lat': 52.308100, 'lon': 4.764169, 'tm': flight, 'name': "Amsterdam Schiphol"},
            {'point': 0, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.309414, 'lon': 4.762311, 'tm': train, 'name': "Amsterdam Schiphol"},
            {'point': 0, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.308695, 'lon': 4.761394, 'tm': bus, 'name': "Amsterdam Schiphol"},
            {'point': 1, 'city': "NL-AMS", 'iata_code': 'ZYA', 'icao_code':   None, 'lat': 52.379135, 'lon': 4.900229, 'tm': train, 'name': "Amsterdam Centraal"},
            {'point': 1, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.376987, 'lon': 4.902171, 'tm': bus, 'name': "Amsterdam Centraal"},
            {'point': 2, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.389032, 'lon': 4.838270, 'tm': train, 'name': "Amsterdam Sloterdijk"},
            {'point': 2, 'city': "NL-AMS", 'iata_code': '006', 'icao_code':   None, 'lat': 52.389053, 'lon': 4.836406, 'tm': bus, 'name': "Amsterdam Sloterdijk"},
            # {'point': 3, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.336816, 'lon': 4.890639, 'tm': train, 'name': "Amsterdan RAI Train Station"},
            # {'point': 3, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.337165, 'lon': 4.890992, 'tm': bus, 'name': "Amsterdan RAI Bus Station"},
            {'point': 4, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.339005, 'lon': 4.873472, 'tm': train, 'name': "Amsterdam-Zuid Train Station"},
            # {'point': 4, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.340683, 'lon': 4.873247, 'tm': bus, 'name': "Amsterdam-Zuid Bus Station"},
            # {'point': 5, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.360987, 'lon': 4.931158, 'tm': train, 'name': "Amsterdam Muiderpoort Train Station"},
            # {'point': 5, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.360476, 'lon': 4.931134, 'tm': bus, 'name': "Amsterdam Muiderpoort Bus Station"},
            # {'point': 6, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.346641, 'lon': 4.918266, 'tm': train, 'name': "Amsterdam - Amstel Train Station"},
            {'point': 6, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.346638, 'lon': 4.918542, 'tm': bus, 'name': "Amsterdam Amstel"},
            {'point': 7, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.326791, 'lon': 4.890366, 'tm': bus, 'name': "Amsterdam Europaboulevard"},
            # {'point': 8, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.357856, 'lon': 4.834012, 'tm': train, 'name': "Amsterdam Lelylaan Train Station"},
            # {'point': 9, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.323559, 'lon': 4.936490, 'tm': train, 'name': "Duivendrecht Train Station"},
            {'point': 9, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.323120, 'lon': 4.936812, 'tm': bus, 'name': "Duivendrecht Bus Station"},
            # # {'point':10, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.388066, 'lon': 4.638647, 'tm': train, 'name': "Station Haarlem Train"},
            # # {'point':10, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.388066, 'lon': 4.638647, 'tm': bus, 'name': "Station Haarlem Bus"},
            # # {'point':11, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.383045, 'lon': 4.671066, 'tm': train, 'name': "Haarlem Spaarnwoude Train"},
            # # {'point':11, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.383045, 'lon': 4.671066, 'tm': bus, 'name': "Haarlem Spaarnwoude Bus"},
            # # {'point':12, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.469174, 'lon': 4.805188, 'tm': train, 'name': "Station Koog-Zaandijk Train"},
            # # {'point':12, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.469174, 'lon': 4.805188, 'tm': bus, 'name': "Station Koog-Zaandijk Bus"},
            {'point':13, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.371417, 'lon': 4.962146, 'tm': bus, 'name': "Amsterdam P+R Zeeburg"},
            {'point':14, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.3106, 'lon': 4.94656, 'tm': bus, 'name': "Amsterdam Arena"},
            # # {'point': 50, 'city': "NL-AMS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.377864, 'lon': 4.915227, 'tm': ferry, 'name': "Amsterdam Ferry Terminal"},

            {'point': 1, 'city': "NL-APE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.209547, 'lon': 5.968627, 'tm': train, 'name': "Apeldoorn Train Station"},
            {'point': 1, 'city': "NL-APE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.209547, 'lon': 5.968627, 'tm': bus, 'name': "Apeldoorn Bus Station"},
            {'point': 2, 'city': "NL-APE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.215694, 'lon': 6.005881, 'tm': train, 'name': "Apeldoorn Osseveld"},
            #
            {'point': 1, 'city': "NL-ARN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.985578, 'lon': 5.899035, 'tm': train, 'name': "Arnhem Train Station"},
            {'point': 1, 'city': "NL-ARN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.985554, 'lon': 5.899619, 'tm': bus, 'name': "Arnhem Bus Station"},
            #
            {'point': 1, 'city': "NL-BRD", 'iata_code':  None, 'icao_code':   None, 'lat': 51.595390, 'lon': 4.780082, 'tm': train, 'name': "Centraal Breda Train Station"},
            {'point': 1, 'city': "NL-BRD", 'iata_code':  None, 'icao_code':   None, 'lat': 51.595993, 'lon': 4.780296, 'tm': bus, 'name': "Centraal Breda Bus Station"},
            {'point': 2, 'city': "NL-BRD", 'iata_code':  None, 'icao_code':   None, 'lat': 51.605295, 'lon': 4.722257, 'tm': train, 'name': "Breda-Prinsenbeek Arnhem Train Station"},
            {'point': 2, 'city': "NL-BRD", 'iata_code':  None, 'icao_code':   None, 'lat': 51.604093, 'lon': 4.723252, 'tm': bus, 'name': "Breda-Prinsenbeek Arnhem Bus Station"},
            #
            {'point': 1, 'city': "NL-DOR", 'iata_code':  None, 'icao_code':   None, 'lat': 51.807529, 'lon':  4.667768, 'tm': train, 'name': "Dordrecht Train Station"},
            {'point': 1, 'city': "NL-DOR", 'iata_code':  None, 'icao_code':   None, 'lat': 51.807425, 'lon':  4.670239, 'tm': bus, 'name': "Dordrecht Bus Station"},
            {'point': 2, 'city': "NL-DOR", 'iata_code':  None, 'icao_code':   None, 'lat': 51.790400, 'lon':  4.671989, 'tm': train, 'name': "Dordrecht Zuid Train Station"},
            {'point': 2, 'city': "NL-DOR", 'iata_code':  None, 'icao_code':   None, 'lat': 51.790582, 'lon':  4.672155, 'tm': bus, 'name': "Dordrecht Zuid Bus Station"},
            #
            {'point': 1, 'city': "NL-EDE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.043385, 'lon':  5.668341, 'tm': train, 'name': "Ede Centrum Train Station"},
            {'point': 1, 'city': "NL-EDE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.043385, 'lon':  5.668341, 'tm': bus, 'name': "Ede Centrum Bus Station"},
            {'point': 2, 'city': "NL-EDE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.028162, 'lon':  5.671481, 'tm': train, 'name': "Ede-Wageningen Train Station"},
            {'point': 2, 'city': "NL-EDE", 'iata_code':  None, 'icao_code':   None, 'lat': 52.028162, 'lon':  5.671481, 'tm': bus, 'name': "Ede-Wageningen Bus Station"},

            {'point': 0, 'city': "NL-EIN", 'iata_code': 'EIN', 'icao_code': 'EHEH', 'lat': 51.450556, 'lon': 5.374167, 'tm': flight, 'name': "Eindhoven Airport"},
            {'point': 0, 'city': "NL-EIN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.458239, 'lon': 5.392107, 'tm': bus, 'name': "Airexpressbus"},
            {'point': 1, 'city': "NL-EIN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.443422, 'lon': 5.479054, 'tm': train, 'name': "Eindhoven Train Station"},
            {'point': 1, 'city': "NL-EIN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.441871, 'lon': 5.481239, 'tm': bus, 'name': "Eindhoven Stationsweg"},
            {'point': 2, 'city': "NL-EIN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.450825, 'lon': 5.456368, 'tm': train, 'name': "Eindhoven Strijp S Train Station"},
            {'point': 2, 'city': "NL-EIN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.449855, 'lon': 5.456670, 'tm': bus, 'name': "Eindhoven Strijp S Bus Station"},
            {'point': 3, 'city': "NL-EIN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.446302, 'lon': 5.399523, 'tm': bus, 'name': "Eindhoven Flight Forum"},

            {'point': 1, 'city': "NL-EMM", 'iata_code':  None, 'icao_code':   None, 'lat': 52.790662, 'lon': 6.899362, 'tm': train, 'name': "Emmen Train Station"},
            {'point': 1, 'city': "NL-EMM", 'iata_code':  None, 'icao_code':   None, 'lat': 52.790662, 'lon': 6.899362, 'tm': bus, 'name': "Emmen Bus Station"},
            {'point': 2, 'city': "NL-EMM", 'iata_code':  None, 'icao_code':   None, 'lat': 52.748801, 'lon': 6.874201, 'tm': train, 'name': "Emmen Zuid"},

            {'point': 1, 'city': "NL-ENS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.222338, 'lon': 6.890330, 'tm': train, 'name': "Enschede Centraal"},
            {'point': 1, 'city': "NL-ENS", 'iata_code':  None, 'icao_code':   None, 'lat': 52.221626, 'lon': 6.889595, 'tm': bus, 'name': "Enschede Centraal"},
            {'point': 2, 'city': "NL-ENS", 'iata_code':  None, 'icao_code':   None, 'lat':   52.2381, 'lon':  6.85024, 'tm': bus, 'name': "Enschede UT"},

            {'point': 0, 'city': "NL-GRQ", 'iata_code': 'GRQ',  'icao_code':'EHGG', 'lat': 53.120556, 'lon': 6.578056, 'tm': flight, 'name': "Groningen Eelde Airport"},
            {'point': 1, 'city': "NL-GRQ", 'iata_code':  None, 'icao_code':   None, 'lat': 53.210966, 'lon': 6.564084, 'tm': train, 'name': "Groningen Hoofstation Train"},
            {'point': 1, 'city': "NL-GRQ", 'iata_code':  None, 'icao_code':   None, 'lat': 53.210966, 'lon': 6.564084, 'tm': bus, 'name': "Groningen Hoofstation Bus"},
            {'point': 2, 'city': "NL-GRQ", 'iata_code':  None, 'icao_code':   None, 'lat': 53.204807, 'lon': 6.585660, 'tm': train, 'name': "Groningen Europapark"},

            # {'point': 1, 'city': "NL-HVH", 'iata_code':  None, 'icao_code':   None, 'lat': 51.976236, 'lon': 4.127440, 'tm': train, 'name': "Hoek van Holland Haven"}, #belongs to Rotterdam
            # # {'point': 1, 'city': "NL-HVH", 'iata_code':  None, 'icao_code':   None, 'lat': 51.977603, 'lon': 4.125049, 'tm': ferry, 'name': "Hoek van Holland Berghaven"},
            #
            {'point': 1, 'city': "NL-LWR", 'iata_code':  None, 'icao_code':   None, 'lat': 53.196459, 'lon': 5.792978, 'tm': train, 'name': "Leeuwarden Train Station"},
            {'point': 1, 'city': "NL-LWR", 'iata_code':  None, 'icao_code':   None, 'lat': 53.196282, 'lon': 5.790997, 'tm': bus, 'name': "Leeuwarden Bus Station"},
            #
            {'point': 1, 'city': "NL-LID", 'iata_code':  None, 'icao_code':   None, 'lat': 52.166409, 'lon': 4.482092, 'tm': train, 'name': "Leiden Centraal"},
            {'point': 1, 'city': "NL-LID", 'iata_code':  None, 'icao_code':   None, 'lat': 52.166409, 'lon': 4.482092, 'tm': bus, 'name': "Leiden Centraal"},
            {'point': 2, 'city': "NL-LID", 'iata_code':  None, 'icao_code':   None, 'lat': 52.148103, 'lon': 4.492351, 'tm': bus, 'name': "Leiden Lammenschans"},

            {'point': 0, 'city': "NL-LEY", 'iata_code': 'LEY', 'icao_code': 'EHLE', 'lat': 52.455278, 'lon': 5.523056, 'tm': flight, 'name': "Lelystad Airport"},
            {'point': 1, 'city': "NL-LEY", 'iata_code':  None, 'icao_code':   None, 'lat': 52.508018, 'lon': 5.472851, 'tm': train, 'name': "Lelystad Centrum Train Station"},
            {'point': 1, 'city': "NL-LEY", 'iata_code':  None, 'icao_code':   None, 'lat': 52.508018, 'lon': 5.472851, 'tm': bus, 'name': "Lelystad Centrum Bus Station"},

            {'point': 0, 'city': "NL-MST", 'iata_code': 'MST', 'icao_code': 'EHBK', 'lat': 50.912558, 'lon': 5.769536, 'tm': flight, 'name': "Maastricht Aachen Airport"},
            {'point': 1, 'city': "NL-MST", 'iata_code': 'ZYT', 'icao_code':   None, 'lat': 50.849727, 'lon': 5.705339, 'tm': train, 'name': "Maastricht Train Station"},
            {'point': 1, 'city': "NL-MST", 'iata_code':  None, 'icao_code':   None, 'lat': 50.849727, 'lon': 5.705339, 'tm': bus, 'name': "Maastricht Bus Station"},
            {'point': 2, 'city': "NL-MST", 'iata_code':  None, 'icao_code':   None, 'lat': 50.837926, 'lon': 5.717599, 'tm': train, 'name': "Maastricht Randwyck Train Station"},
            {'point': 2, 'city': "NL-MST", 'iata_code':  None, 'icao_code':   None, 'lat': 50.837926, 'lon': 5.717599, 'tm': bus, 'name': "Maastricht Randwyck Bus Station"},

            {'point': 1, 'city': "NL-NIJ", 'iata_code':  None, 'icao_code':   None, 'lat': 51.843235, 'lon': 5.853025, 'tm': train, 'name': "Nijmegen Centraal Train Station"},
            {'point': 1, 'city': "NL-NIJ", 'iata_code':  None, 'icao_code':   None, 'lat': 51.842682, 'lon': 5.853486, 'tm': bus, 'name': "Nijmegen Centraal Bus Station"},
            {'point': 2, 'city': "NL-NIJ", 'iata_code':  None, 'icao_code':   None, 'lat': 51.827376, 'lon': 5.823459, 'tm': train, 'name': "Nijmegen Goffert Train Station"},
            {'point': 2, 'city': "NL-NIJ", 'iata_code':  None, 'icao_code':   None, 'lat': 51.827886, 'lon': 5.822624, 'tm': bus, 'name': "Nijmegen Goffert Bus Station"},
            {'point': 3, 'city': "NL-NIJ", 'iata_code':  None, 'icao_code':   None, 'lat': 51.863699, 'lon': 5.859666, 'tm': train, 'name': "Nijmegen Lent Train Station"},
            {'point': 3, 'city': "NL-NIJ", 'iata_code':  None, 'icao_code':   None, 'lat': 51.863681, 'lon': 5.859684, 'tm': bus, 'name': "Nijmegen Lent Bus Station"},

            {'point': 0, 'city': "NL-RTM", 'iata_code': 'RTM', 'icao_code': 'EHRD', 'lat': 51.949020, 'lon': 4.434022, 'tm': flight, 'name': "Rotterdam The Hague Airport"},
            {'point': 1, 'city': "NL-RTM", 'iata_code': 'QRH', 'icao_code':   None, 'lat': 51.923673, 'lon': 4.470500, 'tm': train, 'name': "Rotterdam Centraal"},
            {'point': 1, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.923584, 'lon': 4.466564, 'tm': bus, 'name': "Rotterdam Centraal"},
            # {'point': 2, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.885000, 'lon': 4.286700, 'tm': ferry, 'name': "Rotterdam Ferry Terminal"},
            {'point': 3, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.880396, 'lon': 4.530859, 'tm': train, 'name': "Rotterdam Lombardijen"},
            {'point': 3, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.880899, 'lon': 4.534183, 'tm': bus, 'name': "Rotterdam Lombardijen"},
            {'point': 4, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.886311, 'lon': 4.487591, 'tm': bus, 'name': "Rotterdam Zuid"},
            {'point': 5, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.951668, 'lon': 4.551980, 'tm': train, 'name': "Rotterdam Alexander"},
            {'point': 5, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.952126, 'lon': 4.552240, 'tm': bus, 'name': "Rotterdam Alexander"},
            {'point': 6, 'city': "NL-RTM", 'iata_code':  None, 'icao_code':   None, 'lat': 51.921171, 'lon': 4.558008, 'tm': bus, 'name': "Rotterdam Capelsburg"},

            {'point': 1, 'city': "NL-HTB", 'iata_code':  None, 'icao_code':   None, 'lat': 51.690581, 'lon': 5.293526, 'tm': train, 'name': "'s-Hertogenbosch Train Station"},
            {'point': 1, 'city': "NL-HTB", 'iata_code':  None, 'icao_code':   None, 'lat': 51.690100, 'lon': 5.294509, 'tm': bus, 'name': "'s-Hertogenbosch Bus Station"},
            {'point': 2, 'city': "NL-HTB", 'iata_code':  None, 'icao_code':   None, 'lat': 51.700539, 'lon': 5.318935, 'tm': train, 'name': "'s-Hertogenbosch Oost Train Station"},

            {'point': 1, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.070139, 'lon': 4.322310, 'tm': train, 'name': "Den Haag HS Train Station"},
            {'point': 1, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.070123, 'lon': 4.321836, 'tm': bus, 'name': "Den Haag HS Bus Station"},
            {'point': 2, 'city': "NL-HA9", 'iata_code': 'ZYH', 'icao_code':   None, 'lat': 52.081105, 'lon': 4.324205, 'tm': train, 'name': "Den Haag Centraal Train Station"},
            {'point': 2, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.081105, 'lon': 4.324205, 'tm': bus, 'name': "Den Haag Centraal Bus Station"},
            {'point': 3, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.090548, 'lon': 4.369095, 'tm': train, 'name': "Den Haag Mariahoeve Train Station"},
            {'point': 3, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.090548,  'lon': 4.369095, 'tm': bus, 'name': "Den Haag Mariahoeve Bus Station"},
            {'point': 4, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.007546, 'lon':  4.356519, 'tm': train, 'name': "Delft Train Station"},
            {'point': 4, 'city': "NL-HA9", 'iata_code':  None, 'icao_code':   None, 'lat': 52.007546, 'lon':  4.356519, 'tm': bus, 'name': "Delft Bus Station"},
            # # {'point': 5, 'city': "NL-ZTM", 'iata_code':  None, 'icao_code':   None, 'lat': 52.046455, 'lon': 4.491986, 'tm': train, 'name': "Zoetermeer Oost Train"},
            # {'point': 5, 'city': "NL-ZTM", 'iata_code':  None, 'icao_code':   None, 'lat': 52.046455, 'lon': 4.491986, 'tm': bus, 'name': "Zoetermeer Oost Bus"},

            {'point': 1, 'city': "NL-TLB", 'iata_code':  None, 'icao_code':   None, 'lat': 51.560557, 'lon': 5.083399, 'tm': train, 'name': "Tilburg Train Station"},
            {'point': 1, 'city': "NL-TLB", 'iata_code':  None, 'icao_code':   None, 'lat': 51.560447, 'lon': 5.081753, 'tm': bus, 'name': "Tilburg Bus Station"},

            {'point': 1, 'city': "NL-UTC", 'iata_code':  None, 'icao_code':   None, 'lat': 52.089317, 'lon': 5.110165, 'tm': train, 'name': "Utrecht Centraal"},
            {'point': 1, 'city': "NL-UTC", 'iata_code':  None, 'icao_code':   None, 'lat': 52.089317, 'lon': 5.110165, 'tm': bus, 'name': "Utrecht Centraal"},
            # {'point': 2, 'city': "NL-UTC", 'iata_code':  None, 'icao_code':   None, 'lat': 52.098863, 'lon': 5.065136, 'tm': train, 'name': "Utrecht Leidsche Rijn Train"},
            {'point': 2, 'city': "NL-UTC", 'iata_code':  None, 'icao_code':   None, 'lat': 52.098863, 'lon': 5.065136, 'tm': bus, 'name': "Utrecht Leidsche Rijn"},
            {'point': 3, 'city': "NL-UTC", 'iata_code':  None, 'icao_code':   None, 'lat': 52.056660, 'lon': 5.106809, 'tm': bus, 'name': "Utrecht Westraven"},

            {'point': 1, 'city': "NL-VEN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.365086, 'lon': 6.171421, 'tm': train, 'name': "Venlo Train Station"},
            {'point': 1, 'city': "NL-VEN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.364979, 'lon': 6.172380, 'tm': bus, 'name': "Venlo Bus Station"},
            {'point': 2, 'city': "NL-VEN", 'iata_code':  None, 'icao_code':   None, 'lat': 51.352   , 'lon': 6.18176 , 'tm': bus, 'name': "Venlo De Koel - Kaldenkerkerweg"},

            {'point': 1, 'city': "NL-ZWO", 'iata_code':  None, 'icao_code':   None, 'lat': 52.505578, 'lon': 6.090591, 'tm': train, 'name': "Zwolle Train Station"},
            {'point': 1, 'city': "NL-ZWO", 'iata_code':  None, 'icao_code':   None, 'lat': 52.505578, 'lon': 6.090591, 'tm': bus, 'name': "Zwolle Bus Station"},
        ]

        hubs_BE = [
            {"point": 0, "city": "BE-ANR", "iata_code": "ANR", "icao_code":"EBAW", "lat": 51.189444, "lon": 4.460278, "tm": flight, "name": "Antwerp Airport"},
            {"point": 1, "city": "BE-ANR", "iata_code": "ZWE", "icao_code":  None, "lat": 51.217193, "lon": 4.421250, "tm": train, "name": " Antwerpen Centraal"},
            {"point": 1, "city": "BE-ANR", "iata_code":  None, "icao_code":  None, "lat": 51.218454, "lon": 4.420759, "tm": bus, "name": "Antwerpen Centraal"},
            {"point": 2, "city": "BE-ANR", "iata_code":  None, "icao_code":  None, "lat": 51.218057, "lon": 4.394345, "tm": bus, "name": "Antwerpen Plantinkaai"},
            {"point": 3, "city": "BE-ANR", "iata_code":  None, "icao_code":  None, "lat": 51.196644, "lon": 4.396500, "tm": bus, "name": "Antwerpen Zuid"},
            {"point": 4, "city": "BE-ANR", "iata_code":  None, "icao_code":  None, "lat": 51.201064, "lon": 4.436604, "tm": bus, "name": "Antwerpen Berchem"},

            {"point": 0, "city": "BE-BGS", "iata_code": "OST", "icao_code":"EBOS", "lat": 51.198890, "lon": 2.862220, "tm": flight, "name": "Ostend–Bruges Airport"},
            {"point": 1, "city": "BE-BGS", "iata_code":  None, "icao_code":  None, "lat": 51.197666, "lon": 3.217845, "tm": train, "name": "Brugge Main Station"},
            {"point": 1, "city": "BE-BGS", "iata_code":  None, "icao_code":  None, "lat": 51.195844, "lon": 3.215952, "tm": bus, "name": "Brugge Main Station"},
            {"point": 2, "city": "BE-BGS", "iata_code":  None, "icao_code":  None, "lat": 51.223121, "lon": 3.201753, "tm": train, "name": "Brugge Sint-Pieters"},
            {"point": 2, "city": "BE-BGS", "iata_code":  None, "icao_code":  None, "lat": 51.223082, "lon": 3.202912, "tm": bus, "name": "Brugge Sint-Pieters"},
            # {"point": 3, "city": "BE-BGS", "iata_code":  None, "icao_code":  None, "lat": 51.340610, "lon": 3.189148, "tm": ferry, "name": "Zeebrugge Ferry Terminal"},

            {"point": 0, "city": "BE-BRU", "iata_code": "BRU", "icao_code":"EBBR", "lat": 50.900992, "lon": 4.485489, "tm": flight, "name": "Brussels Airport"},
            {"point": 0, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.898202, "lon": 4.482264, "tm": train, "name": "Brussels Airport"},
            {"point": 0, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.898027, "lon": 4.481022, "tm": bus, "name": "Brussels Airport"},
            {"point": 1, "city": "BE-BRU", "iata_code": "ZYR", "icao_code":  None, "lat": 50.836439, "lon": 4.334788, "tm": train, "name": "Brussels-South Midi"},
            {"point": 1, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.834937, "lon": 4.333031, "tm": bus, "name": "Brussels-South Midi"},
            {"point": 2, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.860525, "lon": 4.361787, "tm": train, "name": "Brussels-North"},
            {"point": 2, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.861487, "lon": 4.359960, "tm": bus, "name": "Brussels-North"},
            {"point": 3, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.845467, "lon": 4.357027, "tm": train, "name": "Brussels Centraal"},
            {"point": 4, "city": "BE-BRU", "iata_code":  None, "icao_code":  None, "lat": 50.838304, "lon": 4.373083, "tm": train, "name": "Brussels-Luxembourg"},

            {"point": 0, "city": "BE-CRL", "iata_code": "CRL", "icao_code":"EBCI", "lat": 50.464277, "lon": 4.464900, "tm": flight, "name": "Charleroi Airport"},
            {"point": 0, "city": "BE-CRL", "iata_code":  None, "icao_code":  None, "lat": 50.470108, "lon": 4.471801, "tm": bus, "name": "Charleroi Airport"},
            {"point": 1, "city": "BE-CRL", "iata_code":  None, "icao_code":  None, "lat": 50.404507, "lon": 4.438761, "tm": train, "name": "Charleroi-Sud Train Station"},
            {"point": 1, "city": "BE-CRL", "iata_code":  None, "icao_code":  None, "lat": 50.404507, "lon": 4.438761, "tm": bus, "name": "Charleroi-Sud Bus Station"},

            # {"point": 1, "city": "BE-GNE", "iata_code":  None, "icao_code":  None, "lat": 51.036130, "lon": 3.710915, "tm": train, "name": "Gent Sint-Pieters Train Station"},
            {"point": 1, "city": "BE-GNE", "iata_code":  None, "icao_code":  None, "lat": 51.036147, "lon": 3.710912, "tm": train, "name": " Gent Sint-Pieters"},
            {"point": 1, "city": "BE-GNE", "iata_code":  None, "icao_code":  None, "lat": 51.035566, "lon": 3.707036, "tm": bus, "name": " Gent Sint-Pieters"},
            {"point": 2, "city": "BE-GNE", "iata_code":  None, "icao_code":  None, "lat": 51.055976, "lon": 3.740654, "tm": train, "name": "Gent Dampoort Train Station"},
            {"point": 2, "city": "BE-GNE", "iata_code":  None, "icao_code":  None, "lat": 51.054971, "lon": 3.739882, "tm": bus, "name": " Gent Dampoort Bus Station"},

            {"point": 1, "city": "BE-LEU", "iata_code":  None, "icao_code":  None, "lat": 50.881341, "lon": 4.715585, "tm": train, "name": "Leuven Train Station"},
            {"point": 1, "city": "BE-LEU", "iata_code":  None, "icao_code":  None, "lat": 50.882278, "lon": 4.714582, "tm": bus, "name": "Leuven Bus Station"},

            {"point": 0, "city": "BE-LGG", "iata_code": "LGG", "icao_code":"EBLG", "lat": 50.636390, "lon": 5.442780, "tm": flight, "name": "Liège Airport"},
            {"point": 0, "city": "BE-LGG", "iata_code":  None, "icao_code":  None, "lat": 50.642510, "lon": 5.460641, "tm": bus, "name": "Liège Airport"},
            {"point": 1, "city": "BE-LGG", "iata_code":  None, "icao_code":  None, "lat": 50.624432, "lon": 5.566713, "tm": train, "name": "Liège Guillemins"},
            {"point": 1, "city": "BE-LGG", "iata_code":  None, "icao_code":  None, "lat": 50.624432, "lon": 5.566713, "tm": bus, "name": "Liège Guillemins"},
            {"point": 2, "city": "BE-LGG", "iata_code":  None, "icao_code":  None, "lat": 50.634919, "lon": 5.567629, "tm": bus, "name": "Liège Boulevard d'Avroy"},

            {"point": 1, "city": "BE-MQS", "iata_code":  None, "icao_code":  None, "lat": 50.453834, "lon": 3.942364, "tm": train, "name": "Mons Train Station"},
            {"point": 2, "city": "BE-MQS", "iata_code":  None, "icao_code":  None, "lat": 50.453520, "lon": 3.945479, "tm": bus, "name": "Mons Bus Station"},
            #
            {"point": 1, "city": "BE-NAM", "iata_code":  None, "icao_code":  None, "lat": 50.469079, "lon": 4.862459, "tm": train, "name": "Namur Train Station"},
            {"point": 1, "city": "BE-NAM", "iata_code":  None, "icao_code":  None, "lat": 50.469079, "lon": 4.862459, "tm": bus, "name": "Namur Bus Station"},
        ]

        hubs_IT = [
           # {"point": 0, "city": "IT-ALL", "iata_code": "ALL", "icao_code": "LIMG", "lat": 44.045833, "lon": 8.125556, "tm": flight, "name": "Albenga Riviera Airport"}, #no comerical flights at airport and city with 24.000 people
           # {"point": 1, "city": "IT-ALL", "iata_code": None, "icao_code": None, "lat": 44.047378, "lon": 8.221392, "tm": train, "name": "Albenga Train Station"},
           # {"point": 2, "city": "IT-ALL", "iata_code": None, "icao_code": None, "lat": 44.047913, "lon": 8.214429, "tm": bus, "name": "Albenga Bus Station"},

            {"point": 1, "city": "IT-ALE", "iata_code": None, "icao_code": None, "lat": 44.908798, "lon": 8.607532, "tm": train, "name": "Alessandria Train Station"},
            {"point": 1, "city": "IT-ALE", "iata_code": None, "icao_code": None, "lat": 44.908633, "lon": 8.608074, "tm": bus, "name": "Alessandria Bus Station"},

            {"point": 0, "city": "IT-AHO", "iata_code": "AHO", "icao_code": "LIEA", "lat": 40.631111, "lon": 8.288611, "tm": flight, "name": "Alghero Airport"},
            {"point": 0, "city": "IT-AHO", "iata_code": None, "icao_code": None, "lat": 40.629472, "lon": 8.295192, "tm": bus, "name": "Alghero Airport Bus Station"},
            {"point": 1, "city": "IT-AHO", "iata_code": None, "icao_code": None, "lat": 40.574890, "lon": 8.322215, "tm": train, "name": "Alghero Train Station"},
            {"point": 2, "city": "IT-AHO", "iata_code": None, "icao_code": None, "lat": 40.560474, "lon": 8.316756, "tm": bus, "name": "Alghero Bus Station"},

            {"point": 0, "city": "IT-AOI", "iata_code": "AOI", "icao_code": "LIPY", "lat": 43.616111, "lon": 13.362222, "tm": flight, "name": "Ancona Marche Airport"},
            {"point": 1, "city": "IT-AOI", "iata_code": None, "icao_code": None, "lat": 43.607477, "lon": 13.497683, "tm": train, "name": "Ancona Train Station"},
            {"point": 1, "city": "IT-AOI", "iata_code": None, "icao_code": None, "lat": 43.607452, "lon": 13.497906, "tm": bus, "name": "Ancona Bus Station"},
            # {"point": 1, "city": "IT-AOI", "iata_code": None, "icao_code": None, "lat": 43.620718, "lon": 13.508813, "tm": ferry, "name": "Ancona Ferry Terminal"},
            {"point": 2, "city": "IT-AOI", "iata_code": None, "icao_code": None, "lat": 43.5982, "lon": 13.5101, "tm": bus, "name": "Ancona"},
            {"point": 3, "city": "IT-AOI", "iata_code": None, "icao_code": None, "lat": 43.597800, "lon": 13.356400, "tm": bus, "name": "Ancona Nord"},

            {"point": 1, "city": "IT-ADR", "iata_code": None, "icao_code":   None, "lat": 41.315433, "lon": 16.278609, "tm": train, "name": "Andria Train Station"},
            {"point": 2, "city": "IT-ADR", "iata_code": None, "icao_code":   None, "lat": 41.240959, "lon": 16.292599, "tm": bus, "name": "Andria Bus Station"},

            {"point": 1, "city": "IT-ARE", "iata_code": None, "icao_code":   None, "lat": 43.461202, "lon": 11.875693, "tm": train, "name": "Arezzo Train Station"},
            {"point": 1, "city": "IT-ARE", "iata_code": None, "icao_code":   None, "lat": 43.462264, "lon": 11.875222, "tm": bus, "name": "Arezzo Terminal"},
            {"point": 2, "city": "IT-ARE", "iata_code": None, "icao_code":   None, "lat": 43.466683, "lon": 11.874965, "tm": bus, "name": "Arezzo Via Rossellino"}, #FlixBus en web FlixBus, no ho he trobat en Google Maps

            {"point": 0, "city": "IT-BRI", "iata_code": "BRI", "icao_code": "LIBD", "lat": 41.138856, "lon": 16.760594, "tm": flight, "name": "Bari Airport"},
            {"point": 1, "city": "IT-BRI", "iata_code": None, "icao_code": None, "lat": 41.117972, "lon": 16.870083, "tm": train, "name": "Bari Train Station"},
            {"point": 2, "city": "IT-BRI", "iata_code": None, "icao_code": None, "lat": 41.117003, "lon": 16.869938, "tm": bus, "name": "Bari Bus Station"},
            # {"point": 3, "city": "IT-BRI", "iata_code": None, "icao_code": None, "lat": 41.136557, "lon": 16.867247, "tm": ferry, "name": "Bari Crociere Ferry Terminal"},
            # {"point": 4, "city": "IT-BRI", "iata_code": None, "icao_code": None, "lat": 41.132718, "lon": 16.866813, "tm": ferry, "name": "Bari Ferry Terminal"},

            {'point': 0, 'city': 'IT-BGO', 'iata_code': 'BGY', 'icao_code':'LIME', 'lat': 45.669569, 'lon': 9.703629, 'tm': flight, 'name': "Orio al Serio Airport"},
            {'point': 0, 'city': 'IT-BGO', 'iata_code':  None, 'icao_code':  None, 'lat': 45.665693, 'lon': 9.698070, 'tm': bus, 'name': "Orio al Serio Airport Bus Station"},
            {'point': 1, 'city': 'IT-BGO', 'iata_code':  None, 'icao_code':  None, 'lat': 45.690402, 'lon': 9.675072, 'tm': train, 'name': "Bergamo Train Station"},
            {'point': 1, 'city': 'IT-BGO', 'iata_code':  None, 'icao_code':  None, 'lat': 45.691977, 'lon': 9.675470, 'tm': bus, 'name': "Bergamo Bus Station"},

            {"point": 0, "city": "IT-BLQ", "iata_code": "BLQ", "icao_code": "LIPE", "lat": 44.535444, "lon": 11.288667, "tm": flight, "name": "Bologna Airport"},
            {"point": 1, "city": "IT-BLQ", "iata_code": "IBT", "icao_code":   None, "lat": 44.505881, "lon": 11.343430, "tm": train, "name": "Bologna Centrale"},
            {"point": 1, "city": "IT-BLQ", "iata_code": None, "icao_code":    None, "lat": 44.503938, "lon": 11.346854, "tm": bus, "name": "Bologna Centrale"},
            {"point": 2, "city": "IT-BLQ", "iata_code": None, "icao_code":    None, "lat":   44.4915, "lon":   11.3852, "tm": train, "name": "Bologna San Vitale"},
            {'point': 3, 'city': 'IT-BLQ', 'iata_code': None, 'icao_code':    None, 'lat': 44.462784, 'lon': 11.372813, 'tm': train, 'name': 'Bologna S. Ruffillo'},

            {"point": 0, "city": "IT-BZO", "iata_code": "BZO", "icao_code": "LIPB", "lat": 46.460278, "lon": 11.326389, "tm": flight, "name": "Bolzano Airport"},
            {"point": 1, "city": "IT-BZO", "iata_code": "BZQ", "icao_code":   None, "lat": 46.496728, "lon": 11.358329, "tm": train, "name": "Bolzano Train Station"},
            {"point": 2, "city": "IT-BZO", "iata_code": None, "icao_code":   None, "lat": 46.495944, "lon": 11.355184, "tm": bus, "name": "Bolzano Bus Station"},

            # {"point": 0, "city": "IT-BRC", "iata_code": "VBS", "icao_code": "LIPO", "lat": 45.428611, "lon": 10.331389, "tm": flight, "name": "Brescia Airport"}, #Not connected to Brescia, but Montichiari and just 1 commercial flight
            {"point": 1, "city": "IT-BRC", "iata_code": None, "icao_code": None, "lat": 45.532528, "lon": 10.212981, "tm": train, "name": "Brescia Train Station"},
            {"point": 1, "city": "IT-BRC", "iata_code": None, "icao_code": None, "lat": 45.532770, "lon": 10.214461, "tm": bus, "name": "Brescia Bus Station"},

            {"point": 0, "city": "IT-BDS", "iata_code": "BDS", "icao_code": "LIBR", "lat": 40.657516, "lon": 17.946897, "tm": flight, "name": "Brindisi Airport"},
            {"point": 0, "city": "IT-BDS", "iata_code": None, "icao_code": None, "lat": 40.658779, "lon": 17.939952, "tm": bus, "name": "Brindisi Airport Bus Station"},
            {"point": 1, "city": "IT-BDS", "iata_code": None, "icao_code": None, "lat": 40.634263, "lon": 17.939279, "tm": train, "name": "Brindisi Train Station"},
            # {"point": 2, "city": "IT-BDS", "iata_code": None, "icao_code": None, "lat": 40.624180, "lon": 17.929449, "tm": train, "name": "Brindisi Train Terminal"}, #coordinates are same as point 4, but no train is here!
            {"point": 3, "city": "IT-BDS", "iata_code": None, "icao_code": None, "lat": 40.629093, "lon": 17.947887, "tm": bus, "name": "Brindisi Viale Arno"},
            {"point": 4, "city": "IT-BDS", "iata_code": None, "icao_code": None, "lat": 40.624181, "lon": 17.929452, "tm": bus, "name": "Brindisi Via Galanti"},
            # {"point": 4, "city": "IT-BDS", "iata_code": None, "icao_code": None, "lat": 40.647567, "lon": 17.964328, "tm": ferry, "name": "Brindisi Ferry Terminal"},

            {"point": 0, "city": "IT-CAG", "iata_code": "CAG", "icao_code": "LIEE", "lat": 39.2514694, "lon": 9.0542833, "tm": flight, "name": "Cagliari-Elmas Airport"},
            {"point": 0, "city": "IT-CAG", "iata_code": None, "icao_code": None, "lat": 39.256201, "lon": 9.065391, "tm": train, "name": "Cagliari-Elmas Airport Train Station"},
            {"point": 1, "city": "IT-CAG", "iata_code": None, "icao_code": None, "lat": 39.215997, "lon": 9.108225, "tm": train, "name": "Cagliari Train Station"},
            {"point": 1, "city": "IT-CAG", "iata_code": None, "icao_code": None, "lat": 39.216147, "lon": 9.108464, "tm": bus, "name": "Cagliari Bus Station"},
            # {"point": 2, "city": "IT-CAG", "iata_code": None, "icao_code": None, "lat": 39.211222, "lon": 9.106730, "tm": ferry, "name": "Cagliari Ferry Terminal"},

          # {"point": 0, "city": "IT-CMD", "iata_code": "UDN", "icao_code": "LIPD", "lat": 46.031389, "lon": 13.186944, "tm": flight, "name": "Udine-Campoformido Airport"}, # aeroclub? --> no comerical flights at airport and city with 8.000 people
          # {"point": 1, "city": "IT-CMD", "iata_code": None, "icao_code": None, "lat": 46.023728, "lon": 13.167462, "tm": bus, "name": "Campoformido Bus Station"},

            {"point": 0, "city": "IT-CTA", "iata_code": "CTA", "icao_code": "LICC", "lat": 37.466667, "lon": 15.063889, "tm": flight, "name": "Catania-Fontanarossa Airport"},
            {"point": 1, "city": "IT-CTA", "iata_code": None, "icao_code": None, "lat": 37.506737, "lon": 15.099920, "tm": train, "name": "Catania Train Station"},
            {"point": 2, "city": "IT-CTA", "iata_code": None, "icao_code": None, "lat": 37.508013, "lon": 15.098238, "tm": bus, "name": "Catania Bus Station"},
            # {"point": 3, "city": "IT-CTA", "iata_code": None, "icao_code": None, "lat": 37.498959, "lon": 15.095490, "tm": ferry, "name": "Catania Ferry Terminal"},

            {"point": 0, "city": "IT-CIY", "iata_code": "CIY", "icao_code": "LICB", "lat": 36.991667, "lon": 14.606944, "tm": flight, "name": "Comiso Airport"},
            {"point": 1, "city": "IT-CIY", "iata_code": None, "icao_code": None, "lat": 36.946276, "lon": 14.600376, "tm": train, "name": "Comiso Train Station"},
            {"point": 2, "city": "IT-CIY", "iata_code": None, "icao_code": None, "lat": 36.957435, "lon": 14.607236, "tm": bus, "name": "Comiso Bus Station"},

            {"point": 0, "city": "IT-CUN", "iata_code": "CUF", "icao_code": "LIMZ", "lat": 44.546944, "lon": 7.623056, "tm": flight, "name": "Cuneo Levaldigi Airport"},
            {"point": 1, "city": "IT-CUN", "iata_code": None, "icao_code": None, "lat": 44.387801, "lon": 7.536326, "tm": train, "name": "Cuneo Train Station"},
            {"point": 1, "city": "IT-CUN", "iata_code": None, "icao_code": None, "lat": 44.386624, "lon": 7.535726, "tm": bus, "name": "Cuneo Bus Station"},

            {'point': 0, 'city': 'IT-EBA', 'iata_code': "EBA", 'icao_code': 'LIRJ', "lat": 42.760278, 'lon': 10.239444, 'tm': flight, 'name': "Elba-Marina di Campo Airport"},
            # {'point': 1, 'city': 'IT-EBA', 'iata_code': None, 'icao_code': None, 'lat': 42.810968, 'lon': 10.306648, 'tm': bus, 'name': "Elba Bus Station"}, #island
            # {'point': 2, 'city': 'IT-EBA', 'iata_code': None, 'icao_code': None, 'lat': 42.812033, 'lon': 10.324515, 'tm': ferry, 'name': "Elba Ferry Terminal"},
            # {'point': 3, 'city': 'IT-EBA', 'iata_code': None, 'icao_code': None, 'lat': 42.815362, 'lon': 10.431017, 'tm': ferry, 'name': "Elba-Rio Marina Ferry Terminal"},

            {"point": 1, "city": "IT-FRR", "iata_code": None, "icao_code":   None, "lat": 44.842892, "lon": 11.603970, "tm": train, "name": "Ferrara Train Station"},
            {"point": 1, "city": "IT-FRR", "iata_code": None, "icao_code":   None, "lat": 44.842925, "lon": 11.604847, "tm":bus, "name": "Ferrara Bus Station"},

            {"point": 0, "city": "IT-FLR", "iata_code": "FLR", "icao_code": "LIRQ", "lat": 43.810000, "lon": 11.203889, "tm": flight, "name": "Florence Airport"},
            {"point": 1, "city": "IT-FLR", "iata_code": 'ZMS', "icao_code": None, "lat": 43.776523, "lon": 11.247888, "tm": train, "name": "Firenze S.M. Novella"},
            {"point": 1, "city": "IT-FLR", "iata_code": None, "icao_code": None, "lat": 43.775329, "lon": 11.246837, "tm": bus, "name": "Firenze S.M. Novella"}, # flixBus
            # {"point": 1, "city": "IT-FLR", "iata_code": None, "icao_code": None, "lat": 43.781006, "lon": 11.246401, "tm": bus, "name": "Florence Bus Station"}, # buscenter.it
            # {"point": 1, "city": "IT-FLR", "iata_code": None, "icao_code": None, "lat": 43.781049, "lon": 11.246700, "tm": bus, "name": "Florence Bus Station"}, # Bus a Alemania
            {"point": 2, "city": "IT-FLR", "iata_code": None, "icao_code": None, "lat": 43.755043, "lon": 11.173470, "tm": bus, "name": "Firenze Villa Costanza"},
            {"point": 3, "city": "IT-FLR", "iata_code":'FIR', "icao_code": None, "lat": 43.777632, "lon": 11.276047, "tm": train, "name": "Firenze Campo di Marte"},
            {"point": 4, "city": "IT-FLR", "iata_code": None, "icao_code": None, "lat": 43.800213, "lon": 11.236445, "tm": train, "name": "Firenze Rifredi"},

            {"point": 0, "city": "IT-FOG", "iata_code": "FOG", "icao_code": "LIBF", "lat": 41.432778, "lon": 15.535000, "tm": flight, "name": "Foggia Airport"},
            {"point": 1, "city": "IT-FOG", "iata_code": None, "icao_code": None, "lat": 41.465558, "lon": 15.555564, "tm": train, "name": "Foggia Train Station"},
            # {"point": 1, "city": "IT-FOG", "iata_code": None, "icao_code": None, "lat": 41.464992, "lon": 15.556066, "tm": bus, "name": "Foggia Bus Station"}, #Saps Line
            {"point": 1, "city": "IT-FOG", "iata_code": None, "icao_code": None, "lat": 41.465958, "lon": 15.553408, "tm": bus, "name": "Foggia Bus Station"}, #FlixBus

            {"point": 1, "city": "IT-FRL", "iata_code": None, "icao_code":   None, "lat": 44.223983, "lon": 12.054645, "tm": train, "name": "Forlì Train Station"},
            {"point": 1, "city": "IT-FRL", "iata_code": None, "icao_code":   None, "lat": 44.223732, "lon": 12.054122, "tm": bus, "name": "Forlì Bus Station"},

            {"point": 0, "city": "IT-GOA", "iata_code": "GOA", "icao_code": "LIMJ", "lat": 44.413333, "lon": 8.837489, "tm": flight, "name": "Genova Airport"}, #havies posat Genoa i Genova, ho he unificat.
            {"point": 1, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.416886, "lon": 8.921535, "tm": train, "name": "Genova Principe"},
            {"point": 1, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.417007, "lon": 8.921784, "tm": bus, "name": "Genova Principe"},
            {"point": 2, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.413095, "lon": 8.887280, "tm": train, "name": "Genova Sampierdarena"},
            {"point": 3, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.406639, "lon": 8.946809, "tm": train, "name": "Genova Brignole"},
            {"point": 4, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.403635, "lon": 8.945906, "tm": bus, "name": "Genova P. d. Vittoria"},
            {"point": 5, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.406751, "lon": 8.934102, "tm": bus, "name": "Genova P. Raffaele de Ferrari"},
            {"point": 6, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat":   44.4286, "lon":  8.75875, "tm": bus, "name": "Genova Voltri"},
            {"point": 7, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat":   44.3812, "lon":  9.03996, "tm": train, "name": "Genova Nervi"},
            # {"point": 5, "city": "IT-GOA", "iata_code": None, "icao_code": None, "lat": 44.411392, "lon": 8.915623, "tm": ferry, "name": "Genova Ferry Terminal"},

           # {"point": 0, "city": "IT-GRS", "iata_code": "GRS", "icao_code": "LIRS", "lat": 42.759722, "lon": 11.071667, "tm": flight, "name": "Grosseto Airport"}, #no commercial flights
           # {"point": 1, "city": "IT-GRS", "iata_code": None, "icao_code": None, "lat": 42.767331, "lon": 11.106472, "tm": train, "name": "Grosseto Train Station"},
           # {"point": 1, "city": "IT-GRS", "iata_code": None, "icao_code": None, "lat": 42.767663, "lon": 11.107014, "tm": bus, "name": "Grosseto Bus Station"},

            {"point": 0, "city": "IT-SUF", "iata_code": "SUF", "icao_code": "LICA", "lat": 38.905278, "lon": 16.242222, "tm": flight, "name": "Lamezia Terme Airport"},
            {"point": 1, "city": "IT-SUF", "iata_code": None, "icao_code": None, "lat": 38.921149, "lon": 16.255438, "tm": train, "name": "Lamezia Terme Train Station"},
            {"point": 1, "city": "IT-SUF", "iata_code": None, "icao_code": None, "lat": 38.921194, "lon": 16.255281, "tm": bus, "name": "Lamezia Terme Bus Station"},

            {"point": 0, "city": "IT-LMP", "iata_code": "LMP", "icao_code": "LICD", "lat": 35.497778, "lon": 12.618056, "tm": flight, "name": "Lampedusa Airport"},
            # {"point": 1, "city": "IT-LMP", "iata_code": None, "icao_code": None, "lat": 35.498366, "lon": 12.603831, "tm": ferry, "name": "Lampedusa Ferry Terminal"},

            {"point": 1, "city": "IT-LTN", "iata_code": None, "icao_code":   None, "lat": 41.538158, "lon": 12.946111, "tm": train, "name": "Latina Train Station"},
            {"point": 1, "city": "IT-LTN", "iata_code": None, "icao_code":   None, "lat": 41.473084, "lon": 12.895125, "tm": bus, "name": "Latina Bus Station"},

            {"point": 1, "city": "IT-SPE", "iata_code": None, "icao_code":   None, "lat": 44.111308, "lon": 9.813454, "tm": train, "name": "La Spezia Centrale"},
            {"point": 2, "city": "IT-SPE", "iata_code": None, "icao_code":   None, "lat": 44.113759, "lon": 9.847514, "tm": bus, "name": "La Spezia Via Giosuè Carducci"},
            {"point": 3, "city": "IT-SPE", "iata_code": None, "icao_code":   None, "lat": 44.104500, "lon": 9.826720, "tm": bus, "name": "La Spezia Viale Italia"},
            {"point": 4, "city": "IT-SPE", "iata_code": None, "icao_code":   None, "lat":   44.1233, "lon":  9.83984, "tm": train, "name": "La Spezia Migliarina"},

            {"point": 1, "city": "IT-LIV", "iata_code": None, "icao_code":   None, "lat": 43.554216, "lon": 10.336002, "tm": train, "name": "Livorno Train Station"},
            {"point": 1, "city": "IT-LIV", "iata_code": None, "icao_code":   None, "lat": 43.554159, "lon": 10.335720, "tm": bus, "name": "Livorno Bus Station"},

           # {"point": 0, "city": "IT-LCV", "iata_code": "LCV", "icao_code": "LIQL", "lat": 43.825849, "lon": 10.577968, "tm": flight, "name": "Lucca-Tassignano Airport"}, #no commercial flights and population 80000 / wrong code
           # {"point": 1, "city": "IT-LCV", "iata_code": None, "icao_code": None, "lat": 43.837348, "lon": 10.506141, "tm": train, "name": "Lucca Train Station"},
           # {"point": 1, "city": "IT-LCV", "iata_code": None, "icao_code": None, "lat": 43.837414, "lon": 10.506149, "tm": bus, "name": "Lucca Bus Station"},
           # {"point": 2, "city": "IT-LCV", "iata_code": None, "icao_code": None, "lat": 43.835179, "lon": 10.494626, "tm": bus, "name": "Lucca Bus Station"},

            {"point": 1, "city": "IT-MSN", "iata_code": None, "icao_code":   None, "lat": 38.185447, "lon": 15.561034, "tm": train, "name": "Messina Train Station"},
            {"point": 1, "city": "IT-MSN", "iata_code": None, "icao_code":   None, "lat": 38.185237, "lon": 15.560324, "tm": bus, "name": "Messina Bus Station"},
            # {"point": 2, "city": "IT-MSN", "iata_code": None, "icao_code":   None, "lat": 38.187504, "lon": 15.562712, "tm": ferry, "name": "Messina Ferry Terminal"},

            {'point': 0, 'city': 'IT-MIL', 'iata_code': 'MXP', 'icao_code':'LIMC', 'lat': 45.630054, 'lon': 8.725511, 'tm': flight, 'name': "Milan Malpensa Airport"},
            {'point': 0, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.627217, 'lon': 8.711025, 'tm': train, 'name': "Milan Malpensa Train Station"},
            {'point': 0, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.625694, 'lon': 8.712667, 'tm': bus, 'name': "Milan Malpensa Terminal 1"},
            {'point':10, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.648326, 'lon': 8.722404, 'tm': bus, 'name': "Milan Malpensa Terminal 2"},
            {'point': 1, 'city': 'IT-MIL', 'iata_code': 'LIN', 'icao_code':'LIML', 'lat': 45.452161, 'lon': 9.276319, 'tm': flight, 'name': "Milan Linate Airport"},
            {'point': 2, 'city': 'IT-MIL', 'iata_code': 'XIK', 'icao_code':  None, 'lat': 45.485883, 'lon': 9.204287, 'tm': train, 'name': "Milano Centrale Train Station"},
            {'point': 2, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.484392, 'lon': 9.202725, 'tm': bus, 'name': "Milano Centrale"},
            {'point': 3, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.484305, 'lon': 9.187682, 'tm': train, 'name': "Milano Porta Garibaldi Train Station"},
            {'point': 4, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.489755, 'lon': 9.127582, 'tm': bus, 'name': "Milano Lampugnano"},
            {'point': 5, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.541863, 'lon': 9.239034, 'tm': bus, 'name': "Milano Sesto San Giovanni"},
            {'point': 6, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.429198, 'lon': 9.256083, 'tm': bus, 'name': "Milano San Donato"},
            {'point': 7, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.464461, 'lon': 9.189535, 'tm': bus, 'name': "Milano Duomo"},
            {'point': 8, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.433433, 'lon': 9.237886, 'tm': bus, 'name': "Milano Rogoredo"},
            {'point': 9, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat': 45.535315, 'lon': 9.291368, 'tm': bus, 'name': "Milano Cologno Nord"},
            {'point':11, 'city': 'IT-MIL', 'iata_code':  None, 'icao_code':  None, 'lat':   45.4337, 'lon':  9.23901, 'tm': train, 'name': 'Milano Rogoredo'},

            {"point": 1, "city": "IT-MZA", "iata_code": None, "icao_code": None, "lat": 45.577943, "lon": 9.272930, "tm": train, "name": "Monza Train Station"},
            {"point": 1, "city": "IT-MZA", "iata_code": None, "icao_code": None, "lat": 45.578214, "lon": 9.273867, "tm": bus, "name": "Monza Bus Station"},
            {"point": 2, "city": "IT-MZA", "iata_code": None, "icao_code": None, "lat": 45.581910, "lon": 9.284499, "tm": train, "name": "Monza Sobborghi Train Station"},

            {"point": 0, "city": "IT-NAP", "iata_code": "NAP", "icao_code": "LIRN", "lat": 40.884444, "lon": 14.290833, "tm": flight, "name": "Naples Airport"},
            {"point": 0, "city": "IT-NAP", "iata_code":  None, "icao_code":   None, "lat": 40.875377, "lon": 14.284290, "tm": bus, "name": "Naples Airport"},
            {"point": 1, "city": "IT-NAP", "iata_code": 'INP', "icao_code": None, "lat": 40.852172, "lon": 14.272781, "tm": train, "name": "Naples Train Station"},
            # {"point": 1, "city": "IT-NAP", "iata_code": None, "icao_code": None, "lat": 40.852115, "lon": 14.271841, "tm": bus, "name": "Naples Bus Station"}, # Italia-Germania
            {"point": 2, "city": "IT-NAP", "iata_code": None, "icao_code": None, "lat": 40.850933, "lon": 14.273614, "tm": bus, "name": "Naples Piazza Garibaldi"},
            {"point": 3, "city": "IT-NAP", "iata_code": None, "icao_code": None, "lat": 40.833209, "lon": 14.249812, "tm": bus, "name": "Naples Via Santa Lucia"}, # FlixBus
            # {"point": 3, "city": "IT-NAP", "iata_code": None, "icao_code": None, "lat": 40.849225, "lon": 14.269252, "tm": train, "name": "Naples Porta Nolana Train Station"},
            {"point": 4, "city": "IT-NAP", "iata_code": None, "icao_code": None, "lat": 40.9314, "lon": 14.3311, "tm": train, "name": "Napoli Afragola"},
            {'point': 5, 'city': 'IT-NAP', 'iata_code': None, 'icao_code':  None, 'lat':  40.846, 'lon': 14.2873, 'tm': train, 'name': 'Napoli Gianturco'},
            # {"point": 9, "city": "IT-NAP", "iata_code": None, "icao_code": None, "lat": 40.838089, "lon": 14.258928, "tm": ferry, "name": "Naples Ferry Terminal"},

            {"point": 1, "city": "IT-NVR", "iata_code": None, "icao_code":   None, "lat": 45.451085, "lon": 8.624537, "tm": train, "name": "Novara Train Station"},
            {"point": 2, "city": "IT-NVR", "iata_code": None, "icao_code":   None, "lat": 45.474358, "lon": 8.564922, "tm": bus, "name": "Novara Bus Station"},

            {"point": 0, "city": "IT-OLB", "iata_code": "OLB", "icao_code": "LIEO", "lat": 40.885833, "lon": 9.516944, "tm": flight, "name": "Olbia Airport"},
            {"point": 1, "city": "IT-OLB", "iata_code": None, "icao_code": None, "lat": 40.924595, "lon": 9.498514, "tm": train, "name": "Olbia Train Station"},
            {"point": 1, "city": "IT-OLB", "iata_code": None, "icao_code": None, "lat": 40.924517, "lon": 9.498589, "tm": bus, "name": "Olbia Bus Station"},
            # {"point": 2, "city": "IT-OLB", "iata_code": None, "icao_code": None, "lat": 40.22577, "lon": 9.524426, "tm": ferry, "name": "Olbia Ferry Terminal"},

            {"point": 1, "city": "IT-PD4", "iata_code": None, "icao_code":   None, "lat": 45.417365, "lon": 11.880460, "tm": train, "name": "Padua Stazione Centrale"}, # En italiano Padova
            {"point": 1, "city": "IT-PD4", "iata_code": None, "icao_code":   None, "lat": 45.416290, "lon": 11.882240, "tm": bus, "name": "Padua Stazione Centrale"}, # En italiano Padova
            {"point": 2, "city": "IT-PD4", "iata_code": None, "icao_code":   None, "lat": 45.412523, "lon": 11.882360, "tm": bus, "name": "Padua Bus Station"}, # En italiano Padova

            {"point": 0, "city": "IT-PMO", "iata_code": "PMO", "icao_code": "LICJ", "lat": 38.181944, "lon": 13.099444, "tm": flight, "name": "Palermo Airport"},
            {"point": 0, "city": "IT-PMO", "iata_code": None, "icao_code": None, "lat": 38.188408, "lon": 13.107932, "tm": bus, "name": "Palermo Airport"},
            {"point": 1, "city": "IT-PMO", "iata_code": None, "icao_code": None, "lat": 38.109852, "lon": 13.367117, "tm": train, "name": "Palermo Centrale"},
            {"point": 1, "city": "IT-PMO", "iata_code": None, "icao_code": None, "lat": 38.109868, "lon": 13.366535, "tm": bus, "name": "Palermo Centrale"},
            {"point": 2, "city": "IT-PMO", "iata_code": None, "icao_code": None, "lat": 38.125271, "lon": 13.357192, "tm": bus, "name": "Palermo Politeama"},

            {"point": 0, "city": "IT-PNL", "iata_code": "PNL", "icao_code": "LICG", "lat": 36.816389, "lon": 11.968611, "tm": flight, "name": "Pantelleria Airport"},
            # {"point": 1, "city": "IT-PNL", "iata_code": None, "icao_code": None, "lat": 36.768565, "lon": 11.963532, "tm": ferry, "name": "Pantelleria Ferry Terminal"},

            {"point": 0, "city": "IT-PMF", "iata_code": "PMF", "icao_code": "LIMP", "lat": 44.822222, "lon": 10.295278, "tm": flight, "name": "Parma Airport"},
            {"point": 1, "city": "IT-PMF", "iata_code": None, "icao_code": None, "lat": 44.810270, "lon": 10.328588, "tm": train, "name": "Parma Train Station"},
            # {"point": 1, "city": "IT-PMF", "iata_code": None, "icao_code": None, "lat": 44.810500, "lon": 10.328715, "tm": bus, "name": "Parma Bus Station"},
            {"point": 1, "city": "IT-PMF", "iata_code": None, "icao_code": None, "lat": 44.811146, "lon": 10.327722, "tm": bus, "name": "Parma Bus Station"}, #FlixBus,
            {"point": 2, "city": "IT-PMF", "iata_code": None, "icao_code": None, "lat": 44.835721, "lon": 10.341026, "tm": bus, "name": "Parma Via Carra"},

            {"point": 0, "city": "IT-PEG", "iata_code": "PEG", "icao_code": "LIRZ", "lat": 43.095833, "lon": 12.513056, "tm": flight, "name": "Perugia San Francesco d'Assisi Airport"},
            {"point": 1, "city": "IT-PEG", "iata_code": None, "icao_code": None, "lat": 43.104055, "lon": 12.375801, "tm": train, "name": "Perugia Stazione"},
            {"point": 1, "city": "IT-PEG", "iata_code": None, "icao_code": None, "lat": 43.105311, "lon": 12.374766, "tm": bus, "name": "Perugia Stazione"},
            {"point": 2, "city": "IT-PEG", "iata_code": None, "icao_code": None, "lat": 43.109491, "lon": 12.361496, "tm": bus, "name": "Perugia Piazzale Umbria Jazz"},
            {"point": 3, "city": "IT-PEG", "iata_code": None, "icao_code": None, "lat": 43.105854, "lon": 12.387780, "tm": bus, "name": "Perugia Partigiani"},

            {"point": 0, "city": "IT-PSR", "iata_code": "PSR", "icao_code": "LIBP", "lat": 42.437222, "lon": 14.187222, "tm": flight, "name": "Pescara-Abruzzo Airport"},
            {"point": 1, "city": "IT-PSR", "iata_code": None, "icao_code": None, "lat": 42.468666, "lon": 14.204014, "tm": train, "name": "Pescara Train Station"},
            {"point": 2, "city": "IT-PSR", "iata_code": None, "icao_code": None, "lat": 42.470004, "lon": 14.204534, "tm": bus, "name": "Pescara Bus Station"},
            {"point": 3, "city": "IT-PSR", "iata_code": None, "icao_code": None, "lat": 42.459722, "lon": 14.210303, "tm": bus, "name": "Pescara Via Lago di Compotosto"},

            {"point": 1, "city": "IT-PCZ", "iata_code": None, "icao_code":   None, "lat": 45.051949, "lon": 9.706079, "tm": train, "name": "Piacenza Train Station"},
            {"point": 1, "city": "IT-PCZ", "iata_code": None, "icao_code":   None, "lat": 45.051626, "lon": 9.705240, "tm": bus, "name": "Piacenza Bus Station"},

            {"point": 0, "city": "IT-PSA", "iata_code": "PSA", "icao_code": "LIRP", "lat": 43.683889, "lon": 10.392500, "tm": flight, "name": "Pisa Airport"},
            {"point": 1, "city": "IT-PSA", "iata_code": None, "icao_code": None, "lat": 43.708428, "lon": 10.398463, "tm": train, "name": "Pisa Central Station"},
            {"point": 1, "city": "IT-PSA", "iata_code": None, "icao_code": None, "lat": 43.705600, "lon": 10.391400, "tm": bus, "name": "Pisa Central Station"},
            {"point": 2, "city": "IT-PSA", "iata_code": None, "icao_code": None, "lat": 43.729560, "lon": 10.389982, "tm": bus, "name": "Pisa Pietrasantina Park"},
            {"point": 3, "city": "IT-PSA", "iata_code": None, "icao_code": None, "lat": 43.724291, "lon": 10.387629, "tm": train, "name": "Pisa S. Rossore"},

           # {"point": 0, "city": "IT-RAN", "iata_code": "RAN", "icao_code": "LIDR", "lat": 44.364444, "lon": 12.225556, "tm": flight, "name": "Ravenna Airport"}, #no commercial flights
           {"point": 1, "city": "IT-RAN", "iata_code": None, "icao_code": None, "lat": 44.419085, "lon": 12.208075, "tm": train, "name": "Ravenna Train Station"},
           {"point": 2, "city": "IT-RAN", "iata_code": None, "icao_code": None, "lat": 44.421939, "lon": 12.225667, "tm": bus, "name": "Ravenna Bus Station"},

            {"point": 0, "city": "IT-REG", "iata_code": "REG", "icao_code": "LICR", "lat": 38.071944, "lon": 15.653611, "tm": flight, "name": "Reggio Calabria-Dello Streto Airport"},
            # {"point": 0, "city": "IT-REG", "iata_code": None, "icao_code": None, "lat": 38.067527, "lon": 15.651776, "tm": train, "name": "Reggio Calabria Train Station Airport"}, # Posa que és a s’aeroport, pero no estic segura
            {"point": 1, "city": "IT-REG", "iata_code": None, "icao_code": None, "lat": 38.103588, "lon": 15.636229, "tm": train, "name": "Reggio Calabria Train Station"},
            {"point": 1, "city": "IT-REG", "iata_code": None, "icao_code": None, "lat": 38.103375, "lon": 15.636089, "tm": bus, "name": "Reggio Calabria Bus Station"},

            {"point": 1, "city": "IT-RNE", "iata_code": None, "icao_code": None, "lat": 44.697537, "lon": 10.643207, "tm": train, "name": "Reggio Emilia Main Station"},
            {"point": 1, "city": "IT-RNE", "iata_code": None, "icao_code": None, "lat": 44.697537, "lon": 10.643207, "tm": bus, "name": "Reggio Emilia Main Station"},
            {"point": 2, "city": "IT-RNE", "iata_code": None, "icao_code": None, "lat": 44.724367, "lon": 10.655010, "tm": train, "name": "Reggio Emilia-AV Mediopadana Train Station"},
            {"point": 2, "city": "IT-RNE", "iata_code": None, "icao_code": None, "lat": 44.724349, "lon": 10.654839, "tm": bus, "name": "Reggio Emilia-AV Mediopadana Bus Station"},

            {"point": 0, "city": "IT-RMI", "iata_code": "RMI", "icao_code": "LIPR", "lat": 44.019444, "lon": 12.609444, "tm": flight, "name": "Rimini Federico Fellini Airport"},
            {"point": 1, "city": "IT-RMI", "iata_code": None, "icao_code": None, "lat": 44.063983, "lon": 12.573743, "tm": train, "name": "Rimini Train Station"},
            {"point": 2, "city": "IT-RMI", "iata_code": None, "icao_code": None, "lat": 44.048053, "lon": 12.602223, "tm": bus, "name": "Rimini Bus Station"},
            {"point": 3, "city": "IT-RMI", "iata_code": None, "icao_code": None, "lat": 44.049762, "lon": 12.582464, "tm": bus, "name": "Rimini Centro Studi"},
            {"point": 4, "city": "IT-RMI", "iata_code": None, "icao_code": None, "lat": 43.989822, "lon": 12.643558, "tm": bus, "name": "Rimini Berlinguer Empoli"},
            {"point": 5, "city": "IT-RMI", "iata_code": None, "icao_code": None, "lat":   44.0317, "lon":   12.6212, "tm": bus, "name": "Rimini Miramare"},
            {"point": 6, "city": "IT-RMI", "iata_code": None, "icao_code": None, "lat":   44.0383, "lon":   12.6132, "tm": bus, "name": "Rimini Rivazzurra"},

            {"point": 0, "city": "IT-ROM", "iata_code": "FCO", "icao_code": "LIRF", "lat": 41.800278, "lon": 12.238889, "tm": flight, "name": "Rome Fiumicino Airport"},
            {"point": 0, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.793687, "lon": 12.251667, "tm": train, "name": "Rome Fiumicino Airport"},
            {"point": 0, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.794330, "lon": 12.250398, "tm": bus, "name": "Rome Fiumicino"}, #FlixBus
            {"point": 1, "city": "IT-ROM", "iata_code": "CIA", "icao_code": "LIRA", "lat": 41.799444, "lon": 12.597222, "tm": flight, "name": "Rome Ciampino Airport"},
            {"point": 1, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.798735, "lon": 12.591253, "tm": bus, "name": "Rome Ciampino Bus Station Airport"},
            {"point": 2, "city": "IT-ROM", "iata_code": 'XRJ', "icao_code": None, "lat": 41.901004, "lon": 12.501904, "tm": train, "name": "Rome Termini"},
            {"point": 3, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.911003, "lon": 12.531014, "tm": train, "name": "Rome Tiburtina"},
            {"point": 3, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.909453, "lon": 12.528290, "tm": bus, "name": "Rome Tiburtina"}, #FlixBus
            {"point": 4, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.872719, "lon": 12.484232, "tm": train, "name": "Rome Ostiense"},
            {"point": 4, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.872908, "lon": 12.484328, "tm": bus, "name": "Rome Ostiense"},
            {"point": 5, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.879422, "lon": 12.523391, "tm": train, "name": "Rome Tuscolana"},
            {"point": 5, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.879515, "lon": 12.523313, "tm": bus, "name": "Rome Tuscolana"},
            {"point": 6, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.894828, "lon": 12.484137, "tm": bus, "name": "Rome Fori Imperiali"},
            {"point": 7, "city": "IT-ROM", "iata_code": None, "icao_code": None, "lat": 41.842362, "lon": 12.587141, "tm": bus, "name": "Rome Anagnina"},

            {"point": 0, "city": "IT-RDL", "iata_code": "TRS", "icao_code":"LIPQ", "lat": 45.827500, "lon": 13.472222, "tm": flight, "name": "Trieste Airport"}, #He afegit es nom des poble
            {"point": 0, "city": "IT-RDL", "iata_code":  None, "icao_code":  None, "lat": 45.820726, "lon": 13.483896, "tm": bus, "name": "Trieste Airport"},
            {"point": 0, "city": "IT-RDL", "iata_code":  None, "icao_code":  None, "lat": 45.817429, "lon": 13.486144, "tm": train, "name": "Trieste Airport"},
            {"point": 1, "city": "IT-RDL", "iata_code":  None, "icao_code":  None, "lat": 45.830613, "lon": 13.505912, "tm": train, "name": "Ronchi dei Legionari Train Station"},
            {"point": 2, "city": "IT-RDL", "iata_code":  None, "icao_code":  None, "lat": 45.829998, "lon": 13.500707, "tm": bus, "name": "Ronchi dei Legionari Bus Station"},

            # {"point": 0, "city": "IT-SAL", "iata_code":  "QSR", "icao_code":  "LIRI", "lat": 40.620399, "lon": 14.911299, "tm": flight, "name": "Salerno Costa d'Amalfi Airport"}, #no commercial flights
            {"point": 1, "city": "IT-SAL", "iata_code": 'ISR', "icao_code":  None, "lat": 40.674117, "lon": 14.772815, "tm": train, "name": "Salerno Stazione"},
            {"point": 1, "city": "IT-SAL", "iata_code":  None, "icao_code":  None, "lat": 40.674219, "lon": 14.772444, "tm": bus, "name": "Salerno Stazione"},
            {"point": 2, "city": "IT-SAL", "iata_code":  None, "icao_code":  None, "lat": 40.673842, "lon": 14.770180, "tm": bus, "name": "Salerno Piazza Concordia"}, #duplicated?
            {"point": 3, "city": "IT-SAL", "iata_code":  None, "icao_code":  None, "lat":   40.6842, "lon":   14.7748, "tm": bus, "name": "Salerno Piazza Montpellier"},
            # {"point": 3, "city": "IT-SAL", "iata_code":  None, "icao_code":  None, "lat": 40.676350, "lon": 14.746034, "tm": ferry, "name": "Salerno Ferry Terminal"},
            # {"point": 4, "city": "IT-SAL", "iata_code":  None, "icao_code":  None, "lat": 40.671787, "lon": 14.766630, "tm": ferry, "name": "Salerno Amalfi Ferry Terminal"},

            # {"point": 1, "city": "IT-QSS", "iata_code": None, "icao_code": None, "lat": 40.729447, "lon": 8.554436, "tm": train, "name": "Sassari Train Station"},
            {"point": 2, "city": "IT-QSS", "iata_code": None, "icao_code": None, "lat": 40.725594, "lon": 8.552640, "tm": bus, "name": "Sassari Bus Station"},

            # {"point": 0, "city": "IT-SNA", "iata_code": "SAY", "icao_code": "LIQS", "lat": 43.256389, "lon": 11.255000, "tm": flight, "name": "Siena-Ampugnano Airport"}, #Airport militar,
            {"point": 1, "city": "IT-SNA", "iata_code": None, "icao_code": None, "lat": 43.331803, "lon": 11.322641, "tm": train, "name": "Siena Train Station"},
            {"point": 1, "city": "IT-SNA", "iata_code": None, "icao_code": None, "lat": 43.331419, "lon": 11.323093, "tm": bus, "name": "Siena Bus Station"}, #FlixBus
            {"point": 2, "city": "IT-SNA", "iata_code": None, "icao_code": None, "lat": 43.322021, "lon": 11.327820, "tm": bus, "name": "Siena Via Tozzi"},

            {"point": 1, "city": "IT-SIR", "iata_code": None, "icao_code": None, "lat": 37.068864, "lon": 15.280693, "tm": train, "name": "Syracuse Train Station"},
            {"point": 2, "city": "IT-SIR", "iata_code": None, "icao_code": None, "lat": 37.067737, "lon": 15.281609, "tm": bus, "name": "Syracuse Bus Station"},

            {"point": 1, "city": "IT-TER", "iata_code": None, "icao_code": None, "lat": 42.570496, "lon": 12.651228, "tm": train, "name": "Terni Train Station"},
            {"point": 1, "city": "IT-TER", "iata_code": None, "icao_code": None, "lat": 42.570341, "lon": 12.651321, "tm": bus, "name": "Terni Bus Station"},

            {"point": 0, "city": "IT-TRN", "iata_code": "TRN", "icao_code": "LIMF", "lat": 45.202485, "lon": 7.649444, "tm": flight, "name": "Turin Airport"}, #Turin amb anglès?
            {"point": 1, "city": "IT-TRN", "iata_code": None, "icao_code": None, "lat": 45.061954, "lon": 7.678265, "tm": train, "name": "Turin Porta Nuova Train Station"},
            {"point": 2, "city": "IT-TRN", "iata_code": None, "icao_code": None, "lat": 45.071700, "lon": 7.665849, "tm": train, "name": "Turin Porta Susa Train Station"},
            {"point": 3, "city": "IT-TRN", "iata_code": None, "icao_code": None, "lat": 45.026402, "lon": 7.656900, "tm": train, "name": "Turin Lingotto Train Station"},
            {"point": 3, "city": "IT-TRN", "iata_code": None, "icao_code": None, "lat": 45.025261, "lon": 7.656467, "tm": bus, "name": "Turin Lingotto Bus Station"}, #FlixBus
            {"point": 4, "city": "IT-TRN", "iata_code": None, "icao_code": None, "lat": 45.069691, "lon": 7.658901, "tm": bus, "name": "Turin Vittorio Emanuele Bus Station"}, #FlixBus
            {"point": 5, "city": "IT-TRN", "iata_code": None, "icao_code": None, "lat": 45.120161, "lon": 7.710951, "tm": bus, "name": "Turin Stura"},

            {"point": 0, "city": "IT-TPS", "iata_code": "TPS", "icao_code": "LICT", "lat": 37.911944, "lon": 12.493333, "tm": flight, "name": "Trapani-Birgi Airport"},
            {"point": 1, "city": "IT-TPS", "iata_code": None, "icao_code": None, "lat": 38.017033, "lon": 12.518471, "tm": train, "name": "Trapani Train Station"},
            {"point": 2, "city": "IT-TPS", "iata_code": None, "icao_code": None, "lat": 38.013800, "lon": 12.510775, "tm": bus, "name": "Trapani Porto"},
            # {"point": 2, "city": "IT-TPS", "iata_code": None, "icao_code": None, "lat": 38.014046, "lon": 12.507260, "tm": ferry, "name": "Trapani Ferry Terminal"},

            {"point": 1, "city": "IT-TRT", "iata_code": None, "icao_code": None, "lat": 46.072168, "lon": 11.119403, "tm": train, "name": "Trento Train Station"},
            {"point": 1, "city": "IT-TRT", "iata_code": None, "icao_code": None, "lat": 46.072588, "lon": 11.119942, "tm": bus, "name": "Trento Piaza Dante"},
            {"point": 2, "city": "IT-TRT", "iata_code": None, "icao_code": None, "lat": 46.069127, "lon": 11.115632, "tm": bus, "name": "Trento Lungadige Monte Grappa"}, #FlixBus

            {"point": 0, "city": "IT-TRV", "iata_code": "TSF", "icao_code": "LIPH", "lat": 45.650833, "lon": 12.197778, "tm": flight, "name": "Treviso Airport"},
            {"point": 0, "city": "IT-TRV", "iata_code": None, "icao_code": None, "lat": 45.655396, "lon": 12.204570, "tm": bus, "name": "Treviso Airport"},
            {"point": 1, "city": "IT-TRV", "iata_code": None, "icao_code": None, "lat": 45.660226, "lon": 12.246320, "tm": train, "name": "Stazione Treviso"},
            {"point": 1, "city": "IT-TRV", "iata_code": None, "icao_code": None, "lat": 45.660226, "lon": 12.246320, "tm": bus, "name": "Stazione Treviso"},
            {"point": 2, "city": "IT-TRV", "iata_code": None, "icao_code": None, "lat": 45.669280, "lon": 12.235484, "tm": bus, "name": "Treviso Viale Fratelli Cairoli"},

           # {"point": 0, "city": "IT-TRS", "iata_code": "TRS", "icao_code": "LIPQ", "lat": 45.827485, "lon": 13.472211, "tm": flight, "name": "Trieste–Friuli Venezia Giulia Airport"}, #too far away, included in Ronchi dei Legionari
           {"point": 1, "city": "IT-TRS", "iata_code": 'TXB', "icao_code": None, "lat": 45.658054, "lon": 13.771550, "tm": train, "name": "Trieste Centrale"},
           {"point": 1, "city": "IT-TRS", "iata_code":  None, "icao_code": None, "lat": 45.657204, "lon": 13.770787, "tm": bus, "name": "Trieste Centrale"}, #FlixBus
           {"point": 2, "city": "IT-TRS", "iata_code":  None, "icao_code": None, "lat": 45.6402, "lon": 13.7894, "tm": bus, "name": "Fermata dell'autobus Trieste"},
           # {"point": 2, "city": "IT-TRS", "iata_code": None, "icao_code": None, "lat": 45.646045, "lon": 13.761084, "tm": ferry, "name": "Trieste Ferry Terminal"},

            {"point": 1, "city": "IT-UDN", "iata_code": None, "icao_code": None, "lat": 46.056032, "lon": 13.242340, "tm": train, "name": "Udine Train Station"},
            # {"point": 1, "city": "IT-UDN", "iata_code": None, "icao_code": None, "lat": 46.056066, "lon": 13.241729, "tm": bus, "name": "Udine Bus Station"},
            {"point": 2, "city": "IT-UDN", "iata_code": None, "icao_code": None, "lat": 46.057219, "lon": 13.242772, "tm": bus, "name": "Udine Bus Station"}, #FlixBus

            {"point": 0, "city": "IT-VCE", "iata_code": "VCE", "icao_code": "LIPZ", "lat": 45.505278, "lon": 12.351944, "tm": flight, "name": "Venice Marco Polo Airport"},
            {"point": 0, "city": "IT-VCE", "iata_code": None, "icao_code": None, "lat": 45.507597, "lon": 12.337886, "tm": bus, "name": "Venice Bus Station Airport"},
            {"point": 1, "city": "IT-VCE", "iata_code": "XVQ", "icao_code": None, "lat": 45.441062, "lon": 12.321022, "tm": train, "name": "Venice Santa Lucia"},
            {"point": 2, "city": "IT-VCE", "iata_code": "XVY", "icao_code": None, "lat": 45.482518, "lon": 12.232824, "tm": train, "name": "Venice Mestre"},
            {"point": 2, "city": "IT-VCE", "iata_code": None, "icao_code": None, "lat": 45.481865, "lon": 12.234744, "tm": bus, "name": "Venice Mestre"},
            {"point": 3, "city": "IT-VCE", "iata_code": None, "icao_code": None, "lat": 45.441977, "lon": 12.307979, "tm": bus, "name": "Venice Tronchetto Bus Station"},
            {"point": 4, "city": "IT-VCE", "iata_code": None, "icao_code": None, "lat": 45.506639, "lon": 12.247750, "tm": train, "name": "Venezia Carpenedo"},
            # {"point": 5, "city": "IT-VCE", "iata_code": None, "icao_code": None, "lat": 45.434990, "lon": 12.304989, "tm": ferry, "name": "Venice Ferry Terminal"},

            {"point": 0, "city": "IT-VRN", "iata_code": "VRN", "icao_code": "LIPX", "lat": 45.396389, "lon": 10.888056, "tm": flight, "name": "Verona Airport"},
            {"point": 1, "city": "IT-VRN", "iata_code": 'XIX', "icao_code": None, "lat": 45.429056, "lon": 10.982551, "tm": train, "name": "Verona Porta Nuova"},
            {"point": 1, "city": "IT-VRN", "iata_code": None, "icao_code": None, "lat": 45.428999, "lon": 10.981553, "tm": bus, "name": "Verona Porta Nuova"},
            {"point": 2, "city": "IT-VRN", "iata_code": None, "icao_code": None, "lat": 45.435704, "lon": 11.018705, "tm": train, "name": "Verona Porta Vescovo"},
            {"point": 3, "city": "IT-VRN", "iata_code": None, "icao_code": None, "lat": 45.431463, "lon": 10.981023, "tm": bus, "name": "Verona Viale Girolamo Cardinale"}, #FlixBus
            {"point": 4, "city": "IT-VRN", "iata_code": None, "icao_code": None, "lat": 45.4342, "lon": 10.9978, "tm": bus, "name": "Verona Staziazone"},

            # {"point": 0, "city": "IT-VIC", "iata_code": "VIC", "icao_code": "LIPT", "lat": 45.573333, "lon": 11.529722, "tm": flight, "name": "Vicenza Airport"}, #no flights
            {"point": 1, "city": "IT-VIC", "iata_code": None, "icao_code": None, "lat": 45.541278, "lon": 11.540758, "tm": train, "name": "Vicenza Train Station"},
            {"point": 1, "city": "IT-VIC", "iata_code": None, "icao_code": None, "lat": 45.541658, "lon": 11.540999, "tm": bus, "name": "Vicenza Bus Station"},
            # {"point": 2, "city": "IT-VIC", "iata_code": None, "icao_code": None, "lat": 45.543124, "lon": 11.537695, "tm": bus, "name": "Vicenza Bus Station"}, #No puc confirmar que sa turada sigui de FlixBus
        ]

        hubs_DK = [
            {"point": 0, "city": "DK-AAL", "iata_code": "AAL", "icao_code": "EKYT", "lat": 57.092778, "lon": 9.849167, "tm": flight, "name": "Aalborg Airport"},
            {"point": 1, "city": "DK-AAL", "iata_code": None, "icao_code": None, "lat": 57.043193, "lon": 9.917161, "tm": train, "name": "Aalborg Train Station"},
            {"point": 1, "city": "DK-AAL", "iata_code": None, "icao_code": None, "lat": 57.041377, "lon": 9.918602, "tm": bus, "name": "Aalborg Bus Station"},
            # {"point": 2, "city": "DK-AAL", "iata_code": None, "icao_code": None, "lat": 57.058663, "lon": 9.881663, "tm": ferry, "name": "Aalborg Ferry Terminal"},

            {"point": 0, "city": "DK-AAR", "iata_code": "AAR", "icao_code": "EKAH", "lat": 56.304167, "lon": 10.619167, "tm": flight, "name": "Aarhus Airport"},
            {"point": 1, "city": "DK-AAR", "iata_code": None, "icao_code": None, "lat": 56.150322, "lon": 10.204706, "tm": train, "name": "Aarhus Central Train Station"},
            {"point": 2, "city": "DK-AAR", "iata_code": None, "icao_code": None, "lat": 56.151673, "lon": 10.209178, "tm": bus, "name": "Aarhus Bus Station"},
            # {"point": 3, "city": "DK-AAR", "iata_code": None, "icao_code": None, "lat": 56.161488, "lon": 10.219872, "tm": ferry, "name": "Aarhus Ferry Terminal"},

            # {"point": 1, "city": "DK-ANH", "iata_code": None, "icao_code": None, "lat": 56.716450, "lon": 11.511196, "tm": ferry, "name": "Anholt Ferry Terminal"},

            {"point": 0, "city": "DK-BLL", "iata_code": "BLL", "icao_code": "EKBI", "lat": 55.740278, "lon": 9.151944, "tm": flight, "name": "Billund Airport"},
            {"point": 0, "city": "DK-BLL", "iata_code": None, "icao_code": None, "lat": 55.746355, "lon": 9.147043, "tm": bus, "name": "Billund Airport Bus Station"},
            {"point": 1, "city": "DK-BLL", "iata_code": None, "icao_code": None, "lat": 55.731440, "lon": 9.118641, "tm": bus, "name": "Billund Bus Station"},

            # {"point": 1, "city": "DK-BOS", "iata_code": None, "icao_code": None, "lat": 55.104680, "lon": 10.082113, "tm": ferry, "name": "Bojden Ferry Terminal"},

            {"point": 0, "city": "DK-BHL", "iata_code": "RNN", "icao_code": "EKRN", "lat": 55.063333, "lon": 14.759444, "tm": flight, "name": "Bornholm Airport"},
            {"point": 1, "city": "DK-BHL", "iata_code": None, "icao_code": None, "lat": 55.074610, "lon": 14.910240, "tm": bus, "name": " Bornholm Aakirkeby Bus Terminalen"},
            # {"point": 2, "city": "DK-BHL", "iata_code": None, "icao_code": None, "lat": 42.701408, "lon": 09.453306, "tm":ferry, "name": "Bornholm Ferry Terminal"},

            {"point": 0, "city": "DK-CPH", "iata_code":"CPH", "icao_code":"EKCH", "lat": 55.618056, "lon": 12.656110, "tm": flight, "name": "Copenhagen Airport"},
            {"point": 0, "city": "DK-CPH", "iata_code": None, "icao_code":  None, "lat": 55.618056, "lon": 12.656110, "tm": train, "name": "Copenhagen Airports Train Station"},
            {"point": 0, "city": "DK-CPH", "iata_code": None, "icao_code":  None, "lat": 55.629891, "lon": 12.652710, "tm": bus, "name": "Copenhagen Airports Bus Station"},
            {"point": 1, "city": "DK-CPH", "iata_code":"ZGH", "icao_code":  None, "lat": 55.672778, "lon": 12.564444, "tm": train, "name": "Copenhagen Central Station"},
            {"point": 1, "city": "DK-CPH", "iata_code": None, "icao_code":  None, "lat": 55.670153, "lon": 12.565466, "tm": bus, "name": "Copenhagen Central Station"},
            {"point": 2, "city": "DK-CPH", "iata_code": None, "icao_code":  None, "lat": 55.663474, "lon": 12.516132, "tm": bus, "name": "Copenhagen Valby"},
            {"point": 3, "city": "DK-CPH", "iata_code": None, "icao_code":  None, "lat":   55.6699, "lon":   12.5654, "tm": train, "name": "Copenhagen Ingerslevsgade"},
            # {"point": 3, "city": "DK-CPH", "iata_code": None, "icao_code": None, "lat": 55.701564, "lon": 12.595855, "tm": ferry, "name": "Copenhagen Ferry Terminal"},

            {"point": 0, "city": "DK-EBJ", "iata_code": "EBJ", "icao_code": "EKEB", "lat": 55.525833, "lon": 8.553333, "tm": flight, "name": "Esbjerg Airport"},
            {"point": 1, "city": "DK-EBJ", "iata_code": None, "icao_code": None, "lat": 55.468099, "lon": 8.457821, "tm": train, "name": "Esbjerg Train Station"},
            {"point": 2, "city": "DK-EBJ", "iata_code": None, "icao_code": None, "lat": 55.469452, "lon": 8.458712, "tm": bus, "name": "Esbjerg Bus Station"},
            # {"point": 3, "city": "DK-EBJ", "iata_code": None, "icao_code": None, "lat": 55.461007, "lon": 8.440325, "tm": ferry, "name": "Esbjerg Ferry Terminal"},

            # {"point": 1, "city": "DK-FYH", "iata_code": None, "icao_code": None, "lat": 54.994149, "lon": 9.984931, "tm": ferry, "name": "Fynshav Ferry Terminal"},

            # {"point": 1, "city": "DK-GRE", "iata_code": None, "icao_code": None, "lat": 56.412760, "lon": 10.880013, "tm": train, "name": "Grenaa Train Station"}, #too small
            # {"point": 1, "city": "DK-GRE", "iata_code": None, "icao_code": None, "lat": 56.413056, "lon": 10.880839, "tm": bus, "name": "Grenaa Bus Station"},
            # {"point": 2, "city": "DK-GRE", "iata_code": None, "icao_code": None, "lat": 56.407584, "lon": 10.923547, "tm": bus, "name": "Grenaa Hav Bus Station"},
            # {"point": 3, "city": "DK-GRE", "iata_code": None, "icao_code": None, "lat": 56.408559, "lon": 10.925592, "tm": ferry, "name": "Grenaa Ferry Terminal"},

            # {"point": 1, "city": "DK-HLS", "iata_code": None, "icao_code": None, "lat": 56.033514, "lon": 12.614440, "tm": train, "name": "Helsingør Train Station"}, #population of 61.000 only
            # {"point": 2, "city": "DK-HLS", "iata_code": None, "icao_code": None, "lat": 56.033285, "lon": 12.615828, "tm": ferry, "name": "Helsingør Ferry Terminal"},

            # {"point": 1, "city": "DK-HIR", "iata_code": None, "icao_code": None, "lat": 57.591781, "lon": 9.962223, "tm": train, "name": "Hirtshals Train Station"},
            # {"point": 2, "city": "DK-HIR", "iata_code": None, "icao_code": None, "lat": 57.588066, "lon": 9.961197, "tm": bus, "name": "Hirtshals Skole Bus Station"},
            # {"point": 2, "city": "DK-HIR", "iata_code": None, "icao_code": None, "lat": 57.595816, "lon": 9.977848, "tm": ferry, "name": "Hirtshals Ferry Terminal"},

            # {"point": 1, "city": "DK-KAL", "iata_code": None, "icao_code": None, "lat": 55.677101, "lon": 11.090459, "tm": ferry, "name": "Kalundborg Ferry Terminal"},

            {"point": 0, "city": "DK-KRP", "iata_code": "KRP", "icao_code": "EKKA", "lat": 56.297500, "lon": 9.124722, "tm": flight, "name": "Karup Airport"},
            {"point": 1, "city": "DK-KRP", "iata_code": None, "icao_code": None, "lat": 56.307999, "lon": 9.165609, "tm": bus, "name": "Karup Bus Station"},

            {"point": 0, "city": "DK-LES", "iata_code": "BYR", "icao_code": "EKLS", "lat": 57.276944, "lon": 10.999722, "tm": flight, "name": "Læsø Airport"},
            {"point": 1, "city": "DK-LES", "iata_code": None, "icao_code": None, "lat": 57.253586, "lon": 11.004955, "tm": bus, "name": "Læsø Bus Station"},
            # {"point": 2, "city": "DK-LES", "iata_code": None, "icao_code": None, "lat": 57.295435, "lon": 10.917274, "tm": ferry, "name": "Læsø Ferry Terminal"},

            # {"point": 1, "city": "DK-MRS", "iata_code": None, "icao_code": None, "lat": 54.856388, "lon": 10.521465, "tm": ferry, "name": "Marstal Ferry Terminal"},

            {"point": 0, "city": "DK-ODE", "iata_code": "ODE", "icao_code":"EKOD", "lat": 55.476667, "lon": 10.330833, "tm": flight, "name": "Odense Airport"},
            {"point": 1, "city": "DK-ODE", "iata_code":  None, "icao_code":  None, "lat": 55.401276, "lon": 10.387149, "tm": train, "name": "Odense City"},
            {"point": 1, "city": "DK-ODE", "iata_code":  None, "icao_code":  None, "lat": 55.403362, "lon": 10.387037, "tm": bus, "name": "Odense City"},
            {"point": 2, "city": "DK-ODE", "iata_code":  None, "icao_code":  None, "lat": 55.372439, "lon": 10.370478, "tm": bus, "name": "Odense Dalum"},

            # {"point": 1, "city": "DK-ROD", "iata_code": None, "icao_code": None, "lat": 54.655737, "lon": 11.355706, "tm": train, "name": "Rodbyhavn Train Station"},
            # {"point": 2, "city": "DK-ROD", "iata_code": None, "icao_code": None, "lat": 54.654738, "lon": 11.351478, "tm": ferry, "name": "Rodbyhavn Ferry Terminal"},

            # {"point": 1, "city": "DK-RNN", "iata_code": None, "icao_code": None, "lat": 55.099302, "lon": 14.690625, "tm": ferry, "name": "Rønne Ferry Terminal"},

            {"point": 0, "city": "DK-RKE", "iata_code": "RKE", "icao_code": "EKRK", "lat": 55.585556, "lon": 12.131389, "tm": flight, "name": "Roskilde Airport"},
            {"point": 1, "city": "DK-RKE", "iata_code": None, "icao_code": None, "lat": 55.639156, "lon": 12.088778, "tm": train, "name": "Roskilde Train Station"},
            {"point": 2, "city": "DK-RKE", "iata_code": None, "icao_code": None, "lat": 55.648358, "lon": 12.131841, "tm": bus, "name": "Roskilde Bus Station"},

            {"point": 0, "city": "DK-SGD", "iata_code": "SGD", "icao_code": "EKSB", "lat": 54.964444, "lon": 9.791731, "tm": flight, "name": "Sønderborg Airport"},
            {"point": 1, "city": "DK-SGD", "iata_code": None, "icao_code": None, "lat": 54.912021, "lon": 9.779158, "tm": train, "name": "Sønderborg Train Station"},
            {"point": 2, "city": "DK-SGD", "iata_code": None, "icao_code": None, "lat": 54.9104, "lon": 9.79398, "tm": bus, "name": "Sønderborg Bus Station"},
        ]

        hubs_FO = [
            # {"point": 1, "city": "FO-TOR", "iata_code": None, "icao_code": None, "lat": 62.007748, "lon": -6765320, "tm": flight, "name": "Tórshavn Ferry Terminal"},

            {"point": 0, "city": "FO-FAE", "iata_code": "FAE", "icao_code": "EKVG", "lat": 62.063611, "lon": -7.277222, "tm": flight, "name": "Vágar Airport"},
        ]

        hubs_SE = [
            {"point": 0, "city": "SE-ANG", "iata_code": "AGH", "icao_code": "ESTA", "lat": 56.296111, "lon": 12.847222, "tm": flight, "name": "Ängelholm–Helsingborg Airport"},
            {"point": 1, "city": "SE-ANG", "iata_code": None, "icao_code": None, "lat": 56.245239, "lon": 12.854188, "tm": train, "name": "Ängelholm Station"},
            {"point": 2, "city": "SE-ANG", "iata_code": None, "icao_code": None, "lat": 56.242987, "lon": 12.861161, "tm": bus, "name": "Ängelholm Station"},

            {"point": 0, "city": "SE-AJR", "iata_code": "AJR", "icao_code": "ESNX", "lat": 65.590278, "lon": 19.281944, "tm": flight, "name": "Arvidsjaur Airport"},
            {"point": 1, "city": "SE-AJR", "iata_code": None, "icao_code": None, "lat": 65.588874, "lon": 19.169274, "tm": train, "name": "Arvidsjaur Station"},
            {"point": 2, "city": "SE-AJR", "iata_code": None, "icao_code": None, "lat": 65.592333, "lon": 19.182415, "tm": bus, "name": "Arvidsjaur Station"},

            {"point": 0, "city": "SE-BLE", "iata_code": "BLE", "icao_code": "ESSD", "lat": 60.421944, "lon": 15.515000, "tm": flight, "name": "Borlänge Dala Airport"}, # També es diu Dala Airport
            {"point": 1, "city": "SE-BLE", "iata_code": None, "icao_code": None, "lat": 60.483536, "lon": 15.425841, "tm": train, "name": "Borlänge Central Station"},
            {"point": 1, "city": "SE-BLE", "iata_code": None, "icao_code": None, "lat": 60.483688, "lon": 15.425460, "tm": bus, "name": "Borlänge Central Station"},

            {"point": 0, "city": "SE-GEV", "iata_code": "GEV", "icao_code": "ESNG", "lat": 67.133056, "lon": 20.812222, "tm": flight, "name": "Gällivare Lapland Airport"},
            {"point": 1, "city": "SE-GEV", "iata_code": None, "icao_code": None, "lat": 67.133620, "lon": 20.651183, "tm": train, "name": "Gällivare Resecentrum"},
            {"point": 1, "city": "SE-GEV", "iata_code": None, "icao_code": None, "lat": 67.133373, "lon": 20.651550, "tm": bus, "name": "Gällivare Resecentrum"},

            {"point": 0, "city": "SE-GOT", "iata_code": "GOT", "icao_code": "ESGG", "lat": 57.660000, "lon": 12.291111, "tm": flight, "name": "Göteborg Landvetter Airport"},
            {"point": 0, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.667881, "lon": 12.295951, "tm": bus, "name": "Göteborg Landvetter Airport"},
            {"point": 1, "city": "SE-GOT", "iata_code": "XWL", "icao_code":   None, "lat": 57.709006, "lon": 11.972806, "tm": train, "name": "Göteborg Central Station"},
            {"point": 1, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.710421, "lon": 11.971896, "tm": bus, "name": "Göteborg Nils Ericson Terminalen"},
            {"point": 2, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.702570, "lon": 11.975167, "tm": bus, "name": "Göteborg Heden"},
            # {"point": 3, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.706392, "lon": 11.956973, "tm": ferry, "name": "Göteborg Stenpiren"},
            {"point": 3, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.705835, "lon": 11.957394, "tm": bus, "name": "Göteborg Stenpiren"},
            # {"point": 4, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.701374, "lon": 11.943683, "tm": ferry, "name": "Göteborg Masthuggskajen"},
            {"point": 4, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.698297, "lon": 11.995279, "tm": train, "name": "Göteborg Liseberg"},
            {"point": 4, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.697259, "lon": 11.991295, "tm": bus, "name": "Göteborg Liseberg"},
            {"point": 5, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.656003, "lon": 12.018080, "tm": train, "name": "Göteborg Mölndal"},
            {"point": 5, "city": "SE-GOT", "iata_code":  None, "icao_code":   None, "lat": 57.656003, "lon": 12.018080, "tm": bus, "name": "Göteborg Mölndal"},

            {"point": 0, "city": "SE-HFS", "iata_code": "HFS", "icao_code": "ESOH", "lat": 60.025000, "lon": 13.580556, "tm": flight, "name": "Hagfors Airport"},
            {"point": 1, "city": "SE-HFS", "iata_code": None, "icao_code": None, "lat": 60.035490, "lon": 13.693640, "tm": bus, "name": "Hagfors Station"},

            {"point": 0, "city": "SE-HAD", "iata_code": "HAD", "icao_code": "ESMT", "lat": 56.690833, "lon": 12.820000, "tm": flight, "name": "Halmstad Airport"},
            {"point": 1, "city": "SE-HAD", "iata_code": None, "icao_code": None, "lat": 56.669222, "lon": 12.864594, "tm": train, "name": "Halmstad C"},
            {"point": 1, "city": "SE-HAD", "iata_code": None, "icao_code": None, "lat": 56.670023, "lon": 12.865487, "tm": bus, "name": "Halmstad Bolmensgatan"},

            {"point": 0, "city": "SE-HMV", "iata_code": "HMV", "icao_code": "ESUT", "lat": 65.806111, "lon": 15.082778, "tm": flight, "name": "Hemavan Airport"},
            {"point": 1, "city": "SE-HMV", "iata_code": None, "icao_code": None, "lat": 65.819465, "lon": 15.084658, "tm": bus, "name": "Hemavan Station"},

            {"point": 0, "city": "SE-JKG", "iata_code": "JKG", "icao_code": "ESGJ", "lat": 57.758333, "lon": 14.071667, "tm": flight, "name": "Jönköping Airport"},
            {"point": 0, "city": "SE-JKG", "iata_code":  None, "icao_code":   None, "lat": 57.750423, "lon": 14.070270, "tm": bus, "name": "Jönköping Airport"},
            {"point": 1, "city": "SE-JKG", "iata_code":  None, "icao_code":   None, "lat": 57.784419, "lon": 14.162584, "tm": train, "name": "Jönköping Resecentrum"},
            {"point": 1, "city": "SE-JKG", "iata_code":  None, "icao_code":   None, "lat": 57.784189, "lon": 14.164509, "tm": bus, "name": "Jönköping Resecentrum"},

            {"point": 0, "city": "SE-KLR", "iata_code": "KLR", "icao_code": "ESMQ", "lat": 56.685278, "lon": 16.287500, "tm": flight, "name": "Kalmar Airport"},
            {"point": 1, "city": "SE-KLR", "iata_code": None, "icao_code": None, "lat": 56.661494, "lon": 16.360272, "tm": train, "name": "Kalmar C"},
            {"point": 1, "city": "SE-KLR", "iata_code": None, "icao_code": None, "lat": 56.661542, "lon": 16.359853, "tm": bus, "name": "Kalmar C"},
            # {"point": 2, "city": "SE-KLR", "iata_code": None, "icao_code": None, "lat": 56.661284, "lon": 16.367846, "tm": ferry, "name": "Kalmar Ferry Terminal"},

            {"point": 0, "city": "SE-KSD", "iata_code": "KSD", "icao_code": "ESOK", "lat": 59.444722, "lon": 13.337500, "tm": flight, "name": "Karlstad Airport"},
            {"point": 1, "city": "SE-KSD", "iata_code": None, "icao_code": None, "lat": 59.377964, "lon": 13.499448, "tm": train, "name": "Karlstad C"},
            {"point": 1, "city": "SE-KSD", "iata_code": None, "icao_code": None, "lat": 59.377975, "lon": 13.498584, "tm": bus, "name": "Karlstad C"},
            {"point": 2, "city": "SE-KSD", "iata_code": None, "icao_code": None, "lat": 59.379172, "lon": 13.492891, "tm": bus, "name": "Karlstad Drottninggatan"}, #same station?

            {"point": 0, "city": "SE-KRN", "iata_code": "KRN", "icao_code": "ESNQ", "lat": 67.822222, "lon": 20.336667, "tm": flight, "name": "Kiruna Airport"},
            {"point": 0, "city": "SE-KRN", "iata_code": None, "icao_code": None, "lat": 67.825769, "lon": 20.335097, "tm": bus, "name": "Kiruna Airport"},
            {"point": 1, "city": "SE-KRN", "iata_code": None, "icao_code": None, "lat": 67.868432, "lon": 20.199372, "tm": train, "name": "Kiruna C"},
            {"point": 1, "city": "SE-KRN", "iata_code": None, "icao_code": None, "lat": 67.868267, "lon": 20.199573, "tm": bus, "name": "Kiruna C"},

            {"point": 0, "city": "SE-KRF", "iata_code": "KRF", "icao_code": "ESNK", "lat": 63.048611, "lon": 17.768889, "tm": flight, "name": "Höga Kusten Airport"},
            {"point": 1, "city": "SE-KRF", "iata_code": None, "icao_code": None, "lat": 62.929247, "lon": 17.778226, "tm": train, "name": "Kramfors Train Station"},
            {"point": 1, "city": "SE-KRF", "iata_code": None, "icao_code": None, "lat": 62.928676, "lon": 17.778927, "tm": bus, "name": "Kramfors Bus Station"},

            {"point": 0, "city": "SE-KID", "iata_code": "KID", "icao_code": "ESMK", "lat": 55.911944, "lon": 14.083333, "tm": flight, "name": "Kristianstad Airport"},
            {"point": 1, "city": "SE-KID", "iata_code": None, "icao_code": None, "lat": 56.031674, "lon": 14.151259, "tm": train, "name": "Kristianstad C"},
            {"point": 1, "city": "SE-KID", "iata_code": None, "icao_code": None, "lat": 56.031534, "lon": 14.151763, "tm": bus, "name": "Kristianstad C"},

            {"point": 0, "city": "SE-LPI", "iata_code": "LPI", "icao_code": "ESSL", "lat": 58.408333, "lon": 15.672778, "tm": flight, "name": "Linköping City Airport"},
            {"point": 1, "city": "SE-LPI", "iata_code":  None, "icao_code":   None, "lat": 58.416084, "lon": 15.625928, "tm": train, "name": "Linköping C"},
            # {"point": 1, "city": "SE-LPI", "iata_code":  None, "icao_code":   None, "lat": 58.416081, "lon": 15.625883, "tm": bus, "name": "Linköping C"},
            {"point": 1, "city": "SE-LPI", "iata_code":  None, "icao_code":   None, "lat": 58.418186, "lon": 15.621085, "tm": bus, "name": "Linköping Järnvägsgatan"},

            {"point": 0, "city": "SE-LLA", "iata_code": "LLA", "icao_code": "ESPA", "lat": 65.543611, "lon": 22.121944, "tm": flight, "name": "Luleå Airport"},
            {"point": 1, "city": "SE-LLA", "iata_code": None, "icao_code": None, "lat": 65.584093, "lon": 22.164937, "tm": train, "name": "Luleå C"},
            {"point": 2, "city": "SE-LLA", "iata_code": None, "icao_code": None, "lat": 65.585730, "lon": 22.160459, "tm": bus, "name": "Luleå Bus Station"},

            {"point": 0, "city": "SE-LYC", "iata_code": "LYC", "icao_code": "ESNL", "lat": 64.548056, "lon": 18.716111, "tm": flight, "name": "Lycksele Airport"},
            {"point": 1, "city": "SE-LYC", "iata_code": None, "icao_code": None, "lat": 64.595371, "lon": 18.667978, "tm": train, "name": "Lycksele Resecentrum/Station"},
            {"point": 1, "city": "SE-LYC", "iata_code": None, "icao_code": None, "lat": 64.595172, "lon": 18.668071, "tm": bus, "name": "Lycksele Resecentrum/Station"},

            {"point": 0, "city": "SE-MMA", "iata_code": "MMX", "icao_code": "ESMS", "lat": 55.530000, "lon": 13.371389, "tm": flight, "name": "Malmö Airport"},
            {"point": 1, "city": "SE-MMA", "iata_code":  None, "icao_code":   None, "lat": 55.609067, "lon": 12.999923, "tm": train, "name": "Malmö C"},
            {"point": 1, "city": "SE-MMA", "iata_code":  None, "icao_code":   None, "lat": 55.607954, "lon": 13.000315, "tm": bus, "name": "Malmö C"},
            # {"point": 2, "city": "SE-MMA", "iata_code":  None, "icao_code":   None, "lat": 55.627411, "lon": 12.990582, "tm": ferry, "name": "Malmö Ferry Terminal"},

            {"point": 0, "city": "SE-MRA", "iata_code": "MXX", "icao_code": "ESKM", "lat": 60.958611, "lon": 14.511111, "tm": flight, "name": "Mora–Siljan Airport"},
            {"point": 1, "city": "SE-MRA", "iata_code": None, "icao_code": None, "lat": 61.008806, "lon": 14.558743, "tm": train, "name": "Mora Train Station"},
            {"point": 1, "city": "SE-MRA", "iata_code": None, "icao_code": None, "lat": 61.008948, "lon": 14.558322, "tm": bus, "name": "Mora Bus Station"},

            {"point": 0, "city": "SE-NRK", "iata_code": "NRK", "icao_code": "ESSP", "lat": 58.586111, "lon": 16.231667, "tm": flight, "name": "Norrköping Airport"},
            {"point": 1, "city": "SE-NRK", "iata_code": None, "icao_code": None, "lat": 58.596431, "lon": 16.183429, "tm": train, "name": "Norrköping C"},
            {"point": 1, "city": "SE-NRK", "iata_code": None, "icao_code": None, "lat": 58.596814, "lon": 16.187792, "tm": bus, "name": "Norrköping Norra Promenaden"},
            # {"point": 2, "city": "SE-NRK", "iata_code": None, "icao_code": None, "lat": 58.595633, "lon": 16.185846, "tm": bus, "name": "Norrköping Bus Station"}, #Duplicate

            {"point": 0, "city": "SE-NYO", "iata_code": "NYO", "icao_code": "ESKN", "lat": 58.788611, "lon": 16.912222, "tm": flight, "name": "Skavsta Nyköping Airport"},
            {"point": 0, "city": "SE-NYO", "iata_code":  None, "icao_code": None, "lat": 58.784431, "lon": 16.923232, "tm": bus, "name": "Skavsta Nyköping Airport"},
            {"point": 1, "city": "SE-NYO", "iata_code":  None, "icao_code": None, "lat": 58.755699, "lon": 16.994787, "tm": train, "name": "Nyköping C"},
            {"point": 1, "city": "SE-NYO", "iata_code":  None, "icao_code": None, "lat": 58.755567, "lon": 16.994518, "tm": bus, "name": "Nyköping C"},
            # {"point": 2, "city": "SE-NYO", "iata_code":  None, "icao_code": None, "lat": 58.749212, "lon": 16.001664, "tm": bus, "name": "Nyköping Station"}, #in the middle of nowhere

            {"point": 0, "city": "SE-ORB", "iata_code": "ORB", "icao_code": "ESOE", "lat": 59.223611, "lon": 15.038056, "tm": flight, "name": "Örebro Airport"},
            {"point": 1, "city": "SE-ORB", "iata_code": None, "icao_code": None, "lat": 59.278702, "lon": 15.211217, "tm": train, "name": "Örebro Resecentrum"},
            {"point": 1, "city": "SE-ORB", "iata_code": None, "icao_code": None, "lat": 59.277516, "lon": 15.210685, "tm": bus, "name": "Örebro Resecentrum"},

            {"point": 0, "city": "SE-OER", "iata_code": "OER", "icao_code": "ESNO", "lat": 63.408333, "lon": 18.990000, "tm": flight, "name": "Örnsköldsvik Airport"},
            {"point": 1, "city": "SE-OER", "iata_code": None, "icao_code": None, "lat": 63.287932, "lon": 18.705449, "tm": train, "name": "Örnsköldsvik ReseC"},
            {"point": 1, "city": "SE-OER", "iata_code": None, "icao_code": None, "lat": 63.287745, "lon": 18.705576, "tm": bus, "name": "Örnsköldsvik ReseC"},

            {"point": 0, "city": "SE-OSD", "iata_code": "OSD", "icao_code": "ESNZ", "lat": 63.194167, "lon": 14.501944, "tm": flight, "name": "Åre Östersund Airport"},
            {"point": 1, "city": "SE-OSD", "iata_code": None, "icao_code": None, "lat": 63.170699, "lon": 14.637342, "tm": train, "name": "Östersund C"},
            {"point": 1, "city": "SE-OSD", "iata_code": None, "icao_code": None, "lat": 63.170181, "lon": 14.638361, "tm": bus, "name": "Östersund C"},

            {"point": 0, "city": "SE-PJA", "iata_code": "PJA", "icao_code": "ESUP", "lat": 67.245556, "lon": 23.068889, "tm": flight, "name": "Pajala Airport"},
            {"point": 1, "city": "SE-PJA", "iata_code": None, "icao_code": None, "lat": 67.210859, "lon": 23.365722, "tm": bus, "name": "Pajala Station"},

            {"point": 0, "city": "SE-RNB", "iata_code": "RNB", "icao_code": "ESDF", "lat": 56.266667, "lon": 15.265000, "tm": flight, "name": "Ronneby Airport"},
            {"point": 1, "city": "SE-RNB", "iata_code": None, "icao_code": None, "lat": 56.266667, "lon": 15.265000, "tm": train, "name": "Ronneby Train Pressbyran"},
            {"point": 1, "city": "SE-RNB", "iata_code": None, "icao_code": None, "lat": 56.266667, "lon": 15.265000, "tm": bus, "name": "Ronneby Bus Pressbyran"},

            {"point": 0, "city": "SE-SFT", "iata_code": "SFT", "icao_code": "ESNS", "lat": 64.624722, "lon": 21.076944, "tm": flight, "name": "Skellefteå Airport"},
            {"point": 1, "city": "SE-SFT", "iata_code": None, "icao_code": None, "lat": 64.753626, "lon": 20.949211, "tm": bus, "name": "Skellefteå Station"},

            {"point": 0, "city": "SE-STO", "iata_code": "ARN", "icao_code": "ESSA", "lat": 59.651944, "lon": 17.918611, "tm": flight, "name": "Stockholm–Arlanda Airport"},
            {"point": 0, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.651529, "lon": 17.930829, "tm": train, "name": "Stockholm–Arlanda Airport"},
            {"point": 0, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.651019, "lon": 17.930808, "tm": bus, "name": "Stockholm–Arlanda Airport"},
            {"point": 1, "city": "SE-STO", "iata_code": "BMA", "icao_code": "ESSB", "lat": 59.354444, "lon": 17.939722, "tm": flight, "name": "Stockholm–Bromma Airport"},
            {"point": 2, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.330601, "lon": 18.058626, "tm": train, "name": "Stockholm Central Station"},
            {"point": 2, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.331137, "lon": 18.056640, "tm": bus, "name": "Stockholm Cityterminalen"},
            {"point": 3, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.312893, "lon": 18.057994, "tm": train, "name": "Stockholms Södra"},
            {"point": 4, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.217980, "lon": 17.945707, "tm": train, "name": "Stockholm Flemingsberg"},
            {"point": 5, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.328696, "lon": 18.092842, "tm": bus, "name": "Stockholm Junibacken"},
            {"point": 6, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.324187, "lon": 18.101858, "tm": bus, "name": "Stockholm Skansen"},
            {"point": 7, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.299367, "lon": 18.029599, "tm": train, "name": "Stockholm Årstaberg"},
            {"point": 8, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.360995, "lon": 17.971228, "tm": train, "name": "Stockholm Sundbyberg"},
            {"point": 8, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.361033, "lon": 17.969951, "tm": bus, "name": "Stockholm Sundbyberg"},
            # {"point": 3, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.350132, "lon": 18.107312, "tm": ferry, "name": "Stockholm Värtahamnen"},
            # {"point": 4, "city": "SE-STO", "iata_code":  None, "icao_code":   None, "lat": 59.316327, "lon": 18.095750 "tm": ferry, "name": "Stockholm Viking Line Terminal"},

            {"point": 0, "city": "SE-SDL", "iata_code": "SDL", "icao_code": "ESNN", "lat": 62.528056, "lon": 17.443889, "tm": flight, "name": "Sundsvall–Timrå Airport"},
            {"point": 1, "city": "SE-SDL", "iata_code": None, "icao_code": None, "lat": 62.386886, "lon": 17.315627, "tm": train, "name": "Sundsvall C"},
            {"point": 1, "city": "SE-SDL", "iata_code": None, "icao_code": None, "lat": 62.386714, "lon": 17.316041, "tm": bus, "name": "Sundsvall C"},
            {"point": 2, "city": "SE-SDL", "iata_code": None, "icao_code": None, "lat": 62.392419, "lon": 17.309450, "tm": bus, "name": "Sundsvall Navet"},

            {"point": 0, "city": "SE-TYF", "iata_code": "TYF", "icao_code": "ESST", "lat": 60.154722, "lon": 12.994444, "tm": flight, "name": "Torsby Airport"},
            {"point": 1, "city": "SE-TYF", "iata_code": None, "icao_code": None, "lat": 60.136722, "lon": 13.003472, "tm": train, "name": "Torsby Train Station"},
            {"point": 1, "city": "SE-TYF", "iata_code": None, "icao_code": None, "lat": 60.136569, "lon": 13.002497, "tm": bus, "name": "Torsby Bus Station"},

            {"point": 0, "city": "SE-THN", "iata_code": "THN", "icao_code": "ESGT", "lat": 58.324167, "lon": 12.336389, "tm": flight, "name": "Trollhättan–Vänersborg Airport"},
            {"point": 1, "city": "SE-THN", "iata_code": None, "icao_code": None, "lat": 58.287490, "lon": 12.299266, "tm": train, "name": "Trollhättan C"},
            {"point": 1, "city": "SE-THN", "iata_code": None, "icao_code": None, "lat": 58.287563, "lon": 12.299162, "tm": bus, "name": "Trollhättan C"},

            {"point": 0, "city": "SE-UME", "iata_code": "UME", "icao_code": "ESNU", "lat": 63.791944, "lon": 20.282778, "tm": flight, "name": "Umeå Airport"},
            {"point": 0, "city": "SE-UME", "iata_code":  None, "icao_code":   None, "lat": 63.793576, "lon": 20.289787, "tm": bus, "name": "Umeå Airport"},
            {"point": 1, "city": "SE-UME", "iata_code":  None, "icao_code":   None, "lat": 63.830062, "lon": 20.266811, "tm": train, "name": "Umeå C"},
            {"point": 1, "city": "SE-UME", "iata_code":  None, "icao_code":   None, "lat": 63.829957, "lon": 20.267087, "tm": bus, "name": "Umeå C"},

            {"point": 1, "city": "SE-UPP", "iata_code": None, "icao_code": None, "lat": 59.858198, "lon": 17.646543, "tm": train, "name": "Uppsala C"},
            {"point": 1, "city": "SE-UPP", "iata_code": None, "icao_code": None, "lat": 59.856940, "lon": 17.651102, "tm": bus, "name": "Uppsala C"},
            # {"point": 2, "city": "SE-UPP", "iata_code": None, "icao_code": None, "lat": 59.856940, "lon": 17.651102, "tm": bus, "name": "Uppsala Station"},

            {"point": 0, "city": "SE-VST", "iata_code": "VST", "icao_code": "ESOW", "lat": 59.589444, "lon": 16.633611, "tm": flight, "name": "Västerås Airport"},
            {"point": 1, "city": "SE-VST", "iata_code": None, "icao_code": None, "lat": 59.607622, "lon": 16.551856, "tm": train, "name": "Västerås C"},
            {"point": 1, "city": "SE-VST", "iata_code": None, "icao_code": None, "lat": 59.608583, "lon": 16.553736, "tm": bus, "name": "Västerås C"},

            {"point": 0, "city": "SE-VXO", "iata_code": "VXO", "icao_code": "ESMX", "lat": 56.928889, "lon": 14.727778, "tm": flight, "name": "Växjö Airport"},
            {"point": 1, "city": "SE-VXO", "iata_code": None, "icao_code": None, "lat": 56.876931, "lon": 14.806820, "tm": train, "name": "Växjö Train Station"},
            {"point": 1, "city": "SE-VXO", "iata_code": None, "icao_code": None, "lat": 56.876889, "lon": 14.806800, "tm": bus, "name": "Växjö Bus Station"},

            {"point": 0, "city": "SE-VHM", "iata_code": "VHM", "icao_code": "ESNV", "lat": 64.578889, "lon": 16.833333, "tm": flight, "name": "Vilhelmina Airport"},
            {"point": 1, "city": "SE-VHM", "iata_code": None, "icao_code": None, "lat": 64.622968, "lon": 16.651353, "tm": train, "name": "Vilhelmina Train Station"},
            {"point": 1, "city": "SE-VHM", "iata_code": None, "icao_code": None, "lat": 64.622889, "lon": 16.651429, "tm": bus, "name": "Vilhelmina Bus Station"},

            {"point": 0, "city": "SE-VBY", "iata_code": "VBY", "icao_code": "ESSV", "lat": 57.662778, "lon": 18.346111, "tm": flight, "name": "Visby Airport"},
            {"point": 1, "city": "SE-VBY", "iata_code": None, "icao_code": None, "lat": 57.635686, "lon": 18.296280, "tm": bus, "name": "Visby Bus Station"},
            # {"point": 2, "city": "SE-VBY", "iata_code": None, "icao_code": None, "lat": 57.634629, "lon": 18.279393, "tm": ferry, "name": "Visby Ferry Terminal"},
            {"point": 2, "city": "SE-VBY", "iata_code": None, "icao_code": None, "lat": 57.634423, "lon": 18.279963, "tm": bus, "name": "Visby hamnterminal"},
        ]

        hubs_NO = [
            {"point": 0, "city": "NO-AES", "iata_code": "AES", "icao_code": "ENAL", "lat": 62.562500, "lon": 6.119722, "tm": flight, "name": "Ålesund Airport, Vigra"},
            {"point": 1, "city": "NO-AES", "iata_code": None, "icao_code": None, "lat": 62.470545, "lon": 6.154131, "tm": bus, "name": "Ålesund rutebilstasjon"},
            {"point": 2, "city": "NO-AES", "iata_code": None, "icao_code": None, "lat": 62.467125, "lon": 6.351432, "tm": bus, "name": "Ålesund Moa trafikkterminal"},
            #{"point": 3, "city": "NO-AES", "iata_code": None, "icao_code": None, "lat": 62.474526, "lon": 6.155172, "tm": ferry, "name": "Ålesund Ferry Terminal"},

            {"point": 0, "city": "NO-ALF", "iata_code": "ALF", "icao_code": "ENAT", "lat": 69.976111, "lon": 23.371667, "tm": flight, "name": "Alta Airport"},

            {"point": 0, "city": "NO-ADN", "iata_code": "ANX", "icao_code": "ENAN", "lat": 69.292500, "lon": 16.144167, "tm": flight, "name": "Andøya Airport, Andenes"},
            # {"point": 1, "city": "NO-ADN", "iata_code": None, "icao_code": None, "lat": 69.326813, "lon": 16.133679, "tm": ferry, "name": "Andøya Fv82"},

            {"point": 0, "city": "NO-BDU", "iata_code": "BDU", "icao_code": "ENDU", "lat": 69.055833, "lon": 18.540278, "tm": flight, "name": "Bardufoss Airport"},

            {"point": 0, "city": "NO-BJF", "iata_code": "BJF", "icao_code": "ENBS", "lat": 70.600278, "lon": 29.692778, "tm": flight, "name": "Båtsfjord Airport"},

            {"point": 0, "city": "NO-BGO", "iata_code": "BGO", "icao_code": "ENBR", "lat": 60.293611, "lon": 5.218056, "tm": flight, "name": "Bergen Airport, Flesland"},
            {"point": 1, "city": "NO-BGO", "iata_code": None, "icao_code": None, "lat": 60.390314, "lon": 5.333350, "tm": train, "name": "Bergen Train Station"},
            {"point": 2, "city": "NO-BGO", "iata_code": None, "icao_code": None, "lat": 60.387375, "lon": 5.335179, "tm": bus, "name": "Bergen Bus Station"},
            # {"point": 3, "city": "NO-BGO", "iata_code": None, "icao_code": None, "lat": 60.391992, "lon": 5.311747, "tm": ferry, "name": "Bergen Nøstegaten 30"},

            {"point": 0, "city": "NO-BVG", "iata_code": "BVG", "icao_code": "ENBV", "lat": 70.871389, "lon": 29.034167, "tm": flight, "name": "Berlevåg Airport"},

            {"point": 0, "city": "NO-BOO", "iata_code": "BOO", "icao_code": "ENBO", "lat": 67.269167, "lon": 14.365278, "tm": flight, "name": "Bodø Airport"},
            {"point": 1, "city": "NO-BOO", "iata_code": None, "icao_code": None, "lat": 67.286468, "lon": 14.391679, "tm": train, "name": "Bodø Jernbaneveien 99"},
            {"point": 2, "city": "NO-BOO", "iata_code": None, "icao_code": None, "lat": 67.280007, "lon": 14.422986, "tm": bus, "name": "Bodø Stormyrveien 3"}, # És una empressa de bus, però per sa forma supós que n’hi ha buses
            # {"point": 3, "city": "NO-BOO", "iata_code": None, "icao_code": None, "lat": 67.288311, "lon": 14.394175, "tm": ferry, "name": "Bodø Ferry Terminal"},

            {"point": 0, "city": "NO-BKS", "iata_code": "OLA", "icao_code": "ENOL", "lat": 63.699167, "lon": 9.603889, "tm": flight, "name": "Ørland Airport"},
            {"point": 1, "city": "NO-BKS", "iata_code": None, "icao_code": None, "lat": 63.686535, "lon": 9.666446, "tm": bus, "name": "Brekstad Bus Station"},
            # {"point": 2, "city": "NO-BKS", "iata_code": None, "icao_code": None, "lat": 63.686333, "lon": 9.666826, "tm": ferry, "name": "Brekstad Bus Station"},

            {"point": 0, "city": "NO-BNN", "iata_code": "BNN", "icao_code": "ENBN", "lat": 65.461111, "lon": 12.217500, "tm": flight, "name": "Brønnøysund Airport, Brønnøy"},
            # {"point": 1, "city": "NO-BNN", "iata_code": None, "icao_code": None, "lat": 65.475657, "lon": 12.211208, "tm": ferry, "name": "Brønnøysund Havnegata 40"},
            # {"point": 2, "city": "NO-BNN", "iata_code": None, "icao_code": None, "lat": 65.472284, "lon": 12.197519, "tm": ferry, "name": "Brønnøysund Ferry Terminal"},

            {"point": 0, "city": "NO-FGN", "iata_code": "VDB", "icao_code": "ENFG", "lat": 61.015556, "lon": 9.288056, "tm": flight, "name": "Fagernes Airport, Leirin"},
            {"point": 1, "city": "NO-FGN", "iata_code": None, "icao_code": None, "lat": 60.985902, "lon": 9.238764, "tm": bus, "name": "Fagernes Bus Station"},

            {"point": 0, "city": "NO-FRO", "iata_code": "FRO", "icao_code": "ENFL", "lat": 61.583611, "lon": 5.024722, "tm": flight, "name": "Florø Airport"},
            # {"point": 1, "city": "NO-FRO", "iata_code": None, "icao_code": None, "lat": 61.583611, "lon": 5.024722, "tm": ferry, "name": "Florø Fugleskjærsgata 3"},

            {"point": 0, "city": "NO-FDE", "iata_code": "FDE", "icao_code": "ENBL", "lat": 61.391111, "lon": 5.756944, "tm": flight, "name": "Førde Airport, Bringeland"},
            {"point": 1, "city": "NO-FDE", "iata_code": None, "icao_code": None, "lat": 61.452445, "lon": 5.854094, "tm": bus, "name": "Førde Bus Station"},

            {"point": 0, "city": "NO-HFT", "iata_code": "HFT", "icao_code": "ENHF", "lat": 70.679722, "lon": 23.668611, "tm": flight, "name": "Hammerfest Airport"},
            # {"point": 1, "city": "NO-HFT", "iata_code": None, "icao_code": None, "lat": 70.664604, "lon": 23.682579, "tm": ferry, "name": "Hammerfest Hamnegata 1"},

            {"point": 0, "city": "NO-HRD", "iata_code": "EVE", "icao_code": "ENEV", "lat": 68.488889, "lon": 16.678333, "tm": flight, "name": "Harstad/Narvik Airport, Evenes"},
            {"point": 1, "city": "NO-HRD", "iata_code":None, "icao_code": None, "lat": 68.799612, "lon": 16.546135, "tm": bus, "name": "Harstad Torvet"},
            # {"point": 2, "city": "NO-HRD", "iata_code":None, "icao_code": None, "lat": 68.799304, "lon": 16.549041, "tm": ferry, "name": "Harstad Torvet 7B"},

            {"point": 0, "city": "NO-HVK", "iata_code": "HAA", "icao_code": "ENHK", "lat": 70.486667, "lon": 22.139722, "tm": flight, "name": "Hasvik Airport"},
            # {"point": 1, "city": "NO-HVK", "iata_code": None, "icao_code": None, "lat": 70.483779, "lon": 22.161986, "tm": ferry, "name": "Hasvik Ferry Terminal"},

            {"point": 0, "city": "NO-HAU", "iata_code": "HAU", "icao_code": "ENHD", "lat": 59.343333, "lon": 5.212500, "tm": flight, "name": "Haugesund Airport, Karmøy"},
            {"point": 1, "city": "NO-HAU", "iata_code": None, "icao_code": None, "lat": 59.416331, "lon": 5.274740, "tm": bus, "name": "Haugesund Bus Station"},
            # {"point": 2, "city": "NO-HAU", "iata_code": None, "icao_code": None, "lat": 59.412115, "lon": 5.255868, "tm": ferry, "name": "Haugesund Ferry Terminal"},

            {"point": 0, "city": "NO-HVG", "iata_code": "HVG", "icao_code": "ENHV", "lat": 71.009722, "lon": 25.983611, "tm": flight, "name": "Honningsvåg Airport, Valan"},
            # {"point": 1, "city": "NO-HVG", "iata_code": None, "icao_code": None, "lat": 70.981340, "lon": 25.968251, "tm": ferry, "name": "Honningsvåg Homen 2"},

            {"point": 0, "city": "NO-KKN", "iata_code": "KKN", "icao_code": "ENKR", "lat": 69.725000, "lon": 29.887778, "tm": flight, "name": "Kirkenes Airport, Høybuktmoen"},

            {"point": 0, "city": "NO-KRS", "iata_code": "KRS", "icao_code": "ENCN", "lat": 58.203889, "lon": 8.0850000, "tm": flight, "name": "Kristiansand Airport, Kjevik"},
            {"point": 1, "city": "NO-KRS", "iata_code": None, "icao_code": None, "lat": 58.145613, "lon": 7.988000, "tm": train, "name": "Kristiansand Train Station"},
            {"point": 1, "city": "NO-KRS", "iata_code": None, "icao_code": None, "lat": 58.145664, "lon": 7.989686, "tm": bus, "name": "Kristiansand Bus Station"},
            # {"point": 2, "city": "NO-KRS", "iata_code": None, "icao_code": None, "lat": 58.144136, "lon": 7.985192, "tm": ferry, "name": "Kristiansand Ferry Terminal"},

            {"point": 0, "city": "NO-KSU", "iata_code": "KSU", "icao_code": "ENKB", "lat": 63.111944, "lon": 7.826111, "tm": flight, "name": "Kristiansund Airport, Kvernberget"},
            {"point": 1, "city": "NO-KSU", "iata_code": None, "icao_code": None, "lat": 63.114308, "lon": 7.733472, "tm": bus, "name": "Kristiansund Bus Station"},
            # {"point": 2, "city": "NO-KSU", "iata_code": None, "icao_code": None, "lat": 63.114127, "lon": 7.734647, "tm": ferry, "name": "Kristiansund Ferry Terminal"},
            # {"point": 3, "city": "NO-KSU", "iata_code": None, "icao_code": None, "lat": 63.111958, "lon": 7.869896, "tm": ferry, "name": "Kristiansund Seivikveien 1"},

            {"point": 0, "city": "NO-LKL", "iata_code": "LKL", "icao_code": "ENNA", "lat": 70.066667, "lon": 24.973889, "tm": flight, "name": "Lakselv Airport, Banak"},

            {"point": 0, "city": "NO-LRI", "iata_code": "SRP", "icao_code": "ENSO", "lat": 59.792778, "lon": 5.339722, "tm": flight, "name": "Stord Airport, Sørstokken"},
            {"point": 1, "city": "NO-LRI", "iata_code": None, "icao_code": None, "lat": 59.779251, "lon": 5.501239, "tm": bus, "name": "Leirvik Bus Station"},
            # {"point": 2, "city": "NO-LRI", "iata_code": None, "icao_code": None, "lat": 59.749771, "lon": 5.465777, "tm": ferry, "name": "Leirvik Stord"},

            {"point": 0, "city": "NO-LKN", "iata_code": "LKN", "icao_code": "ENLK", "lat": 68.152500, "lon": 13.609444, "tm": flight, "name": "Leknes Airport"},
            {"point": 1, "city": "NO-LKN", "iata_code": None, "icao_code": None, "lat": 68.157055, "lon": 13.621648, "tm": bus, "name": "Leknes Boreal Transport Nord, Lofoten Buss"},

            # {"point": 0, "city": "NO-LNG", "iata_code": "LYR", "icao_code": "ENSB", "lat": 78.246111, "lon": 15.465556, "tm": flight, "name": "Svalbard Airport, Longyear"}, #code made up,as no code available for this city
           # {"point": 1, "city": "NO-LNG", "iata_code": None, "icao_code": None, "lat": 78.224865, "lon": 15.629327, "tm": bus, "name": "Longyearbyen sjøområdet, PB 160"},

            {"point": 0, "city": "NO-MEH", "iata_code": "MEH", "icao_code": "ENMH", "lat": 71.028889, "lon": 27.826389, "tm": flight, "name": "Mehamn Airport"},

            {"point": 0, "city": "NO-MQN", "iata_code": "MQN", "icao_code": "ENRA", "lat": 66.363889, "lon": 14.301667, "tm": flight, "name": "Mo i Rana Airport, Røssvoll"},
            {"point": 1, "city": "NO-MQN", "iata_code": None, "icao_code": None, "lat": 66.309614, "lon": 14.133438, "tm": train, "name": "Mo i Rana Train Station"},

            {"point": 0, "city": "NO-MOL", "iata_code": "MOL", "icao_code": "ENML", "lat": 62.744722, "lon": 7.262500, "tm": flight, "name": "Molde Airport, Årø"},
            {"point": 1, "city": "NO-MOL", "iata_code": None, "icao_code": None, "lat": 62.737158, "lon": 7.161304, "tm": bus, "name": "Molde trafikkterminal"},
            {"point": 2, "city": "NO-MOL", "iata_code": None, "icao_code": None, "lat": 62.737284, "lon": 7.168157, "tm": bus, "name": "Molde ferjekai"},
            # {"point": 3, "city": "NO-MOL", "iata_code": None, "icao_code": None, "lat": 62.737003, "lon": 7.169558, "tm": ferry, "name": "Molde ferjekai Ferry Terminal"},

            {"point": 0, "city": "NO-MJF", "iata_code": "MJF", "icao_code": "ENMS", "lat": 65.783997, "lon": 13.214914, "tm": flight, "name": "Mosjøen Airport, Kjærstad"},
            {"point": 1, "city": "NO-MJF", "iata_code": None, "icao_code": None, "lat": 65.844924, "lon": 13.200172, "tm": train, "name": "Mosjøen Train Station"},
            # {"point": 1, "city": "NO-MJF", "iata_code": None, "icao_code": None, "lat": 65.850290, "lon": 13.191032, "tm": ferry, "name": "Mosjøen Ferry Terminal"},

            {"point": 0, "city": "NO-OSY", "iata_code": "OSY", "icao_code": "ENNM", "lat": 64.466667, "lon": 11.600000, "tm": flight, "name": "Namsos Airport, Høknesøra"},
            # {"point": 1, "city": "NO-OSY", "iata_code": None, "icao_code": None, "lat": 64.464777, "lon": 11.491562, "tm": ferry, "name": "Namsos Verftsgata 34"},
            # {"point": 2, "city": "NO-OSY", "iata_code": None, "icao_code": None, "lat": 64.636705, "lon": 11.360221, "tm": ferry, "name": "Namsos Fv777,"},

            {"point": 0, "city": "NO-NTB", "iata_code": "NTB", "icao_code": "ENNO", "lat": 59.565556, "lon": 9.212222, "tm": flight, "name": "Notodden Airport, Tuven"},
            {"point": 1, "city": "NO-NTB", "iata_code": None, "icao_code": None, "lat": 59.558888, "lon": 9.267269, "tm": train, "name": "Notodden Train Station"},
            {"point": 2, "city": "NO-NTB", "iata_code": None, "icao_code": None, "lat": 59.556848, "lon": 9.256524, "tm": bus, "name": "Notodden Bus Station"},

            # {"point": 0, "city": "Ny-Ålesund", "iata_code": None, "icao_code": "ENAS", "lat": 78.927778, "lon": 11.874722, "tm": flight, "name": "Ny-Ålesund Airport, Hamnerabben"},

            {"point": 0, "city": "NO-ORS", "iata_code": "HOV", "icao_code": "ENOV", "lat": 62.178611, "lon": 6.075833, "tm": flight, "name": "Ørsta–Volda Airport, Hovden"},
            {"point": 1, "city": "NO-ORS", "iata_code": None, "icao_code":None, "lat": 62.197759, "lon": 6.126818, "tm": bus, "name": "Ørsta Bus Station"},

            {"point": 0, "city": "NO-OSL", "iata_code": "OSL", "icao_code": "ENGM", "lat": 60.202778, "lon": 11.083889, "tm": flight, "name": "Oslo Airport"},
            {"point": 0, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 60.193944, "lon": 11.096738, "tm": train, "name": "Oslo Airport Train Station"},
            {"point": 0, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 60.193178, "lon": 11.096799, "tm": bus, "name": "Oslo Airport Bus Station"},
            {"point": 1, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 59.911154, "lon": 10.752442, "tm": train, "name": "Oslo Jernbanetorget 1"},
            {"point": 1, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 59.911605, "lon": 10.759301, "tm": bus, "name": "Oslo Bussterminalen Grønland"},
            # {"point": 2, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 59.910655, "lon": 10.729729, "tm": ferry, "name": "Oslo Ferry Terminal"},
            # {"point": 3, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 59.908574, "lon": 10.709435, "tm": ferry, "name": "Oslo Color Line, Filipstadveien 25"},
            # {"point": 4, "city": "NO-OSL", "iata_code":  None, "icao_code":   None, "lat": 59.902917, "lon": 10.743405, "tm": ferry, "name": "Oslo Ferry Terminal"},

            {"point": 0, "city": "NO-RRS", "iata_code": "RRS", "icao_code": "ENRO", "lat": 62.578333, "lon": 11.342222, "tm": flight, "name": "Røros Airport"},
            {"point": 1, "city": "NO-RRS", "iata_code": None, "icao_code": None, "lat": 62.574605, "lon": 11.378910, "tm": train, "name": "Røros Train Station"},
            {"point": 1, "city": "NO-RRS", "iata_code": None, "icao_code": None, "lat": 62.574686, "lon": 11.380118, "tm": bus, "name": "Røros Bus Station"},

            {"point": 0, "city": "NO-RVK", "iata_code": "RVK", "icao_code": "ENRM", "lat": 64.838333, "lon": 11.146111, "tm": flight, "name": "Rørvik Airport, Ryum"},

            {"point": 0, "city": "NO-RET", "iata_code": "RET", "icao_code": "ENRS", "lat": 67.527778, "lon": 12.103333, "tm": flight, "name": "Røst Airport"},
            # {"point": 1, "city": "NO-RET", "iata_code": None, "icao_code": None, "lat": 67.504790, "lon": 12.070819, "tm": ferry, "name": "Røst Ferry Terminal"},

            {"point": 0, "city": "NO-SDN", "iata_code": "SDN", "icao_code": "ENSD", "lat": 61.830000, "lon": 6.105833, "tm": flight, "name": "Sandane Airport, Anda"},
            {"point": 1, "city": "NO-SDN", "iata_code": None, "icao_code": None, "lat": 61.776750, "lon": 6.213883, "tm": bus, "name": "Sandane Bus Station"},
            # {"point": 2, "city": "NO-SDN", "iata_code": None, "icao_code": None, "lat": 61.846423, "lon": 6.082015, "tm": ferry, "name": "Sandane Ferry Terminal"},

            {"point": 0, "city": "NO-TRF", "iata_code": "TRF", "icao_code": "ENTO", "lat": 59.186667, "lon": 10.258611, "tm": flight, "name": "Sandefjord Airport, Torp"},
            {"point": 0, "city": "NO-TRF", "iata_code": None, "icao_code": None, "lat": 59.178995, "lon": 10.252250, "tm": bus, "name": "Sandefjord Airport Bus Station"},
            {"point": 1, "city": "NO-TRF", "iata_code": None, "icao_code": None, "lat": 59.135219, "lon": 10.222715, "tm": train, "name": "Sandefjord Train Station"},
            {"point": 1, "city": "NO-TRF", "iata_code": None, "icao_code": None, "lat": 59.135056, "lon": 10.223308, "tm": bus, "name": "Sandefjord Bus Station"},
            # {"point": 2, "city": "NO-TRF", "iata_code": None, "icao_code": None, "lat": 59.126956, "lon": 10.228010, "tm": ferry, "name": "Sandefjord Tollbugata 5"},

            {"point": 0, "city": "NO-SSJ", "iata_code": "SSJ", "icao_code": "ENST", "lat": 65.956667, "lon": 12.468889, "tm": flight, "name": "Sandnessjøen Airport, Stokka"},
            # {"point": 1, "city": "NO-SSJ", "iata_code": None, "icao_code": None, "lat": 66.021306, "lon": 12.630053, "tm": ferry, "name": "Sandnessjøen Ferry Terminal"},

            {"point": 0, "city": "NO-SOG", "iata_code": "SOG", "icao_code": "ENSG", "lat": 61.157222, "lon": 7.138056, "tm": flight, "name": "Sogndal Airport, Haukåsen"},
            {"point": 1, "city": "NO-SOG", "iata_code": None, "icao_code": None, "lat": 61.230944, "lon": 7.097184, "tm": bus, "name": "Sogndal Bus Station"},
            # {"point": 2, "city": "NO-SOG", "iata_code": None, "icao_code": None, "lat": 61.229721, "lon": 7.104699, "tm": ferry, "name": "Sogndal Ferry Terminal"},

            {"point": 0, "city": "NO-SOJ", "iata_code": "SOJ", "icao_code": "ENSR", "lat": 69.786667, "lon": 20.959722, "tm": flight, "name": "Sørkjosen Airport"},

            {"point": 0, "city": "NO-SVG", "iata_code": "SVG", "icao_code": "ENZV", "lat": 58.876667, "lon": 5.637778, "tm": flight, "name": "Stavanger Airport, Sola"},
            {"point": 1, "city": "NO-SVG", "iata_code": None, "icao_code": None, "lat": 58.966911, "lon": 5.732003, "tm": train, "name": "Stavanger Jernbaneveien 3"},
            {"point": 2, "city": "NO-SVG", "iata_code": None, "icao_code": None, "lat": 58.960568, "lon": 5.738114, "tm": bus, "name": "Stavanger Bus Station"},
           # {"point": 3, "city": "NO-SVG", "iata_code": None, "icao_code": None, "lat": 58.972755, "lon": 5.730039, "tm": ferry, "name": "Stavanger Skagenkaien 35-37"},
           # {"point": 4, "city": "NO-SVG", "iata_code": None, "icao_code": None, "lat": 58.972207, "lon": 5.737805, "tm": ferry, "name": "Stavanger Ferry Terminal"},
           # {"point": 5, "city": "NO-SVG", "iata_code": None, "icao_code": None, "lat": 58.972423, "lon": 5.739813, "tm": ferry, "name": "Stavanger Ferry Terminal"},

            {"point": 0, "city": "NO-SKN", "iata_code": "SKN", "icao_code": "ENSK", "lat": 68.580833, "lon": 15.026111, "tm": flight, "name": "Stokmarknes Airport, Skagen"},
            # {"point": 1, "city": "NO-SKN", "iata_code": None, "icao_code": None, "lat": 68.570210, "lon": 14.912206, "tm": ferry, "name": "Stokmarknes Ferry Terminal"},

            # {"point": 0, "city": "Sveagruva", "iata_code": None, "icao_code": "ENSA", "lat": 77.896900, "lon": 16.724998, "tm": flight, "name": "Svea Airport"}, # No veig s’aeroport a google maps

            {"point": 0, "city": "NO-SVJ", "iata_code": "SVJ", "icao_code": "ENSH", "lat": 68.243300, "lon": 14.669200, "tm": flight, "name": "Svolvær Airport, Helle"},
            # {"point": 1, "city": "NO-SVJ", "iata_code": None, "icao_code": None, "lat": 68.234882, "lon": 14.553429, "tm": ferry, "name": "Svolvær Svolværveien 91"},

            {"point": 0, "city": "NO-TOS", "iata_code": "TOS", "icao_code": "ENTC", "lat": 69.681389, "lon": 18.917778, "tm": flight, "name": "Tromsø Airport"},
            # {"point": 1, "city": "NO-TOS", "iata_code": None, "icao_code": None, "lat": 69.646474, "lon": 18.955701, "tm": ferry, "name": "Tromsø Strandtorget 1"},

            {"point": 0, "city": "NO-TRD", "iata_code": "TRD", "icao_code": "ENVA", "lat": 63.457500, "lon": 10.924167, "tm": flight, "name": "Trondheim Airport, Værnes"},
            {"point": 0, "city": "NO-TRD", "iata_code": None, "icao_code": None, "lat": 63.454106, "lon": 10.913842, "tm": train, "name": "Trondheim Airport Train"},
            {"point": 1, "city": "NO-TRD", "iata_code": None, "icao_code": None, "lat": 63.436626, "lon": 10.398762, "tm": train, "name": "Trondheim Train Station"},
            {"point": 1, "city": "NO-TRD", "iata_code": None, "icao_code": None, "lat": 63.435950, "lon": 10.401337, "tm": bus, "name": "Trondheim Bus Station"},
            # {"point": 2, "city": "NO-TRD", "iata_code": None, "icao_code": None, "lat": 63.437575, "lon": 10.398383, "tm": ferry, "name": "Trondheim Brattørkaia 17B"},

            {"point": 0, "city": "NO-VDS", "iata_code": "VDS", "icao_code": "ENVD", "lat": 70.065278, "lon": 29.844722, "tm": flight, "name": "Vadsø Airport"},
            # {"point": 1, "city": "NO-VDS", "iata_code": None, "icao_code": None, "lat": 70.074534, "lon": 29.748121, "tm": ferry, "name": "Vadsø Havneterminalen, Pb 158"},

            {"point": 0, "city": "NO-VEY", "iata_code": "VRY", "icao_code": "ENVR", "lat": 67.654444, "lon": 12.726944, "tm": flight, "name": "Værøy Heliport"},
            # {"point": 1, "city": "NO-VEY", "iata_code": "VRY", "icao_code": "ENVR", "lat": 67.652615, "lon": 12.710637, "tm": ferry, "name": "Værøy Ferry Terminal"},

            {"point": 0, "city": "NO-VAO", "iata_code": "VAW", "icao_code": "ENSS", "lat": 70.355278, "lon": 31.045000, "tm": flight, "name": "Vardø Airport, Svartnes"},
            # {"point": 1, "city": "NO-VAO", "iata_code": None, "icao_code": None, "lat": 70.374471, "lon": 31.103651, "tm": ferry, "name": "Vardø Kaigata 26 A"},

        ]

        hubs_GB = [
            {"point": 0, "city": "GB-ABD", "iata_code": "ABZ", "icao_code": "EGPD", "lat": 57.202500, "lon": -2.198056, "tm": flight, "name": "Aberdeen Airport"},
            # {"point": 1, "city": "GB-ABD", "iata_code":  None, "icao_code":   None, "lat": 57.143617, "lon": -2.098833, "tm": train, "name": "Aberdeen Main Station"},
            {"point": 1, "city": "GB-ABD", "iata_code":  None, "icao_code":   None, "lat": 57.144492, "lon": -2.096127, "tm": bus, "name": "Aberdeen Main Station"},

            {"point": 0, "city": "GB-ANY", "iata_code": "ACI", "icao_code": "EGJA", "lat": 49.706667, "lon": -2.214444, "tm": flight, "name": "Alderney Airport"},
            # {"point": 1, "city": "GB-ANY", "iata_code": None, "icao_code": None, "lat": 49.724214, "lon": -2.200290, "tm": ferry, "name": "Alderney Terminal"},

            {"point": 0, "city": "GB-VLY", "iata_code": "VLY", "icao_code": "EGOV", "lat": 53.254889, "lon": -4.535095, "tm": flight, "name": "Anglesey Airport"},
            {"point": 1, "city": "GB-VLY", "iata_code": None, "icao_code": None, "lat": 53.307712, "lon": -4.631018, "tm": train, "name": "Anglesey Holyhead"},
            {"point": 2, "city": "GB-VLY", "iata_code": None, "icao_code": None, "lat": 53.222019, "lon": -4.210257, "tm": train, "name": "Anglesey Llanfairpwll"},

             # {"point": 1, "city": "GB-VLY", "iata_code": None, "icao_code": None, "lat": 53.309313, "lon": -4.628904, "tm": ferry, "name": "Anglesey Holyhead"},

            {"point": 0, "city": "GB-AYR", "iata_code": "PIK", "icao_code": "EGPK", "lat": 55.509444, "lon": -4.594444, "tm": flight, "name": "Glasgow Prestwick Airport"},
            {"point": 0, "city": "GB-AYR", "iata_code": None, "icao_code": None, "lat": 55.509042, "lon": -4.614142, "tm": train, "name": "Ayr Prestwick Intl Airport"},
            {"point": 0, "city": "GB-AYR", "iata_code": None, "icao_code": None, "lat": 55.508939, "lon": -4.613835, "tm": bus, "name": "Ayr A79 Opp Prestwick Airport"},
            {"point": 1, "city": "GB-AYR", "iata_code": None, "icao_code": None, "lat": 55.458143, "lon": -4.625848, "tm": train, "name": "Ayr KA7"},
            {"point": 2, "city": "GB-AYR", "iata_code": None, "icao_code": None, "lat": 55.462134, "lon": -4.634077, "tm": bus, "name": "Ayr Stance 2"},

            {"point": 0, "city": "GB-BRR", "iata_code": "BRR", "icao_code": "EGPR", "lat": 57.025357, "lon": -7.449459, "tm": flight, "name": "Barra Airport"},
            {"point": 0, "city": "GB-BRR", "iata_code": None, "icao_code": None, "lat": 57.025384, "lon": -7.4499547, "tm": bus, "name": "Barra Terminal Airport"},
           # {"point": 1, "city": "GB-BRR", "iata_code": None, "icao_code": None, "lat": 57.008618, "lon": -7.403326, "tm": ferry, "name": "Barra Aird Mhor"},
           # {"point": 2, "city": "GB-BRR", "iata_code": None, "icao_code": None, "lat": 57.954330, "lon": -7.488552, "tm": ferry, "name": "Barra Castlebay"},

            {"point": 0, "city": "GB-BEL", "iata_code": "BFS", "icao_code": "EGAA", "lat": 54.657500, "lon": -6.215833, "tm": flight, "name": "Belfast Airport"},
            {"point": 1, "city": "GB-BEL", "iata_code": "BHD", "icao_code": "EGAC", "lat": 54.617621, "lon": -5.871842, "tm": flight, "name": "George Best Belfast City Airport"},
            {"point": 2, "city": "GB-BEL", "iata_code": None, "icao_code": None, "lat": 54.595282, "lon": -5.917262, "tm": train, "name": "Belfast Central Station"},
            {"point": 3, "city": "GB-BEL", "iata_code": None, "icao_code": None, "lat": 54.594517, "lon": -5.936163, "tm": bus, "name": "Belfast Europa Buscentre"},
            {"point": 4, "city": "GB-BEL", "iata_code": None, "icao_code": None, "lat": 54.635852, "lon": -5.881311, "tm": bus, "name": "Belfast Stenaline terminus"},
           # {"point": 5, "city": "GB-BEL", "iata_code": None, "icao_code": None, "lat": 54.629460, "lon": -5.889233, "tm": ferry, "name": "Belfast Victoria Terminal 2"},
           # {"point": 6, "city": "GB-BEL", "iata_code": None, "icao_code": None, "lat": 54.636706, "lon": -5.882969, "tm": ferry, "name": "Belfast Stena Line"},

            {"point": 0, "city": "GB-BBC", "iata_code": "BEB", "icao_code": "EGPL", "lat": 57.481111, "lon": -7.362778, "tm": flight, "name": "Benbecula Airport"},
            {"point": 1, "city": "GB-BBC", "iata_code": None, "icao_code": None, "lat": 57.473194, "lon": -7.377545, "tm": bus, "name": "Benbecula Bank of Scotland"},

            {'point': 0, 'city': 'GB-BHM', 'iata_code': 'BHX', 'icao_code':'EGBB', 'lat': 52.453889, 'lon': -1.748056, 'tm': flight, 'name': "Birmingham Airport"},
            {'point': 0, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.450707, 'lon': -1.725237, 'tm': train, 'name': "Birmingham Airport"},
            {'point': 0, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.450489, 'lon': -1.725712, 'tm': bus, 'name': "Birmingham Airport"},
            {'point': 1, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.477779, 'lon': -1.898927, 'tm': train, 'name': "Birmingham New Street Station"},
            {'point': 2, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.475331, 'lon': -1.888481, 'tm': bus, 'name': "Birmingham Coach Station"},
            {'point': 3, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.547898, 'lon': -1.935290, 'tm': bus, 'name': "Birmingham Great Barr"},
            {'point': 4, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.471427, 'lon': -1.969897, 'tm': bus, 'name': "Birmingham Bearwood"},
            {'point': 5, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.472744, 'lon': -1.920110, 'tm': bus, 'name': "Birmingham Hagley Rd Five Ways"},
            {'point': 6, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.478732, 'lon': -1.892610, 'tm': train, 'name': "Birmingham Moor Street "},
            {'point': 6, 'city': 'GB-BHM', 'iata_code':  None, 'icao_code': None, 'lat': 52.478986, 'lon': -1.892527, 'tm': bus, 'name': "Birmingham Moor Street "},

            {"point": 1, "city": "GB-BLB", "iata_code": None, "icao_code": None, "lat": 53.746504, "lon": -2.479542, "tm": train, "name": "Blackburn Sta Boulevard"},
            {"point": 2, "city": "GB-BLB", "iata_code": None, "icao_code": None, "lat": 53.748805, "lon": -2.480806, "tm": bus, "name": "Blackburn Bus Station"},

            {"point": 1, "city": "GB-BLK", "iata_code": None, "icao_code": None, "lat": 53.821933, "lon": -3.049268, "tm": train, "name": "Blackpool North"},
            {"point": 2, "city": "GB-BLK", "iata_code": None, "icao_code": None, "lat": 53.798618, "lon": -3.049058, "tm": train, "name": "Blackpool South"},
            {"point": 3, "city": "GB-BLK", "iata_code": None, "icao_code": None, "lat": 53.813505, "lon": -3.052757, "tm": bus, "name": "Blackpool Central Dr"},

            # {"point": 1, "city": "GB-BLT", "iata_code": None, "icao_code": None, "lat": 53.574442, "lon": -2.426836, "tm": train, "name": "Bolton BL3"}, #included inside Manchester
            # {"point": 1, "city": "GB-BLT", "iata_code": None, "icao_code": None, "lat": 53.575504, "lon": -2.427151, "tm": bus, "name": "Bolton Great Moor Street"},

            {"point": 0, "city": "GB-BOH", "iata_code": "BOH", "icao_code": "EGHH", "lat": 50.780000, "lon": -1.842500, "tm": flight, "name": "Bournemouth Airport"},
            {"point": 1, "city": "GB-BOH", "iata_code":  None, "icao_code":   None, "lat": 50.727270, "lon": -1.864487, "tm": train, "name": "Bournemouth Coach Station"},
            {"point": 1, "city": "GB-BOH", "iata_code":  None, "icao_code":   None, "lat": 50.726801, "lon": -1.864799, "tm": bus, "name": "Bournemouth Coach Station"},
            {"point": 2, "city": "GB-BOH", "iata_code":  None, "icao_code":   None, "lat": 50.716725, "lon": -1.877202, "tm": bus, "name": "Bournemouth Pier"},
            {"point": 3, "city": "GB-BOH", "iata_code":  None, "icao_code":   None, "lat": 50.742899, "lon": -1.898665, "tm": bus, "name": "Bournemouth University"},
            {'point': 5, 'city': 'GB-BOH', 'iata_code':  None, 'icao_code':  None, 'lat': 50.719104, 'lon': -1.983604, 'tm': train, 'name': "Poole Train Station"},
            {'point': 6, 'city': 'GB-BOH', 'iata_code':  None, 'icao_code':  None, 'lat': 50.717181, 'lon': -1.977055, 'tm': bus, 'name': "Poole Dorset Station"},
           # {'point': 7, 'city': 'GB-BOH', 'iata_code':  None, 'icao_code':  None, 'lat': 50.711881, 'lon': -1.985329, 'tm': ferry, 'name': "Poole Quay Landing"},
           # {'point': 8, 'city': 'GB-BOH', 'iata_code':  None, 'icao_code':  None, 'lat': 50.709456, 'lon': -1.992703, 'tm': ferry, 'name': "Poole Ferry Terminal"},

            {"point": 1, "city": "GB-BRF", "iata_code": None, "icao_code": None, "lat": 53.796944, "lon": -1.752960, "tm": train, "name": "Bradford Forster Square"},
            {"point": 2, "city": "GB-BRF", "iata_code": None, "icao_code": None, "lat": 53.791281, "lon": -1.749776, "tm": train, "name": "Bradford Interchange"},
            {"point": 2, "city": "GB-BRF", "iata_code": None, "icao_code": None, "lat": 53.791222, "lon": -1.750325, "tm": bus, "name": "Bradford Interchange"},

            {"point": 1, "city": "GB-BSH", "iata_code": None, "icao_code": None, "lat": 50.829012, "lon": -0.141261, "tm": train, "name": "Brighton Terminus"},
            {"point": 2, "city": "GB-BSH", "iata_code": None, "icao_code": None, "lat": 50.819846, "lon": -0.138103, "tm": bus, "name": "Brighton Coach Station"},

            {"point": 0, "city": "GB-BRS", "iata_code": "BRS", "icao_code": "EGGD", "lat": 51.382878, "lon": -2.719167, "tm": flight, "name": "Bristol Airport"},
            {"point": 0, "city": "GB-BRS", "iata_code":  None, "icao_code":   None, "lat": 51.386668, "lon": -2.711403, "tm": bus, "name": "Bristol Airport"},
            {"point": 1, "city": "GB-BRS", "iata_code": "TPB", "icao_code":   None, "lat": 51.449800, "lon": -2.580993, "tm": train, "name": "Bristol Temple Meads Railway Station"},
            {"point": 2, "city": "GB-BRS", "iata_code": "BPR", "icao_code":   None, "lat": 51.514210, "lon": -2.543245, "tm": train, "name": "Bristol Parkway Railway Station"},
            {"point": 3, "city": "GB-BRS", "iata_code":  None, "icao_code":   None, "lat": 51.459017, "lon": -2.593138, "tm": bus, "name": "Bristol Coach Station"},
            {"point": 4, "city": "GB-BRS", "iata_code":  None, "icao_code":   None, "lat": 51.463947, "lon": -2.609337, "tm": bus, "name": "Bristol Clifton Down"},
            {"point": 5, "city": "GB-BRS", "iata_code":  None, "icao_code":   None, "lat": 51.471246, "lon": -2.616060, "tm": bus, "name": "Bristol Black Bow Hill"},
            {'point': 6, 'city': 'GB-BRS', 'iata_code':  None, 'icao_code':   None, 'lat':   51.5049, 'lon':  -2.56244, 'tm': train, 'name': 'Bristol Filton Abbeywood'},

            {"point": 1, "city": "GB-CMG", "iata_code": None, "icao_code": None, "lat": 52.194091, "lon": 0.137301, "tm": train, "name": "Cambridge Station RD"},
            {"point": 2, "city": "GB-CMG", "iata_code": None, "icao_code": None, "lat": 52.203239, "lon": 0.129225, "tm": bus, "name": "Cambridge Parkside"},

            {"point": 0, "city": "GB-CBT", "iata_code": "CAL", "icao_code": "EGEC", "lat": 55.437500, "lon": -5.688056, "tm": flight, "name": "Campbeltown Airport"},
            {"point": 1, "city": "GB-CBT", "iata_code": None, "icao_code": None, "lat": 55.426020, "lon": -5.604796, "tm": bus, "name": "Campbeltown Terminus"},

               # {"point": 1, "city": "GB-CBT", "iata_code": None, "icao_code": None, "lat": 55.424061, "lon": -5.599422, "tm": ferry, "name": "Campbeltown Terminal"},

            {"point": 0, "city": "GB-CDF", "iata_code": "CWL", "icao_code": "EGFF", "lat": 51.398549, "lon": -3.339457, "tm": flight, "name": "Cardiff Airport"},
            {"point": 0, "city": "GB-CDF", "iata_code": None, "icao_code":   None, "lat": 51.398973, "lon": -3.339900, "tm": bus, "name": "Cardiff Airport"},
            {"point": 1, "city": "GB-CDF", "iata_code": "CFW", "icao_code":   None, "lat": 51.475967, "lon": -3.179014, "tm": train, "name": "Cardiff Central Railway Station"},
            {"point": 2, "city": "GB-CDF", "iata_code":  None, "icao_code":   None, "lat": 51.483965, "lon": -3.189541, "tm": bus, "name": "Cardiff Sophia Gardens"},
            {"point": 3, "city": "GB-CDF", "iata_code":  None, "icao_code":   None, "lat": 51.501373, "lon": -3.196142, "tm": bus, "name": "Cardiff North Road Clinic"},

            {"point": 1, "city": "GB-COL", "iata_code":  None, "icao_code":  None, "lat": 51.900729, "lon": 0.892633, "tm": train, "name": "Colchester Station"},
            {"point": 1, "city": "GB-COL", "iata_code":  None, "icao_code":  None, "lat": 51.899668, "lon": 0.894897, "tm": bus, "name": "Colchester Layby (Stand Ea)"},
            {"point": 2, "city": "GB-COL", "iata_code":  None, "icao_code":  None, "lat": 51.886539, "lon": 0.904420, "tm": train, "name": "Colchester Town"},
            {"point": 3, "city": "GB-COL", "iata_code":  None, "icao_code":  None, "lat": 51.886976, "lon": 0.901260, "tm": bus, "name": "Colchester Stanwell St"},
            {"point": 4, "city": "GB-COL", "iata_code":  None, "icao_code":  None, "lat": 51.876116, "lon": 0.942034, "tm": bus, "name": "Colchester University of Essex"},

            {"point": 0, "city": "GB-OLL", "iata_code": "COL", "icao_code": "EGEL", "lat": 56.601944, "lon": -6.617778, "tm": flight, "name": "Coll Airport"},
           # {"point": 1, "city": "GB-OLL", "iata_code": None, "icao_code": None, "lat": 56.615053, "lon": -6.524223, "tm": ferry, "name": "Coll Terminal"},

            {"point": 0, "city": "GB-CSA", "iata_code": "CSA", "icao_code": "EGEY", "lat": 56.057500, "lon": -6.243056, "tm": flight, "name": "Colonsay Airport"},
            #{"point": 1, "city": "GB-CSA", "iata_code": None, "icao_code": None, "lat": 56.068589, "lon": -6.188167, "tm": ferry, "name": "Colonsay Ferry Terminal"},

            {"point": 0, "city": "GB-CVT", "iata_code": "CVT", "icao_code": "EGBE", "lat": 52.372500, "lon": -1.479722, "tm": flight, "name": "Coventry Airport"},
            {"point": 1, "city": "GB-CVT", "iata_code": None, "icao_code": None, "lat": 52.401071, "lon": -1.513637, "tm": train, "name": "Coventry Station Square"},
            {"point": 2, "city": "GB-CVT", "iata_code": None, "icao_code": None, "lat": 52.410374, "lon": -1.506965, "tm": bus, "name": "Coventry Pool Meadow"},

           {"point": 1, "city": "GB-DXY", "iata_code":  None, "icao_code":   None, "lat": 52.916139, "lon": -1.463340, "tm": train, "name": "Derby Railway Terrace"},
           {"point": 2, "city": "GB-DXY", "iata_code":  None, "icao_code":   None, "lat": 52.922098, "lon": -1.471344, "tm": bus, "name": "Derby Station"},

            {"point": 0, "city": "GB-LDY", "iata_code": "LDY", "icao_code": "EGAE", "lat": 55.042778, "lon": -7.161944, "tm": flight, "name": "City of Derry Airport"},
            {"point": 1, "city": "GB-LDY", "iata_code": None, "icao_code": None, "lat": 54.991907, "lon": -7.313674, "tm": train, "name": "Derry Londonderry Station"},
            {"point": 2, "city": "GB-LDY", "iata_code": None, "icao_code": None, "lat": 54.996760, "lon": -7.318241, "tm": bus, "name": "Derry Buscentre"},

            {"point": 0, "city": "GB-DON", "iata_code": "DSA", "icao_code": "EGCN", "lat": 53.475278, "lon": -1.004167, "tm": flight, "name": "Doncaster Sheffield Airport"},
            {"point": 1, "city": "GB-DON", "iata_code": None, "icao_code": None, "lat": 53.522168, "lon": -1.139742, "tm": train, "name": "Doncaster Railway Cottage"},
            {"point": 2, "city": "GB-DON", "iata_code": None, "icao_code": None, "lat": 53.524342, "lon": -1.138893, "tm": bus, "name": "Doncaster Coach Station"},

           {"point": 1, "city": "GB-DDL", "iata_code":  None, "icao_code":   None, "lat": 52.524701, "lon": -2.049482, "tm": train, "name": " Dudley Port Station"},
           {"point": 2, "city": "GB-DDL", "iata_code":  None, "icao_code":   None, "lat": 52.508752, "lon": -2.011709, "tm": train, "name": "Sandwell & Dudley Station"},
           {"point": 3, "city": "GB-DDL", "iata_code":  None, "icao_code":   None, "lat": 52.511017, "lon": -2.079110, "tm": bus, "name": "Dudley DY2 AT"},

            {'point': 0, 'city': 'GB-DUN', 'iata_code': 'DND', 'icao_code': 'EGPN', 'lat': 56.452500, 'lon': -3.017500, 'tm': flight, 'name': "Dundee Airport"},
            {'point': 1, 'city': 'GB-DUN', 'iata_code': None, 'icao_code': None, 'lat': 56.456864, 'lon': -2.970210, 'tm': train, 'name': "Dundee DD1 4BX"},
            {'point': 2, 'city': 'GB-DUN', 'iata_code': None, 'icao_code': None, 'lat': 56.463068, 'lon': -2.965971, 'tm': bus, 'name': "Dundee Seagate Station"},

            {'point': 1, 'city': 'GB-EBO', 'iata_code':  None, 'icao_code':  None, 'lat': 50.769509, 'lon': 0.281412, 'tm': train, 'name': "Eastbourne Centra Stationl"},
            {'point': 1, 'city': 'GB-EBO', 'iata_code':  None, 'icao_code':  None, 'lat': 50.769466, 'lon': 0.281958, 'tm': bus, 'name': "Eastbourne Central Station"},

            {"point": 0, "city": "GB-EOI", "iata_code": "EOI", "icao_code": "EGED", "lat": 59.190556, "lon": -2.772222, "tm": flight, "name": "Eday Airport"},
           # {"point": 1, "city": "GB-EOI", "iata_code": None, "icao_code": None, "lat": 59.155541, "lon": -2.747389, "tm": ferry, "name": "Eday Orkney Terminal"},

            {'point': 0, 'city': 'GB-EDI', 'iata_code': 'EDI', 'icao_code':'EGPH', 'lat': 55.950000, 'lon': -3.372500, 'tm': flight, 'name': "Edinburgh Airport"},
            {'point': 1, 'city': 'GB-EDI', 'iata_code': None, 'icao_code': None, 'lat': 55.952015, 'lon': -3.189984, 'tm': train, 'name': "Edinburgh Waverley"},
            # {'point': 2, 'city': 'GB-EDI', 'iata_code': None, 'icao_code': None, 'lat': 55.945600, 'lon': -3.218278, 'tm': train, 'name': "Edinburgh Haymarket"}, #all trains will pass only through Waverleyy
            {'point': 3, 'city': 'GB-EDI', 'iata_code':  None, 'icao_code': None, 'lat': 55.955399, 'lon': -3.191279, 'tm': bus, 'name': "Edinburgh Bus Station"},


            {"point": 0, "city": "GB-EXE", "iata_code": "EXT", "icao_code": "EGTE", "lat": 50.7344, "lon": -3.41389, "tm": flight, "name": "Exeter Airport"},
            {"point": 1, "city": "GB-EXE", "iata_code": "EXS", "icao_code":   None, "lat": 50.717249, "lon": -3.539229, "tm": train, "name": "Exeter St Thomas Station"},
            {"point": 2, "city": "GB-EXE", "iata_code":  None, "icao_code":   None, "lat": 50.725484, "lon": -3.524478, "tm": bus, "name": "Exeter Coach Station"},
            {"point": 3, "city": "GB-EXE", "iata_code":  None, "icao_code":   None, "lat": 50.725166, "lon": -3.471704, "tm": bus, "name": "Exeter The Barn Owl"},
            {"point": 4, "city": "GB-EXE", "iata_code": None, "icao_code":   None, "lat": 50.726038, "lon": -3.533259, "tm": train, "name": "Exeter Central Station"},
            {"point": 5, "city": "GB-EXE", "iata_code": None, "icao_code":   None, "lat": 50.729381, "lon": -3.543583, "tm": train, "name": "Exeter St Davids Station"},

            {"point": 0, "city": "GB-GLW", "iata_code": "GLA", "icao_code": "EGPF", "lat": 55.871944, "lon": -4.433056, "tm": flight, "name": "Glasgow Airport"},
            {"point": 1, "city": "GB-GLW", "iata_code": None, "icao_code": None, "lat": 55.859136, "lon": -4.258093, "tm": train, "name": "Glasgow Central Station"},
            {"point": 1, "city": "GB-GLW", "iata_code": None, "icao_code": None, "lat": 55.858544, "lon": -4.260079, "tm": bus, "name": "Glasgow Collage"},
            {"point": 2, "city": "GB-GLW", "iata_code": None, "icao_code": None, "lat": 55.862511, "lon": -4.251178, "tm": train, "name": "Glasgow Queen Street"},
            {"point": 3, "city": "GB-GLW", "iata_code": None, "icao_code": None, "lat": 55.865321, "lon": -4.251739, "tm": bus, "name": "Glasgow Buchanan Station"},

            {"point": 1, "city": "GB-GLO", "iata_code": None, "icao_code": None, "lat": 51.865443, "lon": -2.238654, "tm": train, "name": "Gloucester Railway Station"},
            {"point": 1, "city": "GB-GLO", "iata_code": None, "icao_code": None, "lat": 51.865332, "lon": -2.240795, "tm": bus, "name": "Gloucester Bus Station"},
            {"point": 2, "city": "GB-GLO", "iata_code": None, "icao_code": None, "lat":   51.8741, "lon":  -2.21066, "tm": bus, "name": "Gloucester Longlevens"},

            {"point": 0, "city": "GB-PPO", "iata_code": "GCI", "icao_code": "EGJB", "lat": 49.434722, "lon": -2.601944, "tm": flight, "name": "Guernsey Airport"},
           # {"point": 1, "city": "GB-PPO", "iata_code": None, "icao_code":None, "lat": 49.457306, "lon": -2.529014, "tm": ferry, "name": "Guernsey Terminal"},

           {"point": 1, "city": "GB-HDF", "iata_code":  None, "icao_code":   None, "lat": 53.648596, "lon": -1.784731, "tm": train, "name": "Huddersfield Train Station"},
           {"point": 1, "city": "GB-HDF", "iata_code":  None, "icao_code":   None, "lat": 53.645523, "lon": -1.786575, "tm": bus, "name": "Huddersfield Bus Station"},

            {"point": 0, "city": "GB-INV", "iata_code": "INV", "icao_code": "EGPE", "lat": 57.542500, "lon": -4.047500, "tm": flight, "name": "Inverness Airport"},
            {"point": 1, "city": "GB-INV", "iata_code":  None, "icao_code":   None, "lat": 57.479879, "lon": -4.223523, "tm": train, "name": "Inverness Station Square"},
            {"point": 1, "city": "GB-INV", "iata_code":  None, "icao_code":   None, "lat": 57.480771, "lon": -4.225084, "tm": bus, "name": "Inverness Bus Station"},

            {"point": 1, "city": "GB-IPS", "iata_code":  None, "icao_code":   None, "lat": 52.050554, "lon": 1.144962, "tm": train, "name": "Ipswich Train Station"},
            {"point": 2, "city": "GB-IPS", "iata_code":  None, "icao_code":   None, "lat": 52.053282, "lon": 1.150174, "tm": bus, "name": "Ipswich Bus Station"},

            {"point": 0, "city": "GB-ISY", "iata_code": "ILY", "icao_code": "EGPI", "lat": 55.683333, "lon": -6.259722, "tm": flight, "name": "Islay Airport"},
           # {"point": 1, "city": "GB-ISY", "iata_code": None, "icao_code": None, "lat": 55.847713, "lon": -6.105066, "tm": ferry, "name": "Islay Ferry Terminal"},
           # {"point": 2, "city": "GB-ISY", "iata_code": None, "icao_code": None, "lat": 55.627827, "lon": -6.189782, "tm": ferry, "name": "Islay Port Ellen"},

            {"point": 0, "city": "GB-DGL", "iata_code": "IOM", "icao_code": "EGNS", "lat": 54.083333, "lon": -4.6233333, "tm": flight, "name": "Isle of Man Airport"},
            {"point": 1, "city": "GB-DGL", "iata_code": None, "icao_code": None, "lat": 54.147887, "lon": -4.485295, "tm": train, "name": "Isle of Man Douglas Rail Station"},
           # {"point": 2, "city": "GB-DGL", "iata_code": None, "icao_code": None, "lat": 54.148038, "lon": -4.474697, "tm": ferry, "name": "Isle of Man Ferry Terminal"},

            {"point": 0, "city": "GB-TNR", "iata_code": "JER", "icao_code": "EGJJ", "lat": 49.208056, "lon": -2.195278, "tm": flight, "name": "Jersey Airport"},
            {"point": 1, "city": "GB-TNR", "iata_code": None, "icao_code": None, "lat": 49.172935, "lon": -2.109333, "tm": bus, "name": "Jersey Libertybus"},
           # {"point": 2, "city": "GB-TNR", "iata_code": None, "icao_code": None, "lat": 49.178488, "lon": -2.117040, "tm": ferry, "name": "Jersey terminal"},

            {"point": 1, "city": "GB-KUH", "iata_code": None, "icao_code": None, "lat": 53.744253, "lon": -0.346945, "tm": train, "name": "Kingston upon Hull Paragon Interchange"},
            {"point": 1, "city": "GB-KUH", "iata_code": None, "icao_code": None, "lat": 53.744291, "lon": -0.348223, "tm": bus, "name": "Kingston upon Hull City Centre"},
            # {"point": 2, "city": "GB-KUH", "iata_code": None, "icao_code": None, "lat": 53.740867, "lon": -0.281266, "tm": ferry, "name": "Hull Ferry Terminal"},

            {"point": 0, "city": "GB-KWL", "iata_code": "KOI", "icao_code": "EGPA", "lat": 58.958056, "lon": -2.900556, "tm": flight, "name": "Kirkwall Airport"},
            {"point": 1, "city": "GB-KWL", "iata_code": None, "icao_code": None, "lat": 58.984674, "lon": -2.958906, "tm": bus, "name": "Kirkwall Hotel"},
          # {"point": 2, "city": "GB-KWL", "iata_code": None, "icao_code": None, "lat": 58.986470, "lon": -2.960360, "tm": ferry, "name": "Kirkwall Ferry Terminal"},
          # {"point": 3, "city": "GB-KWL", "iata_code": None, "icao_code": None, "lat": 58.985313, "lon": -2.960471, "tm": ferry, "name": "Kirkwall Shapinsay Terminal"},

            {"point": 0, "city": "GB-KMG", "iata_code": "HUY", "icao_code": "EGNJ", "lat": 53.574444, "lon": -0.350833, "tm": flight, "name": "Kirmington Humberside Airport"},
            {"point": 0, "city": "GB-KMG", "iata_code": None, "icao_code": None, "lat": 53.583516, "lon": -0.349980, "tm": bus, "name": "Kirmington Terminal Airport"},

            {"point": 0, "city": "GB-LBA", "iata_code": "LBA", "icao_code": "EGNM", "lat": 53.8661, "lon": -1.66083, "tm": flight, "name": "Leeds Bradford Airport"},
            {"point": 1, "city": "GB-LBA", "iata_code":  None, "icao_code":   None, "lat": 53.794957, "lon": -1.547686, "tm": train, "name": "Leeds New Station"},
            {"point": 2, "city": "GB-LBA", "iata_code":  None, "icao_code":   None, "lat": 53.797526, "lon": -1.536068, "tm": bus, "name": "Leeds Coach Station"},
            {"point": 3, "city": "GB-LBA", "iata_code":  None, "icao_code":   None, "lat": 53.808117, "lon": -1.552308, "tm": bus, "name": "Leeds University"},

            {"point": 1, "city": "GB-LCS", "iata_code": None, "icao_code": None, "lat": 52.631191, "lon": -1.125131, "tm": train, "name": "Leicester Station"},
            {"point": 2, "city": "GB-LCS", "iata_code": None, "icao_code": None, "lat": 52.639576, "lon": -1.133864, "tm": bus, "name": "Leicester St Margaret’s Station"},
            {"point": 3, "city": "GB-LCS", "iata_code": None, "icao_code": None, "lat": 52.614455, "lon": -1.163971, "tm": bus, "name": "Leicester Braunstone (Hand Luggage)"},

            {'point': 0, 'city': 'GB-LIV', 'iata_code': 'LPL', 'icao_code':'EGGP', 'lat': 53.333611, 'lon': -2.849722, 'tm': flight, 'name': "Liverpool Airport"},
            {'point': 1, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.404658, 'lon': -2.980008, 'tm': train, 'name': "Liverpool Central Station"},
            {'point': 2, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.401821, 'lon': -2.987991, 'tm': bus, 'name': "Liverpool Bus Station"}, #make sure this belongs to the code LXC from TVGN
            {'point': 3, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.408231, 'lon': -2.943416, 'tm': bus, 'name': "Liverpool Botanic Place"},
            {'point': 4, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.406118, 'lon': -2.963841, 'tm': bus, 'name': "Liverpool University"},
            {'point': 5, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.407545, 'lon': -2.904749, 'tm': bus, 'name': "Liverpool Edge Lane Drive"},
            {'point': 6, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.410373, 'lon': -2.926322, 'tm': bus, 'name': "Liverpool Edge Lane"},
            {'point': 7, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.485600, 'lon': -2.950090, 'tm': bus, 'name': "Liverpool Old Roan"},
            # {'point': 8, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.407628, 'lon': -2.977312, 'tm': train, 'name': "Liverpool Lime Street Station"},
            # {'point': 9, 'city': 'GB-LIV', 'iata_code':  None, 'icao_code':  None, 'lat': 53.357806, 'lon': -2.889539, 'tm': train, 'name': "Liverpool South Parkway"},

            {'point': 0, 'city': 'GB-LON', 'iata_code': 'LHR', 'icao_code':'EGLL', 'lat': 51.477500, 'lon': -0.461389, 'tm': flight, 'name': "London Heathrow Airport"},
            {'point': 0, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.472169, 'lon': -0.454833, 'tm': train, 'name': "London Heathrow Terminals 2-3 (via Paddington)"},
            {'point': 0, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.471152, 'lon': -0.453475, 'tm': bus, 'name': "London Heathrow Bus Station"},
            {'point': 1, 'city': 'GB-LON', 'iata_code': 'LGW', 'icao_code':'EGKK', 'lat': 51.147222, 'lon': -0.190278, 'tm': flight, 'name': "London Gatwick Airport"},
            {'point': 1, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.156631, 'lon': -0.161159, 'tm': train, 'name': "London Gatwick  (via Reading)"},
            {'point': 1, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.157751, 'lon': -0.161972, 'tm': bus, 'name': "London Gatwick South Terminal"},
            {'point': 2, 'city': 'GB-LON', 'iata_code': 'STN', 'icao_code':'EGSS', 'lat': 51.885000, 'lon': 0.235000, 'tm': flight, 'name': "London Stansted Airport"},
            {'point': 2, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.888716, 'lon': 0.260740, 'tm': train, 'name': "London Stansted Train Station"},
            {'point': 2, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.889363, 'lon': 0.263491, 'tm': bus, 'name': "London Stansted Bus Station"},
            {'point': 3, 'city': 'GB-LON', 'iata_code': 'LTN', 'icao_code':'EGGW', 'lat': 51.874722, 'lon': -0.368333, 'tm': flight, 'name': "London Luton Airport"},
            {'point': 3, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.872454, 'lon': -0.396222, 'tm': train, 'name': "London Luton Train Station"},
            {'point': 3, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.879936, 'lon': -0.376291, 'tm': bus, 'name': "London Luton Bus Station"},
            {'point': 4, 'city': 'GB-LON', 'iata_code': 'LCY', 'icao_code':'EGLC', 'lat': 51.505278, 'lon': 0.055278, 'tm': flight, 'name': "London City Airport"},
            {'point': 5, 'city': 'GB-LON', 'iata_code': 'SEN', 'icao_code':'EGMC', 'lat': 51.570278, 'lon': 0.693333, 'tm': flight, 'name': "London Southend Airport"},
            {'point': 5, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.569672, 'lon': 0.705181, 'tm': train, 'name': "London Southend Airport"},
            {'point': 5, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.570328, 'lon': 0.704605, 'tm': bus, 'name': "London Southend Airport"},
            {'point': 6, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.503167, 'lon': -0.112305, 'tm': train, 'name': "London Waterloo"},
            {'point': 6, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.503527, 'lon': -0.111417, 'tm': bus, 'name': "London Waterloo"},
            {'point': 7, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.495213, 'lon': -0.143898, 'tm': train, 'name': "London Victoria"},
            {'point': 7, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.492483, 'lon': -0.148333, 'tm': bus, 'name': "London Victoria"},
            {'point': 8, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.518763, 'lon': -0.081427, 'tm': train, 'name': "London Liverpool Street"},
            {'point': 8, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.519071, 'lon': -0.079534, 'tm': bus, 'name': "London Liverpool Street (Stop G)"},
            {'point': 9, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.504710, 'lon': -0.085974, 'tm': train, 'name': "London London Bridge"},
            {'point': 10, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.493242, 'lon': -0.199663, 'tm': bus, 'name': "London West Cromwell Road"},
            {'point': 11, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.491659, 'lon': -0.226531, 'tm': bus, 'name': "London Hammersmith"},
            {'point': 12, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.511894, 'lon': -0.158534, 'tm': bus, 'name': "London Marble Arch"},
            {'point': 13, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.571802, 'lon': -0.194738, 'tm': bus, 'name': "London Golders Green"},
            {'point': 14, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.548199, 'lon': -0.180606, 'tm': bus, 'name': "London Finchley Road"},
            {'point': 15, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.523289, 'lon': -0.157973, 'tm': bus, 'name': "London Baker Street Station"},
            {'point': 16, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.514956, 'lon': -0.075113, 'tm': bus, 'name': "London St Botolph St"},
            {'point': 17, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.541167, 'lon': -0.001873, 'tm': bus, 'name': "London Stratford"},
            {'point': 18, 'city': 'GB-LON', 'iata_code': 'QQS', 'icao_code':  None, 'lat': 51.531454, 'lon': -0.126122, 'tm': train, 'name': "London St-Pancras"},
            {'point': 19, 'city': 'GB-LON', 'iata_code': 'QQP', 'icao_code':  None, 'lat': 51.516658, 'lon': -0.176935, 'tm': train, 'name': "London Paddington"},
            {'point': 20, 'city': 'GB-LON', 'iata_code': 'QQU', 'icao_code':  None, 'lat': 51.528071, 'lon': -0.133284, 'tm': train, 'name': "London Euston"},
            {'point': 21, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat':   51.5883, 'lon': -0.059922, 'tm': train, 'name': 'London Tottenham Hale'},
            {'point': 22, 'city': 'GB-LON', 'iata_code':  None, 'icao_code':  None, 'lat': 51.522506, 'lon': -0.163064, 'tm': train, 'name': 'London Marylebone'},

            # {'point': 0, 'city': 'GB-LUT', 'iata_code': 'LTN', 'icao_code': 'EGGW', 'lat': 51.874722, 'lon': -0.368333, 'tm': flight, 'name': "Luton Airport"},
            # {'point': 0, 'city': 'GB-LUT', 'iata_code': None, 'icao_code': None, 'lat': 51.872454, 'lon': -0.396222, 'tm': train, 'name': "Luton Airport Train Station"},
           # {'point': 0, 'city': 'GB-LUT', 'iata_code': None, 'icao_code': None, 'lat': 51.879936, 'lon': -0.376291, 'tm': bus, 'name': " Luton Airport Bus Station"},
            # {'point': 1, 'city': 'GB-LUT', 'iata_code': None, 'icao_code': None, 'lat': 51.882298, 'lon': -0.413699, 'tm': train, 'name': "Luton Station Interchange (Stand 4)"},
            # {'point': 1, 'city': 'GB-LUT', 'iata_code': None, 'icao_code': None, 'lat': 51.882191, 'lon': -0.414784, 'tm': bus, 'name': "Luton Interchange for Town centre"},

            {"point": 0, "city": "GB-LYX", "iata_code": "LYX", "icao_code": "EGMD", "lat": 50.956111, "lon": 0.939167, "tm": flight, "name": "Lydd Airport"},
            {"point": 1, "city": "GB-LYX", "iata_code": None, "icao_code": None, "lat": 50.954071, "lon": 0.912002, "tm": bus, "name": "Lydd Poplar Lane"},

            {'point': 0, 'city': 'GB-MNC', 'iata_code': 'MAN', 'icao_code':'EGCC', 'lat': 53.353889, 'lon': -2.275000, 'tm': flight, 'name': "Manchester Airport"},
            {'point': 0, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.365075, 'lon': -2.272985, 'tm': train, 'name': "Manchester Airport"},
            {'point': 0, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.365677, 'lon': -2.272596, 'tm': bus, 'name': "Manchester Airport"},
            {'point': 1, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.487563, 'lon': -2.242156, 'tm': train, 'name': "Manchester Victoria"},
            {'point': 2, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.477435, 'lon': -2.230945, 'tm': train, 'name': "Manchester Piccadilly"},
            {'point': 2, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.478080, 'lon': -2.237360, 'tm': bus, 'name': "Manchester Coach Station"},
            {'point': 3, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.496166, 'lon': -2.209827, 'tm': bus, 'name': "Manchester Queens Rd"},
            {'point': 4, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.520589, 'lon': -2.166427, 'tm': bus, 'name': "Manchester New Moston"},
            # {'point': 5, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.495211, 'lon': -2.212042, 'tm': bus, 'name': "Manchester Miles Platting"}, #same as Manchester Queens Rd
            {'point': 6, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.477049, 'lon': -2.257511, 'tm': bus, 'name': "Manchester Science Museum"},
            {'point': 7, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.473994, 'lon': -2.242220, 'tm': train, 'name': "Manchester Oxford Road"},
            {'point': 8, 'city': 'GB-MNC', 'iata_code':  None, 'icao_code': None, 'lat': 53.462296, 'lon': -2.290857, 'tm': train, 'name': "Manchester United Football Ground Station"},

            {"point": 0, "city": "GB-MID", "iata_code": "MME", "icao_code": "EGNV", "lat": 54.509167, "lon": -1.429444, "tm": flight, "name": "Durham Tees Valley Airport"},
            {"point": 0, "city": "GB-MID", "iata_code":  None, "icao_code":   None, "lat": 54.518612, "lon": -1.425292, "tm": train, "name": "Teesside Airport"},
            {"point": 1, "city": "GB-MID", "iata_code":  None, "icao_code":   None, "lat": 54.579363, "lon": -1.234458, "tm": train, "name": "Middlesbrough Train Station"},
            {"point": 2, "city": "GB-MID", "iata_code":  None, "icao_code":   None, "lat": 54.576045, "lon": -1.239505, "tm": bus, "name": "Middlesbrough Coach Station"},

           {"point": 1, "city": "GB-MIK", "iata_code": None, "icao_code": None, "lat": 52.034292, "lon": -0.773563, "tm": train, "name": "Milton Keynes Central Station"},
           {"point": 1, "city": "GB-MIK", "iata_code": None, "icao_code": None, "lat": 52.034984, "lon": -0.774363, "tm": bus, "name": "Milton Keynes Central Station"},
           {"point": 2, "city": "GB-MIK", "iata_code": None, "icao_code": None, "lat": 52.042284, "lon": -0.755282, "tm": bus, "name": "Milton Keynes The Point"},

            {"point": 0, "city": "GB-NCL", "iata_code": "NCL", "icao_code": "EGNT", "lat": 55.038056, "lon": -1.689722, "tm": flight, "name": "Newcastle Airport"},
            {"point": 1, "city": "GB-NCL", "iata_code":  None, "icao_code":   None, "lat": 54.968574, "lon": -1.617065, "tm": train, "name": "Newcastle Central Station"},
            {"point": 2, "city": "GB-NCL", "iata_code":  None, "icao_code":   None, "lat": 54.967519, "lon": -1.622628, "tm": bus, "name": "Newcastle Coach Station"},

            {"point": 0, "city": "GB-NQY", "iata_code": "NQY", "icao_code": "EGHQ", "lat": 50.440833, "lon": -4.995278, "tm": flight, "name": "Newquay Cornwall Airport"},
            {"point": 1, "city": "GB-NQY", "iata_code":  None, "icao_code":   None, "lat": 50.415112, "lon": -5.075754, "tm": train, "name": "Newquay Train Station"},
            {"point": 2, "city": "GB-NQY", "iata_code":  None, "icao_code":   None, "lat": 50.413043, "lon": -5.085607, "tm": bus, "name": "Newquay Coach Station"},
            {"point": 3, "city": "GB-NQY", "iata_code":  None, "icao_code":   None, "lat": 50.418487, "lon": -5.057978, "tm": bus, "name": "Newquay Porth"},

            {"point": 0, "city": "GB-NRO", "iata_code": "NRL", "icao_code": "EGEN", "lat": 59.367500, "lon": -2.434444, "tm": flight, "name": "North Ronaldsay Airport"},

            {"point": 1, "city": "GB-NHP", "iata_code":  None, "icao_code":   None, "lat": 52.237544, "lon": -0.906637, "tm": train, "name": "Northampton Black Lion Hill"},
            {"point": 1, "city": "GB-NHP", "iata_code":  None, "icao_code":   None, "lat": 52.240912, "lon": -0.895110, "tm": bus, "name": "Northampton Town Centre"},


            {"point": 0, "city": "GB-NRW", "iata_code": "NWI", "icao_code": "EGSH", "lat": 52.675800, "lon": 1.282780, "tm": flight, "name": "Norwich Airport"},
            {'point': 1, 'city': 'GB-NRW', 'iata_code':  None, 'icao_code': None, 'lat': 52.626864, 'lon': 1.306784, 'tm': train, 'name': "Norwich Station Approach"},
            {'point': 1, 'city': 'GB-NRW', 'iata_code':  None, 'icao_code': None, 'lat': 52.624258, 'lon': 1.292897, 'tm': bus, 'name': "Norwich Bus Station"},
            {'point': 2, 'city': 'GB-NRW', 'iata_code':  None, 'icao_code': None, 'lat': 52.621707, 'lon': 1.236632, 'tm': bus, 'name': "Norwich University of East Anglia"},

            {'point': 0, 'city': 'GB-NTG', 'iata_code': 'EMA', 'icao_code':'EGNX', 'lat': 52.831111, 'lon': -1.327778, 'tm': flight, 'name': "East Midlands Airport"},
            {'point': 0, 'city': 'GB-NTG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.826338, 'lon': -1.328130, 'tm': bus, 'name': "Nottingham East Midlands Airport"},
            {'point': 2, 'city': 'GB-NTG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.947142, 'lon': -1.146730, 'tm': train, 'name': "Nottingham Station Street"},
            {'point': 2, 'city': 'GB-NTG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.949154, 'lon': -1.147070, 'tm': bus, 'name': "Nottingham Coach Station"},
            {'point': 3, 'city': 'GB-NTG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.981331, 'lon': -1.146172, 'tm': bus, 'name': "Nottingham North"},
            {'point': 4, 'city': 'GB-NTG', 'iata_code':  None, 'icao_code':  None, 'lat': 52.944285, 'lon': -1.191932, 'tm': bus, 'name': "Nottingham University"},

            {"point": 0, "city": "GB-OBA", "iata_code": "OBN", "icao_code": "EGEO", "lat": 56.463611, "lon": -5.40000, "tm": flight, "name": "Oban Airport"},
            {"point": 1, "city": "GB-OBA", "iata_code": None, "icao_code": None, "lat": 56.412517, "lon": -5.473964, "tm": train, "name": "Oban Train Station"},
            {"point": 1, "city": "GB-OBA", "iata_code": None, "icao_code": None, "lat": 56.412512, "lon": -5.473204, "tm": bus, "name": "Oban Station Road Stance 3"},
           # {"point": 2, "city": "GB-OBA", "iata_code": None, "icao_code": None, "lat": 56.412242, "lon": -5.476005, "tm": ferry, "name": "Oban Ferry Terminal"},

            {'point': 1, 'city': 'GB-OXF', 'iata_code':  None, 'icao_code':  None, 'lat': 51.753364, 'lon': -1.269505, 'tm': train, 'name': "Oxford Train Station"},
            {'point': 1, 'city': 'GB-OXF', 'iata_code':  None, 'icao_code':  None, 'lat': 51.753801, 'lon': -1.262529, 'tm': bus, 'name': "Oxford Bus Station"},
            {'point': 2, 'city': 'GB-OXF', 'iata_code':  None, 'icao_code':  None, 'lat': 51.755766, 'lon': -1.259623, 'tm': bus, 'name': "Oxford Saint Giles"},
            {'point': 3, 'city': 'GB-OXF', 'iata_code':  None, 'icao_code':  None, 'lat': 51.752730, 'lon': -1.250689, 'tm': bus, 'name': "Oxford Queens Lane"},
            {'point': 4, 'city': 'GB-OXF', 'iata_code':  None, 'icao_code':  None, 'lat': 51.750474, 'lon': -1.240858, 'tm': bus, 'name': "Oxford St Clements"},

            {"point": 0, "city": "GB-PPW", "iata_code": "PPW", "icao_code": "EGEP", "lat": 59.351667, "lon": -2.900278, "tm": flight, "name": "Papa Westray Airport"},
            # {"point": 1, "city": "GB-PPW", "iata_code": None, "icao_code": None, "lat": 59.326896, "lon": -2.891585, "tm": ferry, "name": "Papa Westray Orkney"},

            {'point': 1, 'city': 'GB-PET', 'iata_code':  None, 'icao_code':  None, 'lat': 52.574447, 'lon': -2.249788, 'tm': train, 'name': "Peterborough Train Station"},
            {'point': 1, 'city': 'GB-PET', 'iata_code':  None, 'icao_code':  None, 'lat': 52.574490, 'lon': -2.246447, 'tm': bus, 'name': "Peterborough Bus Station"},

            {"point": 1, "city": "GB-PLY", "iata_code":  None, "icao_code":   None, "lat": 50.377773, "lon": -4.143106, "tm": train, "name": "Plymouth Train Station"},
            {"point": 2, "city": "GB-PLY", "iata_code":  None, "icao_code":   None, "lat": 50.372895, "lon": -4.143553, "tm": bus, "name": "Plymouth Coach Station"},
           # {"point": 3, "city": "GB-PLY", "iata_code":  None, "icao_code":   None, "lat": 50.364750, "lon": -4.158613, "tm": ferry, "name": "Plymouth Ferry Terminal"},

            {"point": 1, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.798517, "lon": -1.090675, "tm": train, "name": "Portsmouth and Southsea Station"},
            {"point": 2, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.796941, "lon": -1.107831, "tm": train, "name": "Portsmouth Harbour Train Station"},
            # {"point": 2, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.796888, "lon": -1.108335, "tm": bus, "name": "Portsmouth Harbour Bus Station"}, #same as The Hard
           # {"point": 2, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.797059, "lon": -1.109208, "tm": ferry, "name": "Portsmouth Harbour Station Pier"},
            {"point": 3, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.797458, "lon": -1.106167, "tm": bus, "name": "Portsmouth The Hard"},
            {"point": 4, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.810729, "lon": -1.086690, "tm": bus, "name": "Portsmouth International Port Station"},
           # {"point": 4, "city": "GB-PME", "iata_code":  None, "icao_code":  None, "lat": 50.812084, "lon": -1.088574, "tm": ferry, "name": "Portsmouth International Port Terminal"},

            {"point": 1, "city": "GB-PRE", "iata_code":  None, "icao_code":   None, "lat": 53.755394, "lon": -2.707134, "tm": train, "name": "Preston Train Station"},
            {"point": 2, "city": "GB-PRE", "iata_code":  None, "icao_code":   None, "lat": 53.761400, "lon": -2.696598, "tm": bus, "name": "Preston Lancashire Station"},

            {"point": 1, "city": "GB-RDN", "iata_code":  None, "icao_code":  None, "lat": 51.458433, "lon": -0.971479, "tm": train, "name": "Reading Station Approach"},
            {"point": 2, "city": "GB-RDN", "iata_code":  None, "icao_code":  None, "lat": 51.460522, "lon": -0.971374, "tm": bus, "name": "Reading Station North Interchange"},
            {"point": 3, "city": "GB-RDN", "iata_code":  None, "icao_code":  None, "lat": 51.455514, "lon": -0.990095, "tm": train, "name": "Reading West"},
            {"point": 4, "city": "GB-RDN", "iata_code":  None, "icao_code":  None, "lat":   51.4419, "lon":  -1.06102, "tm": bus, "name": "Reading Calcot Coachway"},
            {"point": 5, "city": "GB-RDN", "iata_code":  None, "icao_code":  None, "lat":   51.4061, "lon":  -0.980262, "tm": bus, "name": "Reading Main Coach Stops"},

            # {"point": 1, "city": "GB-RTH", "iata_code":  None, "icao_code":  None, "lat": 53.432317, "lon": -1.360448, "tm": train, "name": "Rotherham Central Station"},
            # {"point": 2, "city": "GB-RTH", "iata_code":  None, "icao_code":  None, "lat": 53.433637, "lon": -1.346655, "tm": bus, "name": "Rotherham Interchange"},

            {"point": 0, "city": "GB-SJU", "iata_code": "LEQ", "icao_code": "EGHC", "lat": 50.102778, "lon": -5.670556, "tm": flight, "name": "Land's End Airport"},
            {"point": 1, "city": "GB-SJU", "iata_code": None, "icao_code": None, "lat": 50.126190, "lon": -5.681557, "tm": bus, "name": "Saint Just Top Nancherrow Hill"},

            {"point": 0, "city": "GB-NDY", "iata_code": "NDY", "icao_code": "EGES", "lat": 59.250278, "lon": -2.576667, "tm": flight, "name": "Sanday Airport"},
           # {"point": 1, "city": "GB-NDY", "iata_code": None, "icao_code": None, "lat": 59.250278, "lon": -2.576667, "tm": ferry, "name": "Sanday Orkney Ferry Terminal"},

            {"point": 1, "city": "GB-SHE", "iata_code":  None, "icao_code":  None, "lat": 53.378240, "lon": -1.462137, "tm": train, "name": "Sheffield Train Station"},
            {"point": 1, "city": "GB-SHE", "iata_code":  None, "icao_code":  None, "lat": 53.380304, "lon": -1.463753, "tm": bus, "name": "Sheffield Interchange"},
            {"point": 2, "city": "GB-SHE", "iata_code":  None, "icao_code":  None, "lat": 53.416415, "lon": -1.412879, "tm": bus, "name": "Sheffield Meadowhall Interchange"},

            {"point": 0, "city": "GB-TLD", "iata_code": "LSI", "icao_code": "EGPB", "lat": 59.881389, "lon": -1.293889, "tm": flight, "name": "Sumburgh Shetland Airport"},
            {"point": 1, "city": "GB-TLD", "iata_code": "LWK", "icao_code": "EGET", "lat": 60.191944, "lon": -1.243611, "tm": flight, "name": "Tingwall Shetland Airport"},
            # {"point": 2, "city": "GB-TLD", "iata_code": None, "icao_code": None, "lat": 60.191944, "lon": -1.243611, "tm": ferry, "name": "Shetland Lerwick Terminal"},

            # {"point": 1, "city": "GB-SLO", "iata_code":  None, "icao_code":   None, "lat": 51.511919, "lon": -0.591440, "tm": train, "name": "Slough Brunelway Station"}, #Slough inside London
            # {"point": 1, "city": "GB-SLO", "iata_code":  None, "icao_code":   None, "lat": 51.510895, "lon": -0.593340, "tm": bus, "name": "Slough Brunel Station"},

            {"point": 0, "city": "GB-SOU", "iata_code": "SOU", "icao_code":"EGHI", "lat": 50.950278, "lon": -1.356667, "tm": flight, "name": "Southampton Airport"},
            {'point': 0, 'city': 'GB-SOU', 'iata_code':  None, 'icao_code':  None, 'lat': 50.950841, 'lon': -1.363161, 'tm': train, 'name': "Southampton Airport Parkway"},
            {'point': 1, 'city': 'GB-SOU', 'iata_code':  None, 'icao_code':  None, 'lat': 50.907259, 'lon': -1.413355, 'tm': train, 'name': "Southampton Central Station"},
            {'point': 1, 'city': 'GB-SOU', 'iata_code':  None, 'icao_code':  None, 'lat': 50.906087, 'lon': -1.408929, 'tm': bus, 'name': "Southampton Coach Station"},
            {'point': 2, 'city': 'GB-SOU', 'iata_code':  None, 'icao_code':  None, 'lat': 50.936241, 'lon': -1.396882, 'tm': bus, 'name': "Southampton Uni Interchange"},

            # {"point": 1, "city": "GB-SAA", "iata_code":  None, "icao_code":   None, "lat": 51.537133, "lon": 0.711721, "tm": train, "name": "Southend-on-Sea Central Station"}, #considered inside London for the moment
            # {"point": 1, "city": "GB-SAA", "iata_code":  None, "icao_code":   None, "lat": 51.536376, "lon": 0.714726, "tm": bus, "name": "Southend-on-Sea Bus Station"},
            # {"point": 2, "city": "GB-SAA", "iata_code":  None, "icao_code":   None, "lat": 51.541541, "lon": 0.711532, "tm": train, "name": "Southend-on-Sea Victoria Station"},
            # {"point": 3, "city": "GB-SAA", "iata_code":  None, "icao_code":   None, "lat": 51.539004, "lon": 0.731816, "tm": train, "name": "Southend-on-Sea Est"},
            # {"point": 4, "city": "GB-SAA", "iata_code":  None, "icao_code":   None, "lat": 51.543611, "lon": 0.693065, "tm": bus, "name": "Southend-on-Sea Westcliff-on-Sea"},

            {"point": 0, "city": "GB-SVZ", "iata_code": "ISC", "icao_code": "EGHE", "lat": 49.913333, "lon": -6.291667, "tm": flight, "name": "St Mary's Airport (Isles of Scilly)"},
            # {"point": 1, "city": "GB-SVZ", "iata_code": None, "icao_code": None, "lat": 49.918494, "lon": -6.316599, "tm": ferry, "name": "St Mary's Ferry Terminal (Isles of Scilly)"},

            # {"point": 1, "city": "GB-STK", "iata_code":  None, "icao_code":   None, "lat": 53.405801, "lon": -2162444, "tm": train, "name": "Stockport Grand Central Way"}, #inside Manchester
            # {"point": 1, "city": "GB-STK", "iata_code":  None, "icao_code":   None, "lat": 53.408622, "lon": -2162631, "tm": bus, "name": "Stockport Bus Station"},

            {"point": 1, "city": "GB-SOT", "iata_code":  None, "icao_code":   None, "lat": 53.008038, "lon": -2.180914, "tm": train, "name": "Stoke on Trent Station Road"},
            {"point": 1, "city": "GB-SOT", "iata_code":  None, "icao_code":   None, "lat": 53.009938, "lon": -2.181378, "tm": bus, "name": "Stoke on Trent Staffordshire University"},
            {"point": 2, "city": "GB-SOT", "iata_code":  None, "icao_code":   None, "lat": 53.022566, "lon": -2.174414, "tm": bus, "name": "Stoke on Trent Hanley"},

            {"point": 0, "city": "GB-STO", "iata_code": "SYY", "icao_code": "EGPO", "lat": 58.215556, "lon": -6.331111, "tm": flight, "name": "Stornoway Airport"},
            {"point": 1, "city": "GB-STO", "iata_code": None, "icao_code": None, "lat": 58.207740, "lon": -6.386855, "tm": bus, "name": "Stornoway Bus Station"},
            # {"point": 2, "city": "GB-STO", "iata_code": None, "icao_code": None, "lat": 58.206159, "lon": -6.387187, "tm": ferry, "name": "Stornoway Lewis Ferry Terminal"},

            {"point": 0, "city": "GB-SOY", "iata_code": "SOY", "icao_code": "EGER", "lat": 59.155278, "lon": -2.641389, "tm": flight, "name": "Stronsay Airport"},
            # {"point": 1, "city": "GB-SOY", "iata_code": None, "icao_code": None, "lat": 59.142637, "lon": -2.597920, "tm": ferry, "name": "Stronsay Orlney Ferrt Terminal"},

            {"point": 1, "city": "GB-SUN", "iata_code":  None, "icao_code":   None, "lat": 54.905537, "lon": -1.382360, "tm": train, "name": "Sunderland Tayn and Wear"},
            {"point": 1, "city": "GB-SUN", "iata_code":  None, "icao_code":   None, "lat": 54.902237, "lon": -1.384968, "tm": bus, "name": "Sunderland Interchange"},

            # {"point": 1, "city": "GB-SUC", "iata_code":  None, "icao_code":   None, "lat": 52.564992, "lon": -1.824889, "tm": train, "name": "Sutton Coldfield Station Street"}, #inside Birmingham
            # {"point": 2, "city": "GB-SUC", "iata_code":  None, "icao_code":   None, "lat": 52.566369, "lon": -1.813803, "tm": bus, "name": "Sutton Coldfield Good Hope Hospital"},

            {"point": 1, "city": "GB-SWA", "iata_code":  None, "icao_code":   None, "lat": 51.625265, "lon": -3.940949, "tm": train, "name": "Swansea High Street"},
            {"point": 2, "city": "GB-SWA", "iata_code":  None, "icao_code":   None, "lat": 51.617148, "lon": -3.946173, "tm": bus, "name": "Swansea Bus Station"},

            {"point": 1, "city": "GB-SNN", "iata_code":  None, "icao_code":   None, "lat": 51.565802, "lon": -1.784682, "tm": train, "name": "Swindon Station Road"},
            {"point": 1, "city": "GB-SNN", "iata_code":  None, "icao_code":   None, "lat": 51.564108, "lon": -1.783330, "tm": bus, "name": "Swindon New Bridge Square"},
            {"point": 2, "city": "GB-SNN", "iata_code":  None, "icao_code":   None, "lat": 51.559268, "lon": -1.762712, "tm": bus, "name": "Swindon Sussex Square"},
            {"point": 3, "city": "GB-SNN", "iata_code":  None, "icao_code":   None, "lat": 51.544987, "lon": -1.742802, "tm": bus, "name": "Swindon Coate Water"},
            {"point": 4, "city": "GB-SNN", "iata_code":  None, "icao_code":   None, "lat": 51.5778  , "lon": -1.72956 , "tm": bus, "name": "Swindon Stratton"},

            {"point": 1, "city": "GB-TEF", "iata_code":  None, "icao_code":   None, "lat": 52.681202, "lon": -2.441003, "tm": train, "name": "Telford Central Railway Station"},
            {"point": 2, "city": "GB-TEF", "iata_code":  None, "icao_code":   None, "lat": 52.675922, "lon": -2.448195, "tm": bus, "name": "Telford Town Centre"},

            {"point": 0, "city": "GB-TRE", "iata_code": "TRE", "icao_code": "EGPU", "lat": 56.499167, "lon": -6.869167, "tm": flight, "name": "Tiree Airport"},
             # {"point": 1, "city": "GB-TRE", "iata_code": None, "icao_code": None, "lat": 56.508312, "lon": -6.798890, "tm": ferry, "name": "Tiree Ferry Terminal"},

            # {"point": 1, "city": "GB-WAL", "iata_code":  None, "icao_code":   None, "lat": 52.584259, "lon": -1.985531, "tm": train, "name": "Walsall Saddlers Centre"},  #inside Birmingham
            # {"point": 2, "city": "GB-WAL", "iata_code":  None, "icao_code":   None, "lat": 52.586737, "lon": -1.981522, "tm": bus, "name": "Walsall Hatherton"},

            # {"point": 1, "city": "GB-WAF", "iata_code":  None, "icao_code":   None, "lat": 51.663721, "lon": -0.396456, "tm": train, "name": "Watford Junction Train Station"}, #considered inside London
            # {"point": 1, "city": "GB-WAF", "iata_code":  None, "icao_code":   None, "lat": 51.663578, "lon": -0.396568, "tm": bus, "name": "Watford Junction Bus Station"},

            {"point": 0, "city": "GB-WRY", "iata_code": "WRY", "icao_code": "EGEW", "lat": 59.350278, "lon": -2.950000, "tm": flight, "name": "Westray Airport"},
            # {"point": 1, "city": "GB-WRY", "iata_code": None, "icao_code": None, "lat": 59.323698, "lon": -2.973979, "tm": ferry, "name": "Westray Pierowall"},
            # {"point": 2, "city": "GB-WRY", "iata_code": None, "icao_code": None, "lat": 59.248847, "lon": -2.859647, "tm": ferry, "name": "Westray Rapness"},

            {"point": 0, "city": "GB-WIC", "iata_code": "WIC", "icao_code": "EGPC", "lat": 58.458889, "lon": -3.093056, "tm": flight, "name": "Wick Airport"},
            {"point": 1, "city": "GB-WIC", "iata_code": None, "icao_code": None, "lat": 58.458889, "lon": -3.093056, "tm": train, "name": "Wick Bankhead"},

            # {"point": 1, "city": "GB-WOV", "iata_code":  None, "icao_code":   None, "lat": 52.587580, "lon": -2.120140, "tm": train, "name": "Wolverhampton Railway Drive"}, #inside Birmingham
            # {"point": 2, "city": "GB-WOV", "iata_code":  None, "icao_code":   None, "lat": 52.585450, "lon": -2.122536, "tm": bus, "name": "Wolverhampton Railway Drive"},

            {"point": 1, "city": "GB-YRK", "iata_code":  None, "icao_code":   None, "lat": 53.957985, "lon": -1.093193, "tm": train, "name": "York Train Station Rd"},
            {"point": 1, "city": "GB-YRK", "iata_code":  None, "icao_code":   None, "lat": 53.958129, "lon": -1.092134, "tm": bus, "name": "York Bus Station Rd"},
        ]

        hubs_IE = [
            {"point": 0, "city": "IE-ORK", "iata_code": "ORK", "icao_code": "EICK", "lat": 51.841389, "lon": -8.491111, "tm": flight, "name": "Cork Airport"},
            {"point": 0, "city": "IE-ORK", "iata_code":  None, "icao_code":   None, "lat": 51.848990, "lon": -8.489091, "tm": bus, "name": "Cork Airport"},
            {"point": 1, "city": "IE-ORK", "iata_code":  None, "icao_code":   None, "lat": 51.901885, "lon": -8.458027, "tm": train, "name": "Cork Kent"},
            {"point": 2, "city": "IE-ORK", "iata_code":  None, "icao_code":   None, "lat": 51.899676, "lon": -8.466500, "tm": train, "name": "Cork Parnell Place"},
            {"point": 3, "city": "IE-ORK", "iata_code":  None, "icao_code":   None, "lat":   51.9008, "lon":  -8.46805, "tm": bus, "name": "Cork St Patrick's Quay"},

            {"point": 0, "city": "IE-CFN", "iata_code": "CFN", "icao_code": "EIDL", "lat": 55.044167, "lon": -8.341111, "tm": flight, "name": "Donegal Airport"},
            {"point": 1, "city": "IE-CFN", "iata_code":  None, "icao_code":   None, "lat": 54.653620, "lon": -8.110742, "tm": bus, "name": "Donegal Abbey Hotel"},

            {'point': 0, 'city': 'IE-DUB', 'iata_code': 'DUB', 'icao_code':'EIDW', 'lat': 53.426449, 'lon': -6.249912, 'tm': flight, 'name': "Dublin Airport"},
            {'point': 0, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.428060, 'lon': -6.244079, 'tm': bus, 'name': "Dublin Airport"},
            {'point':10, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.429444, 'lon': -6.230202, 'tm': bus, 'name': "Dublin Airport Roundabout"},
            {'point': 1, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.351396, 'lon': -6.249556, 'tm': train, 'name': "Dublin Connolly"},
            {'point': 2, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.346361, 'lon': -6.294136, 'tm': train, 'name': "Dublin Heuston"},
            {'point': 3, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.343350, 'lon': -6.248042, 'tm': train, 'name': "Dublin Pearse"},
            {'point': 4, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.349942, 'lon': -6.252043, 'tm': bus, 'name': "Dublin Busáras"},
            {'point': 5, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.334100, 'lon': -6.286360, 'tm': bus, 'name': "Dublin Burgh Quay"},
            {'point': 6, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.3558  , 'lon': -6.39194 , 'tm': bus, 'name': "Dublin Liffey Valley, Kings Hospital"},
           # {'point': 15, 'city': 'IE-DUB', 'iata_code':  None, 'icao_code':  None, 'lat': 53.345133 'lon': -6.196183, 'tm': ferrys, 'name': "Dublin Ferry Terminal 1"},
            # {'point':10, 'city': 'IE-DUB', 'iata_code': None, 'icao_code': None, 'lat': 53.429444, 'lon': -6.230202, 'tm': bus, 'name': "Dublin Airport Roundabout Station"}, #already next to airport

            {"point": 0, "city": "IE-GWY", "iata_code": "NNR", "icao_code": "EICA", "lat": 53.230556, "lon": -9.467778, "tm": flight, "name": "Connemara Airport"},
            {"point": 1, "city": "IE-GWY", "iata_code": None, "icao_code": None, "lat": 53.273543, "lon": -9.047022, "tm": train, "name": "Galway Céannt"},
            {"point": 1, "city": "IE-GWY", "iata_code": None, "icao_code": None, "lat": 53.273662, "lon": -9.046151, "tm": bus, "name": "Galway Ayre Square"},

            {"point": 0, "city": "IE-INQ", "iata_code": "INQ", "icao_code": "EIIR", "lat": 53.064444, "lon": -9.511111, "tm": flight, "name": "Inisheer Aerodrome"},
            # {"point": 1, "city": "IE-INQ", "iata_code": None, "icao_code": None, "lat": 53.068322, "lon": -9.522680, "tm": ferry, "name": "Inisheer Ferry Terminal"},

            {"point": 0, "city": "IE-IIA", "iata_code": "IIA", "icao_code": "EIMN", "lat": 53.091944, "lon": -9.570000, "tm": flight, "name": "Inishmaan Aerodrome"},
            # {"point": 1, "city": "IE-IIA", "iata_code": None, "icao_code": None, "lat": 53.102180, "lon": -9.579524, "tm": ferry, "name": "Inishmaan Ferry Terminal"},

            {"point": 0, "city": "IE-IOR", "iata_code": "IOR", "icao_code": "EIIM", "lat": 53.106944, "lon": -9.653889, "tm": flight, "name": "Inishmore Aerodrome"},
            # {"point": 1, "city": "IE-IOR", "iata_code": None, "icao_code": None, "lat": 53.118206, "lon": -9.666887, "tm": ferry, "name": "Inishmore Ferry Terminal"},

            {"point": 0, "city": "IE-KLY", "iata_code": "KIR", "icao_code": "EIKY", "lat": 52.180833, "lon": -9.523889, "tm": flight, "name": "Kerry Airport"},
            {"point": 1, "city": "IE-KLY", "iata_code": None, "icao_code": None, "lat": 52.059210, "lon": -9.502152, "tm": train, "name": "Killarney An Ascaill Thoir"},
            {"point": 1, "city": "IE-KLY", "iata_code": None, "icao_code": None, "lat": 52.059818, "lon": -9.501917, "tm": bus, "name": "Killarney Ardshanavooly"},

            {"point": 0, "city": "IE-NOC", "iata_code": "NOC", "icao_code": "EIKN", "lat": 53.910278, "lon": -8.818611, "tm": flight, "name": "Ireland West Airport Knock"},
            {"point": 0, "city": "IE-NOC", "iata_code": None, "icao_code": None, "lat": 53.914084, "lon": -8.812642, "tm": bus, "name": "Knock Luga Airport"},
            {"point": 1, "city": "IE-NOC", "iata_code": None, "icao_code": None, "lat": 53.794431, "lon": -8.918924, "tm": bus, "name": "Knock St Anne’s"},

            {"point": 0, "city": "IE-SNN", "iata_code": "SNN", "icao_code": "EINN", "lat": 52.701944, "lon": -8.924722, "tm": flight, "name": "Shannon Airport"},
            {"point": 0, "city": "IE-SNN", "iata_code": None, "icao_code": None, "lat": 52.691949, "lon": -8.918657, "tm": bus, "name": "Shannon Airport"},
            {"point": 1, "city": "IE-SNN", "iata_code": None, "icao_code": None, "lat": 52.704481, "lon": -8.897058, "tm": bus, "name": "Shannon In Est"}, # És s’única estació que té dos buses...
        ]

        hubs_FI = [
            {"point": 0, "city": "FI-ENF", "iata_code": "ENF", "icao_code": "EFET", "lat": 68.364444, "lon": 23.427500, "tm": flight, "name": "Enontekiö Airport"},
            {"point": 1, "city": "FI-ENF", "iata_code": None, "icao_code": None, "lat": 68.385524, "lon": 23.643719, "tm": bus, "name": "Enontekiö Station"},

            {"point": 0, "city": "FI-HEL", "iata_code": "HEL", "icao_code": "EFHK", "lat": 60.317222, "lon": 24.963333, "tm": flight, "name": "Helsinki-Vantaa Airport"},
            {"point": 0, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.315144, "lon": 24.971430, "tm": bus, "name": "Helsinki-Vantaa T1 Airport"},
            {"point": 1, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.171881, "lon": 24.941433, "tm": train, "name": "Helsinki Central Station"},
            {"point": 2, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.169793, "lon": 24.933723, "tm": bus, "name": "Helsinki Kamppi"},
            # {"point": 3, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.160822, "lon": 24.958785, "tm": ferry, "name": "Helsinki Olympia Terminaali"},
            {"point": 3, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.160301, "lon": 24.959074, "tm": bus, "name": "Helsinki Olympiaterminaali"},
            # {"point": 4, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.154379, "lon": 24.921138, "tm": ferry, "name": "Helsinki Länsisatama"},
            # {"point": 5, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.163815, "lon": 24.968543, "tm": ferry, "name": "Helsinki Katajanokan"},
            # {"point": 6, "city": "FI-HEL", "iata_code": None, "icao_code": None, "lat": 60.161730, "lon": 24.957626, "tm": ferry, "name": "Helsinki Hansaterminal-Vuosaaren Satama"},

            {"point": 0, "city": "FI-IVL", "iata_code": "IVL", "icao_code": "EFIV", "lat": 68.610833, "lon": 27.413889, "tm": flight, "name": "Ivalo Airport"},
            {"point": 0, "city": "FI-IVL", "iata_code": None, "icao_code": None, "lat": 68.608273, "lon": 27.420529, "tm": bus, "name": "Ivalo Airport"},

            {"point": 0, "city": "FI-JOE", "iata_code": "JOE", "icao_code": "EFJO", "lat": 62.658889, "lon": 29.624444, "tm": flight, "name": "Joensuu Airport"},
            {"point": 1, "city": "FI-JOE", "iata_code": None, "icao_code": None, "lat": 62.599763, "lon": 29.776341, "tm": train, "name": "Joensuu Station"},

            {"point": 0, "city": "FI-JYV", "iata_code": "JYV", "icao_code": "EFJY", "lat": 62.400833, "lon": 25.672778, "tm": flight, "name": "Jyväskylä Airport"},
            {"point": 1, "city": "FI-JYV", "iata_code": None, "icao_code": None, "lat": 62.241841, "lon": 25.754928, "tm": train, "name": "Jyväskylä Central Station"},
            {"point": 1, "city": "FI-JYV", "iata_code": None, "icao_code": None, "lat": 62.241792, "lon": 25.755034, "tm": bus, "name": "Jyväskylä Central Station"},

            {"point": 0, "city": "FI-KAJ", "iata_code": "KAJ", "icao_code": "EFKI", "lat": 64.284167, "lon": 27.687500, "tm": flight, "name": "Kajaani Airport"},
            {"point": 1, "city": "FI-KAJ", "iata_code": None, "icao_code": None, "lat": 64.219964, "lon": 27.738515, "tm": train, "name": "Kajaani Train Station"},
            {"point": 2, "city": "FI-KAJ", "iata_code": None, "icao_code": None, "lat": 64.222034, "lon": 27.729485, "tm": bus, "name": "Kajaani Bus Station"},

            {"point": 0, "city": "FI-KEM", "iata_code": "KEM", "icao_code": "EFKE", "lat": 65.779167, "lon": 24.584722, "tm": flight, "name": "Kemi-Tornio Airport"},
            {"point": 1, "city": "FI-KEM", "iata_code": None, "icao_code": None, "lat": 65.736334, "lon": 24.572048, "tm": train, "name": "Kemi Train Station"},
            {"point": 1, "city": "FI-KEM", "iata_code": None, "icao_code": None, "lat": 65.736750, "lon": 24.569768, "tm": bus, "name": "Kemi Bus Station"},

            {"point": 0, "city": "FI-KTT", "iata_code": "KTT", "icao_code": "EFKT", "lat": 67.698611, "lon": 24.848056, "tm": flight, "name": "Kittilä Airport"},
            {"point": 1, "city": "FI-KTT", "iata_code": None, "icao_code": None, "lat": 67.659781, "lon": 24.905693, "tm": bus, "name": "Kittilä Station"},

            {"point": 0, "city": "FI-KOK", "iata_code": "KOK", "icao_code": "EFKK", "lat": 63.720278, "lon": 23.139167, "tm": flight, "name": "Kokkola-Pietarsaari Airport"},
            {"point": 1, "city": "FI-KOK", "iata_code": None, "icao_code": None, "lat": 63.835018, "lon": 23.131425, "tm": train, "name": "Kokkola Train Station"},
            {"point": 1, "city": "FI-KOK", "iata_code": None, "icao_code": None, "lat": 63.835570, "lon": 23.128047, "tm": bus, "name": "Kokkola Bus Station"},

            {"point": 0, "city": "FI-KUO", "iata_code": "KUO", "icao_code": "EFKU", "lat": 63.008611, "lon": 27.794444, "tm": flight, "name": "Kuopio Airport"},
            {"point": 1, "city": "FI-KUO", "iata_code": None, "icao_code": None, "lat": 62.896745, "lon": 27.681852, "tm": train, "name": "Kuopio Train Station"},
            {"point": 1, "city": "FI-KUO", "iata_code": None, "icao_code": None, "lat": 62.898400, "lon": 27.679644, "tm": bus, "name": "Kuopio Bus Station"},

            {"point": 0, "city": "FI-KAO", "iata_code": "KAO", "icao_code": "EFKS", "lat": 65.990278, "lon": 29.231944, "tm": flight, "name": "Kuusamo Airport"},
            {"point": 1, "city": "FI-KAO", "iata_code": None, "icao_code": None, "lat": 65.968930, "lon": 29.174537, "tm": bus, "name": "Kuusamo Station"},

            {"point": 1, "city": "FI-LHI", "iata_code": None, "icao_code": None, "lat": 60.976375, "lon": 25.657474, "tm": train, "name": "Lahti Station"},
            {"point": 1, "city": "FI-LHI", "iata_code": None, "icao_code": None, "lat": 60.977075, "lon": 25.658507, "tm": bus, "name": "Lahti Matkakeskus"},

            {"point": 0, "city": "FI-LPP", "iata_code": "LPP", "icao_code": "EFLP", "lat": 61.045833, "lon": 28.148611, "tm": flight, "name": "Lappeenranta Airport"},
            {"point": 1, "city": "FI-LPP", "iata_code": None, "icao_code": None, "lat": 61.048195, "lon": 28.194956, "tm": train, "name": "Lappeenranta Station"},
            {"point": 1, "city": "FI-LPP", "iata_code": None, "icao_code": None, "lat": 61.047897, "lon": 28.193028, "tm": bus, "name": "Lappeenranta Matkakeskus"}, #No he pogut averiguar ses destinacions

            {"point": 0, "city": "FI-MHQ", "iata_code": "MHQ", "icao_code": "EFMA", "lat": 60.121944, "lon": 19.896389, "tm": flight, "name": "Mariehamn Airport"},
            {"point": 1, "city": "FI-MHQ", "iata_code":None, "icao_code": None, "lat": 60.102199, "lon": 19.942257, "tm": bus, "name": "Mariehamn Station"}, # No he pogut averiguar ses destinacions
            # {"point": 1, "city": "FI-MHQ", "iata_code":None, "icao_code": None, "lat": 60.092076, "lon": 19.929017, "tm": ferry, "name": "Mariehamn Ferry Terminal"},

            {"point": 0, "city": "FI-OUL", "iata_code": "OUL", "icao_code": "EFOU", "lat": 64.929167, "lon": 25.355556, "tm": flight, "name": "Oulu Airport"},
            {"point": 1, "city": "FI-OUL", "iata_code": None, "icao_code": None, "lat": 65.011483, "lon": 25.483850, "tm": train, "name": "Oulu Train Station"},
            {"point": 1, "city": "FI-OUL", "iata_code": None, "icao_code": None, "lat": 65.009831, "lon": 25.483926, "tm": bus, "name": "Oulu Bus Station"},

            {"point": 0, "city": "FI-POR", "iata_code": "POR", "icao_code": "EFPO", "lat": 61.461389, "lon": 21.797778, "tm": flight, "name": "Pori Airport"},
            {"point": 1, "city": "FI-POR", "iata_code": None, "icao_code": None, "lat": 61.477497, "lon": 21.787751, "tm": train, "name": "Pori Train Station"},
            {"point": 1, "city": "FI-POR", "iata_code": None, "icao_code": None, "lat": 61.477837, "lon": 21.788621, "tm": bus, "name": "Pori Bus Station"},

            {"point": 0, "city": "FI-RVN", "iata_code": "RVN", "icao_code": "EFRO", "lat": 66.561667, "lon": 25.830833, "tm": flight, "name": "Rovaniemi Airport"},
            {"point": 1, "city": "FI-RVN", "iata_code": None, "icao_code": None, "lat": 66.498269, "lon": 25.705330, "tm": train, "name": "Rovaniemi Train Station"},
            {"point": 1, "city": "FI-RVN", "iata_code": None, "icao_code": None, "lat": 66.498460, "lon": 25.703834, "tm": bus, "name": "Rovaniemi Bus Station"},
            # {"point": 2, "city": "FI-RVN", "iata_code": None, "icao_code": None, "lat": 66.498481, "lon": 25.707546, "tm": ferry, "name": "Rovaniemi Ferry Terminal"}, # No ho entenc, perquè em surt aquesta terminal de ferry, pero no veig la mar per cap banda... a més sembla més una estació de bus...

            {"point": 0, "city": "FI-SVL", "iata_code": "SVL", "icao_code": "EFSA", "lat": 61.942778, "lon": 28.945000, "tm": flight, "name": "Savonlinna Airport"},
            {"point": 1, "city": "FI-SVL", "iata_code": None, "icao_code": None, "lat": 61.875030, "lon": 28.873576, "tm": train, "name": "Savonlinna Old Railway Station"},
            {"point": 2, "city": "FI-SVL", "iata_code": None, "icao_code": None, "lat": 61.868984, "lon": 28.886618, "tm": train, "name": "Savonlinna Market Square"},
            {"point": 3, "city": "FI-SVL", "iata_code": None, "icao_code": None, "lat": 61.870007, "lon": 28.872758, "tm": bus, "name": "Savonlinna Station"},

            {"point": 0, "city": "FI-TMP", "iata_code": "TMP", "icao_code": "EFTP", "lat": 61.415278, "lon": 23.587778, "tm": flight, "name": "Tampere-Pirkkala Airport"},
            {"point": 1, "city": "FI-TMP", "iata_code": None, "icao_code": None, "lat": 61.498602, "lon": 23.773051, "tm": train, "name": "Tampere Train Station"},
            {"point": 1, "city": "FI-TMP", "iata_code": None, "icao_code": None, "lat": 61.498021, "lon": 23.772080, "tm": bus, "name": "Tampere Bus Station"},

            {"point": 0, "city": "FI-TKU", "iata_code": "TKU", "icao_code": "EFTU", "lat": 60.514722, "lon": 22.261667, "tm": flight, "name": "Turku Airport"},
            {"point": 1, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.453946, "lon": 22.252931, "tm": train, "name": "Turku Jamvags"},
            {"point": 1, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.453567, "lon": 22.253295, "tm": bus, "name": "Turku Station"},
            {"point": 2, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.434726, "lon": 22.223447, "tm": train, "name": "Turku Harbour Station"},
            {"point": 2, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.434881, "lon": 22.223632, "tm": bus, "name": "Turku Bus Station"},
            {"point": 3, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.450533, "lon": 22.297002, "tm": train, "name": "Turku Kupitaa"},
            # {"point": 4, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.434010, "lon": 22.220902, "tm": ferry, "name": "Turku Viking"},
            # {"point": 5, "city": "FI-TKU", "iata_code": None, "icao_code": None, "lat": 60.435172, "lon": 22.217974, "tm": ferry, "name": "Turku Ferry Terminal"},

            {"point": 0, "city": "FI-VAA", "iata_code": "VAA", "icao_code": "EFVA", "lat": 63.045278, "lon": 21.764167, "tm": flight, "name": "Vaasa Airport"},
            {"point": 0, "city": "FI-VAA", "iata_code": None, "icao_code": None, "lat": 63.043766, "lon": 21.760077, "tm": bus, "name": "Vaasa Lentoasema"},
            {"point": 1, "city": "FI-VAA", "iata_code": None, "icao_code": None, "lat": 63.097557, "lon": 21.621682, "tm": train, "name": "Vaasa Station"},
            {"point": 1, "city": "FI-VAA", "iata_code": None, "icao_code": None, "lat": 63.096773, "lon": 21.624056, "tm": bus, "name": "Vaasa Matkakeskus"},
            # {"point": 2, "city": "FI-VAA", "iata_code": None, "icao_code": None, "lat": 63.087648, "lon": 21.556924, "tm": ferry, "name": "Vaasa Terminal"},
        ]

        hubs_CZ = [
            {"point": 0, "city": "CZ-BRQ", "iata_code": "BRQ", "icao_code":"LKTB", "lat": 49.151389, "lon": 16.694444, "tm": flight, "name": "Brno Airport"},
            {"point": 1, "city": "CZ-BRQ", "iata_code":  None, "icao_code":  None, "lat": 49.190839, "lon": 16.612643, "tm": train, "name": "Brno Main Station"},
            {"point": 1, "city": "CZ-BRQ", "iata_code": "ZDN", "icao_code":  None, "lat": 49.190839, "lon": 16.612643, "tm": bus, "name": "Brno Main Station"},
            {"point": 2, "city": "CZ-BRQ", "iata_code":  None, "icao_code":  None, "lat": 49.204153, "lon": 16.636676, "tm": train, "name": "Brno Zidenice"},
            {"point": 2, "city": "CZ-BRQ", "iata_code":  None, "icao_code":  None, "lat": 49.204153, "lon": 16.636676, "tm": bus, "name": "Brno Zidenice"},
            {"point": 3, "city": "CZ-BRQ", "iata_code":  None, "icao_code":  None, "lat": 49.186049, "lon": 16.574394, "tm": bus, "name": "Brno Bauerova"},

            {"point": 0, "city": "CZ-KLV", "iata_code": "KLV", "icao_code":"LKKV", "lat": 50.203064, "lon": 12.915017, "tm": flight, "name": "Karlovy Vary Airport"},
            {"point": 1, "city": "CZ-KLV", "iata_code":  None, "icao_code":  None, "lat": 50.235348, "lon": 12.866557, "tm": train, "name": "Karlovy Vary Train Station"},
            {"point": 2, "city": "CZ-KLV", "iata_code":  None, "icao_code":  None, "lat": 50.230225, "lon": 12.864248, "tm": train, "name": "Karlovy Vary Dolni N. Train Station"},
            {"point": 2, "city": "CZ-KLV", "iata_code":  None, "icao_code":  None, "lat": 50.229989, "lon": 12.863980, "tm": bus, "name": "Karlovy Vary Dolni N. Bus Station"},

            {"point": 1, "city": "CZ-LBR", "iata_code": None, "icao_code": None, "lat": 50.761623, "lon": 15.046642, "tm": train, "name": "Liberec Train Station"},
            {"point": 2, "city": "CZ-LBR", "iata_code": None, "icao_code": None, "lat": 50.763640, "lon": 15.046603, "tm": bus, "name": "Liberec An Bus Station"},
            #
            {"point": 1, "city": "CZ-OLO", "iata_code": None, "icao_code": None, "lat": 49.592499, "lon": 17.277776, "tm": train, "name": "Olomouc Train Station"},
            {"point": 1, "city": "CZ-OLO", "iata_code": None, "icao_code": None, "lat": 49.593535, "lon": 17.276698, "tm": bus, "name": "Olomouc Bus Station"},

            {"point": 0, "city": "CZ-OSR", "iata_code": "OSR", "icao_code":"LKMT", "lat": 49.696111, "lon": 18.110833, "tm": flight, "name": "Ostrava Airport"},
            {"point": 1, "city": "CZ-OSR", "iata_code": "XJV", "icao_code":  None, "lat": 49.850621, "lon": 18.266460, "tm": train, "name": "Ostrava hl. n."},
            {"point": 1, "city": "CZ-OSR", "iata_code":  None, "icao_code":  None, "lat": 49.850447, "lon": 18.267646, "tm": bus, "name": "Ostrava hl. n."},
            # {"point": 2, "city": "CZ-OSR", "iata_code":  None, "icao_code":  None, "lat": 49.852225, "lon": 18.269221, "tm": bus, "name": "Ostrava Bus Station"}, #same as hl. n.
            {"point": 3, "city": "CZ-OSR", "iata_code":  None, "icao_code":  None, "lat": 49.821198, "lon": 18.208530, "tm": train, "name": "Ostrava Svinov"},
            {"point": 3, "city": "CZ-OSR", "iata_code":  None, "icao_code":  None, "lat": 49.821210, "lon": 18.208494, "tm": bus, "name": "Ostrava Svinov"},
            # {"point": 4, "city": "CZ-OSR", "iata_code":  None, "icao_code":  None, "lat":   49.8345, "lon":   18.2813, "tm": bus, "name": "Ostrava Porazkova"}, #no bus station found..
            {"point": 5, "city": "CZ-OSR", "iata_code":  None, "icao_code":  None, "lat": 49.830444, "lon": 18.280405, "tm": bus, "name": "Ostrava ÚAN"},

            {"point": 0, "city": "CZ-PRB", "iata_code": "PED", "icao_code":"LKPD", "lat": 50.013333, "lon": 15.738611, "tm": flight, "name": "Pardubice Airport"},
            {"point": 1, "city": "CZ-PRB", "iata_code":  None, "icao_code":  None, "lat": 50.032402, "lon": 15.757118, "tm": train, "name": "Pardubice Train Station"},
            {"point": 1, "city": "CZ-PRB", "iata_code":  None, "icao_code":  None, "lat": 50.032484, "lon": 15.757112, "tm": bus, "name": "Pardubice Bus Station"},

            {"point": 1, "city": "CZ-PLZ", "iata_code": None, "icao_code": None, "lat": 49.743246, "lon": 13.387984, "tm": train, "name": "Pilsen Train Station"},
            {"point": 1, "city": "CZ-PLZ", "iata_code": None, "icao_code": None, "lat": 49.744600, "lon": 13.386910, "tm": bus, "name": "Pilsen Bus Station"},
            {"point": 2, "city": "CZ-PLZ", "iata_code": None, "icao_code": None, "lat": 49.746501, "lon": 13.362348, "tm": bus, "name": "Pilsen CAN Husova Bus Station"},

            {"point": 0, "city": "CZ-PRG", "iata_code": "PRG", "icao_code":"LKPR", "lat": 50.100833, "lon": 14.260000, "tm": flight, "name": "Prague Airport"},
            {"point": 0, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.107338, "lon": 14.269132, "tm": bus, "name": "Prague Airport Bus Station"},
            {"point": 1, "city": "CZ-PRG", "iata_code": "XYG", "icao_code":  None, "lat": 50.083230, "lon": 14.435290, "tm": train, "name": "Prague Main Station"},
            {"point": 1, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.083374, "lon": 14.434608, "tm": bus, "name": "Prague Main Station"},
            {"point": 2, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.089390, "lon": 14.439570, "tm": bus, "name": "Prague Florenc Bus Station"},
            {"point": 3, "city": "CZ-PRG", "iata_code": 'XYJ', "icao_code":  None, "lat": 50.109485, "lon": 14.439760, "tm": train, "name": "Prague Holesovice"},
            {"point": 3, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.109896, "lon": 14.441546, "tm": bus, "name": "Prague Holesovice"},
            {"point": 4, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.101294, "lon": 14.501613, "tm": train, "name": "Prague Liben"},
            {"point": 4, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat":   50.1012, "lon":   14.5016, "tm": bus, "name": "Prague Liben"},
            {"point": 5, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.055338, "lon": 14.290158, "tm": bus, "name": "Prague Metro Zličín"},
            {"point": 6, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.064983, "lon": 14.297101, "tm": bus, "name": "Prague Praha-Zličín"},
            {"point": 7, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.098114, "lon": 14.405219, "tm": bus, "name": "Prague Hradčanská"},
            {"point": 8, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.109331, "lon": 14.578000, "tm": bus, "name": "Prague Cerny Most"},
            {"point": 9, "city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.068608, "lon": 14.404342, "tm": bus, "name": "Prague Na Knížecí"},
            {"point": 10,"city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.087940, "lon": 14.420891, "tm": bus, "name": "Prague Old Town Square (Staroměstské náměstí)"},
            {"point": 11,"city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.037868, "lon": 14.476981, "tm": bus, "name": "Praha Rozttyly"},
            {"point": 12,"city": "CZ-PRG", "iata_code":  None, "icao_code":  None, "lat": 50.079249, "lon": 14.475742, "tm": bus, "name": "Prague Zhelivskeho"},
        ]

        hubs_AT = [
            {"point": 0, "city": "AT-GRZ", "iata_code": "GRZ", "icao_code":"LOWG", "lat": 46.993056, "lon": 15.439167, "tm": flight, "name": "Graz Airport"},
            {"point": 1, "city": "AT-GRZ", "iata_code": "GGZ", "icao_code":  None, "lat": 47.072893, "lon": 15.417030, "tm": train, "name": "Graz Hbf"},
            {"point": 1, "city": "AT-GRZ", "iata_code":  None, "icao_code":  None, "lat": 47.073711, "lon": 15.416848, "tm": bus, "name": "Graz Hbf"},
            {"point": 2, "city": "AT-GRZ", "iata_code":  None, "icao_code":  None, "lat": 47.067368, "lon": 15.443406, "tm": bus, "name": "Graz Jakominiplatz"},
            {"point": 3, "city": "AT-GRZ", "iata_code":  None, "icao_code":  None, "lat": 47.040759, "lon": 15.465221, "tm": bus, "name": "Graz Murpark"},
            {"point": 4, "city": "AT-GRZ", "iata_code":  None, "icao_code":  None, "lat": 47.036444, "lon": 15.410432, "tm": bus, "name": "Graz Webling"},

            {"point": 0, "city": "AT-INN", "iata_code": "INN", "icao_code":"LOWI", "lat": 47.260278, "lon": 11.343889, "tm": flight, "name": "Innsbruck Airport"},
            {"point": 1, "city": "AT-INN", "iata_code": "IOB", "icao_code":  None, "lat": 47.263333, "lon": 11.400486, "tm": train, "name": "Innsbruck Central Station"},
            {"point": 1, "city": "AT-INN", "iata_code":  None, "icao_code":  None, "lat": 47.258352, "lon": 11.399818, "tm": bus, "name": "Innsbruck Südbahnstr."},
            {"point": 2, "city": "AT-INN", "iata_code":  None, "icao_code":  None, "lat": 47.270590, "lon": 11.399027, "tm": bus, "name": "Innsbruck Hofgarten"},

            {"point": 0, "city": "AT-KLU", "iata_code": "KLU", "icao_code":"LOWK", "lat": 46.642778, "lon": 14.337222, "tm": flight, "name": "Klagenfurt Airport"},
            {"point": 0, "city": "AT-KLU", "iata_code":  None, "icao_code":  None, "lat": 46.642778, "lon": 14.337222, "tm": train, "name": "Klagenfurt Airport Train Station"},
            {"point": 0, "city": "AT-KLU", "iata_code":  None, "icao_code":  None, "lat": 46.642778, "lon": 14.337222, "tm": bus, "name": "Klagenfurt Airport Bus Station"},
            {"point": 1, "city": "AT-KLU", "iata_code": "KGV", "icao_code":  None, "lat": 46.615994, "lon": 14.313567, "tm": train, "name": "Klagenfurt Train Station"},
            {"point": 1, "city": "AT-KLU", "iata_code":  None, "icao_code":  None, "lat": 46.616335, "lon": 14.311552, "tm": bus, "name": "Klagenfurt Bus Station"},
            {"point": 2, "city": "AT-KLU", "iata_code":  None, "icao_code":  None, "lat": 46.620306, "lon": 14.267875, "tm": bus, "name": "Klagenfurt Minimundis Bus Station"},

            {"point": 0, "city": "AT-LNZ", "iata_code": "LNZ", "icao_code":"LOWL", "lat": 48.233333, "lon": 14.187500, "tm": flight, "name": "Linz Airport"},
            {"point": 1, "city": "AT-LNZ", "iata_code": "LZS", "icao_code":  None, "lat": 48.290607, "lon": 14.291175, "tm": train , "name": "Linz Train Central Station"},
            {"point": 1, "city": "AT-LNZ", "iata_code":  None, "icao_code":  None, "lat": 48.290411, "lon": 14.291478, "tm": bus, "name": "Linz Bus Central Station"},
            {"point": 2, "city": "AT-LNZ", "iata_code":  None, "icao_code":  None, "lat": 48.310527, "lon": 14.314191, "tm": bus, "name": "Linz Hafen Bus Station"},
            {"point": 3, "city": "AT-LNZ", "iata_code":  None, "icao_code":  None, "lat": 48.299669, "lon": 14.322041, "tm": bus, "name": "Linz Industriezeile"},
            # {"point": 4, "city": "AT-LNZ", "iata_code":  None, "icao_code":  None, "lat": 48.328826, "lon": 14.178450, "tm": ferry, "name": "Linz Ferry Terminal"},

            {"point": 0, "city": "AT-SZG", "iata_code": "SZG", "icao_code":"LOWS", "lat": 47.794444, "lon": 13.003333, "tm": flight, "name": "Salzburg Airport"},
            {"point": 1, "city": "AT-SZG", "iata_code": "ZSB", "icao_code":  None, "lat": 47.813050, "lon": 13.045071, "tm": train, "name": "Salzburg Train Station"},
            {"point": 1, "city": "AT-SZG", "iata_code":  None, "icao_code":  None, "lat": 47.813982, "lon": 13.047987, "tm": bus, "name": "Salzburg Bus Station"},
            {"point": 2, "city": "AT-SZG", "iata_code":  None, "icao_code":  None, "lat": 47.836286, "lon": 12.977900, "tm": bus, "name": "Salzburg Freilassing Bus Station"},
            {"point": 3, "city": "AT-SZG", "iata_code":  None, "icao_code":  None, "lat": 47.769845, "lon": 13.071784, "tm": bus, "name": "Salzburg P+R Süd"},

            {"point": 0, "city": "AT-VIE", "iata_code": "VIE", "icao_code":"LOWW", "lat": 48.110278, "lon": 16.569722, "tm": flight, "name": "Vienna Airport"},
            {"point": 0, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.120903, "lon": 16.563071, "tm": train, "name": "Vienna Airport Train Station"},
            {"point": 0, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.119970, "lon": 16.563242, "tm": bus, "name": "Vienna Airport Bus Station"},
            {"point": 1, "city": "AT-VIE", "iata_code": "XWC", "icao_code":"ZSXZ", "lat": 48.185197, "lon": 16.376478, "tm": train, "name": "Vienna Central Station"},
            {"point": 1, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.185197, "lon": 16.376478, "tm": bus, "name": "Vienna Central Station"},
            {"point": 2, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.190994, "lon": 16.414154, "tm": bus, "name": "Vienna Erdberg"},
            # {"point": 3, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.196797, "lon": 16.337696, "tm": train, "name": "Vienna West Train Station"},
            {"point": 3, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.197844, "lon": 16.337404, "tm": bus, "name": "Vienna Westbahnhof"},
            # {"point": 4, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.197339, "lon": 16.260986, "tm": train, "name": "Vienna Hutteldorf Train Station"},
            {"point": 4, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.197778, "lon": 16.261383, "tm": bus, "name": "Vienna Hutteldorf Bus Station"},
            {"point": 5, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.210623, "lon": 16.422382, "tm": bus, "name": "Vienna Stadion"},
            {"point": 6, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.219186, "lon": 16.391907, "tm": bus, "name": "Vienna Praterstern"},
            {"point": 7, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.205619, "lon": 16.384272, "tm": bus, "name": "Vienna Mitte"},
            {"point": 8, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.1745, "lon": 16.334, "tm": bus, "name": "Vienna Meidling"},
            {"point": 9, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.1953, "lon": 16.3861, "tm": bus, "name": "Vienna Rennweg"},
            {"point":10, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.1795, "lon": 16.3588, "tm": bus, "name": "Vienna Matzleinsdorfer Platz"},
            {"point":11, "city": "AT-VIE", "iata_code":  None, "icao_code":  None, "lat": 48.200808, "lon": 16.369841, "tm": bus, "name": "Vienna Karlsplatz"},
        ]

        hubs_LU = [
            {"point": 0, "city": "LU-LUX", "iata_code": "LUX", "icao_code": "ELLX", "lat": 49.6233, "lon": 6.20444, "tm": flight, "name": "Luxembourg Airport"},
            {"point": 0, "city": "LU-LUX", "iata_code":  None, "icao_code":   None, "lat": 49.635133, "lon": 6.216518, "tm": bus, "name": "Luxembourg Airport"},
            {"point": 1, "city": "LU-LUX", "iata_code":  None, "icao_code":   None, "lat": 49.600046, "lon": 6.134094, "tm": train, "name": "Luxembourg central station"},
            {"point": 1, "city": "LU-LUX", "iata_code":  None, "icao_code":   None, "lat": 49.599246, "lon": 6.133053, "tm": bus, "name": "Luxembourg central station"},
            {"point": 2, "city": "LU-LUX", "iata_code":  None, "icao_code":   None, "lat": 49.632246, "lon": 6.169858, "tm": bus, "name": "Luxembourg Kirchberg"},
            {"point": 3, "city": "LU-LUX", "iata_code":  None, "icao_code":   None, "lat": 49.615945, "lon": 6.122074, "tm": bus, "name": "Luxembourg Limpertsberg"},
        ]

        hubs_IS = [
            {"point": 0, "city": "IS-AKU", "iata_code": "AEY", "icao_code": "BIAR", "lat": 65.6611, "lon": -18.0722, "tm": flight, "name": "Akureyri Airport"},

            # {"point": 0, "city": "IS-BIU", "iata_code": "BIU", "icao_code": "BIBD", "lat": 65.6417, "lon": -23.5458, "tm": flight, "name": "Bíldudalur Airport"},

            {"point": 0, "city": "IS-EGS", "iata_code": "EGS", "icao_code": "BIEG", "lat": 65.2833, "lon": -14.4014, "tm": flight, "name": "Egilsstaðir Airport"},

            # {"point": 0, "city": "IS-DPV", "iata_code": "GJR", "icao_code": "BIGJ", "lat": 65.9944, "lon": -21.3292, "tm": flight, "name": "Gjögur Airport"},

            # {"point": 0, "city": "IS-GRY", "iata_code": "GRY", "icao_code": "BIGR", "lat": 66.5458, "lon": -18.0167, "tm": flight, "name": "Grímsey Airport"},

            # {"point": 0, "city": "IS-HFN", "iata_code": "HFN", "icao_code": "BIHN", "lat": 64.2956, "lon": -15.2272, "tm": flight, "name": "Hornafjörður Airport"},

            # {"point": 0, "city": "IS-ISA", "iata_code": "IFJ", "icao_code": "BIIS", "lat": 66.0581, "lon": -23.1353, "tm": flight, "name": "Ísafjörður Airport"},

            {"point": 0, "city": "IS-REY", "iata_code": "RKV", "icao_code": "BIRK", "lat": 64.13, "lon": -21.9406, "tm": flight, "name": "Reykjavík Airport"},
            {"point": 1, "city": "IS-REY", "iata_code": "KEF", "icao_code": "BIKF", "lat": 63.985, "lon": -22.6056, "tm": flight, "name": "Keflavík Airport"},

            # {"point": 0, "city": "Þórshöfn", "iata_code": "THO", "icao_code": "BITN", "lat": 66.2183, "lon": -15.3356, "tm": flight, "name": "Þórshöfn Airport"},

            # {"point": 0, "city": "IS-VPN", "iata_code": "VPN", "icao_code": "BIVO", "lat": 65.7206, "lon": -14.8506, "tm": flight, "name": "Vopnafjörður Airport"},
        ]

        hubs_GR = [
            {"point": 0, "city": "GR-AXD", "iata_code": "AXD", "icao_code": "LGAL", "lat": 40.855869, "lon": 25.956264, "tm": flight, "name": "Alexandroupolis Airport"},
            {"point": 1, "city": "GR-AXD", "iata_code": None, "icao_code": None, "lat": 40.845045, "lon": 25.878598, "tm": train, "name": "Alexandroupolis Port"},
            {"point": 1, "city": "GR-AXD", "iata_code": None, "icao_code": None, "lat": 40.845148, "lon": 25.878974, "tm": bus, "name": "Alexandroupolis Port"},
            {"point": 2, "city": "GR-AXD", "iata_code": None, "icao_code": None, "lat": 40.846154, "lon": 25.875262, "tm": bus, "name": "Alexandroupolis Evros Municipality"},
            # {"point": 3, "city": "GR-AXD", "iata_code": None, "icao_code": None, "lat": 40.842566, "lon": 25.877795 "tm": ferry, "name": "Alexandroupolis Saos Ferries"},

            # {"point": 1, "city": "GR-AMO", "iata_code": None, "icao_code": None, "lat": 36.901579, "lon": 25.975820, "tm": ferry, "name": "Amorgós Aegiali Terminal"},
            # {"point": 2, "city": "GR-AMO", "iata_code": None, "icao_code": None, "lat": 36.828096, "lon": 25.865699, "tm": ferry, "name": "Amorgós Katapola Terminal"},

            {"point": 0, "city": "GR-JTY", "iata_code": "JTY", "icao_code": "LGPL", "lat": 36.579886, "lon": 26.375822, "tm": flight, "name": "Astypalaia Airport"},
            # {"point": 1, "city": "GR-JTY", "iata_code": None, "icao_code": None, "lat": 36.573135, "lon": 26.340260, "tm": ferry, "name": "Astypalaia Ferry Terminal"},
            # {"point": 2, "city": "GR-JTY", "iata_code": None, "icao_code": None, "lat": 36.547122, "lon": 26.355381, "tm": ferry, "name": "Astypalaia Ferry Terminal"},

            {"point": 0, "city": "GR-ATH", "iata_code": "ATH", "icao_code": "LGAV", "lat": 37.936389, "lon": 23.947222, "tm": flight, "name": "Athens Airport"},
            {"point": 0, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.936518, "lon": 23.946729, "tm": bus, "name": "Athens Bus Station"},
            {"point": 1, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.992305, "lon": 23.720802, "tm": train, "name": "Athens Αθήνα"},
            {"point": 1, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.991942, "lon": 23.720794, "tm": bus, "name": "Athens Athina"},
            {"point": 2, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.986784, "lon": 23.723479, "tm": bus, "name": "Athens Station"},
            {"point": 3, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.991354, "lon": 23.732301, "tm": bus, "name": "Athens KTEL"},
            {"point": 4, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.949111, "lon": 23.642496, "tm": train, "name": "Athens Pireás"}, #GR-PIR
            {"point": 5, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.949455, "lon": 23.636441, "tm": bus, "name": "Athens Pireás"}, #GR-PIR
            # {"point": 6, "city": "GR-ATH", "iata_code": None, "icao_code": None, "lat": 37.947786, "lon": 23.641792, "tm": ferry, "name": "Athens Pireás Ferry Terminal"}, #N’hi ha molts ferrys. He posat sa terminal que està enmig...

            {"point": 0, "city": "GR-CHQ", "iata_code": "CHQ", "icao_code": "LGSA", "lat": 35.531667, "lon": 24.149722, "tm": flight, "name": "Chania Airport"},
            {"point": 1, "city": "GR-CHQ", "iata_code": None, "icao_code": None, "lat": 35.511994, "lon": 24.016896, "tm": bus, "name": "Chania Kentriko KTEL Chanion"},
           # {"point": 2, "city": "GR-CHQ", "iata_code": None, "icao_code": None, "lat": 35.518740, "lon": 24.019938, "tm": ferry, "name": "Chania Ferry Terminal"},

            {"point": 0, "city": "GR-JKH", "iata_code": "JKH", "icao_code": "LGHI", "lat": 38.343056, "lon": 26.140556, "tm": flight, "name": "Chios Airport"},
            {"point": 1, "city": "GR-JKH", "iata_code": None, "icao_code": None, "lat": 38.371401, "lon": 26.137086, "tm": bus, "name": "Chios Ladis Station"},
            # {"point": 2, "city": "GR-JKH", "iata_code": None, "icao_code": None, "lat": 38.369025, "lon": 26.138235, "tm": ferry, "name": "Chios Ferry Terminal"},

            {"point": 0, "city": "GR-CFU", "iata_code": "CFU", "icao_code": "LGKR", "lat": 39.601944, "lon": 19.911667, "tm": flight, "name": "Corfu Airport"},
            # {"point": 1, "city": "GR-CFU", "iata_code": None, "icao_code": None, "lat": 39.621660, "lon": 19.918460, "tm": bus, "name": "Corfu Blue City Bus Station"},
            # {"point": 2, "city": "GR-CFU", "iata_code": None, "icao_code": None, "lat": 39.615746, "lon": 19.912144, "tm": bus, "name": "Kerkira KTEL"}, #KTEL és s’empresa més gran d’autocars de Grecia.
            # {"point": 3, "city": "GR-CFU", "iata_code": None, "icao_code": None, "lat": 39.629675, "lon": 19.901754, "tm": ferry, "name": "Corfu Ferry Terminal"},
            # {"point": 4, "city": "GR-CFU", "iata_code": None, "icao_code": None, "lat": 39.626932, "lon": 19.919385, "tm": ferry, "name": "Corfu Ferry Terminal"},

            # {"point": 1, "city": "GR-DON", "iata_code": None, "icao_code": None, "lat": 37.099162, "lon": 25.794047, "tm": ferry, "name": "Donousa Ferry terminal"},

            {"point": 0, "city": "GR-HKL", "iata_code": "HER", "icao_code": "LGIR", "lat": 35.339722, "lon": 25.180278, "tm": flight, "name": "Heraklion Airport"},
            {"point": 1, "city": "GR-HKL", "iata_code": None, "icao_code": None, "lat": 35.341133, "lon": 25.139359, "tm": bus, "name": "Heraklion Bus Station"},
            # {"point": 2, "city": "GR-HKL", "iata_code": None, "icao_code": None, "lat": 35.343338, "lon": 25.143037, "tm": ferry, "name": "Heraklion Ferry Terminal"},

            {"point": 0, "city": "GR-JIK", "iata_code": "JIK", "icao_code": "LGIK", "lat": 37.683083, "lon": 26.344376, "tm": flight, "name": "Ikaria Airport"},
            # {"point": 1, "city": "GR-JIK", "iata_code": None, "icao_code": None, "lat": 37.613116, "lon": 26.294747, "tm": ferry, "name": "Ikaria Ferry Terminal"},

            {"point": 0, "city": "GR-IOA", "iata_code": "IOA", "icao_code": "LGIO", "lat": 39.696389, "lon": 20.822500, "tm": flight, "name": "Ioannina Airport"},
            {"point": 1, "city": "GR-IOA", "iata_code": None, "icao_code": None, "lat": 39.674581, "lon": 20.846772, "tm": bus, "name": "Ioannina Bus Station"},

            {"point": 0, "city": "GR-KLX", "iata_code": "KLX", "icao_code": "LGKL", "lat": 37.068383, "lon": 22.025366, "tm": flight, "name": "Kalamata Airport"},
            {"point": 1, "city": "GR-KLX", "iata_code": None, "icao_code": None, "lat": 37.047208, "lon": 22.114162, "tm": bus, "name": "Kalamata Artemidos Station"},
            # {"point": 2, "city": "GR-KLX", "iata_code": None, "icao_code": None, "lat": 37.021918, "lon": 22.115811, "tm": ferry, "name": "Kalamata Ferry Terminal"},

            {"point": 0, "city": "GR-KMI", "iata_code": "JKL", "icao_code": "LGKY", "lat": 36.963333, "lon": 26.940556, "tm": flight, "name": "Kalymnos Airport"},
            # {"point": 1, "city": "GR-KMI", "iata_code": None, "icao_code": None, "lat": 36.947587, "lon": 26.985976, "tm": ferry, "name": "Kalymnos Ferry Terminal"},

            {"point": 0, "city": "GR-AOK", "iata_code": "AOK", "icao_code": "LGKP", "lat": 35.420556, "lon": 27.146667, "tm": flight, "name": "Karpathos Airport"},
            # {"point": 1, "city": "GR-AOK", "iata_code": None, "icao_code": None, "lat": 35.506939, "lon": 27.210347, "tm": bus, "name": "Karpathos Bus Terminal"},
            # {"point": 2, "city": "GR-AOK", "iata_code": None, "icao_code": None, "lat": 35.509619, "lon": 27.215398, "tm": ferry, "name": "Karpathos Ferry Terminal"},

            {"point": 0, "city": "GR-KSJ", "iata_code": "KSJ", "icao_code": "LGKS", "lat": 35.420470, "lon": 26.914342, "tm": flight, "name": "Kassos Airport"},
            # {"point": 1, "city": "GR-KSJ", "iata_code": None, "icao_code": None, "lat": 35.418831, "lon": 26.924695, "tm": ferry, "name": "Kassos Ferry Terminal"},

            {"point": 0, "city": "GR-KZS", "iata_code": "KZS", "icao_code": "LGKJ", "lat": 36.141670, "lon": 29.576376, "tm": flight, "name": "Kastelorizo Airport"},
            # {"point": 1, "city": "GR-KZS", "iata_code": None, "icao_code": None, "lat": 36.150283, "lon": 29.592135, "tm": ferry, "name": "Kastelorizo Ferry Terminal"},

            {"point": 0, "city": "GR-KSO", "iata_code": "KSO", "icao_code": "LGKA", "lat": 40.446294, "lon": 21.282186, "tm": flight, "name": "Kastoria Airport"},
            {"point": 1, "city": "GR-KSO", "iata_code": None, "icao_code": None, "lat": 40.521623, "lon": 21.260068, "tm": bus, "name": "Kastoria Athanasiou Diakou"},

            {"point": 0, "city": "GR-KVA", "iata_code": "KVA", "icao_code": "LGKV", "lat": 40.913333, "lon": 24.619167, "tm": flight, "name": "Kavala Airport"},
            {"point": 1, "city": "GR-KVA", "iata_code": None, "icao_code": None, "lat": 40.935771, "lon": 24.408464, "tm": bus, "name": "Kavala Mitropolitou Chrisostomou"},
            # {"point": 2, "city": "GR-KVA", "iata_code": None, "icao_code": None, "lat": 40.934055, "lon": 24.411502, "tm": ferry, "name": "Kavala Ferry Terminal"},

            {"point": 0, "city": "GR-K33", "iata_code": "EFL", "icao_code": "LGKF", "lat": 38.120000, "lon": 20.500278, "tm": flight, "name": "Kefalonia Island Airport"},
            # {"point": 0, "city": "GR-K33", "iata_code": None, "icao_code": None, "lat": 38.119320, "lon": 20.505411, "tm": bus, "name": "Kefalonia Argostoli"},
            # {"point": 1, "city": "GR-K33", "iata_code": None, "icao_code": None, "lat": 38.199687, "lon": 20.439594, "tm": ferry, "name": "Kefalonia Ferry Terminal"},
            # {"point": 2, "city": "GR-K33", "iata_code": None, "icao_code": None, "lat": 38.252138, "lon": 20.645947, "tm": ferry, "name": "Kefalonia Sami"},
            # {"point": 3, "city": "GR-K33", "iata_code": None, "icao_code": None, "lat": 38.462314, "lon": 20.576160, "tm": ferry, "name": "Kefalonia Fiskardo"},
            # {"point": 4, "city": "GR-K33", "iata_code": None, "icao_code": None, "lat": 38.147525, "lon": 20.782988, "tm": ferry, "name": "Kefalonia Poros"},
            # {"point": 5, "city": "GR-K33", "iata_code": None, "icao_code": None, "lat": 38.107576, "lon": 20.589607, "tm": ferry, "name": "Kefalonia Pessada Harbour"},

            {"point": 0, "city": "GR-KGS", "iata_code": "KGS", "icao_code": "LGKO", "lat": 36.793336, "lon": 27.091667, "tm": flight, "name": "Kos Island Airport"},
            # {"point": 1, "city": "GR-KGS", "iata_code": None, "icao_code": None, "lat": 36.891401, "lon": 27.287688, "tm": bus, "name": "Kos Bus Station"},
            # {"point": 2, "city": "GR-KGS", "iata_code": None, "icao_code": None, "lat": 36.898549, "lon": 27.290379, "tm": ferry, "name": "Kos Ferry Terminal"},

            {"point": 0, "city": "GR-KZI", "iata_code": "KZI", "icao_code": "LGKZ", "lat": 40.286111, "lon": 21.840833, "tm": flight, "name": "Kozani Airport"},
            {"point": 1, "city": "GR-KZI", "iata_code": None, "icao_code": None, "lat": 40.294622, "lon": 21.792826, "tm": train, "name": "Kozani Train Station"},
            {"point": 2, "city": "GR-KZI", "iata_code": None, "icao_code": None, "lat": 40.300258, "lon": 21.797330, "tm": bus, "name": "Kozani Giannari"},

            {"point": 0, "city": "GR-KIT", "iata_code": "KIT", "icao_code": "LGKC", "lat": 36.274258, "lon": 23.016978, "tm": flight, "name": "Kythira Airport"},

            {"point": 1, "city": "GR-LRA", "iata_code": None, "icao_code": None, "lat": 39.629480, "lon": 22.422483, "tm": train, "name": "Lárisa Sidirodromikos Stathmos"},
            {"point": 1, "city": "GR-LRA", "iata_code": None, "icao_code": None, "lat": 39.629620, "lon": 22.423016, "tm": bus, "name": "Lárisa Sidirodromikos Stathmos"},
            {"point": 2, "city": "GR-LRA", "iata_code": None, "icao_code": None, "lat": 39.643104, "lon": 22.419197, "tm": bus, "name": "Lárisa Bus Station"},

            {"point": 0, "city": "GR-LXS", "iata_code": "LXS", "icao_code": "LGLM", "lat": 39.917072, "lon": 25.236308, "tm": flight, "name": "Lemnos Airport"},
            # {"point": 1, "city": "GR-LXS", "iata_code": None, "icao_code": None, "lat": 39.870927, "lon": 25.055143, "tm": ferry, "name": "Lemnos Ferry Terminal"},

            {"point": 0, "city": "GR-LRS", "iata_code": "LRS", "icao_code": "LGLE", "lat": 37.184722, "lon": 26.800278, "tm": flight, "name": "Leros Airport"},
            # {"point": 1, "city": "GR-LRS", "iata_code": None, "icao_code": None, "lat": 37.127892, "lon": 26.848964, "tm": ferry, "name": "Leros Ferry Terminal"},

            {"point": 0, "city": "GR-MLO", "iata_code": "MLO", "icao_code": "LGML", "lat": 36.696900, "lon": 24.476900, "tm": flight, "name": "Milos Airport"},
            # {"point": 1, "city": "GR-MLO", "iata_code": None, "icao_code": None, "lat": 36.723610, "lon": 24.444915, "tm": ferry, "name": "Milos Ferry Terminal"},

            {"point": 0, "city": "GR-JMK", "iata_code": "JMK", "icao_code": "LGMK", "lat": 37.435128, "lon": 25.348103, "tm": flight, "name": "Mykonos Airport"},
            # {"point": 1, "city": "GR-JMK", "iata_code": None, "icao_code": None, "lat": 37.465471, "lon": 25.322846, "tm": ferry, "name": "Mykonos Sea Bus"},
            # {"point": 2, "city": "GR-JMK", "iata_code": None, "icao_code": None, "lat": 37.463730, "lon": 25.325695, "tm": ferry, "name": "Mykonos Ferry Terminal Port"},

            {"point": 0, "city": "GR-MJT", "iata_code": "MJT", "icao_code": "LGMT", "lat": 39.056667, "lon": 26.598333, "tm": flight, "name": "Mytilene Airport"},
            # {"point": 1, "city": "GR-MJT", "iata_code": None, "icao_code": None, "lat": 39.101259, "lon": 26.556983, "tm": ferry, "name": "Mytilene Ferry Terminal"},

            {"point": 0, "city": "GR-JNX", "iata_code": "JNX", "icao_code": "LGNX", "lat": 37.081072, "lon": 25.368158, "tm": flight, "name": "Naxos Airport"},
            # {"point": 1, "city": "GR-JNX", "iata_code": None, "icao_code": None, "lat": 37.106230, "lon": 25.371445, "tm": ferry, "name": "Naxos Ferry Terminal"},

            {"point": 0, "city": "GR-GPA", "iata_code": "GPA", "icao_code": "LGRX", "lat": 38.151111, "lon": 21.425556, "tm": flight, "name": "Araxos Airport"},
            {"point": 1, "city": "GR-GPA", "iata_code": None, "icao_code": None, "lat": 38.239096, "lon": 21.727310, "tm": train, "name": "Patras Agios Andreas"},
            {"point": 2, "city": "GR-GPA", "iata_code": None, "icao_code": None, "lat": 38.249683, "lon": 21.734712, "tm": bus, "name": "Patras Bus Station"},
            # {"point": 3, "city": "GR-GPA", "iata_code": None, "icao_code": None, "lat": 38.226640, "lon": 21.721053, "tm": ferry, "name": "Patras Port"},

            # {"point": 1, "city": "GR-RAF", "iata_code": None, "icao_code": None, "lat": 38.022783, "lon": 24.010285, "tm": ferry, "name": "Rafina Port"},

            {"point": 0, "city": "GR-RHO", "iata_code": "RHO", "icao_code": "LGRP", "lat": 36.405419, "lon": 28.086192, "tm": flight, "name": "Rhodes Airport"},
            # {"point": 1, "city": "GR-RHO", "iata_code": None, "icao_code": None, "lat": 36.447248, "lon": 28.224958, "tm": bus, "name": "Rhodes Papagou"},
            # {"point": 2, "city": "GR-RHO", "iata_code": None, "icao_code": None, "lat": 36.446790, "lon": 28.232539, "tm": ferry, "name": "Rhodes Ferry Terminal"},

            {"point": 0, "city": "GR-SMI", "iata_code": "SMI", "icao_code": "LGSM", "lat": 37.690000, "lon": 26.911667, "tm": flight, "name": "Samos Airport"},
            # {"point": 1, "city": "GR-SMI", "iata_code": None, "icao_code": None, "lat": 36.446790, "lon": 28.232539, "tm": ferry, "name": "Samos Ferry Terminal"},

            {"point": 0, "city": "GR-ATN", "iata_code": "JTR", "icao_code": "LGSR", "lat": 36.399169, "lon": 25.479333, "tm": flight, "name": "Santorini Airport"},
            # {"point": 1, "city": "GR-ATN", "iata_code": None, "icao_code": None, "lat": 36.386132, "lon": 25.428412, "tm": ferry, "name": "Santorini Athinios Port"},

            {"point": 0, "city": "GR-JSH", "iata_code": "JSH", "icao_code": "LGST", "lat": 35.216108, "lon": 26.101325, "tm": flight, "name": "Sitia Airport"},
            {"point": 1, "city": "GR-JSH", "iata_code": None, "icao_code": None, "lat": 35.204426, "lon": 26.104485, "tm": bus, "name": "Sitia Station"},
            # {"point": 2, "city": "GR-JSH", "iata_code": None, "icao_code": None, "lat": 35.212437, "lon": 26.111556, "tm": ferry, "name": "Sitia Ferry Terminal"},

            {"point": 0, "city": "GR-JSI", "iata_code": "JSI", "icao_code": "LGSK", "lat": 39.177500, "lon": 23.503675, "tm": flight, "name": "Skiathos Airport"},
            # {"point": 1, "city": "GR-JSI", "iata_code": None, "icao_code": None, "lat": 39.165604, "lon": 23.492085, "tm": bus, "name": "Skiathos Bus Station"},
            # {"point": 2, "city": "GR-JSI", "iata_code": None, "icao_code": None, "lat": 39.162808, "lon": 23.491002, "tm": ferry, "name": "Skiathos Ferry Terminal"},

            {"point": 0, "city": "GR-SKU", "iata_code": "SKU", "icao_code": "LGSY", "lat": 38.967500, "lon": 24.487222, "tm": flight, "name": "Skyros Airport"},

            {"point": 0, "city": "GR-SKG", "iata_code": "SKG", "icao_code": "LGTS", "lat": 40.519722, "lon": 22.970833, "tm": flight, "name": "Thessaloniki Airport"},
            {"point": 1, "city": "GR-SKG", "iata_code": None, "icao_code": None, "lat": 40.644416, "lon": 22.929762, "tm": train, "name": "Thessaloniki Train Station"},
            {"point": 1, "city": "GR-SKG", "iata_code": None, "icao_code": None, "lat": 40.644267, "lon": 22.929953, "tm": bus, "name": "Thessaloniki Bus Station"},
            {"point": 2, "city": "GR-SKG", "iata_code": None, "icao_code": None, "lat": 40.654678, "lon": 22.902303, "tm": bus, "name": "Thessaloniki Macedonia Intercity"},
            # {"point": 3, "city": "GR-SKG", "iata_code": None, "icao_code": None, "lat": 40.634603, "lon": 22.934047, "tm": ferry, "name": "Thessaloniki Ferry Terminal"},

            {"point": 0, "city": "GR-VOL", "iata_code": "VOL", "icao_code": "LGBL", "lat": 39.219444, "lon": 22.794167, "tm": flight, "name": "Nea Anchialos Airport"},
            {"point": 1, "city": "GR-VOL", "iata_code": None, "icao_code": None, "lat": 39.364695, "lon": 22.936437, "tm": train, "name": "Volos Train Station"},
            {"point": 1, "city": "GR-VOL", "iata_code": None, "icao_code": None, "lat": 39.364002, "lon": 22.936345, "tm": bus, "name": "Volos Bus Station"},
            # {"point": 2, "city": "GR-VOL", "iata_code": None "icao_code": None, "lat": 39.357830, "lon": 22.944118, "tm": ferry, "name": "Volos Ferry Terminal"},

            {"point": 0, "city": "GR-ZTH", "iata_code": "ZTH", "icao_code": "LGZA", "lat": 37.750833, "lon": 20.884167, "tm": flight, "name": "Zakynthos Airport"},
            # {"point": 1, "city": "GR-ZTH", "iata_code": None, "icao_code": None, "lat": 37.781567, "lon": 20.892918, "tm": bus, "name": "Zakynthos Central Bus Station KTEL"},
            # {"point": 2, "city": "GR-ZTH", "iata_code": None, "icao_code": None, "lat": 37.779357, "lon": 20.901509, "tm": ferry, "name": "Zakynthos Ferry Station"},
        ]


        hubs_LT = [
            {"point": 0, "city": "LT-KUN", "iata_code": "KUN", "icao_code": "EYKA", "lat": 54.963889, "lon": 24.084722, "tm": flight, "name": "Kaunas Airport"},
            {"point": 1, "city": "LT-KUN", "iata_code":  None, "icao_code":   None, "lat": 54.886225, "lon": 23.931801, "tm": train, "name": "Kaunas Train Station"},
            {"point": 2, "city": "LT-KUN", "iata_code":  None, "icao_code":   None, "lat": 54.889858, "lon": 23.928921, "tm": bus, "name": "Kaunas Bus Station"},

            {"point": 1, "city": "LT-KLJ", "iata_code":  None, "icao_code":   None, "lat": 55.721012, "lon": 21.134962, "tm": train, "name": "Klaipėda Train Station"},
            {"point": 1, "city": "LT-KLJ", "iata_code":  None, "icao_code":   None, "lat": 55.719557, "lon": 21.137668, "tm": bus, "name": "Klaipėda Bus Station"},
            # {"point": 3, "city": "LT-KLJ ", "iata_code":  None, "icao_code":   None, "lat":  55.661222, "lon": 21.144883, "tm": ferry, "name": "Klaipėda Ferry Terminal"},

            {"point": 0, "city": "LT-PLQ", "iata_code": "PLQ", "icao_code": "EYPA", "lat": 55.973333, "lon": 21.093889, "tm": flight, "name": "Palanga Airport"},
            {"point": 1, "city": "LT-PLQ", "iata_code":  None, "icao_code":   None, "lat": 55.914054, "lon": 21.078749, "tm": bus, "name": "Palanga Bus Station"},

            {"point": 1, "city": "LT-PNV", "iata_code":  None, "icao_code":   None, "lat":  55.745125, "lon": 24.354774, "tm": train, "name": " Panevėžys Train Station"},
            {"point": 2, "city": "LT-PNV", "iata_code":  None, "icao_code":   None, "lat": 55.727556, "lon": 24.364652, "tm": bus, "name": " Panevėžys Bus Station"},

            {"point": 1, "city": "LT-SQQ", "iata_code":  None, "icao_code":   None, "lat": 55.923248, "lon": 23.313522, "tm": train, "name": "Šiauliai Station"},
            {"point": 2, "city": "LT-SQQ", "iata_code":  None, "icao_code":   None, "lat": 55.927836, "lon": 23.307732, "tm": bus, "name": "Šiauliai Tilžės"},

            {"point": 0, "city": "LT-VIL", "iata_code": "VNO", "icao_code": "EYVI", "lat": 54.636944, "lon": 25.287778, "tm": flight, "name": "Vilnius Airport"},
            {"point": 0, "city": "LT-VIL", "iata_code":  None, "icao_code":   None, "lat":  54.643313, "lon": 25.2796, "tm": bus, "name": "Vilnius Airport"}, #No sé d’on surt aquesta coordenada que tenies “25.2796”. He posat sa que em surt a jo. Diu que té flixbus, però a sa pàgina de flixbus, no he trobat res...
            {"point": 2, "city": "LT-VIL", "iata_code":  None, "icao_code":   None, "lat": 54.670207, "lon": 25.284404, "tm": train, "name": "Vilnius Geležinkelio Stotis"},
            {"point": 2, "city": "LT-VIL", "iata_code":  None, "icao_code":   None, "lat": 54.670600, "lon": 25.281960, "tm": bus, "name": "Vilnius Stotis Bus Station"},
        ]

        #ongoing
        hubs_LV = [
            {"point": 1, "city": "LV-DGP", "iata_code": None, "icao_code": None, "lat": 55.874881, "lon": 26.527576, "tm": train, "name": "Daugavpils Station"},
            {"point": 1, "city": "LV-DGP", "iata_code": None, "icao_code": None, "lat": 55.871197, "lon": 26.524769, "tm": bus, "name": "Daugavpils Viestura iela"},
            {"point": 2, "city": "LV-DGP", "iata_code": None, "icao_code": None, "lat": 55.874107, "lon": 26.521937, "tm": bus, "name": "Daugavpils Sakņu iela"},

            {"point": 0, "city": "LV-LPX", "iata_code": "LPX", "icao_code": "EVLA", "lat": 56.517530, "lon": 21.096880, "tm": flight, "name": "Liepāja Airport"},
            {"point": 0, "city": "LV-LPX", "iata_code": None, "icao_code": None, "lat": 56.520690, "lon": 21.096601, "tm": bus, "name": "Liepāja Airport Bus"},
            {"point": 1, "city": "LV-LPX", "iata_code": None, "icao_code": None, "lat": 56.524327, "lon": 21.017065, "tm": train, "name": "Liepāja Train Station"},
            {"point": 1, "city": "LV-LPX", "iata_code": None, "icao_code": None, "lat": 56.524120, "lon": 21.017378, "tm": bus, "name": "Liepāja Bus Station"},
            {"point": 2, "city": "LV-LPX", "iata_code": None, "icao_code": None, "lat": 56.502239, "lon": 21.007822, "tm": bus, "name": "Liepāja Ecolines"},
            # {"point": 3, "city": "LV-LPX", "iata_code": None, "icao_code": None, "lat": 56.529159, "lon": 20.998443, "tm": ferry, "name": "Liepāja Ferry Terminal"},

            {"point": 0, "city": "LV-RIX", "iata_code": "RIX", "icao_code": "EVRA", "lat": 56.923623, "lon": 23.971089, "tm": flight, "name": "Riga Airport"},
            {"point": 1, "city": "LV-RIX", "iata_code": None, "icao_code": None, "lat": 56.946810, "lon": 24.120112, "tm": train, "name": "Riga Station"},
            {"point": 2, "city": "LV-RIX", "iata_code": None, "icao_code": None, "lat": 56.944955, "lon": 24.114490, "tm": bus, "name": "Riga Prāgas iela"},
            # {"point": 3, "city": "LV-RIX", "iata_code": None, "icao_code": None, "lat": 56.959293, "lon": 24.094668, "tm": ferry, "name": "Riga Ferry Terminal"},
        ]

        hubs_EE = [
            {"point": 0, "city": "EE-KDL", "iata_code": "KDL", "icao_code": "EEKA", "lat": 58.990833, "lon": 22.830833, "tm": flight, "name": "Kärdla Airport"},
            {"point": 1, "city": "EE-KDL", "iata_code": None, "icao_code": None, "lat": 59.001653, "lon": 22.747034, "tm": bus, "name": "Kärdla Station"},

            # {"point": 0, "city": "Kihnu", "iata_code": None, "icao_code": "EEKU", "lat": 58.148333, "lon": 24.002500, "tm": flight, "name": "Kihnu Airfield"},
            # {"point": 1, "city": "Kihnu", "iata_code": None, "icao_code": None, "lat": 58.141672, "lon": 24.021974, "tm": ferry, "name": "Kihnu Terminal"},

            {"point": 0, "city": "EE-URE", "iata_code": "URE", "icao_code": "EEKE", "lat": 58.230000, "lon": 22.509444, "tm": flight, "name": "Kuressaare Airport"},
            {"point": 0, "city": "EE-URE", "iata_code": None, "icao_code": None, "lat": 58.232209, "lon": 22.504474, "tm": bus, "name": "Kuressaare Lennujaam"},
            {"point": 1, "city": "EE-URE", "iata_code": None, "icao_code": None, "lat": 58.254871, "lon": 22.493965, "tm": bus, "name": "Kuressaare Bussijaam"},

            {"point": 0, "city": "EE-PRN", "iata_code": "EPU", "icao_code": "EEPU", "lat": 58.418889, "lon": 24.472778, "tm": flight, "name": "Pärnu Airport"},
            {"point": 1, "city": "EE-PRN", "iata_code": None, "icao_code": None, "lat": 58.372528, "lon": 24.555508, "tm": train, "name": "Pärnu Raudteejaam"},
            {"point": 2, "city": "EE-PRN", "iata_code": None, "icao_code": None, "lat": 58.385617, "lon": 24.505121, "tm": bus, "name": "Pärnu Bussijaam"},

            # {"point": 0, "city": "Ruhnu", "iata_code": None, "icao_code": "EERU", "lat": 57.783889, "lon": 23.266111, "tm": flight, "name": "Ruhnu Airfield"},
            # {"point": 1, "city": "Ruhnu", "iata_code": None, "icao_code": None, "lat": 57.781113, "lon": 23.269728, "tm": ferry, "name": "Ruhnu terminal"},

            {"point": 0, "city": "EE-TLL", "iata_code": "TLL", "icao_code": "EETN", "lat": 59.413333, "lon": 24.832500, "tm": flight, "name": "Tallinn Airport"},
            {"point": 1, "city": "EE-TLL", "iata_code": None, "icao_code": None, "lat": 59.440633, "lon": 24.738027, "tm": train, "name": "Tallinn Balti jaam"},
            {"point": 1, "city": "EE-TLL", "iata_code": None, "icao_code": None, "lat": 59.440532, "lon": 24.738390, "tm": bus, "name": "Tallinn Balti jaam"},
            # {"point": 2, "city": "EE-TLL", "iata_code": None, "icao_code": None, "lat": 59.444767, "lon": 24.761983, "tm": ferry, "name": "Tallinn Sadam"},

            {"point": 0, "city": "EE-TAY", "iata_code": "TAY", "icao_code": "EETU", "lat": 58.307500, "lon": 26.686944, "tm": flight, "name": "Tartu Airport"},
            {"point": 1, "city": "EE-TAY", "iata_code": None, "icao_code": None, "lat": 58.373821, "lon": 26.706740, "tm": train, "name": "Tartu Raudteejaam"},
            {"point": 2, "city": "EE-TAY", "iata_code": None, "icao_code": None, "lat": 58.378062, "lon": 26.732092, "tm": bus, "name": "Tartu Bussijaam"},

        ]

        hubs_SI = [
            {"point": 0, "city": "SI-MBX", "iata_code": "MBX", "icao_code": "LJMB", "lat": 46.4797, "lon": 15.6861, "tm": flight, "name": "Maribor Airport"},
            {"point": 1, "city": "SI-MBX", "iata_code":  None, "icao_code":   None, "lat": 46.562066, "lon": 15.658005, "tm": train, "name": "Maribor Train Station"},
            {"point": 2, "city": "SI-MBX", "iata_code": "MSB", "icao_code":   None, "lat": 46.559547, "lon": 15.655764, "tm": bus, "name": "Maribor Bus Station"},

            {"point": 0, "city": "SI-LJA", "iata_code": "LJU", "icao_code": "LJLJ", "lat": 46.2244, "lon": 14.4561, "tm": flight, "name": "Ljubljana Airport"},
            {"point": 1, "city": "SI-LJA", "iata_code":  None, "icao_code":   None, "lat": 46.058792, "lon": 14.512905, "tm": train, "name": "Ljubljana"},
            {"point": 1, "city": "SI-LJA", "iata_code":  None, "icao_code":   None, "lat": 46.057743, "lon": 14.509621, "tm": bus, "name": "Ljubljana Avtobusna Postaja"},
            # {"point": 2, "city": "SI-LJA", "iata_code":  None, "icao_code":   None, "lat": 46.056678, "lon": 14.507785, "tm": bus, "name": "Ljubljana Bus Station"}, #Switched to point 1 and changed to fake coordinates for a while. to be deleted starting from september 2018

        ]

        hubs_HR = [
            {"point": 0, "city": "HR-SUP", "iata_code": "BWK", "icao_code": "LDSB", "lat": 43.285833, "lon": 16.679722, "tm": flight, "name": "Brač Airport"},
            # {"point": 1, "city": "HR-SUP", "iata_code": None, "icao_code": None, "lat": 43.385231, "lon": 16.556956, "tm": ferry, "name": "Brač Trajektna Luka Supetar"},
            # {"point": 1, "city": "HR-SUP", "iata_code": None, "icao_code": None, "lat": 43.385030, "lon": 16.556650, "tm": ferry, "name": "Brač Jadrolinija"},
            # {"point": 2, "city": "HR-SUP", "iata_code": None, "icao_code": None, "lat": 43.285143, "lon": 16.870927, "tm": ferry, "name": "Brač Sumartin-Makarska"},

            {"point": 0, "city": "HR-DBV", "iata_code": "DBV", "icao_code": "LDDU", "lat": 42.561389, "lon": 18.268333, "tm": flight, "name": "Dubrovnik Airport"},
            {"point": 1, "city": "HR-DBV", "iata_code":  None, "icao_code":  None, "lat": 42.662807, "lon": 18.083555, "tm": bus, "name": "Dubrovnik Bus Station"}, #No n’hi trens, així que supos que es numero ha de ser 1
            # {"point": 2, "city": "HR-DBV", "iata_code":  None, "icao_code":  None, "lat": 42.658461, "lon": 18.085618, "tm": ferry, "name": "Dubrovnik Ferry Terminal"},

            {"point": 0, "city": "HR-OSI", "iata_code": "OSI", "icao_code": "LDOS", "lat": 45.462778, "lon": 18.810278, "tm": flight, "name": "Osijek Airport"},
            {"point": 1, "city": "HR-OSI", "iata_code": None, "icao_code": None, "lat": 45.553233, "lon": 18.684828, "tm": train, "name": "Osijek Train Station"},
            {"point": 1, "city": "HR-OSI", "iata_code": None, "icao_code": None, "lat": 45.553199, "lon": 18.680025, "tm": bus, "name": "Osijek Bartola Kašića"},

            {"point": 0, "city": "HR-PUY", "iata_code": "PUY", "icao_code": "LDPL", "lat": 44.893611, "lon": 13.922222, "tm": flight, "name": "Pula Airport"},
            {"point": 1, "city": "HR-PUY", "iata_code":  None, "icao_code":   None, "lat": 44.879587, "lon": 13.847529, "tm": train, "name": "Pula Train Station"},
            {"point": 2, "city": "HR-PUY", "iata_code":  None, "icao_code":   None, "lat": 44.876105, "lon": 13.855095, "tm": bus, "name": "Pula Autobusni Kolodvor"},
            # {"point": 3, "city": "HR-PUY", "iata_code":  None, "icao_code":   None, "lat": 44.874966, "lon": 13.846359, "tm": ferry, "name": "Pula Ferry Terminal"},

            {"point": 0, "city": "HR-RJK", "iata_code": "RJK", "icao_code": "LDRI", "lat": 45.216944, "lon": 14.570278, "tm": flight, "name": "Rijeka Airport"},
            {"point": 1, "city": "HR-RJK", "iata_code": None, "icao_code": None, "lat": 45.330274, "lon": 14.430369, "tm": train, "name": "Rijeka Station"},
            {"point": 2, "city": "HR-RJK", "iata_code": None, "icao_code": None, "lat": 45.327921, "lon": 14.436855, "tm": bus, "name": "Rijeka Žabica"},
            # {"point": 3, "city": "HR-RJK", "iata_code": None, "icao_code": None, "lat": 45.323456, "lon": 14.440958, "tm": ferry, "name": "Rijeka Ferry Terminal"},

            {"point": 0, "city": "HR-SPU", "iata_code": "SPU", "icao_code": "LDSP", "lat": 43.538889, "lon": 16.298056, "tm": flight, "name": "Split Airport"},
            {"point": 1, "city": "HR-SPU", "iata_code": None, "icao_code": None, "lat": 43.504732, "lon": 16.442957, "tm": train, "name": "Split Station"},
            {"point": 1, "city": "HR-SPU", "iata_code": None, "icao_code": None, "lat": 43.504114, "lon": 16.442789, "tm": bus, "name": "Split Obala kneza Domagoja"},
            # {"point": 2, "city": "HR-SPU", "iata_code": None, "icao_code": None, "lat": 43.504533, "lon": 16.440306, "tm": ferry, "name": "Split Ferry Terminal"},
            # {"point": 3, "city": "HR-SPU", "iata_code": None, "icao_code": None, "lat": 43.502996, "lon": 16.441387, "tm": ferry, "name": "Split Gat Svetog Duje"},

            {"point": 0, "city": "HR-ZAD", "iata_code": "ZAD", "icao_code": "LDZD", "lat": 44.108333, "lon": 15.346667, "tm": flight, "name": "Zadar Airport"},
            {"point": 1, "city": "HR-ZAD", "iata_code": None, "icao_code": None, "lat": 44.106564, "lon": 15.242131, "tm": train, "name": "Zadar Station"},
            {"point": 1, "city": "HR-ZAD", "iata_code": None, "icao_code": None, "lat": 44.106436, "lon": 15.241137, "tm": bus, "name": "Zadar Anter Starčevića"},
            # {"point": 2, "city": "HR-ZAD", "iata_code": None, "icao_code": None, "lat": 44.116705, "lon": 15.227715, "tm": ferry, "name": "Zadar Liburnska obala"},
            # {"point": 3, "city": "HR-ZAD", "iata_code": None, "icao_code": None, "lat": 44.093982, "lon": 15.259703, "tm": ferry, "name": "Zadar Gaženička cesta"},

            {"point": 0, "city": "HR-ZAG", "iata_code": "ZAG", "icao_code": "LDZA", "lat": 45.743056, "lon": 16.068889, "tm": flight, "name": "Zagreb Airport"},
            {"point": 1, "city": "HR-ZAG", "iata_code":  None, "icao_code":   None, "lat": 45.804672, "lon": 15.978812, "tm": train, "name": "Zagreb Trg kralja Tomislava"},
            {"point": 2, "city": "HR-ZAG", "iata_code":  None, "icao_code":   None, "lat": 45.804005, "lon": 15.993273, "tm": bus, "name": "Zagreb Autobusni Kolodvor"},
        ]

        hubs_MT = [
            {"point": 0, "city": "MT-MLA", "iata_code": "MLA", "icao_code": "LMML", "lat": 35.8575, "lon": 14.4775, "tm": flight, "name": "Malta Airport"},
        ]

        hubs_HU = [
            {"point": 0, "city": "HU-BTN", "iata_code": "SOB", "icao_code": "LHSM", "lat": 46.686389, "lon": 17.159167, "tm": flight, "name": "Hévíz-Balaton Airport"},
            {"point": 1, "city": "HU-BTN", "iata_code":  None, "icao_code":   None, "lat": 46.758326, "lon": 17.247979, "tm": train, "name": "Keszthley Station"}, #Balaton és un llac. Keszthley ciutat més propera a s’aeroport
            {"point": 1, "city": "HU-BTN", "iata_code":  None, "icao_code":   None, "lat": 46.758094, "lon": 17.246557, "tm": bus, "name": "Keszthley Station"}, #Balaton és un llac. Keszthley ciutat més propera a s’aeroport

            {"point": 0, "city": "HU-BUD", "iata_code": "BUD", "icao_code": "LHBP", "lat": 47.439444, "lon": 19.261944, "tm": flight, "name": "Budapest Airport"},
            {"point": 0, "city": "HU-BUD", "iata_code":  None, "icao_code":   None, "lat": 47.433029, "lon": 19.261969, "tm": bus, "name": "Budapest Airport"},
            {"point": 1, "city": "HU-BUD", "iata_code": "XXQ", "icao_code":   None, "lat": 47.500311, "lon": 19.084062, "tm": train, "name": "Budapest Keleti"},
            {"point": 2, "city": "HU-BUD", "iata_code":  None, "icao_code":   None, "lat": 47.474307, "lon": 19.098436, "tm": bus, "name": "Budapest Népliget"},
            {"point": 3, "city": "HU-BUD", "iata_code":  None, "icao_code":   None, "lat": 47.464367, "lon": 19.020400, "tm": train, "name": "Budapest Kelenföld"},
            {"point": 3, "city": "HU-BUD", "iata_code":  None, "icao_code":   None, "lat": 47.463489, "lon": 19.022750, "tm": bus, "name": "Budapest Kelenföld"},
            {"point": 4, "city": "HU-BUD", "iata_code":  None, "icao_code":   None, "lat": 47.510738, "lon": 19.057467, "tm": train, "name": "Budapest Nyugati"},

            {"point": 0, "city": "HU-DEB", "iata_code": "DEB", "icao_code": "LHDC", "lat": 47.488889, "lon": 21.615278, "tm": flight, "name": "Debrecen Airport"},
            {"point": 1, "city": "HU-DEB", "iata_code": None, "icao_code": None, "lat": 47.520453, "lon": 21.628286, "tm": train, "name": "Debrecen Station"},
            {"point": 1, "city": "HU-DEB", "iata_code": None, "icao_code": None, "lat": 47.520605, "lon": 21.628773, "tm": bus, "name": "Debrecen Station"},
            {"point": 2, "city": "HU-DEB", "iata_code": None, "icao_code": None, "lat": 47.525597, "lon": 21.618059, "tm": bus, "name": "Debrecen Külsö-Vásártér"},

            {"point": 0, "city": "HU-GYO", "iata_code": "QGY", "icao_code": "LHPR", "lat": 47.623348, "lon": 17.804457, "tm": flight, "name": "Győr-Pér Airport"},
            {"point": 1, "city": "HU-GYO", "iata_code":  None, "icao_code":   None, "lat": 47.682050, "lon": 17.635255, "tm": train, "name": "Győr Station"},
            {"point": 1, "city": "HU-GYO", "iata_code":  None, "icao_code":   None, "lat": 47.681381, "lon": 17.636529, "tm": bus, "name": "Győr Station"},

            {"point": 1, "city": "HU-MCQ", "iata_code": None, "icao_code": None, "lat": 48.098619, "lon": 20.811393, "tm": train, "name": "Miskolc-Tiszai"},
            {"point": 1, "city": "HU-MCQ", "iata_code": None, "icao_code": None, "lat": 48.097784, "lon": 20.809008, "tm": bus, "name": "Miskolc-Tiszai"},
            {"point": 2, "city": "HU-MCQ", "iata_code": None, "icao_code": None, "lat": 48.104814, "lon": 20.791119, "tm": bus, "name": "Miskolc Station"},

            {"point": 1, "city": "HU-NGH", "iata_code": None, "icao_code": None, "lat": 47.946553, "lon": 21.705936, "tm": train, "name": "Nyíregyháza Station"},
            {"point": 1, "city": "HU-NGH", "iata_code": None, "icao_code": None, "lat": 47.946219, "lon": 21.706173, "tm": bus, "name": "Nyíregyháza Station"},

            {"point": 1, "city": "HU-PEC", "iata_code": None, "icao_code": None, "lat": 46.065976, "lon": 18.223694, "tm": train, "name": "Pécs Station"},
            {"point": 1, "city": "HU-PEC", "iata_code": None, "icao_code": None, "lat": 46.066934, "lon": 18.226231, "tm": bus, "name": "Pécs Főpályaudvar"},

            {"point": 1, "city": "HU-SZE", "iata_code": None, "icao_code": None, "lat": 46.239728, "lon": 20.143059, "tm": train, "name": "Szeged Station"},
            {"point": 1, "city": "HU-SZE", "iata_code": None, "icao_code": None, "lat": 46.240041, "lon": 20.143222, "tm": bus, "name": "Szeged Station"},
            {"point": 2, "city": "HU-SZE", "iata_code": None, "icao_code": None, "lat": 46.257082, "lon": 20.140728, "tm": bus, "name": "Szeged Mars tér"},

            {"point": 1, "city": "HU-SZR", "iata_code": None, "icao_code": None, "lat": 47.183612, "lon": 18.424720, "tm": train, "name": "Székesfehérvár Station"},
            {"point": 1, "city": "HU-SZR", "iata_code": None, "icao_code": None, "lat": 47.183664, "lon": 18.424977, "tm": bus, "name": "Székesfehérvár Station"},
            {"point": 2, "city": "HU-SZR", "iata_code": None, "icao_code": None, "lat": 47.188926, "lon": 18.409008, "tm": bus, "name": "Székesfehérvár Piac Tér"},
        ]

        hubs_PL = [
            {"point": 0, "city": "PL-WAW", "iata_code": "WAW", "icao_code": "EPWA", "lat": 52.1658, "lon": 20.9672, "tm": flight, "name": "Warsaw Chopin Airport"},
            {"point": 0, "city": "PL-WAW", "iata_code":  None, "icao_code":   None, "lat": 52.169361, "lon": 20.973693, "tm": bus, "name": "Warsaw Chopin Airport"},
            {"point": 1, "city": "PL-WAW", "iata_code": "WMI", "icao_code": "EPMO", "lat": 52.4511, "lon": 20.6517, "tm": flight, "name": "Warsaw-Modlin Mazovia Airport"},
            {"point": 2, "city": "PL-WAW", "iata_code":  None, "icao_code":   None, "lat": 52.290582, "lon": 20.927823, "tm": bus, "name": "Warsaw Mlociny"},
            {"point": 3, "city": "PL-WAW", "iata_code":  None, "icao_code":   None, "lat": 52.218391, "lon": 20.961755, "tm": bus, "name": "Warsaw West"},
            {"point": 4, "city": "PL-WAW", "iata_code":  None, "icao_code":   None, "lat": 52.1798, "lon": 21.0236, "tm": bus, "name": "Warsaw Wilanowska"},
            {"point": 5, "city": "PL-WAW", "iata_code":  None, "icao_code":   None, "lat": 52.2289, "lon": 21.0033, "tm": bus, "name": "Warsaw Centralna"},

            {"point": 0, "city": "PL-GDN", "iata_code": "GDN", "icao_code": "EPGD", "lat": 54.3775, "lon": 18.4661, "tm": flight, "name": "Gdańsk Airport"},
            {"point": 1, "city": "PL-GDN", "iata_code":  None, "icao_code":   None, "lat": 54.356589, "lon": 18.642711, "tm": bus, "name": "Gdańsk bus station"},

            {"point": 0, "city": "PL-KTW", "iata_code": "KTW", "icao_code": "EPKT", "lat": 50.4742, "lon": 19.0800, "tm": flight, "name": "Katowice Airport"},
            {"point": 0, "city": "PL-KTW", "iata_code":  None, "icao_code":  None, "lat": 50.470745, "lon": 19.073086, "tm": bus, "name": "Katowice Airport"},
            {"point": 2, "city": "PL-KTW", "iata_code":  None, "icao_code":  None, "lat": 50.258751, "lon": 19.026790, "tm": bus, "name": "Katowice Warszawska 18"},
            {"point": 3, "city": "PL-KTW", "iata_code":  None, "icao_code":  None, "lat": 50.2627,   "lon": 19.0172, "tm": bus, "name": "Katowice Skargi 8"},

            {"point": 0, "city": "PL-WRO", "iata_code": "WRO", "icao_code": "EPWR", "lat": 51.1094, "lon": 16.8803, "tm": flight, "name": "Wrocław Airport"},
            {"point": 0, "city": "PL-WRO", "iata_code":  None, "icao_code":  None, "lat": 51.110351, "lon": 16.879203, "tm": bus, "name": "Wrocław Airport"},
            {"point": 1, "city": "PL-WRO", "iata_code":  None, "icao_code":  None, "lat": 51.098738, "lon": 17.036509, "tm": train, "name": "Wrocław Glowny"},
            {"point": 2, "city": "PL-WRO", "iata_code":  None, "icao_code":  None, "lat": 51.097241, "lon": 17.035091, "tm": bus, "name": "Wrocław DA"},

            {"point": 0, "city": "PL-POZ", "iata_code": "POZ", "icao_code": "EPPO", "lat": 52.4211, "lon": 16.8264, "tm": flight, "name": "Poznań-Ławica Airport"},
            {"point": 2, "city": "PL-POZ", "iata_code":  None, "icao_code":  None, "lat": 52.402757, "lon": 16.913959, "tm": bus, "name": "Poznań Główny"},

            {"point": 0, "city": "PL-RZE", "iata_code": "RZE", "icao_code": "EPRZ", "lat": 50.1100, "lon": 22.0189, "tm": flight, "name": "Rzeszów-Jasionka Airport"},

            {"point": 0, "city": "PL-SZZ", "iata_code": "SZZ", "icao_code": "EPSC", "lat": 53.5847, "lon": 14.9022, "tm": flight, "name": "Szczecin-Goleniów Airport"},
            {"point": 2, "city": "PL-SZZ", "iata_code":  None, "icao_code":  None, "lat": 53.415172, "lon": 14.547246, "tm": bus, "name": "Szczecin Kolumba"},
            {"point": 3, "city": "PL-SZZ", "iata_code":  None, "icao_code":  None, "lat": 53.386419, "lon": 14.481960, "tm": bus, "name": "Szczecin Warzymice"},
            {"point": 4, "city": "PL-SZZ", "iata_code":  None, "icao_code":  None, "lat": 53.402485, "lon": 14.499306, "tm": bus, "name": "Szczecin Uniwersytet"},

            {"point": 0, "city": "PL-BZG", "iata_code": "BZG", "icao_code": "EPBY", "lat": 53.0967, "lon": 17.9778, "tm": flight, "name": "Bydgoszcz Airport"},
            {"point": 2, "city": "PL-BZG", "iata_code":  None, "icao_code":   None, "lat": 53.1219, "lon": 18.0177, "tm": bus, "name": "Bydgoszcz Dworzec autobusowy"},

            {"point": 0, "city": "PL-LOD", "iata_code": "LCJ", "icao_code": "EPLL", "lat": 51.7219, "lon": 19.3981, "tm": flight, "name": "Łódź Airport"},
            {"point": 2, "city": "PL-LOD", "iata_code":  None, "icao_code":   None, "lat": 51.757573, "lon": 19.432222, "tm": bus, "name": "Łódź Kaliska"},
            {"point": 3, "city": "PL-LOD", "iata_code":  None, "icao_code":   None, "lat": 51.7702, "lon": 19.4705, "tm": bus, "name": "Łódź Fabryczna"},
            # {"point": 4, "city": "PL-LOD", "iata_code":  None, "icao_code":   None, "lat": 51.7575, "lon": 19.4323, "tm": bus, "name": "Łódź Kaliska"},

            {"point": 0, "city": "PL-LUL", "iata_code": "LUZ", "icao_code": "EPLB", "lat": 51.2403, "lon": 22.7136, "tm": flight, "name": "Lublin Airport"},
            {"point": 2, "city": "PL-LUL", "iata_code":  None, "icao_code":   None, "lat": 51.2519, "lon":  22.571, "tm": bus, "name": "Lublin Dworzec Aleje Tysiąclecia"},

            {"point": 0, "city": "PL-IEG", "iata_code": "IEG", "icao_code": "EPZG", "lat": 52.1386, "lon": 15.7986, "tm": flight, "name": "Zielona Góra Airport"},
            {"point": 2, "city": "PL-IEG", "iata_code":  None, "icao_code":  None, "lat": 51.946311, "lon": 15.510475, "tm": bus, "name": "Zielona Góra Bus Station"},

            {"point": 0, "city": "PL-RDM", "iata_code": "RDO", "icao_code": "EPRA", "lat": 51.3892, "lon": 21.2136, "tm": flight, "name": "Radom Airport"},
            {"point": 2, "city": "PL-RDM", "iata_code":  None, "icao_code":   None, "lat": 51.3925, "lon": 21.1578, "tm": bus, "name": "Radom Dworzec autobusowy"},

            {"point": 0, "city": "PL-OLS", "iata_code": "SZY", "icao_code": "EPSY", "lat": 53.4819, "lon": 20.9378, "tm": flight, "name": "Olsztyn-Mazury Airport"},

            {"point": 0, "city": "PL-KRK", "iata_code": "KRK", "icao_code": "EPKK", "lat": 50.0778, "lon": 19.7847, "tm": flight, "name": "Kraków Airport"},
            {"point": 0, "city": "PL-KRK", "iata_code":  None, "icao_code":   None, "lat": 50.071764, "lon": 19.800958, "tm": bus, "name": "Kraków Airport"},
            {"point": 1, "city": "PL-KRK", "iata_code":  None, "icao_code":   None, "lat": 50.067717, "lon": 19.949333, "tm": bus, "name": "Kraków MDA"},
        ]

        hubs_SK = [
            {"point": 0, "city": "SK-BTS", "iata_code": "BTS", "icao_code": "LZIB", "lat": 48.170000, "lon": 17.212778, "tm": flight, "name": "Bratislava Airport"},
            {"point": 0, "city": "SK-BTS", "iata_code": None, "icao_code": None, "lat": 48.170039, "lon": 17.199189, "tm": bus, "name": "Bratislava Airport"},
            {"point": 1, "city": "SK-BTS", "iata_code": None, "icao_code": None, "lat": 48.158640, "lon": 17.106259, "tm": train, "name": "Bratislava Hl.St."},
            {"point": 2, "city": "SK-BTS", "iata_code": None, "icao_code": None, "lat": 48.121645, "lon": 17.098803, "tm": train, "name": "Bratislava Petržalka"},
            {"point": 3, "city": "SK-BTS", "iata_code": None, "icao_code": None, "lat": 48.144504, "lon": 17.129301, "tm": bus, "name": "Bratislava Bottova"},
            {"point": 4, "city": "SK-BTS", "iata_code": None, "icao_code": None, "lat": 48.140353, "lon": 17.104210, "tm": bus, "name": "Bratislava Most SNP"},
            {"point": 5, "city": "SK-BTS", "iata_code": None, "icao_code": None, "lat": 48.132226, "lon": 17.098857, "tm": bus, "name": "Bratislava Einsteinova"},

            {"point": 0, "city": "SK-KSC", "iata_code": "KSC", "icao_code": "LZKZ", "lat": 48.663056, "lon": 21.241111, "tm": flight, "name": "Košice Airport"},
            {"point": 1, "city": "SK-KSC", "iata_code": None, "icao_code": None, "lat": 48.722651, "lon": 21.267752, "tm": train, "name": "Košice Station"},
            {"point": 1, "city": "SK-KSC", "iata_code": None, "icao_code": None, "lat": 48.721327, "lon": 21.267351, "tm": bus, "name": "Košice AS"},

            {"point": 0, "city": "SK-POP", "iata_code": "TAT", "icao_code": "LZTT", "lat": 49.073611, "lon": 20.241111, "tm": flight, "name": "Poprad-Tatry Airport"},
            {"point": 1, "city": "SK-POP", "iata_code": None, "icao_code": None, "lat": 49.059613, "lon": 20.295662, "tm": train, "name": "Poprad-Tatry"},
            # {"point": 1, "city": "SK-POP", "iata_code": None, "icao_code": None, "lat": 49.059674, "lon": 20.295511, "tm": bus, "name": "Poprad-Tatry Bus Station, LEO"},
            {"point": 1, "city": "SK-POP", "iata_code": None, "icao_code": None, "lat": 49.059101, "lon": 20.293168, "tm": bus, "name": "Poprad-Tatry"}, #A Flixbus surten aquestes dues estacions de bus. Totes dues molt juntes.

            {"point": 0, "city": "SK-SLD", "iata_code": "SLD", "icao_code": "LZSL", "lat": 48.638056, "lon": 19.134167, "tm": flight, "name": "Sliač Airport"}, #No he trobat ni trens, ni bus. Havia una estació de tren però está tencada permanentement
        ]


        hubs_BA = [
            {"point": 0, "city": "BA-BNX", "iata_code": "BNX", "icao_code": "LQBK", "lat": 44.941389, "lon": 17.291944, "tm": flight, "name": "Banja Luka Airport"},
            {"point": 1, "city": "BA-BNX", "iata_code": None, "icao_code": None, "lat": 44.788688, "lon": 17.212506, "tm": train, "name": "Banja Luka Train Station"},
            {"point": 1, "city": "BA-BNX", "iata_code": None, "icao_code": None, "lat": 44.788662, "lon": 17.210019, "tm": bus, "name": "Banja Luka Braće Podgornika"},

            {"point": 1, "city": "BA-BHC", "iata_code": None, "icao_code": None, "lat": 44.818620, "lon": 15.886530, "tm": train, "name": "Bihać Bihaćkih Branilaca"},
            {"point": 2, "city": "BA-BHC", "iata_code": None, "icao_code": None, "lat": 44.814197, "lon": 15.878551, "tm": bus, "name": "Bihać Put Armije Republike Bosne i Hercegovine"},

            {"point": 0, "city": "BA-OMO", "iata_code": "OMO", "icao_code": "LQMO", "lat": 43.282778, "lon": 17.845833, "tm": flight, "name": "Mostar Airport"},
            {"point": 1, "city": "BA-OMO", "iata_code": None, "icao_code": None, "lat": 43.349090, "lon": 17.813537, "tm": train, "name": "Mostar Trg Ivana Krndelja"},
            {"point": 1, "city": "BA-OMO", "iata_code": None, "icao_code": None, "lat": 43.348159, "lon": 17.813391, "tm": bus, "name": "Mostar Maršala Tita"},
            {"point": 2, "city": "BA-OMO", "iata_code": None, "icao_code": None, "lat": 43.351976, "lon": 17.798460, "tm": bus, "name": "Mostar Vukovarska"},

            {"point": 0, "city": "BA-SJJ", "iata_code": "SJJ", "icao_code": "LQSA", "lat": 43.824722, "lon": 18.331389, "tm": flight, "name": "Sarajevo Airport"},
            {"point": 1, "city": "BA-SJJ", "iata_code": None, "icao_code": None, "lat": 43.860164, "lon": 18.399489, "tm": train, "name": "Sarajevo Train Station"},
            {"point": 2, "city": "BA-SJJ", "iata_code": None, "icao_code": None, "lat": 43.858673, "lon": 18.396652, "tm": bus, "name": "Sarajevo Bus Station"},

            {"point": 0, "city": "BA-TZL", "iata_code": "TZL", "icao_code": "LQTZ", "lat": 44.458611, "lon": 18.724722, "tm": flight, "name": "Tuzla Airport"},
            {"point": 1, "city": "BA-TZL", "iata_code": None, "icao_code": None, "lat": 44.532587, "lon": 18.657912, "tm": train, "name": "Tuzla Train Station"},
            {"point": 1, "city": "BA-TZL", "iata_code": None, "icao_code": None, "lat": 44.534855, "lon": 18.657777, "tm": bus, "name": "Tuzla Bosne Srebrene"},

            {"point": 1, "city": "BA-ZCA", "iata_code": None, "icao_code": None, "lat": 44.210159, "lon": 17.912240, "tm": train, "name": "Zenica Train Station"},
            {"point": 1, "city": "BA-ZCA", "iata_code": None, "icao_code": None, "lat": 44.209084, "lon": 17.912559, "tm": bus, "name": "Zenica Bus Station"},
        ]

        hubs_RS = [
            {"point": 0, "city": "RS-BEG", "iata_code": "BEG", "icao_code": "LYBE", "lat": 44.819444, "lon": 20.306944, "tm": flight, "name": "Belgrade Airport"},
            {"point": 1, "city": "RS-BEG", "iata_code": None, "icao_code": None, "lat": 44.793649, "lon": 20.453312, "tm": train, "name": "Belgrade Centar"},
            {"point": 2, "city": "RS-BEG", "iata_code": None, "icao_code": None, "lat": 44.808514, "lon": 20.455728, "tm": train, "name": "Belgrade Železnička"},
            {"point": 2, "city": "RS-BEG", "iata_code": None, "icao_code": None, "lat": 44.810116, "lon": 20.454153, "tm": bus, "name": "Belgrade Železnička"},
            # {"point": 3, "city": "RS-BEG", "iata_code": None, "icao_code": None, "lat": 44.808769, "lon": 20.455458, "tm": bus, "name": "Belgrade Station"},

            # {"point": 0, "city": "RS-BOR", "iata_code": None, "icao_code": "LYBO", "lat": 44.018236, "lon": 22.137136, "tm": flight, "name": "Bor Airport"}, #no iata code --> error when creating url_links
            # {"point": 1, "city": "RS-BOR", "iata_code": None, "icao_code": None, "lat": 44.072857, "lon": 22.102721, "tm": train, "name": "Bor Nikole Pašića"},
            # {"point": 2, "city": "RS-BOR", "iata_code": None, "icao_code": None, "lat": 44.076917, "lon": 22.098267, "tm": bus, "name": "Bor Moše Pijade"},

            {"point": 1, "city": "RS-KGV", "iata_code": None, "icao_code": None, "lat": 44.010384, "lon": 20.927919, "tm": train, "name": "Kragujevac Sumadijska Train Station"},
            {"point": 1, "city": "RS-KGV", "iata_code": None, "icao_code": None, "lat": 44.011135, "lon": 20.928105, "tm": bus, "name": "Kragujevac Sumadijska Bus Station"},

            {"point": 1, "city": "RS-LVC", "iata_code": None, "icao_code": None, "lat": 42.996290, "lon": 21.957047, "tm": train, "name": "Leskovac Train Station"},
            {"point": 1, "city": "RS-LVC", "iata_code": None, "icao_code": None, "lat": 42.996539, "lon": 21.957009, "tm": bus, "name": "Leskovac Bus Station"},

            {"point": 0, "city": "RS-INI", "iata_code": "INI", "icao_code": "LYNI", "lat": 43.337222, "lon": 21.853611, "tm": flight, "name": "Niš Airport"},
            {"point": 1, "city": "RS-INI", "iata_code": None, "icao_code": None, "lat": 43.332622, "lon": 21.881583, "tm": train, "name": "Niš Crveni Krst Bulevar"},
            {"point": 2, "city": "RS-INI", "iata_code": None, "icao_code": None, "lat": 43.316487, "lon": 21.877230, "tm": bus, "name": "Niš Bulevar Bus Station"},

            {"point": 1, "city": "RS-NVS", "iata_code": None, "icao_code":None, "lat": 45.265478, "lon": 19.829557, "tm": train, "name": "Novi Sad Bulevar Jaše Tomića"},
            {"point": 1, "city": "RS-NVS", "iata_code": None, "icao_code":None, "lat": 45.264547, "lon": 19.828417, "tm": bus, "name": "Novi Sad Bulevar Jaše Tomića"},

            {"point": 1, "city": "RS-PYJ", "iata_code": None, "icao_code": None, "lat": 44.870037, "lon": 20.666380, "tm": train, "name": "Pančevo Laze Lazarevića"},
            {"point": 2, "city": "RS-PYJ", "iata_code": None, "icao_code": None, "lat": 44.871029, "lon": 20.648225, "tm": bus, "name": "Pančevo Vojvode Radomira Putnika"},

            # {"point": 1, "city": "RS-PRN", "iata_code": None, "icao_code": None, "lat": 42.658952, "lon": 21.151238, "tm": train, "name": "Priština Tirana"},
            # {"point": 2, "city": "RS-PRN", "iata_code": None, "icao_code": None, "lat": 42.650117, "lon": 21.146865, "tm": bus, "name": "Priština Bus Station"},

            # {"point": 1, "city": "RS-PRZ", "iata_code": None, "icao_code": None, "lat": 42.212854, "lon": 20.729183, "tm": bus, "name": "Prizren Bus Station"},

           {"point": 1, "city": "RS-SUB", "iata_code": None, "icao_code": None, "lat": 46.102116, "lon": 19.670858, "tm": train, "name": "Subotica Train Station"},
           {"point": 1, "city": "RS-SUB", "iata_code": None, "icao_code": None, "lat": 46.101778, "lon": 19.673210, "tm": bus, "name": "Subotica Jovana Mikića"},
           {"point": 2, "city": "RS-SUB", "iata_code": None, "icao_code": None, "lat": 46.095085, "lon": 19.674418, "tm": bus, "name": "Subotica Senćanski put"},
        ]

        hubs_ME = [
            {"point": 0, "city": "ME-TGD", "iata_code": "TGD", "icao_code": "LYPG", "lat": 42.359444, "lon": 19.251944, "tm": flight, "name": "Podgorica Airport"},
            {"point": 1, "city": "ME-TGD", "iata_code": None, "icao_code": None, "lat": 42.432241, "lon": 19.269167, "tm": train, "name": "Podgorica 7 Trg Golootočkih Žrtava Train Station"},
            {"point": 1, "city": "ME-TGD", "iata_code": None, "icao_code": None, "lat": 42.432381, "lon": 19.268193, "tm": bus, "name": "Podgorica 1 Trg Golootočkih Žrtava Bus Station"},

            {"point": 0, "city": "ME-TIV", "iata_code": "TIV", "icao_code": "LYTV", "lat": 42.404722, "lon": 18.723333, "tm": flight, "name": "Tivat Airport"},
            {"point": 1, "city": "ME-TIV", "iata_code": None, "icao_code": None, "lat": 42.422153, "lon": 18.711020, "tm": bus, "name": "Tivat Bus Station"},
        ]

        hubs_CY = [
            {"point": 0, "city": "CY-LCA", "iata_code": "LCA", "icao_code": "LCLK", "lat": 34.8789, "lon": 33.6303, "tm": flight, "name": "Larnaca Airport"},
            {"point": 0, "city": "CY-PFO", "iata_code": "PFO", "icao_code": "LCPH", "lat": 34.7183, "lon": 32.485, "tm": flight, "name": "Paphos Airport"},
            {"point": 0, "city": "CY-NIC", "iata_code": "ECN", "icao_code": "LCEN", "lat": 35.1597, "lon": 33.5, "tm": flight, "name": "Ercan Airport"},
        ]

        hubs_MK = [
            {"point": 0, "city": "MK-OHD", "iata_code": "OHD", "icao_code": "LWOH", "lat": 41.180000, "lon": 20.742222, "tm": flight, "name": "Ohrid Airport"},
            {"point": 1, "city": "MK-OHD", "iata_code": None, "icao_code": None, "lat": 41.124587, "lon": 20.812306, "tm": bus, "name": "Ohrid 7-mi Noemvri"},
            # {"point": 2, "city": "MK-OHD", "iata_code": None, "icao_code": None, "lat": 41.111249, "lon": 20.798534, "tm": ferry, "name": "Ohrid Kosta Abrash"},

            {"point": 0, "city": "MK-SKP", "iata_code": "SKP", "icao_code": "LWSK", "lat": 41.961111, "lon": 21.626944, "tm": flight, "name": "Skopje Airport"},
            {"point": 1, "city": "MK-SKP", "iata_code": None, "icao_code": None, "lat": 41.991261, "lon": 21.446404, "tm": train, "name": "Skopje Railway Station"},
            {"point": 1, "city": "MK-SKP", "iata_code": None, "icao_code": None, "lat": 41.990592, "lon": 21.445810, "tm": bus, "name": "Skopje Bus Station"},
            {"point": 2, "city": "MK-SKP", "iata_code": None, "icao_code": None, "lat": 42.016876, "lon": 21.365193, "tm": train, "name": "Skopje Gjorche Petrov"},
        ]

        hubs_AL = [
            {"point": 1, "city": "AL-DRZ", "iata_code": None, "icao_code": None, "lat": 41.317834, "lon": 19.454685, "tm": train, "name": "Durrës Rruga Adria Train Station"},
            {"point": 1, "city": "AL-DRZ", "iata_code": None, "icao_code": None, "lat": 41.317932, "lon": 19.453887, "tm": bus, "name": "Durrës Rruga Adria Bus Station"},
            # {"point": 2, "city": "AL-DRZ", "iata_code": None, "icao_code": None, "lat": 41.315876, "lon": 19.45446, "tm": ferry, "name": "Durrës Rruga Doganes Ferry Terminal"},

            {"point": 1, "city": "AL-NPP", "iata_code": None, "icao_code": None, "lat": 41.108845, "lon": 20.082639, "tm": bus, "name": "Elbasan Bus Station"},
            {"point": 2, "city": "AL-NPP", "iata_code": None, "icao_code": None, "lat": 41.116407, "lon": 20.089992, "tm": bus, "name": "Elbasan Librazhd Bound Bus"},

            {"point": 0, "city": "AL-TIA", "iata_code": "TIA", "icao_code": "LATI", "lat": 41.414722, "lon": 19.720556, "tm": flight, "name": "Tirana Airport"},
            {"point": 1, "city": "AL-TIA", "iata_code": None, "icao_code": None, "lat": 41.358395, "lon": 19.741220, "tm": train, "name": "Tirana Kashar"},
            {"point": 2, "city": "AL-TIA", "iata_code": None, "icao_code": None, "lat": 41.332995, "lon": 19.801190, "tm": bus, "name": "Tirana International Bus Station"},
            {"point": 3, "city": "AL-TIA", "iata_code": None, "icao_code": None, "lat": 41.338175, "lon": 19.816551, "tm": bus, "name": "Tirana Shkoder"},
            {"point": 4, "city": "AL-TIA", "iata_code": None, "icao_code": None, "lat": 41.327565, "lon": 19.822512, "tm": bus, "name": "Tirana Rruga George W. Bush"},

            {"point": 1, "city": "AL-VOA", "iata_code": None, "icao_code": None, "lat": 40.466058, "lon": 19.482328, "tm": train, "name": "Vlorë Rruga Gjergj Kastrioti"},
            {"point": 1, "city": "AL-VOA", "iata_code": None, "icao_code": None, "lat": 40.464987, "lon": 19.482514, "tm": bus, "name": "Vlorë Intracity Bus Station"},
            {"point": 2, "city": "AL-VOA", "iata_code": None, "icao_code": None, "lat": 40.457691, "lon": 19.470869, "tm": bus, "name": "Vlorë Plazhi i Vjeter"},
            # {"point": 3, "city": "AL-VOA", "iata_code": None, "icao_code": None, "lat": 40.449307, "lon": 19.480745, "tm": ferry, "name": "Vlorë Ferry Terminal"},
        ]

        hubs_RO = [
            {"point": 0, "city": "RO-ARW", "iata_code": "ARW", "icao_code": "LRAR", "lat": 46.176667, "lon": 21.261944, "tm": flight, "name": "Arad Airport"},
            {"point": 1, "city": "RO-ARW", "iata_code":  None, "icao_code":   None, "lat": 46.190708, "lon": 21.324759, "tm": train, "name": "Arad Station"},
            {"point": 1, "city": "RO-ARW", "iata_code":  None, "icao_code":   None, "lat": 46.190516, "lon": 21.319486, "tm": bus, "name": "Arad Transdara"},
            {"point": 2, "city": "RO-ARW", "iata_code":  None, "icao_code":   None, "lat": 46.185428, "lon": 21.316965, "tm": bus, "name": "Arad CTP Station"},

            {"point": 0, "city": "RO-BCM", "iata_code": "BCM", "icao_code": "LRBC", "lat": 46.521944, "lon": 26.910278, "tm": flight, "name": "Bacău George Enescu Airport"},
            {"point": 1, "city": "RO-BCM", "iata_code":  None, "icao_code":   None, "lat": 46.565223, "lon": 26.894676, "tm": train, "name": "Bacău Station"},
            {"point": 1, "city": "RO-BCM", "iata_code":  None, "icao_code":   None, "lat": 46.565898, "lon": 26.895156, "tm": bus, "name": "Bacău Station"},

            # {"point": 0, "city": "RO-BAY", "iata_code": "BAY", "icao_code": "LRBM", "lat": 47.658333, "lon": 23.466389, "tm": flight, "name": "Maramureș Airport"}, # Airport with no flights
            {"point": 1, "city": "RO-BAY", "iata_code":  None, "icao_code":   None, "lat": 47.647314, "lon": 23.552503, "tm": train, "name": "Baia Mare Station"},
            {"point": 1, "city": "RO-BAY", "iata_code":  None, "icao_code":   None, "lat": 47.648659, "lon": 23.551495, "tm": bus, "name": "Baia Mare Station"},

            {"point": 1, "city": "RO-BOS", "iata_code":  None, "icao_code":   None, "lat": 47.753205, "lon": 26.644580, "tm": train, "name": "Botoșani Station"},
            {"point": 2, "city": "RO-BOS", "iata_code":  None, "icao_code":   None, "lat": 47.742295, "lon": 26.665784, "tm": bus, "name": "Botoșani Calea Națională"}, # No ho sé segur

            {"point": 1, "city": "RO-BRA", "iata_code":  None, "icao_code":   None, "lat": 45.281399, "lon": 27.956020, "tm": train, "name": "Brăila Station"},
            {"point": 1, "city": "RO-BRA", "iata_code":  None, "icao_code":   None, "lat": 45.280690, "lon": 27.955870, "tm": bus, "name": "Brăila GSM TRANS"},
            # {"point": 2, "city": "RO-BRA", "iata_code":  None, "icao_code":   None, "lat": 45.279587, "lon": 27.959238, "tm": bus, "name": "Brăila Dorobantilor"}, #nothing found..

            {"point": 1, "city": "RO-BRV", "iata_code":  None, "icao_code":   None, "lat": 45.661236, "lon": 25.613610, "tm": train, "name": "Brașov Station"},
            {"point": 1, "city": "RO-BRV", "iata_code":  None, "icao_code":   None, "lat": 45.660967, "lon": 25.614197, "tm": bus, "name": "Brașov Station"},
            {"point": 2, "city": "RO-BRV", "iata_code":  None, "icao_code":   None, "lat": 45.659797, "lon": 25.570024, "tm": bus, "name": "Brașov Soseaua Cristianului"},

            {"point": 0, "city": "RO-BUH", "iata_code": "OTP", "icao_code": "LROP", "lat": 44.571111, "lon": 26.085000, "tm": flight, "name": "Henri Coandă Airport"},
            {"point": 1, "city": "RO-BUH", "iata_code":  None, "icao_code":   None, "lat": 44.445842, "lon": 26.075029, "tm": train, "name": "Bucharest Northern"},
            {"point": 2, "city": "RO-BUH", "iata_code":  None, "icao_code":   None, "lat": 44.432959, "lon": 26.006244, "tm": bus, "name": "Bucharest Autogari Militari"},
            {"point": 3, "city": "RO-BUH", "iata_code":  None, "icao_code":   None, "lat": 44.3982  , "lon": 26.0432  , "tm": bus, "name": "Bucharest Autogara Internationala Rahova"},
            {"point": 4, "city": "RO-BUH", "iata_code":  None, "icao_code":   None, "lat": 44.448517, "lon": 26.082931, "tm": bus, "name": "Bucharest Strada Buzesti"},

            {"point": 1, "city": "RO-BUZ", "iata_code":  None, "icao_code":   None, "lat": 45.143023, "lon": 26.825855, "tm": train, "name": "Buzău Station"},
            {"point": 2, "city": "RO-BUZ", "iata_code":  None, "icao_code":   None, "lat": 45.137190, "lon": 26.815196, "tm": bus, "name": "Buzău Bulevardul Industriei"},

            {"point": 0, "city": "RO-CLJ", "iata_code": "CLJ", "icao_code": "LRCL", "lat": 46.785000, "lon": 23.686111, "tm": flight, "name": "Cluj Airport"},
            {"point": 1, "city": "RO-CLJ", "iata_code":  None, "icao_code":   None, "lat": 46.784329, "lon": 23.586448, "tm": train, "name": "Cluj Napoca Station"},
            {"point": 2, "city": "RO-CLJ", "iata_code":  None, "icao_code":   None, "lat": 46.786582, "lon": 23.581118, "tm": bus, "name": "Cluj Napoca Giordano Bruno"},

            {"point": 0, "city": "RO-CND", "iata_code": "CND", "icao_code": "LRCK", "lat": 44.362222, "lon": 28.488333, "tm": flight, "name": "Constanța Airport"},
            {"point": 1, "city": "RO-CND", "iata_code":  None, "icao_code":   None, "lat": 44.168813, "lon": 28.632016, "tm": train, "name": "Constanța Station"},
            {"point": 1, "city": "RO-CND", "iata_code":  None, "icao_code":   None, "lat": 44.169161, "lon": 28.632607, "tm": bus, "name": "Constanța Station"},

            {"point": 0, "city": "RO-CRV", "iata_code": "CRA", "icao_code": "LRCV", "lat": 44.318056, "lon": 23.888611, "tm": flight, "name": "Craiova Airport"},
            {"point": 1, "city": "RO-CRV", "iata_code":  None, "icao_code":   None, "lat": 44.328716, "lon": 23.816530, "tm": train, "name": "Craiova Constantin Brâncuși"},
            {"point": 1, "city": "RO-CRV", "iata_code":  None, "icao_code":   None, "lat": 44.328575, "lon": 23.816108, "tm": bus, "name": "Craiova Constantin Brâncuși"},

            {"point": 1, "city": "RO-GAL", "iata_code":  None, "icao_code":   None, "lat": 45.444538, "lon": 28.060416, "tm": train, "name": "Galați Station"},
            {"point": 1, "city": "RO-GAL", "iata_code":  None, "icao_code":   None, "lat": 45.441322, "lon": 28.060229, "tm": bus, "name": "Galați Station"},

            {"point": 0, "city": "RO-IAS", "iata_code": "IAS", "icao_code": "LRIA", "lat": 47.178889, "lon": 27.620000, "tm": flight, "name": "Iași Airport"},
            {"point": 1, "city": "RO-IAS", "iata_code":  None, "icao_code":   None, "lat": 47.165541, "lon": 27.569870, "tm": train, "name": "Iași Station"},
            {"point": 2, "city": "RO-IAS", "iata_code":  None, "icao_code":   None, "lat": 47.168689, "lon": 27.580605, "tm": bus, "name": "Iași Statiua Independentei"},

            {"point": 0, "city": "RO-OMR", "iata_code": "OMR", "icao_code": "LROD", "lat": 47.025278, "lon": 21.902500, "tm": flight, "name": "Oradea Airport"},
            {"point": 1, "city": "RO-OMR", "iata_code":  None, "icao_code":   None, "lat": 47.069843, "lon": 21.935779, "tm": train, "name": "Oradea Piața București"},
            {"point": 2, "city": "RO-OMR", "iata_code":  None, "icao_code":   None, "lat": 47.043074, "lon": 21.958485, "tm": bus, "name": "Oradea Station"},

            {"point": 1, "city": "RO-PIT", "iata_code":  None, "icao_code":   None, "lat": 44.847400, "lon": 24.887456, "tm": train, "name": "Pitești Station"},
            {"point": 2, "city": "RO-PIT", "iata_code":  None, "icao_code":   None, "lat": 44.851935, "lon": 24.885440, "tm": bus, "name": "Pitești Station"},
            {"point": 3, "city": "RO-PIT", "iata_code":  None, "icao_code":   None, "lat": 44.825176, "lon": 24.914918, "tm": bus, "name": "Pitești PIC"},

            {"point": 1, "city": "RO-PLT", "iata_code":  None, "icao_code":   None, "lat": 44.924588, "lon": 25.994649, "tm": train, "name": "Ploiești Vest"},
            {"point": 2, "city": "RO-PLT", "iata_code":  None, "icao_code":   None, "lat": 44.925232, "lon": 26.029587, "tm": train, "name": "Ploiești Sud"},
            {"point": 2, "city": "RO-PLT", "iata_code":  None, "icao_code":   None, "lat": 44.925272, "lon": 26.026711, "tm": bus, "name": "Ploiești Station"},

            {"point": 0, "city": "RO-SUJ", "iata_code": "SUJ", "icao_code": "LRSM", "lat": 47.703333, "lon": 22.885556, "tm": flight, "name": "Satu Mare Airport"},
            {"point": 1, "city": "RO-SUJ", "iata_code":  None, "icao_code":   None, "lat": 47.795459, "lon": 22.892716, "tm": train, "name": "Satu Mare Szatmarnemeti"},
            {"point": 1, "city": "RO-SUJ", "iata_code":  None, "icao_code":   None, "lat": 47.795313, "lon": 22.892217, "tm": bus, "name": "Satu Mare Station"},

            {"point": 0, "city": "RO-SBZ", "iata_code": "SBZ", "icao_code": "LRSB", "lat": 45.785833, "lon": 24.085556, "tm": flight, "name": "Sibiu Airport"},
            {"point": 0, "city": "RO-SBZ", "iata_code":  None, "icao_code":   None, "lat": 45.795483, "lon": 24.087485, "tm": bus, "name": "Sibiu Auropa Unita Airport"},
            {"point": 1, "city": "RO-SBZ", "iata_code":  None, "icao_code":   None, "lat": 45.800033, "lon": 24.161434, "tm": train, "name": "Sibiu Station"},
            {"point": 2, "city": "RO-SBZ", "iata_code":  None, "icao_code":   None, "lat": 45.784316, "lon": 24.144856, "tm": bus, "name": "Sibiu Q7"},
            {"point": 3, "city": "RO-SBZ", "iata_code":  None, "icao_code":   None, "lat": 45.793869, "lon": 24.130452, "tm": bus, "name": "Sibiu Station"},

            {"point": 0, "city": "RO-SCV", "iata_code": "SCV", "icao_code": "LRSV", "lat": 47.687500, "lon": 26.354167, "tm": flight, "name": "Suceava Airport"},
            {"point": 1, "city": "RO-SCV", "iata_code":  None, "icao_code":   None, "lat": 47.670624, "lon": 26.266216, "tm": train, "name": "Suceava Gara"},
            {"point": 1, "city": "RO-SCV", "iata_code":  None, "icao_code":   None, "lat": 47.671342, "lon": 26.267098, "tm": bus, "name": "Suceava Burdujeni"},
            {"point": 2, "city": "RO-SCV", "iata_code":  None, "icao_code":   None, "lat": 47.667960, "lon": 26.273625, "tm": bus, "name": "Suceava Station"},

            {"point": 0, "city": "RO-TGM", "iata_code": "TGM", "icao_code": "LRTM", "lat": 46.467778, "lon": 24.412500, "tm": flight, "name": "Târgu Mureș Airport"},
            {"point": 1, "city": "RO-TGM", "iata_code":  None, "icao_code":   None, "lat": 46.533375, "lon": 24.549306, "tm": train, "name": "Târgu Mureș Station"},
            {"point": 2, "city": "RO-TGM", "iata_code":  None, "icao_code":   None, "lat": 46.527324, "lon": 24.544880, "tm": bus, "name": "Târgu Mureș Station"},

            {"point": 0, "city": "RO-TSR", "iata_code": "TSR", "icao_code": "LRTR", "lat": 45.810000, "lon": 21.338056, "tm": flight, "name": "Timișoara Airport"},
            {"point": 0, "city": "RO-TSR", "iata_code":  None, "icao_code":   None, "lat": 45.810185, "lon": 21.319230, "tm": bus, "name": "Timișoara Station Airport"},
            {"point": 1, "city": "RO-TSR", "iata_code":  None, "icao_code":   None, "lat": 45.750781, "lon": 21.207712, "tm": train, "name": "Timișoara Nord"},
            {"point": 1, "city": "RO-TSR", "iata_code":  None, "icao_code":   None, "lat": 45.750593, "lon": 21.207947, "tm": bus, "name": "Timișoara Nord"},
            {"point": 2, "city": "RO-TSR", "iata_code":  None, "icao_code":   None, "lat": 45.716112, "lon": 21.202986, "tm": train, "name": "Timișoara Sud"},
            {"point": 3, "city": "RO-TSR", "iata_code":  None, "icao_code":   None, "lat": 45.745640, "lon": 21.254296, "tm": bus, "name": "Timișoara Normandia"},
            {"point": 4, "city": "RO-TSR", "iata_code":  None, "icao_code":   None, "lat": 45.745780, "lon": 21.206629, "tm": bus, "name": "Timișoara Splaiul Tudor Vladimirescu 30"},
        ]

        hubs_BG = [
            {"point": 0, "city": "BG-BOJ", "iata_code": "BOJ", "icao_code": "LBBG", "lat": 42.570278, "lon": 27.515278, "tm": flight, "name": "Burgas Airport"},
            {"point": 1, "city": "BG-BOJ", "iata_code": None, "icao_code": None, "lat": 42.491052, "lon": 27.472654, "tm": train, "name": 'Burgas bul. "Ivan Vazov" 1'},
            {"point": 1, "city": "BG-BOJ", "iata_code": None, "icao_code": None, "lat": 42.490401, "lon": 27.473628, "tm": bus, "name": "Burgas FlixBus" },
            {"point": 2, "city": "BG-BOJ", "iata_code": None, "icao_code": None, "lat": 42.503075, "lon": 27.458136, "tm": bus, "name": "Burgas Arda Tur" },

            {"point": 1, "city": "BG-PVN", "iata_code": None, "icao_code": None, "lat": 43.420877, "lon": 24.614493, "tm": train, "name": "Pleven Train Station"},
            {"point": 1, "city": "BG-PVN", "iata_code": None, "icao_code": None, "lat": 43.420092, "lon": 24.615663, "tm": bus, "name": "Pleven 5805 ж.к. Воден Bus Station"},

            {"point": 0, "city": "BG-PDV", "iata_code": "PDV", "icao_code": "LBPD", "lat": 42.067778, "lon": 24.864722, "tm": flight, "name": "Plovdiv Airport"},
            {"point": 1, "city": "BG-PDV", "iata_code": None, "icao_code": None, "lat": 42.134471, "lon": 24.741528, "tm": train, "name": "Plovdiv бул. „Христо Ботев“ 46"},
            {"point": 1, "city": "BG-PDV", "iata_code": None, "icao_code": None, "lat": 42.135525, "lon": 24.744267, "tm": bus, "name": "Plovdiv 4000 Tsentar"},
            {"point": 2, "city": "BG-PDV", "iata_code": None, "icao_code": None, "lat": 42.164709, "lon": 24.736183, "tm": bus, "name": "Plovdiv Dimitar Stambolov Str 2"},

            {"point": 1, "city": "BG-RDU", "iata_code": None, "icao_code": None, "lat": 43.833533, "lon": 25.956120, "tm": train, "name": "Ruse Central Railway Station"}, #Ruse 7001 Tsentralna Zhp Gara
            {"point": 1, "city": "BG-RDU", "iata_code": None, "icao_code": None, "lat": 43.834915, "lon": 25.957791, "tm": bus, "name": "Ruse South / Central Railway Station"},
            # {"point": 2, "city": "BG-RDU", "iata_code": None, "icao_code": None, "lat": 43.839286, "lon": 25.943976, "tm": train, "name": 'Ruse ul. "Pristanishtna" 6'}, # Goods train station
            {"point": 3, "city": "BG-RDU", "iata_code": None, "icao_code": None, "lat": 43.855597, "lon": 25.997937, "tm": bus, "name": "Ruse East"},

            {"point": 0, "city": "BG-SOF", "iata_code": "SOF", "icao_code": "LBSF", "lat": 42.695000, "lon": 23.408333, "tm": flight, "name": "Sofia Airport"},
            {"point": 1, "city": "BG-SOF", "iata_code": None, "icao_code": None, "lat": 42.712069, "lon": 23.320740, "tm": train, "name": "Sofia бул. Княгиня Мария Луиза 102А"},
            {"point": 1, "city": "BG-SOF", "iata_code": None, "icao_code": None, "lat": 42.710042, "lon": 23.323238, "tm": bus, "name": 'Sofia bulevard "Knyaginya Maria Luiza" 100'},

            {"point": 1, "city": "BG-SZR", "iata_code": None, "icao_code": None, "lat": 42.416268, "lon": 25.629380, "tm": train, "name": "Stara Zagora ул. „Герасим Папазчев“ 20"},
            {"point": 1, "city": "BG-SZR", "iata_code": None, "icao_code": None, "lat": 42.420007, "lon": 25.632614, "tm": bus, "name": "Stara Zagora 6002 Promishlena Zona Zapad"},

            {"point": 0, "city": "BG-VAR", "iata_code": "VAR", "icao_code": "LBWN", "lat": 43.231944, "lon": 27.825278, "tm": flight, "name": "Varna Airport"},
            {"point": 1, "city": "BG-VAR", "iata_code": None, "icao_code": None, "lat": 43.198403, "lon": 27.912257, "tm": train, "name": "Varna пл. Петко Славейков 1"},
            {"point": 2, "city": "BG-VAR", "iata_code": None, "icao_code": None, "lat": 43.215978, "lon": 27.897220, "tm": bus, "name": "Varna bul. Vladislav Varnenchik 158"},
            # {"point": 3, "city": "BG-VAR", "iata_code": None, "icao_code": None, "lat": 43.191399, "lon": 27.917355, "tm": bus, "name": "Varna bul. Vladislav Varnenchik 158"},
        ]

        hubs_RU = [
            {"point": 0, "city": "RU-MOW", "iata_code": "DME", "icao_code": "UUDD", "lat": 55.410307, "lon": 37.902436, "tm": flight, "name": "Moscow Domodedovo"},
            {"point": 1, "city": "RU-MOW", "iata_code": "SVO", "icao_code": "UUEE", "lat": 55.973768, "lon": 37.412439, "tm": flight, "name": "Moscow Sheremetyevo"},
            {"point": 2, "city": "RU-MOW", "iata_code": "VKO", "icao_code": "UUWW", "lat": 55.599763, "lon": 37.271245, "tm": flight, "name": "Moscow Vnukovo"},
            {"point": 3, "city": "RU-MOW", "iata_code": "ZIA", "icao_code": "UUBW", "lat": 55.562051, "lon": 38.117983, "tm": flight, "name": "Moscow Zhukovsky"},
            {"point": 5, "city": "RU-MOW", "iata_code":  None, "icao_code":   None, "lat": 55.776919, "lon": 37.581484, "tm": train, "name": "Moscow Belorusskaya"},

            {"point": 0, "city": "RU-LED", "iata_code": "LED", "icao_code": "ULLI", "lat": 59.803015, "lon": 30.267785, "tm": flight, "name": "Saint Petersburg Pulkovo"},

            {"point": 0, "city": "RU-KGD", "iata_code": "KGD", "icao_code": "UMKK", "lat": 54.883029, "lon": 20.586563, "tm": flight, "name": "Kaliningrad Khrabrovo"},

            {"point": 0, "city": "RU-KZN", "iata_code": "KZN", "icao_code": "UWKD", "lat": 55.607411, "lon": 49.300805, "tm": flight, "name": "Kazan Airport"},

            # {"point": 0, "city": "RU-KRR", "iata_code": "KRR", "icao_code": "URKK", "lat": 45.031790, "lon": 39.166692, "tm": flight, "name": "Krasnodar Airport"},

            {"point": 0, "city": "RU-GOJ", "iata_code": "GOJ", "icao_code": "UWGG", "lat": 56.225850, "lon": 43.784304, "tm": flight, "name": "Nizhny Novgorod Strigino"},

            {"point": 0, "city": "RU-KUF", "iata_code": "KUF", "icao_code": "UWWW", "lat": 53.512314, "lon": 50.157379, "tm": flight, "name": "Samara Kurumoch"},

            # {"point": 0, "city": "RU-UFA", "iata_code": "UFA", "icao_code": "UWUU", "lat": 54.563611, "lon": 55.880278, "tm": flight, "name": "Ufa Airport"},

            {"point": 0, "city": "RU-VOG", "iata_code": "VOG", "icao_code": "URWW", "lat": 48.792223, "lon": 44.356227, "tm": flight, "name": "Volgograd Airport"},

            {"point": 0, "city": "RU-SKX", "iata_code": "SKX", "icao_code": "UWPS", "lat": 54.147508, "lon": 45.221776, "tm": flight, "name": "Saransk Airport"},

            {"point": 0, "city": "RU-RND", "iata_code": "ROV", "icao_code": "URRR", "lat": 47.254934, "lon": 39.803188, "tm": flight, "name": "Rostov-on-Don Airport"},

            {"point": 0, "city": "RU-AER", "iata_code": "AER", "icao_code": "URSS", "lat": 43.448888, "lon": 39.942035, "tm": flight, "name": "Sochi Airport"},

            {"point": 0, "city": "RU-YEK", "iata_code": "SVX", "icao_code": "USSS", "lat": 56.744816, "lon": 60.802948, "tm": flight, "name": "Yekaterinburg Koltsovo"},
        ]

        hubs_GI = [
            {"point": 0, "city": "GI-GIB", "iata_code": "GIB", "icao_code":"LXGB", "lat": 36.151965, "lon": -5.346739, "tm": flight, "name": "Gibraltar Airport"},
            {"point": 1, "city": "GI-GIB", "iata_code":  None, "icao_code":  None, "lat": 36.157990, "lon": -5.349992, "tm": bus, "name": "La Línea de la Concepción (ES)"},
        ]


        hubs_UA = [
            {"point": 1, "city": "UA-ACK", "iata_code": None, "icao_code": None, "lat": 48.483425, "lon": 38.778780, "tm": train, "name": "Alchevsk Train Station"},
            {"point": 2, "city": "UA-ACK", "iata_code": None, "icao_code": None, "lat": 48.467736, "lon": 38.820216, "tm": bus, "name": "Alchevsk Train Popova St"},

            {"point": 1, "city": "UA-ERD", "iata_code": None, "icao_code": None, "lat": 46.750962, "lon": 36.803710, "tm": train, "name": "Berdyansk Train Station"},
            {"point": 2, "city": "UA-ERD", "iata_code": None, "icao_code": None, "lat": 46.759076, "lon": 36.778201, "tm": bus, "name": "Berdyansk Bus Station"},

            {"point": 1, "city": "UA-BZW", "iata_code": None, "icao_code": None, "lat": 49.811909, "lon": 30.109716, "tm": train, "name": "Bila Tserkva Train Station"},
            {"point": 1, "city": "UA-BZW", "iata_code": None, "icao_code": None, "lat": 49.811519, "lon": 30.109254, "tm": bus, "name": "Bila Tserkva Bus Station"},

            # DELETE CITY: population 56000 and airport included in Kiev
            # {"point": 0, "city": "UA-KBP", "iata_code": "KBP", "icao_code": "UKBB", "lat": 50.344722, "lon": 30.893333, "tm": flight, "name": "Borýspil Airport"},
            {"point": 0, "city": "UA-KBP", "iata_code": None, "icao_code": None, "lat": 50.342793, "lon": 30.895522, "tm": train, "name": "Borýspil Bus Station Airport"},
            {"point": 1, "city": "UA-KBP", "iata_code": None, "icao_code": None, "lat": 50.376675, "lon": 30.944786, "tm": train, "name": "Borýspil Train Station"},
            {"point": 2, "city": "UA-KBP", "iata_code": None, "icao_code": None, "lat": 50.355584, "lon": 30.989081, "tm": bus, "name": "Borýspil Train Bezhivka St 164"},

            {"point": 1, "city": "UA-ZUQ", "iata_code": None, "icao_code": None, "lat": 51.485868, "lon": 31.267246, "tm": train, "name": "Chernihiv Train Station"},
            {"point": 1, "city": "UA-ZUQ", "iata_code": None, "icao_code": None, "lat": 51.486017, "lon": 31.267603, "tm": bus, "name": "Chernihiv Bus Station"},

            {"point": 0, "city": "UA-CWC", "iata_code": "CWC", "icao_code": "UKLN", "lat": 48.258889, "lon": 25.981111, "tm": flight, "name": "Chernivtsi Airport"},
            {"point": 1, "city": "UA-CWC", "iata_code": None, "icao_code": None, "lat": 48.301070, "lon": 25.930038, "tm": train, "name": "Chernivtsi Train Station"},
            {"point": 2, "city": "UA-CWC", "iata_code": None, "icao_code": None, "lat": 48.264883, "lon": 25.951997, "tm": bus, "name": "Chernivtsi Bus Station"},

            {"point": 0, "city": "UA-DNK", "iata_code": "DNK", "icao_code": "UKDD", "lat": 48.357222, "lon": 35.100556, "tm": flight, "name": "Dnipropetrovsk Airport"}, # He baratat el que posava es teu...
            {"point": 1, "city": "UA-DNK", "iata_code": None, "icao_code": None, "lat": 48.477470, "lon": 35.015097, "tm": train, "name": "Dnipropetrovsk Train Station"},
            {"point": 2, "city": "UA-DNK", "iata_code": None, "icao_code": None, "lat": 48.474805, "lon": 35.008919, "tm": bus, "name": "Dnipropetrovsk Bus Station"},

            {"point": 1, "city": "UA-DOK", "iata_code": None, "icao_code": None, "lat": 48.043890, "lon": 37.746194, "tm": train, "name": "Donetsk Train Station"},
            {"point": 2, "city": "UA-DOK", "iata_code": None, "icao_code": None, "lat": 47.991461, "lon": 37.795722, "tm": bus, "name": "Donetsk Bus Pivdennyi"},

            {"point": 1, "city": "UA-HOR", "iata_code": None, "icao_code": None, "lat": 48.311233, "lon": 38.044148, "tm": train, "name": "Hórlivka Train Station"},
            {"point": 2, "city": "UA-HOR", "iata_code": None, "icao_code": None, "lat": 48.296280, "lon": 38.030021, "tm": bus, "name": "Hórlivka Bus Station"},

            {"point": 0, "city": "UA-IFO", "iata_code": "IFO", "icao_code": "UKLI", "lat": 48.884167, "lon": 24.686111, "tm": flight, "name": "Ivano-Frankivsk Airport"},
            {"point": 1, "city": "UA-IFO", "iata_code": None, "icao_code": None, "lat": 48.925276, "lon": 24.723522, "tm": train, "name": "Ivano-Frankivsk Train Station"},
            {"point": 2, "city": "UA-IFO", "iata_code": None, "icao_code": None, "lat": 48.922067, "lon": 24.724795, "tm": bus, "name": "Ivano-Frankivsk Bus Zaliznychna 30"},

            {"point": 1, "city": "UA-KHM", "iata_code": None, "icao_code": None, "lat": 49.441864, "lon": 26.930515, "tm": train, "name": "Jmelnitski Train Station"},
            {"point": 2, "city": "UA-KHM", "iata_code": None, "icao_code": None, "lat": 49.429675, "lon": 26.982556, "tm": bus, "name": "Jmelnitski Bus Station"},

            {"point": 1, "city": "UA-DZK", "iata_code": None, "icao_code": None, "lat": 49.497513, "lon": 34.6042015, "tm": train, "name": "Kamianské Train Station"},
            {"point": 1, "city": "UA-DZK", "iata_code": None, "icao_code": None, "lat": 49.497822, "lon": 34.604165, "tm": bus, "name": "Kamianské Bus Station"},

            {"point": 1, "city": "UA-KEH", "iata_code": None, "icao_code": None, "lat": 45.359215, "lon": 36.483581, "tm": train, "name": "Kerch Train Port Station"},
            {"point": 2, "city": "UA-KEH", "iata_code": None, "icao_code": None, "lat": 45.362422, "lon": 36.470595, "tm": bus, "name": "Kerch Bus Station"},
            #{"point": 3, "city": "UA-KEH", "iata_code": None, "icao_code": None, "lat": 45.359048, "lon": 36.483698, "tm": ferry, "name": "Kerch Ferry Terminal"},
            #{"point": 4, "city": "UA-KEH", "iata_code": None, "icao_code": None, "lat": 45.356286, "lon": 36.476920, "tm": ferry, "name": "Kerch Ferry Terminal"},
            #{"point": 5, "city": "UA-KEH", "iata_code": None, "icao_code": None, "lat": 45.364625, "lon": 36.626353, "tm": ferry, "name": "Kerch Ferry Terminal"},

            {"point": 0, "city": "UA-KIV", "iata_code": "HRK", "icao_code": "UKHH", "lat": 49.924722, "lon": 36.290000, "tm": flight, "name": "Kharkiv Airport"},
            {"point": 1, "city": "UA-KIV", "iata_code": None, "icao_code": None, "lat": 49.989579, "lon": 36.204319, "tm": train, "name": "Kharkiv Train Station"},
            {"point": 2, "city": "UA-KIV", "iata_code": None, "icao_code": None, "lat": 49.978980, "lon": 36.247460, "tm": bus, "name": "Kharkiv Bus Station"},

            {"point": 0, "city": "UA-KHE", "iata_code": "KHE", "icao_code": "UKOH", "lat": 46.668056, "lon": 32.502222, "tm": flight, "name": "Kherson Airport"},
            {"point": 1, "city": "UA-KHE", "iata_code": None, "icao_code": None, "lat": 46.656239, "lon": 32.604868, "tm": train, "name": "Kherson Train Station"},
            {"point": 2, "city": "UA-KHE", "iata_code": None, "icao_code": None, "lat": 46.660504, "lon": 32.593754, "tm": bus, "name": "Kherson Bus Station"},

            {"point": 0, "city": "UA-IEV", "iata_code": "KBP", "icao_code": "UKBB", "lat": 50.344722, "lon": 30.893333, "tm": flight, "name": "Kiev Borýspil Airport"},
            {"point": 1, "city": "UA-IEV", "iata_code": None, "icao_code": None, "lat": 50.440393, "lon": 30.489463, "tm": train, "name": "Kiev Train Vokzalna St, 1"},
            {"point": 2, "city": "UA-IEV", "iata_code": None, "icao_code": None, "lat": 50.442328, "lon": 30.495393, "tm": bus, "name": "Kiev Bus Simona Petlyury 32"},
            {"point": 3, "city": "UA-IEV", "iata_code": None, "icao_code": None, "lat": 50.455370, "lon": 30.350138, "tm": bus, "name": "Kiev Bus Prospekt Peremogy 142"},
            {"point": 4, "city": "UA-IEV", "iata_code": "IEV", "icao_code": "UKKK", "lat": 50.4017, "lon": 30.4517, "tm": flight, "name": "Kiev Zhuliany Airport"},

            {"point": 1, "city": "UA-KIR", "iata_code": None, "icao_code": None, "lat": 48.523735, "lon": 32.259987, "tm": train, "name": "Kirovogrado Train Station"},
            {"point": 2, "city": "UA-KIR", "iata_code": None, "icao_code": None, "lat": 48.527687, "lon": 32.288790, "tm": bus, "name": "Kirovogrado Bus Leytenanta Shmidta, 48"},

            {"point": 1, "city": "UA-KRQ", "iata_code": None, "icao_code": None, "lat": 48.726274, "lon": 37.544200, "tm": train, "name": "Kramatorsk Train Station"},
            {"point": 2, "city": "UA-KRQ", "iata_code": None, "icao_code": None, "lat": 48.735841, "lon": 37.576239, "tm": bus, "name": "Kramatorsk Bus Mashynobudivnykiv Blvd 28"},

            {"point": 1, "city": "UA-KRE", "iata_code": None, "icao_code": None, "lat": 49.067902, "lon": 33.427722, "tm": train, "name": "Kremenchuk Train Station"},
            {"point": 1, "city": "UA-KRE", "iata_code": None, "icao_code": None, "lat": 49.064226, "lon": 33.421886, "tm": bus, "name": "Kremenchuk Bus Teatralna St, 32/6"},

            {"point": 0, "city": "UA-KWR", "iata_code": "KWG", "icao_code": "UKDR", "lat": 48.043056, "lon": 33.206944, "tm": flight, "name": "Kryvyi Rih Airport"},
            {"point": 1, "city": "UA-KWR", "iata_code": None, "icao_code": None, "lat": 47.912492, "lon": 33.451359, "tm": train, "name": "Kryvyi Rih Train Station"},
            {"point": 2, "city": "UA-KWR", "iata_code": None, "icao_code": None, "lat": 47.909427, "lon": 33.423324, "tm": bus, "name": "Kryvyi Rih Bus Station"},

            {"point": 1, "city": "UA-VSG", "iata_code": None, "icao_code": None, "lat": 48.575793, "lon": 39.288657, "tm": train, "name": "Lugansk Train Station"},
            {"point": 2, "city": "UA-VSG", "iata_code": None, "icao_code": None, "lat": 48.544692, "lon": 39.335324, "tm": bus, "name": "Lugansk Bus Station"},

            {"point": 1, "city": "UA-UCK", "iata_code": None, "icao_code": None, "lat": 50.757946, "lon": 25.350688, "tm": train, "name": "Lutsk Train Station"},
            {"point": 2, "city": "UA-UCK", "iata_code": None, "icao_code": None, "lat": 50.723102, "lon": 25.292606, "tm": bus, "name": "Lutsk Bus Station"},

            {"point": 0, "city": "UA-LVV", "iata_code": "LWO", "icao_code": "UKLL", "lat": 49.812500, "lon": 23.956111, "tm": flight, "name": "Lviv Danylo Halytskyi Airport"},
            {"point": 1, "city": "UA-LVV", "iata_code":  None, "icao_code":  None, "lat": 49.839216, "lon": 23.994421, "tm": train, "name": "Lviv Train Station"},
            {"point": 2, "city": "UA-LVV", "iata_code":  None, "icao_code": None, "lat": 49.786792, "lon": 24.016245, "tm": bus, "name": "Lviv Bus Stryiska St, 109"},

            {"point": 1, "city": "UA-ISI", "iata_code": None, "icao_code": None, "lat": 48.915110, "lon": 38.453189, "tm": train, "name": "Lysychansk Train Station"},
            {"point": 2, "city": "UA-ISI", "iata_code": None, "icao_code": None, "lat": 48.921152, "lon": 38.405116, "tm": bus, "name": "Lysychansk Bus Station"},

            {"point": 1, "city": "UA-MKV", "iata_code": None, "icao_code": None, "lat": 48.007698, "lon": 37.981546, "tm": train, "name": "Makiivka Train Station"},
            {"point": 2, "city": "UA-MKV", "iata_code": None, "icao_code": None, "lat": 48.043066, "lon": 37.959729, "tm": bus, "name": "Makiivka Bus Station"},

            {"point": 1, "city": "UA-MPW", "iata_code": None, "icao_code": None, "lat": 47.052383, "lon": 37.555062, "tm": train, "name": "Mariupol Train Station"},
            {"point": 2, "city": "UA-MPW", "iata_code": None, "icao_code": None, "lat": 47.052383, "lon": 37.555062, "tm": bus, "name": "Mariupol Bus Station #2"},

            {"point": 1, "city": "UA-ZZO", "iata_code": None, "icao_code": None, "lat": 46.868074, "lon": 35.356870, "tm": train, "name": "Melitopol' Train Station"},
            {"point": 2, "city": "UA-ZZO", "iata_code": None, "icao_code": None, "lat": 46.852238, "lon": 35.360480, "tm": bus, "name": "Melitopol' Bus Oleksandra Chyhrina St"},

            {"point": 1, "city": "UA-NLV", "iata_code": None, "icao_code": None, "lat": 46.938400, "lon": 32.061863, "tm": train, "name": "Mykolaiv Train Station"},
            {"point": 2, "city": "UA-NLV", "iata_code": None, "icao_code": None, "lat": 46.968313, "lon": 31.973411, "tm": bus, "name": "Mykolaiv Bus Station"},

            {"point": 1, "city": "UA-POL", "iata_code": None, "icao_code": None, "lat": 47.585374, "lon": 34.391364, "tm": train, "name": "Nikopol’ Train Station"},
            {"point": 2, "city": "UA-POL", "iata_code": None, "icao_code": None, "lat": 47.582377, "lon": 34.384938, "tm": bus, "name": "Nikopol’ Bus Station"},

            {"point": 0, "city": "UA-ODS", "iata_code": "ODS", "icao_code": "UKOO", "lat": 46.426944, "lon": 30.6780586, "tm": flight, "name": "Odessa Airport"},
            {"point": 1, "city": "UA-ODS", "iata_code": None, "icao_code": None, "lat": 46.467738, "lon": 30.740545, "tm": train, "name": "Odessa Train Holovna"},
            {"point": 1, "city": "UA-ODS", "iata_code": None, "icao_code": None, "lat": 46.467607, "lon": 30.736760, "tm": bus, "name": "Odessa Bus Novoshchipnyi Ryad St"},
            {"point": 2, "city": "UA-ODS", "iata_code": None, "icao_code": None, "lat": 46.476848, "lon": 30.708571, "tm": bus, "name": "Odessa Bus Kolontaivs'ka St"},
            {"point": 3, "city": "UA-ODS", "iata_code": None, "icao_code": None, "lat": 46.465098, "lon": 30.735868, "tm": bus, "name": "Odessa Bus Starosinna Square"},

            {"point": 1, "city": "UA-PAH", "iata_code": None, "icao_code": None, "lat": 48.549659, "lon": 35.856478, "tm": train, "name": "Pavlohrad Train Station"},
            {"point": 2, "city": "UA-PAH", "iata_code": None, "icao_code": None, "lat": 48.494348, "lon": 35.938018, "tm": bus, "name": "Pavlohrad Bus Dniprovska St"},

            {"point": 1, "city": "UA-PLV", "iata_code": None, "icao_code": None, "lat": 49.603379, "lon": 34.525760, "tm": train, "name": "Poltava Train Station"},
            {"point": 2, "city": "UA-PLV", "iata_code": None, "icao_code": None, "lat": 49.582176, "lon": 34.594825, "tm": train, "name": "Poltava Pivdenna"},
            {"point": 2, "city": "UA-PLV", "iata_code": None, "icao_code": None, "lat": 49.581749, "lon": 34.593179, "tm": bus, "name": "Poltava Pivdenna"},
            {"point": 3, "city": "UA-PLV", "iata_code": None, "icao_code": None, "lat": 49.566595, "lon": 34.490860, "tm": bus, "name": "Poltava Velykotyrnivs'ka St"},

            {"point": 1, "city": "UA-RIV", "iata_code": None, "icao_code": None, "lat": 50.627663, "lon": 26.239814, "tm": train, "name": "Rivne Train Station"},
            {"point": 2, "city": "UA-RIV", "iata_code": None, "icao_code": None, "lat": 50.614720, "lon": 26.282689, "tm": bus, "name": "Rivne Bus Station"},

            {"point": 1, "city": "UA-ZUC", "iata_code": None, "icao_code": None, "lat": 48.957634, "lon": 38.466153, "tm": train, "name": "Sievierodonetsk Train Station"},
            {"point": 2, "city": "UA-ZUC", "iata_code": None, "icao_code": None, "lat": 48.951989, "lon": 38.508619, "tm": bus, "name": "Sievierodonetsk Bus Station"},

            {"point": 0, "city": "UA-SIP", "iata_code": "SIP", "icao_code": None, "lat": 45.051944, "lon": 33.973611, "tm": flight, "name": "Simferopol Airport"},
            {"point": 0, "city": "UA-SIP", "iata_code": None, "icao_code": None, "lat": 45.020720, "lon": 34.000576, "tm": bus, "name": "Simferopol Bus Airport Terminal"},
            {"point": 1, "city": "UA-SIP", "iata_code": None, "icao_code": None, "lat": 44.961827, "lon": 34.082531, "tm": train, "name": "Simferopol Train Station"}, # Sembla que està tencada permanentement
            {"point": 2, "city": "UA-SIP", "iata_code": None, "icao_code": None, "lat": 44.948286, "lon": 34.125942, "tm": bus, "name": "Simferopol Bus Station"},

            {"point": 1, "city": "UA-SYA", "iata_code": None, "icao_code": None, "lat": 48.831673, "lon": 37.560154, "tm": train, "name": "Sloviansk Train Station"},
            {"point": 2, "city": "UA-SYA", "iata_code": None, "icao_code": None, "lat": 48.846283, "lon": 37.593300, "tm": bus, "name": "Sloviansk Bus Station"},

            {"point": 1, "city": "UA-UMY", "iata_code": None, "icao_code": None, "lat": 50.926944, "lon": 34.808752, "tm": train, "name": "Sumy Train Station"},
            {"point": 2, "city": "UA-UMY", "iata_code": None, "icao_code": None, "lat": 50.915085, "lon": 34.770217, "tm": bus, "name": "Sumy Bus Station"},

            {"point": 1, "city": "UA-TNL", "iata_code": None, "icao_code": None, "lat": 49.553743, "lon": 25.600691, "tm": train, "name": "Ternópil Train Station"},
            {"point": 2, "city": "UA-TNL", "iata_code": None, "icao_code": None, "lat": 49.544081, "lon": 25.596986, "tm": bus, "name": "Ternópil Bus Station"},

            {"point": 1, "city": "UA-UZH", "iata_code": None, "icao_code": None, "lat": 48.609501, "lon": 22.300688, "tm": train, "name": "Úzhgorod Train Stantsiina St, 9"},
            {"point": 1, "city": "UA-UZH", "iata_code": None, "icao_code": None, "lat": 48.609525, "lon": 22.298054, "tm": bus, "name": "Úzhgorod Bus Station"},

            {"point": 0, "city": "UA-VIN", "iata_code": "VIN", "icao_code": "UKWW", "lat": 49.239722, "lon": 28.613889, "tm": flight, "name": "Havryshivka Airport"},
            {"point": 1, "city": "UA-VIN", "iata_code": None, "icao_code": None, "lat": 49.239289, "lon": 28.510635, "tm": train, "name": "Havryshivka Train Station"},
            {"point": 2, "city": "UA-VIN", "iata_code": None, "icao_code": None, "lat": 49.237034, "lon": 28.404095, "tm": bus, "name": "Havryshivka Bus Station"},

            {"point": 1, "city": "UA-YEN", "iata_code": None, "icao_code": None, "lat": 48.225907, "lon": 38.203234, "tm": train, "name": "Yenákiyeve Train Station"},
            {"point": 2, "city": "UA-YEN", "iata_code": None, "icao_code": None, "lat": 48.215639, "lon": 38.211712, "tm": bus, "name": "Yenákiyeve Bus Station"},

            {"point": 0, "city": "UA-ZPR", "iata_code": "OZH", "icao_code": "UKDE", "lat": 47.866944, "lon": 35.315833, "tm": flight, "name": "Zaporizhia Airport"},
            {"point": 1, "city": "UA-ZPR", "iata_code": None, "icao_code": None, "lat": 47.852889, "lon": 35.129164, "tm": train, "name": "Zaporizhia Train Station"},
            {"point": 2, "city": "UA-ZPR", "iata_code": None, "icao_code": None, "lat": 47.849019, "lon": 35.131150, "tm": bus, "name": "Zaporizhia Bus Station"},

            {"point": 1, "city": "UA-ZTR", "iata_code": None, "icao_code": None, "lat": 50.267893, "lon": 28.697509, "tm": train, "name": "Zhytómyr Railways Station"},
            {"point": 1, "city": "UA-ZTR", "iata_code": None, "icao_code": None, "lat": 50.268389, "lon": 28.692186, "tm": bus, "name": "Zhytómyr Railways Station"},
            # {"point": 2, "city": "UA-ZTR", "iata_code": None, "icao_code": None, "lat": 50.254251, "lon": 28.658721, "tm": bus, "name": "Zhytómyr Bus Station"},

        ]

        hubs_BY = [
            {"point": 1, "city": "BY-MBV", "iata_code": None, "icao_code": None, "lat": 54.220333, "lon": 28.530529, "tm": train, "name": "Barysaŭ Ulitsa Trusova 36"},
            {"point": 1, "city": "BY-MBV", "iata_code": None, "icao_code": None, "lat": 54.220116, "lon": 28.530291, "tm": bus, "name": "Barysaŭ Bus Station"}, #No ho sé...

            {"point": 0, "city": "BY-BQT", "iata_code": "BQT", "icao_code": "UMBB", "lat": 52.108333, "lon": 23.898056, "tm": flight, "name": "Brest Airport"},
            {"point": 1, "city": "BY-BQT", "iata_code": None, "icao_code": None, "lat": 52.100580, "lon": 23.680680, "tm": train, "name": "Brest Train Station"},
            {"point": 2, "city": "BY-BQT", "iata_code": None, "icao_code": None, "lat": 52.098357, "lon": 23.691268, "tm": bus, "name": "Brest Mickeviča 35"},

            {"point": 0, "city": "BY-GME", "iata_code": "GME", "icao_code": "UMGG", "lat": 52.526944, "lon": 31.016667, "tm": flight, "name": "Gomel Airport"},
            {"point": 1, "city": "BY-GME", "iata_code": None, "icao_code": None, "lat": 52.430881, "lon": 30.991302, "tm": train, "name": "Gomel Pryvakzaĺnaja Square"},
            {"point": 1, "city": "BY-GME", "iata_code": None, "icao_code": None, "lat": 52.434150, "lon": 30.993164, "tm": bus, "name": "Gomel Avtovokzal G. Gomelya Filial Oao Gomel'oblavtotrans"},

            {"point": 0, "city": "BY-GDO", "iata_code": "GNA", "icao_code": "UMMG", "lat": 53.601944, "lon": 24.053611, "tm": flight, "name": "Hrodna Airport"},
            {"point": 1, "city": "BY-GDO", "iata_code": None, "icao_code": None, "lat": 53.686481, "lon": 23.848526, "tm": train, "name": "Grodno Budzionnaha 37"},
            {"point": 2, "city": "BY-GDO", "iata_code": None, "icao_code": None, "lat": 53.677741, "lon": 23.843708, "tm": bus, "name": "Grodno Bus Station"},

            {"point": 0, "city": "BY-MSQ", "iata_code": "MSQ", "icao_code": "UMMS", "lat": 53.882222, "lon": 28.030556, "tm": flight, "name": "Minsk National Airport"},
            {"point": 1, "city": "BY-MSQ", "iata_code": None, "icao_code": None, "lat": 53.890781, "lon": 27.550648, "tm": train, "name": "Minsk Train Station"},
            {"point": 1, "city": "BY-MSQ", "iata_code": None, "icao_code": None, "lat": 53.890572, "lon": 27.554131, "tm": bus, "name": "Minsk Ulitsa Bobruyskaya 6"},

            {"point": 0, "city": "BY-MVQ", "iata_code": "MVQ", "icao_code": "UMOO", "lat": 53.954722, "lon": 30.095000, "tm": flight, "name": "Mogilev Airport"},
            {"point": 1, "city": "BY-MVQ", "iata_code":None, "icao_code": None, "lat": 53.926263, "lon": 30.338510, "tm": train, "name": "Mogilev Train Station"},
            {"point": 2, "city": "BY-MVQ", "iata_code":None, "icao_code": None, "lat": 53.913470, "lon": 30.347306, "tm": bus, "name": "Mogilev Leninskaya St 93"},

            {"point": 1, "city": "BY-SHO", "iata_code": None, "icao_code": None, "lat": 52.793363, "lon": 27.545491, "tm": train, "name": "Salihorsk Train Station"},
            {"point": 1, "city": "BY-SHO", "iata_code": None, "icao_code": None, "lat": 52.793058, "lon": 27.544430, "tm": bus, "name": "Salihorsk Lienіnskaha Kamsamola 38"},

            {"point": 0, "city": "BY-VTB", "iata_code": "VTB", "icao_code": "UMII", "lat": 55.126389, "lon": 30.349444, "tm": flight, "name": "Vitebsk Vostochny Airport"},
            {"point": 1, "city": "BY-VTB", "iata_code": None, "icao_code": None, "lat": 55.194863, "lon": 30.185809, "tm": train, "name": "Vitebsk Train Kasmanaŭtaŭ"},
            {"point": 2, "city": "BY-VTB", "iata_code": None, "icao_code": None, "lat": 55.196353, "lon": 30.187969, "tm": bus, "name": "Vitebsk Bus Kasmanaŭtaŭ 12"},

        ]

        hubs_TR = [
            {"point": 0, "city": "TR-ANK", "iata_code": "ESB", "icao_code": "LTAC", "lat": 40.124155, "lon": 32.991776, "tm": flight, "name": "Ankara Airport"},
            {"point": 1, "city": "TR-ANK", "iata_code":  None, "icao_code":   None, "lat": 39.918184, "lon": 32.812215, "tm": bus, "name": "Ankara Terminal AŞTİ"},

            {"point": 0, "city": "TR-AYT", "iata_code": "AYT", "icao_code": "LTAI", "lat": 36.904298, "lon": 30.801920, "tm": flight, "name": "Antalya Airport"},
            {"point": 1, "city": "TR-AYT", "iata_code":  None, "icao_code":   None, "lat": 36.921904, "lon": 30.665123, "tm": bus, "name": "Antalya Otgar"},

            {"point": 0, "city": "TR-IST", "iata_code": "IST", "icao_code": "LTBA", "lat": 40.982932, "lon": 28.810281, "tm": flight, "name": "Istanbul Atatürk Airport"},
            {"point": 1, "city": "TR-IST", "iata_code": "SAW", "icao_code": "LTFJ", "lat": 40.905347, "lon": 29.316839, "tm": flight, "name": "Istambul Sabiha Gökçen Airport"},
            {"point": 2, "city": "TR-IST", "iata_code":  None, "icao_code":   None, "lat": 41.040122, "lon": 28.894516, "tm": bus, "name": "Istanbul Esenler Otogar"},
            {"point": 3, "city": "TR-IST", "iata_code":  None, "icao_code":   None, "lat": 41.011240, "lon": 29.011174, "tm": bus, "name": "Istanbul Harem"},
            {"point": 4, "city": "TR-IST", "iata_code":  None, "icao_code":   None, "lat": 41.088119, "lon": 28.944986, "tm": bus, "name": "Istanbul Alibeyköy Mobile"},

            {"point": 0, "city": "TR-IZM", "iata_code": "ADB", "icao_code": "LTBJ", "lat": 38.293746, "lon": 27.152023, "tm": flight, "name": "İzmir Airport"},
            {"point": 1, "city": "TR-IZM", "iata_code":  None, "icao_code":   None, "lat": 38.430740, "lon": 27.213838, "tm": bus, "name": "İzmir Otgar"},
        ]

        hubs_AD = [
            {"point": 1, "city": "AD-ALV", "iata_code":  None, "icao_code":   None, "lat": 42.505636, "lon": 1.527702, "tm": bus, "name": "Andorra Estació d'Autobusos"},
            {"point": 2, "city": "AD-ALV", "iata_code":  None, "icao_code":   None, "lat": 42.462143, "lon": 1.490435, "tm": bus, "name": "Andorra Sant Julià de Lòria"},

        ]

        hubs_XK = [
            {"point": 1, "city": "XK-DKV", "iata_code": None, "icao_code": None, "lat": 42.387767, "lon": 20.432958, "tm": bus, "name": "Đakovica Bus Station"},

            {"point": 1, "city": "XK-GNJ", "iata_code": None, "icao_code": None, "lat": 42.458929, "lon": 21.465783, "tm": bus, "name": "Gnjilane Idriz Seferi"},

            {"point": 1, "city": "XK-MIT", "iata_code":None, "icao_code": None, "lat": 42.899843, "lon": 20.870704, "tm": train, "name": "Mitrovicë Vojni Remont"},
            {"point": 2, "city": "XK-MIT", "iata_code":None, "icao_code": None, "lat": 42.878804, "lon": 20.865164, "tm": bus, "name": "Mitrovicë Bus Station"},

            {"point": 0, "city": "XK-PRN", "iata_code": "PRN", "icao_code": "BKPR", "lat": 42.572778, "lon": 21.035833, "tm": flight, "name": "Pristina Airport Adem Jashari"},
            {"point": 1, "city": "XK-PRN", "iata_code": None, "icao_code": None, "lat": 42.658949, "lon": 21.151235, "tm": train, "name": "Pristina Tirana"},
            {"point": 2, "city": "XK-PRN", "iata_code": None, "icao_code": None, "lat": 42.650108, "lon": 21.146868, "tm": bus, "name": "Pristina Bus Station"},

            {"point": 0, "city": "XK-PRZ", "iata_code": None, "icao_code": None, "lat": 42.212850, "lon": 20.729197, "tm": bus, "name": "Prizren Bus Station"},
        ]

        hubs_LI = [
            {"point": 1, "city": "LI-SCN", "iata_code": None, "icao_code": None, "lat": 47.168385, "lon": 9.507946, "tm": train, "name": "Liechtenstein Schaan"},
            {"point": 1, "city": "LI-SCN", "iata_code": None, "icao_code": None, "lat": 47.168262, "lon": 9.508628, "tm": bus, "name": "Liechtenstein Schaan"},

            {"point": 2, "city": "LI-SCN", "iata_code": None, "icao_code": None, "lat": 47.138331, "lon": 9.521703, "tm": bus, "name": "Liechtenstein Vaduz"},
        ]

        # no bus, train or car-pooling to be found in APIs
        # hubs_SM = [
        #     {"point": 1, "city": "SM-SAI", "iata_code": None, "icao_code": None, "lat": 43.935100, "lon": 12.446466, "tm": bus, "name": "San Marino Piazzale Marino Calcigini"},
        # ]

        # # no bus, train or car-pooling to be found in APIs
        # hubs_MC = [
        #     {"point": 1, "city": "MC-MON", "iata_code": None, "icao_code":   None, "lat": 43.738750, "lon": 7.418994, "tm": train, "name": "Monaco Place Sainte Dévote"},
        #     {"point": 2, "city": "MC-MON", "iata_code": None, "icao_code":   None, "lat": 43.740182, "lon": 7.425345, "tm": bus, "name": "Monaco 31 Avenue de la Costa"},
        # ]

        hubs_MD =  [
            {"point": 0, "city": "MD-KIV", "iata_code": "KIV", "icao_code": "LUKK", "lat": 46.935208, "lon": 28.935345, "tm": flight, "name": "Chișinău Airport"},
            {"point": 1, "city": "MD-KIV", "iata_code": None, "icao_code": None, "lat": 47.012839, "lon": 28.859829, "tm": train, "name": "Chișinău Main Station"},
            {"point": 1, "city": "MD-KIV", "iata_code": None, "icao_code": None, "lat": 47.011661, "lon": 28.857300, "tm": bus, "name": "Chișinău Gara Feroviară"},

            {"point": 0, "city": "MD-BEL", "iata_code": "BZY", "icao_code": "LUBL", "lat": 47.845859, "lon": 27.777174, "tm": flight, "name": "Bălți Airport"},
            {"point": 1, "city": "MD-BEL", "iata_code": None, "icao_code": None, "lat": 47.760948, "lon": 27.910411, "tm": train, "name": "Bălți Belcs'-Orash"},
            {"point": 2, "city": "MD-BEL", "iata_code": None, "icao_code": None, "lat": 47.770065, "lon": 27.941828, "tm": bus, "name": "Bălți Central Bus Station"},
            {"point": 3, "city": "MD-BEL", "iata_code": None, "icao_code": None, "lat": 47.785968, "lon": 27.925867, "tm": train, "name": "Bălți Belcs'-Sloboziya"},
        ]



        all_hubs = (hubs_DE + hubs_ES + hubs_PT + hubs_FR + hubs_CH + hubs_NL + hubs_BE + hubs_IT +
                            hubs_DK + hubs_FO + hubs_SE + hubs_NO + hubs_GB + hubs_IE + hubs_FI +
                            hubs_CZ + hubs_AT + hubs_LU + hubs_IS + hubs_GR + hubs_LT + hubs_LV +  hubs_EE +
                            hubs_SI + hubs_HR + hubs_MT + hubs_HU + hubs_PL + hubs_SK + hubs_BA + hubs_RS +
                            hubs_ME + hubs_CY + hubs_MK + hubs_AL + hubs_RO + hubs_BG + hubs_RU + hubs_GI +
                            hubs_TR + hubs_AD + hubs_XK + hubs_LI + hubs_BY + hubs_UA + hubs_MD)

        return all_hubs

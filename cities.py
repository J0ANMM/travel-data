    def cities_dict(self):
        """List of dictionaries, being each element of the list one city."""

        #for city codes see https://www.unece.org/fileadmin/DAM/cefact/locode/de.htm

        country = 'DE'
        cities_DE= [
            {'code': 'DE-AAH', 'country': country, 'region': 'DE-NW', 'name': 'Aachen'},
            {'code': 'DE-AGB', 'country': country, 'region': 'DE-BY', 'name': 'Augsburg'},
            {'code': 'DE-BAB', 'country': country, 'region': 'DE-BW', 'name': 'Baden-Baden'},
            {'code': 'DE-BER', 'country': country, 'region': 'DE-BE', 'name': 'Berlin'},
            {'code': 'DE-BFE', 'country': country, 'region': 'DE-NW', 'name': 'Bielefeld'},
            {'code': 'DE-BOM', 'country': country, 'region': 'DE-NW', 'name': 'Bochum'},
            {'code': 'DE-BON', 'country': country, 'region': 'DE-NW', 'name': 'Bonn'},
            {'code': 'DE-BWE', 'country': country, 'region': 'DE-NI', 'name': 'Braunschweig'},
            {'code': 'DE-BRE', 'country': country, 'region': 'DE-HB', 'name': 'Bremen'},
            {'code': 'DE-BRV', 'country': country, 'region': 'DE-HB', 'name': 'Bremerhaven'},
            {'code': 'DE-CHE', 'country': country, 'region': 'DE-SN', 'name': 'Chemnitz'}, #not in public deutschebahn API
            {'code': 'DE-CGN', 'country': country, 'region': 'DE-NW', 'name': 'Cologne',},
            {'code': 'DE-CUX', 'country': country, 'region': 'DE-NW', 'name': 'Cuxhaven',},
            {'code': 'DE-DAR', 'country': country, 'region': 'DE-HE', 'name': 'Darmstadt'},
            {'code': 'DE-DTM', 'country': country, 'region': 'DE-NW', 'name': 'Dortmund'},
            {'code': 'DE-DRS', 'country': country, 'region': 'DE-SN', 'name': 'Dresden'},#no ryanair
            {'code': 'DE-DUI', 'country': country, 'region': 'DE-NW', 'name': 'Duisburg'},
            {'code': 'DE-DUS', 'country': country, 'region': 'DE-NW', 'name': 'Düsseldorf'},#no ryanair
            {'code': 'DE-ERF', 'country': country, 'region': 'DE-TH', 'name': 'Erfurt'},
            # {'code': 'DE-ERL', 'country': country, 'region': 'DE-BY', 'name': 'Erlangen'}, #near Nuremberg
            {'code': 'DE-ESS', 'country': country, 'region': 'DE-NW', 'name': 'Essen'},
            {'code': 'DE-FRA', 'country': country, 'region': 'DE-HE', 'name': 'Frankfurt'},
            {'code': 'DE-HNH', 'country': country, 'region': 'DE-RP', 'name': 'Frankfurt-Hahn'},
            {'code': 'DE-FBG', 'country': country, 'region': 'DE-BW', 'name': 'Freiburg im Breisgau'},
            {'code': 'DE-FDH', 'country': country, 'region': 'DE-BW', 'name': 'Friedrichshafen'},
            # {'code': 'DE-FUE', 'country': country, 'region': 'DE-BY', 'name': 'Fürth'},
            {'code': 'DE-GOE', 'country': country, 'region': 'DE-NI', 'name': 'Göttingen'},
            {'code': 'DE-HAL', 'country': country, 'region': 'DE-ST', 'name': 'Halle (Saale)'},
            {'code': 'DE-HDF', 'country': country, 'region': 'DE-MV', 'name': 'Heringsdorf'},
            {'code': 'DE-HAM', 'country': country, 'region': 'DE-HH', 'name': 'Hamburg'},
            {'code': 'DE-HMM', 'country': country, 'region': 'DE-NW', 'name': 'Hamm'},
            {'code': 'DE-HAJ', 'country': country, 'region': 'DE-NI', 'name': 'Hannover'},#no ryanair
            {'code': 'DE-HEI', 'country': country, 'region': 'DE-BW', 'name': 'Heidelberg'},
            {'code': 'DE-HEN', 'country': country, 'region': 'DE-BW', 'name': 'Heilbronn'},
            {'code': 'DE-ING', 'country': country, 'region': 'DE-BY', 'name': 'Ingolstadt'},
            {'code': 'DE-JEN', 'country': country, 'region': 'DE-TH', 'name': 'Jena'},
            {'code': 'DE-KLT', 'country': country, 'region': 'DE-RP', 'name': 'Kaiserslautern'},
            {'code': 'DE-KAE', 'country': country, 'region': 'DE-BW', 'name': 'Karlsruhe'},
            {'code': 'DE-KAS', 'country': country, 'region': 'DE-HE', 'name': 'Kassel'},
            {'code': 'DE-KEL', 'country': country, 'region': 'DE-SH', 'name': 'Kiel'},
            {'code': 'DE-KOB', 'country': country, 'region': 'DE-RP', 'name': 'Koblenz'},
            {'code': 'DE-KON', 'country': country, 'region': 'DE-BW', 'name': 'Konstanz'},
            {'code': 'DE-LEJ', 'country': country, 'region': 'DE-SN', 'name': 'Leipzig'},
            {'code': 'DE-LBC', 'country': country, 'region': 'DE-SH', 'name': 'Lübeck'},
            {'code': 'DE-MAG', 'country': country, 'region': 'DE-ST', 'name': 'Magdeburg'},
            # {'code': 'DE-MAI', 'country': country, 'region': 'DE-RP', 'name': 'Mainz'},
            {'code': 'DE-MHG', 'country': country, 'region': 'DE-BW', 'name': 'Mannheim'},
            {'code': 'DE-MMN', 'country': country, 'region': 'DE-BY', 'name': 'Memmingen'},
            {'code': 'DE-MUC', 'country': country, 'region': 'DE-BY', 'name': 'Munich'},#no ryanair
            {'code': 'DE-MSR', 'country': country, 'region': 'DE-NW', 'name': 'Münster'},#no ryanair
            {'code': 'DE-NUE', 'country': country, 'region': 'DE-BY', 'name': 'Nuremberg'},
            {'code': 'DE-OLO', 'country': country, 'region': 'DE-NI', 'name': 'Oldenburg'},
            {'code': 'DE-OSN', 'country': country, 'region': 'DE-NI', 'name': 'Osnabrück'},
            {'code': 'DE-PAD', 'country': country, 'region': 'DE-NW', 'name': 'Paderborn'},#no ryanair
            # {'code': 'DE-PFO', 'country': country, 'region': 'DE-BW', 'name': 'Pforzheim'}, #in a second step
            {'code': 'DE-REG', 'country': country, 'region': 'DE-BY', 'name': 'Regensburg'},
            {'code': 'DE-REU', 'country': country, 'region': 'DE-BW', 'name': 'Reutlingen'},
            {'code': 'DE-RSK', 'country': country, 'region': 'DE-MV', 'name': 'Rostock'},
            {'code': 'DE-SCN', 'country': country, 'region': 'DE-SL', 'name': 'Saarbrücken'},#no ryanair
            {'code': 'DE-SGE', 'country': country, 'region': 'DE-NW', 'name': 'Siegen'},
            {'code': 'DE-STR', 'country': country, 'region': 'DE-BW', 'name': 'Stuttgart'},
            {'code': 'DE-SYT', 'country': country, 'region': 'DE-SH', 'name': 'Sylt'},
            {'code': 'DE-TRI', 'country': country, 'region': 'DE-RP', 'name': 'Trier'},
            {'code': 'DE-ULM', 'country': country, 'region': 'DE-BW', 'name': 'Ulm'},
            # {'code': 'DE-UEL', 'country': country, 'region': 'DE-NI', 'name': 'Uelzen'}, #too small
            {'code': 'DE-WZE', 'country': country, 'region': 'DE-NW', 'name': 'Weeze'},
            {'code': 'DE-WIB', 'country': country, 'region': 'DE-HE', 'name': 'Wiesbaden'},
            {'code': 'DE-WOB', 'country': country, 'region': 'DE-NI', 'name': 'Wolfsburg'},
            {'code': 'DE-WUP', 'country': country, 'region': 'DE-NW', 'name': 'Wuppertal'},
            {'code': 'DE-WUE', 'country': country, 'region': 'DE-BY', 'name': 'Würzburg'},
        ]

        country = 'ES'
        cities_ES = [
            {'code': 'ES-LCG', 'country': country, 'region': 'ES-GA', 'name': 'A Coruña'},
            {'code': 'ES-ALB', 'country': country, 'region': 'ES-CM', 'name': 'Albacete'},
            {'code': 'ES-ALG', 'country': country, 'region': 'ES-AN', 'name': 'Algeciras'},
            {'code': 'ES-ALC', 'country': country, 'region': 'ES-VC', 'name': 'Alicante'},
            {'code': 'ES-LEI', 'country': country, 'region': 'ES-AN', 'name': 'Almeria'},
            {'code': 'ES-AVI', 'country': country, 'region': 'ES-CL', 'name': 'Ávila'},
            {'code': 'ES-AVS', 'country': country, 'region': 'ES-CL', 'name': 'Avilés'},
            {'code': 'ES-BJZ', 'country': country, 'region': 'ES-EX', 'name': 'Badajoz'},
            {'code': 'ES-BCN', 'country': country, 'region': 'ES-CT', 'name': 'Barcelona'},
            {'code': 'ES-BIO', 'country': country, 'region': 'ES-PV', 'name': 'Bilbao'},
            {'code': 'ES-BUR', 'country': country, 'region': 'ES-CL', 'name': 'Burgos'},
            {'code': 'ES-CCS', 'country': country, 'region': 'ES-EX', 'name': 'Cáceres'},
            {'code': 'ES-CAD', 'country': country, 'region': 'ES-AN', 'name': 'Cadiz'},
            {'code': 'ES-CAR', 'country': country, 'region': 'ES-MC', 'name': 'Cartagena'},
            {'code': 'ES-CAS', 'country': country, 'region': 'ES-VC', 'name': 'Castellón de la Plana'},
            # {'code': 'ES-CEU', 'country': country, 'region': 'ES-CE', 'name': 'Ceuta'},
            {'code': 'ES-CIR', 'country': country, 'region': 'ES-CL', 'name': 'Ciudad Real'},
            {'code': 'ES-ODB', 'country': country, 'region': 'ES-AN', 'name': 'Cordoba'},
            {'code': 'ES-CUE', 'country': country, 'region': 'ES-CM', 'name': 'Cuenca'},
            {'code': 'ES-DNA', 'country': country, 'region': 'ES-VC', 'name': 'Denia'},
            {'code': 'ES-NST', 'country': country, 'region': 'ES-PV', 'name': 'San Sebastian'},
            {'code': 'ES-ECE', 'country': country, 'region': 'ES-VC', 'name': 'Elche'},
            {'code': 'ES-VDH', 'country': country, 'region': 'ES-CN', 'name': 'El Hierro'},
            {'code': 'ES-FUE', 'country': country, 'region': 'ES-CN', 'name': 'Fuerteventura'},
            {'code': 'ES-GIJ', 'country': country, 'region': 'ES-AS', 'name': 'Gijon'},
            {'code': 'ES-GRO', 'country': country, 'region': 'ES-CT', 'name': 'Girona'},
            {'code': 'ES-LPA', 'country': country, 'region': 'ES-CN', 'name': 'Gran Canaria'},
            {'code': 'ES-GRX', 'country': country, 'region': 'ES-AN', 'name': 'Granada'},
            {'code': 'ES-GUA', 'country': country, 'region': 'ES-CL', 'name': 'Guadalajara'},
            {'code': 'ES-HUV', 'country': country, 'region': 'ES-AN', 'name': 'Huelva'},
            {'code': 'ES-HUC', 'country': country, 'region': 'ES-AR', 'name': 'Huesca'},
            {'code': 'ES-IBZ', 'country': country, 'region': 'ES-IB', 'name': 'Ibiza'},
            {'code': 'ES-JAE', 'country': country, 'region': 'ES-AN', 'name': 'Jaen'},
            {'code': 'ES-JRZ', 'country': country, 'region': 'ES-AN', 'name': 'Jerez'},
            {'code': 'ES-ACE', 'country': country, 'region': 'ES-CN', 'name': 'Lanzarote'},
            {'code': 'ES-PPS', 'country': country, 'region': 'ES-CN', 'name': 'La Gomera'},
            {'code': 'ES-SPC', 'country': country, 'region': 'ES-CN', 'name': 'La Palma'},
            {'code': 'ES-LEN', 'country': country, 'region': 'ES-CL', 'name': 'Leon'},
            {'code': 'ES-LLE', 'country': country, 'region': 'ES-CT', 'name': 'Lleida'},
            {'code': 'ES-LGR', 'country': country, 'region': 'ES-RI', 'name': 'Logroño'},
            {'code': 'ES-LGO', 'country': country, 'region': 'ES-GA', 'name': 'Lugo'},
            {'code': 'ES-MAD', 'country': country, 'region': 'ES-MD', 'name': 'Madrid'},
            {'code': 'ES-AGP', 'country': country, 'region': 'ES-AN', 'name': 'Malaga'},
            {'code': 'ES-PMI', 'country': country, 'region': 'ES-IB', 'name': 'Mallorca'},
            {'code': 'ES-MQE', 'country': country, 'region': 'ES-AN', 'name': 'Marbella'},
            {'code': 'ES-MLN', 'country': country, 'region': 'ES-ML', 'name': 'Melilla'},
            {'code': 'ES-MEA', 'country': country, 'region': 'ES-EX', 'name': 'Mérida'},
            {'code': 'ES-MAH', 'country': country, 'region': 'ES-IB', 'name': 'Menorca'},
            {'code': 'ES-MJV', 'country': country, 'region': 'ES-MC', 'name': 'Murcia'},
            {'code': 'ES-ORE', 'country': country, 'region': 'ES-GA', 'name': 'Ourense'},
            {'code': 'ES-OVO', 'country': country, 'region': 'ES-AS', 'name': 'Oviedo'},
            {'code': 'ES-PAC', 'country': country, 'region': 'ES-CL', 'name': 'Palencia'},
            {'code': 'ES-PNA', 'country': country, 'region': 'ES-NC', 'name': 'Pamplona'},
            {'code': 'ES-PON', 'country': country, 'region': 'ES-GA', 'name': 'Ponferrada'},
            {'code': 'ES-PEV', 'country': country, 'region': 'ES-CL', 'name': 'Pontevedra'},
            {'code': 'ES-REU', 'country': country, 'region': 'ES-CT', 'name': 'Reus'},
            {'code': 'ES-RNA', 'country': country, 'region': 'ES-AN', 'name': 'Ronda'},
            {'code': 'ES-SLM', 'country': country, 'region': 'ES-CL', 'name': 'Salamanca'},
            {'code': 'ES-SDR', 'country': country, 'region': 'ES-CB', 'name': 'Santander'},
            {'code': 'ES-SCQ', 'country': country, 'region': 'ES-GA', 'name': 'Santiago de Compostela'},
            {'code': 'ES-SEG', 'country': country, 'region': 'ES-CL', 'name': 'Segovia'},
            {'code': 'ES-SVQ', 'country': country, 'region': 'ES-AN', 'name': 'Seville'},
            {'code': 'ES-SOR', 'country': country, 'region': 'ES-CL', 'name': 'Soria'},
            {'code': 'ES-TAR', 'country': country, 'region': 'ES-CT', 'name': 'Tarragona'},
            {'code': 'ES-TCI', 'country': country, 'region': 'ES-CN', 'name': 'Tenerife'},
            {'code': 'ES-TER', 'country': country, 'region': 'ES-AR', 'name': 'Teruel'},
            {'code': 'ES-TOL', 'country': country, 'region': 'ES-CL', 'name': 'Toledo'},
            {'code': 'ES-VLC', 'country': country, 'region': 'ES-VC', 'name': 'Valencia'},
            {'code': 'ES-VLL', 'country': country, 'region': 'ES-CL', 'name': 'Valladolid'},
            {'code': 'ES-VGO', 'country': country, 'region': 'ES-GA', 'name': 'Vigo'},
            {'code': 'ES-VIT', 'country': country, 'region': 'ES-PV', 'name': 'Vitoria-Gasteiz'},
            {'code': 'ES-ZMR', 'country': country, 'region': 'ES-CL', 'name': 'Zamora'},
            {'code': 'ES-ZAZ', 'country': country, 'region': 'ES-AR', 'name': 'Zaragoza'},
        ]

        country = 'PT'
        cities_PT = [
            {"code": "PT-ALM", "country": country, "region": 'PT-15', "name": "Almada"},
            # {"code": "PT-AMA", "country": country, "region": 'PT-11', "name": "Amadora"},
            {"code": "PT-AVE", "country": country, "region": 'PT-06', "name": "Aveiro"}, #78.000 inhabitants + big uni + metropole with Ílhavo > 100.000
            {'code': 'PT-BGZ', 'country': country, 'region': 'PT-03', 'name': 'Braga'},
            {"code": "PT-BGC", "country": country, "region": 'PT-04', "name": "Bragança"}, #Bragança Airport
            {"code": "PT-CAS", "country": country, "region": 'PT-11', "name": "Cascais"}, #Cascais Aerodrome
            {'code': 'PT-CBP', 'country': country, 'region': 'PT-06', 'name': 'Coimbra'},
            {"code": "PT-CVU", "country": country, "region": 'PT-20', "name": "Corvo Island"}, #Corvo Airport
            {'code': 'PT-ENT', 'country': country, 'region': 'PT-06', 'name': 'Entroncamento'},
            {"code": "PT-HOR", "country": country, "region": 'PT-20', "name": "Faial Island"}, #Horta Airport
            {'code': 'PT-FAO', 'country': country, 'region': 'PT-08', 'name': 'Faro'},
            {"code": "PT-SCF", "country": country, "region": 'PT-20', "name": "Flores Island"}, #Flores Airport
            {'code': 'PT-LIS', 'country': country, 'region': 'PT-11', 'name': 'Lisbon'},
            {"code": "PT-M6E", "country": country, "region": 'PT-30', "name": "Madeira"}, #Madeira Airport
            {"code": "PT-MAD", "country": country, "region": 'PT-20', "name": "Pico Island"}, #Pico Airport
            {'code': 'PT-OPO', 'country': country, 'region': 'PT-13', 'name': 'Porto'},
            {"code": "PT-PRM", "country": country, "region": 'PT-08', "name": "Portimão"}, #Portimão Airport
            {"code": "PT-PXO", "country": country, "region": 'PT-30', "name": "Porto Santo"}, #Porto Santo Airport
            {"code": "PT-VDP", "country": country, "region": 'PT-20', "name": "Santa Maria Island"}, #Santa Maria Airport (Azores)
            {'code': 'PT-PDL', 'country': country, 'region': 'PT-20', 'name': 'São Miguel'},
            {'code': 'PT-LDP', 'country': country, 'region': 'PT-20', 'name': 'Terceira Island'},
            {"code": "PT-VRL", "country": country, "region": 'PT-17', "name": "Vila Real"}, #Vila Real Airport
            {"code": "PT-VSE", "country": country, "region": 'PT-18', "name": "Viseu"}, #Viseu Airport
        ]

        country = 'IE'
        cities_IE = [
            {"code": "IE-ORK", "country": country, "region": None, "name": "Cork"}, #Cork Airport
            {"code": "IE-CFN", "country": country, "region": None, "name": "Donegal"}, #Donegal Airport
            {'code': 'IE-DUB', 'country': country, 'region': None, 'name': 'Dublin'},
            {"code": "IE-GWY", "country": country, "region": None, "name": "Galway"}, #Connemara Airport
            {"code": "IE-INQ", "country": country, "region": None, "name": "Inisheer"}, #Inisheer Aerodrome
            {"code": "IE-IIA", "country": country, "region": None, "name": "Inishmaan"}, #Inishmaan Aerodrome
            {"code": "IE-IOR", "country": country, "region": None, "name": "Inishmore"}, #Inishmore Aerodrome
            {"code": "IE-KLY", "country": country, "region": None, "name": "Killarney"}, #Kerry Airport
            {"code": "IE-NOC", "country": country, "region": None, "name": "Knock"}, #Ireland West Airport Knock
            {"code": "IE-SNN", "country": country, "region": None, "name": "Shannon"}, #Shannon Airport


        ]

        country = 'FR'
        cities_FR = [
            {'code': 'FR-QXB', 'country': country, 'region': None, 'name': 'Aix-en-Provence'},
            {'code': 'FR-AGF', 'country': country, 'region': None, 'name': 'Agen'},
            {'code': 'FR-AJA', 'country': country, 'region': None, 'name': 'Ajaccio'},
            {'code': 'FR-AMI', 'country': country, 'region': None, 'name': 'Amiens'},
            {'code': 'FR-ANE', 'country': country, 'region': None, 'name': 'Angers'},
            # {'code': 'FR-ATL', 'country': country, 'region': None, 'name': 'Argenteuil'}, #included in Paris
            {'code': 'FR-AUR', 'country': country, 'region': None, 'name': 'Aurillac'},
            {'code': 'FR-BIA', 'country': country, 'region': None, 'name': 'Bastia'},
            {'code': 'FR-BVA', 'country': country, 'region': None, 'name': 'Beauvais'},
            {'code': 'FR-EGC', 'country': country, 'region': None, 'name': 'Bergerac'},
            {'code': 'FR-BSN', 'country': country, 'region': None, 'name': 'Besançon'},
            {'code': 'FR-BZR', 'country': country, 'region': None, 'name': 'Béziers'},
            {'code': 'FR-BIQ', 'country': country, 'region': None, 'name': 'Biarritz'},
            {'code': 'FR-BOD', 'country': country, 'region': None, 'name': 'Bordeaux'},
            {'code': 'FR-BES', 'country': country, 'region': None, 'name': 'Brest'},
            {'code': 'FR-BVE', 'country': country, 'region': None, 'name': 'Brive-la-Gaillarde'},
            {'code': 'FR-CFR', 'country': country, 'region': None, 'name': 'Caen'},
            # {'code': 'FR-CQF', 'country': country, 'region': None, 'name': 'Calais'},  #Ferry only
            {'code': 'FR-CLY', 'country': country, 'region': None, 'name': 'Calvi'},
            {'code': 'FR-CCF', 'country': country, 'region': None, 'name': 'Carcassonne'},
            {'code': 'FR-CAS', 'country': country, 'region': None, 'name': 'Castres'},
            {'code': 'FR-CSM', 'country': country, 'region': None, 'name': 'Châlons-en-Champagne'},
            {'code': 'FR-CMF', 'country': country, 'region': None, 'name': 'Chambéry'},
           # {'code': 'FR-CER', 'country': country, 'region': None, 'name': 'Cherbourg'},  #Ferry only
            {'code': 'FR-CFE', 'country': country, 'region': None, 'name': 'Clermont-Ferrand'},
            {'code': 'FR-DOL', 'country': country, 'region': None, 'name': 'Deauville'},
           # {'code': 'FR-DPE', 'country': country, 'region': None, 'name': 'Dieppe'},  #Ferry only
            {'code': 'FR-DIJ', 'country': country, 'region': None, 'name': 'Dijon'},
            {'code': 'FR-DNR', 'country': country, 'region': None, 'name': 'Dinard'},
            {'code': 'FR-DLE', 'country': country, 'region': None, 'name': 'Dole'},
           # {'code': 'FR-DKK', 'country': country, 'region': None, 'name': 'Dunkerque'},  #Ferry only
           # {'code': 'FR-GFR', 'country': country, 'region': None, 'name': 'Granville'},  #Ferry only
            {'code': 'FR-GNB', 'country': country, 'region': None, 'name': 'Grenoble'},
            {'code': 'FR-HEN', 'country': country, 'region': None, 'name': 'Hendaye'},
            {'code': 'FR-LRH', 'country': country, 'region': None, 'name': 'La Rochelle'},
            {'code': 'FR-LAI', 'country': country, 'region': None, 'name': 'Lannion'},
            {'code': 'FR-LEH', 'country': country, 'region': None, 'name': 'Le Havre'},
            {'code': 'FR-LME', 'country': country, 'region': None, 'name': 'Le-Mans'},
           # {'code': 'FR-LP2', 'country': country, 'region': None, 'name': 'Le-Palais'}, #Ferry only
           # {'code': 'FR-ILR', 'country': country, 'region': None, 'name': 'L'Île-Rousse'},  #Ferry only
           # {'code': 'FR-???', 'country': country, 'region': None, 'name': 'L'Île d'Artz'},  #Ferry only
            {'code': 'FR-LLE', 'country': country, 'region': None, 'name': 'Lille'},
            {'code': 'FR-LIG', 'country': country, 'region': None, 'name': 'Limoges'},
            {'code': 'FR-LRT', 'country': country, 'region': None, 'name': 'Lorient'},
            {'code': 'FR-LDE', 'country': country, 'region': None, 'name': 'Lourdes'},
            {'code': 'FR-LIO', 'country': country, 'region': None, 'name': 'Lyon'},
            {'code': 'FR-MRS', 'country': country, 'region': None, 'name': 'Marseille'},
            {'code': 'FR-MZM', 'country': country, 'region': None, 'name': 'Metz'},
            {'code': 'FR-MPL', 'country': country, 'region': None, 'name': 'Montpellier'},
            {'code': 'FR-MLH', 'country': country, 'region': None, 'name': 'Mulhouse'},
            {'code': 'FR-ENC', 'country': country, 'region': None, 'name': 'Nancy'},
            {'code': 'FR-NTE', 'country': country, 'region': None, 'name': 'Nantes'},
            {'code': 'FR-NCE', 'country': country, 'region': None, 'name': 'Nice'},
            {'code': 'FR-FNI', 'country': country, 'region': None, 'name': 'Nîmes'},
            {'code': 'FR-ORR', 'country': country, 'region': None, 'name': 'Orléans'},
            {'code': 'FR-PAR', 'country': country, 'region': None, 'name': 'Paris'},
            {'code': 'FR-PUF', 'country': country, 'region': None, 'name': 'Pau'},
            {'code': 'FR-PGX', 'country': country, 'region': None, 'name': 'Périgueux'},
            {'code': 'FR-PGF', 'country': country, 'region': None, 'name': 'Perpignan'},
            {'code': 'FR-PIS', 'country': country, 'region': None, 'name': 'Poitiers'},
            {'code': 'FR-PVO', 'country': country, 'region': None, 'name': 'Porto-Vecchio'},
           # {'code': 'FR-QUI', 'country': country, 'region': None, 'name': 'Quiberon'}, # Ferry only
            {'code': 'FR-UIP', 'country': country, 'region': None, 'name': 'Quimper'},
            {'code': 'FR-RHE', 'country': country, 'region': None, 'name': 'Reims'},
            {'code': 'FR-RNS', 'country': country, 'region': None, 'name': 'Rennes'},
            {'code': 'FR-RDZ', 'country': country, 'region': None, 'name': 'Rodez'},
            # {'code': 'FR-ROS', 'country': country, 'region': None, 'name': 'Roscoff'}, #Ferry only
            {'code': 'FR-URO', 'country': country, 'region': None, 'name': 'Rouen'},
            # {'code': 'FR-YSD', 'country': country, 'region': None, 'name': 'Saint-Denis'}, #included in Paris
            {'code': 'FR-EBU', 'country': country, 'region': None, 'name': 'Saint-Étienne'},
           # {'code': 'FR-SML', 'country': country, 'region': None, 'name': 'Saint-Malo'}, #Ferry only
           # {'code': 'FR-SNR', 'country': country, 'region': None, 'name': 'Saint-Nazaire'}, #Ferry only
           # {'code': 'FR-STP', 'country': country, 'region': None, 'name': 'Saint-Tropez'}, #Ferry only
           # {'code': 'FR-SET', 'country': country, 'region': None, 'name': 'Sete'}, #Ferry only
            {'code': 'FR-CRO', 'country': country, 'region': None, 'name': 'Strasbourg'},
            {'code': 'FR-TLN', 'country': country, 'region': None, 'name': 'Toulon'},
            {'code': 'FR-TLS', 'country': country, 'region': None, 'name': 'Toulouse'},
            {'code': 'FR-TUF', 'country': country, 'region': None, 'name': 'Tours'},
           # {'code': 'FR-VNE', 'country': country, 'region': None, 'name': 'Vannes'}, #Ferry only, bus and train, but no airport and 50,000 people

        ]

        country = 'GB'
        cities_GB = [
            {"code": "GB-ABD", "country": country, "region": None, "name": "Aberdeen"}, #Aberdeen Airport
            {"code": "GB-ANY", "country": country, "region": None, "name": "Alderney"}, #No code in UNLOCODE, code made-up #Alderney Airport
            {"code": "GB-VLY", "country": country, "region": None, "name": "Anglesey"}, #No code in UNLOCODE, code made-up #Alderney Airport
            {"code": "GB-AYR", "country": country, "region": None, "name": "Ayr"}, #Prestwick Airport
            {"code": "GB-BRR", "country": country, "region": None, "name": "Barra"}, #Barra Airport (Scotland)
            {"code": "GB-BEL", "country": country, "region": None, "name": "Belfast"}, #George Best Belfast City Airport
            {"code": "GB-BBC", "country": country, "region": None, "name": "Benbecula"}, #Benbecula Airport
            {'code': 'GB-BHM', 'country': country, 'region': None, 'name': 'Birmingham'},
            {'code': 'GB-BLB', 'country': country, 'region': None, 'name': 'Blackburn'},
            {'code': 'GB-BLK', 'country': country, 'region': None, 'name': 'Blackpool'},
            # {'code': 'GB-BLT', 'country': country, 'region': None, 'name': 'Bolton'},  #included inside Manchester
            {"code": "GB-BOH", "country": country, "region": None, "name": "Bournemouth"},
            {"code": "GB-BRF", "country": country, "region": None, "name": "Bradford"},
            {"code": "GB-BSH", "country": country, "region": None, "name": "Brighton"},
            {"code": "GB-BRS", "country": country, "region": None, "name": "Bristol"}, #Bristol Airport
            {"code": "GB-CMG", "country": country, "region": None, "name": "Cambridge"},
            {"code": "GB-CBT", "country": country, "region": None, "name": "Campbeltown"}, #Campbeltown Airport
            {"code": "GB-CDF", "country": country, "region": None, "name": "Cardiff"}, #Coll Airport
            {"code": "GB-COL", "country": country, "region": None, "name": "Colchester"},
            {"code": "GB-OLL", "country": country, "region": None, "name": "Coll"}, #Coll Airport
            {"code": "GB-CSA", "country": country, "region": None, "name": "Colonsay"}, #Colonsay Airport
            {"code": "GB-CVT", "country": country, "region": None, "name": "Coventry"}, #Coventry Airport
            # {"code": "GB-CWY", "country": country, "region": None, "name": "Crawley"}, # Next to Gatwick Airport, considered inside London
            {"code": "GB-DXY", "country": country, "region": None, "name": "Derby"},
            {"code": "GB-LDY", "country": country, "region": None, "name": "Derry"}, #City of Derry Airport
            {"code": "GB-DON", "country": country, "region": None, "name": "Doncaster"}, #Doncaster Sheffield Airport
            {"code": "GB-DDL", "country": country, "region": None, "name": "Dudley"},
            {"code": "GB-DUN", "country": country, "region": None, "name": "Dundee"},
            {"code": "GB-EBO", "country": country, "region": None, "name": "Eastbourne"},
            {"code": "GB-EOI", "country": country, "region": None, "name": "Eday"}, #Eday Airport
            {'code': 'GB-EDI', 'country': country, 'region': None, 'name': 'Edinburgh'},
            {"code": "GB-EXE", "country": country, "region": None, "name": "Exeter"},
            {"code": "GB-GLW", "country": country, "region": None, "name": "Glasgow"}, #Glasgow Airport
            {"code": "GB-GLO", "country": country, "region": None, "name": "Gloucester"},
            {"code": "GB-PPO", "country": country, "region": None, "name": "Guernsey"}, #Guernsey Airport
            {"code": "GB-HDF", "country": country, "region": None, "name": "Huddersfield"},
            {"code": "GB-INV", "country": country, "region": None, "name": "Inverness"}, #Inverness Airport
            {"code": "GB-IPS", "country": country, "region": None, "name": "Ipswich"},
            {"code": "GB-ISY", "country": country, "region": None, "name": "Islay"}, #Islay Airport
            {"code": "GB-DGL", "country": country, "region": None, "name": "Isle of Man"}, #Isle of Man Airport
            {"code": "GB-TNR", "country": country, "region": None, "name": "Jersey"}, #Jersey Airport
            {"code": "GB-KUH", "country": country, "region": None, "name": "Kingston upon Hull"},
            {"code": "GB-KWL", "country": country, "region": None, "name": "Kirkwall"}, #Kirkwall Airport
            {"code": "GB-KMG", "country": country, "region": None, "name": "Kirmington"}, #Humberside Airport
            {"code": "GB-LBA", "country": country, "region": None, "name": "Leeds"}, #Leeds Bradford Airport
            {'code': 'GB-LCS', 'country': country, 'region': None, 'name': 'Leicester'},
            {'code': 'GB-LIV', 'country': country, 'region': None, 'name': 'Liverpool'},
            {'code': 'GB-LON', 'country': country, 'region': None, 'name': 'London'},
            # {'code': 'GB-LUT', 'country': country, 'region': None, 'name': 'Luton'},
            {"code": "GB-LYX", "country": country, "region": None, "name": "Lydd"},
            {'code': 'GB-MNC', 'country': country, 'region': None, 'name': 'Manchester'},
            {"code": "GB-MID", "country": country, "region": None, "name": "Middlesbrough"}, #Durham Tees Valley Airport
            {'code': 'GB-MIK', 'country': country, 'region': None, 'name': 'Milton Keynes'},
            # {"code": "GB-NCS", "country": country, "region": None, "name": "Newcastle"}, #to be deleted
            {'code': 'GB-NCL', 'country': country, 'region': None, 'name': 'Newcastle'},
            {"code": "GB-NQY", "country": country, "region": None, "name": "Newquay"},
            {"code": "GB-NRO", "country": country, "region": None, "name": "North Ronaldsay"}, #North Ronaldsay Airport
            {"code": "GB-NHP", "country": country, "region": None, "name": "Northampton"},
            {"code": "GB-NRW", "country": country, "region": None, "name": "Norwich"},
            {'code': 'GB-NTG', 'country': country, 'region': None, 'name': 'Nottingham'},
            {"code": "GB-OBA", "country": country, "region": None, "name": "Oban"}, #Oban Airport
            {"code": "GB-OXF", "country": country, "region": None, "name": "Oxford"},
            {"code": "GB-PPW", "country": country, "region": None, "name": "Papa Westray"}, #Papa Westray Airport
            {"code": "GB-PET", "country": country, "region": None, "name": "Peterborough"},
            {"code": "GB-PLY", "country": country, "region": None, "name": "Plymouth"},
            # {"code": "GB-POO", "country": country, "region": None, "name": "Poole"}, #merged with Bournemouth
            {"code": "GB-PME", "country": country, "region": None, "name": "Portsmouth"},
            {"code": "GB-PRE", "country": country, "region": None, "name": "Preston"},
            {"code": "GB-RDN", "country": country, "region": None, "name": "Reading"},
            # {"code": "GB-RTH", "country": country, "region": None, "name": "Rotherham"}, # for the moment not considered as it is close to Sheffield
            {"code": "GB-SJU", "country": country, "region": None, "name": "Saint Just"}, #Land's End Airport
            {"code": "GB-NDY", "country": country, "region": None, "name": "Sanday, Orkney"}, #Sanday Airport
            {"code": "GB-SHE", "country": country, "region": None, "name": "Sheffield"},
            {"code": "GB-TLD", "country": country, "region": None, "name": "Shetland"}, #Sumburgh Airport #Tingwall Airport
            # {"code": "GB-SLO", "country": country, "region": None, "name": "Slough"}, #next to Heathrow, inside London
            {"code": "GB-SOU", "country": country, "region": None, "name": "Southampton"},
            # {"code": "GB-SAA", "country": country, "region": None, "name": "Southend-on-Sea"}, #it has London's Southend airport: considered inside London for the moment
            {"code": "GB-SVZ", "country": country, "region": None, "name": "St Mary's, Isles of Scilly"}, #St Mary's Airport (Isles of Scilly)
            # {"code": "GB-STK", "country": country, "region": None, "name": "Stockport"}, #inside Manchester
            {"code": "GB-SOT", "country": country, "region": None, "name": "Stoke-on-Trent"},
            {"code": "GB-STO", "country": country, "region": None, "name": "Stornoway"}, #Stornoway Airport
            {"code": "GB-SOY", "country": country, "region": None, "name": "Stronsay"}, #Stronsay Airport
            {"code": "GB-SUN", "country": country, "region": None, "name": "Sunderland"},
            # {"code": "GB-SUC", "country": country, "region": None, "name": "Sutton Coldfield"}, #inside Birmingham
            {"code": "GB-SWA", "country": country, "region": None, "name": "Swansea"},
            {"code": "GB-SNN", "country": country, "region": None, "name": "Swindon"},
            {"code": "GB-TEF", "country": country, "region": None, "name": "Telford"},
            {"code": "GB-TRE", "country": country, "region": None, "name": "Tiree"}, #Tiree Airport
            # {"code": "GB-WAL", "country": country, "region": None, "name": "Walsall"}, #inside Birmingham
            # {"code": "GB-WAF", "country": country, "region": None, "name": "Watford"}, #considered inside London
            {"code": "GB-WRY", "country": country, "region": None, "name": "Westray"}, #Westray Airport
            {"code": "GB-WIC", "country": country, "region": None, "name": "Wick, Highland"}, #Wick Airport
            # {"code": "GB-WOV", "country": country, "region": None, "name": "Wolverhampton"}, #inside Birmingham
            {"code": "GB-YRK", "country": country, "region": None, "name": "York"},

        ]

        country = 'IT'
        cities_IT = [
            # {'code': 'IT-ALL', 'country': country, 'region': None, 'name': "Albenga"}, #no comerical flights at airport and city with 24.000 people
            {'code': 'IT-ALE', 'country': country, 'region': None, 'name': "Alessandria"},
            {'code': 'IT-AHO', 'country': country, 'region': None, 'name': "Alghero"},
            {'code': 'IT-AOI', 'country': country, 'region': None, 'name': "Ancona"},
            {'code': 'IT-ADR', 'country': country, 'region': None, 'name': "Andria"},
            {'code': 'IT-ARE', 'country': country, 'region': None, 'name': "Arezzo"},
            {'code': 'IT-BRI', 'country': country, 'region': None, 'name': "Bari"},
            {'code': 'IT-BGO', 'country': country, 'region': None, 'name': 'Bergamo'},
            {'code': 'IT-BLQ', 'country': country, 'region': None, 'name': "Bologna"},
            {'code': 'IT-BZO', 'country': country, 'region': None, 'name': "Bolzano"},
            {'code': 'IT-BRC', 'country': country, 'region': None, 'name': "Brescia"},
            {'code': 'IT-BDS', 'country': country, 'region': None, 'name': "Brindisi"},
            {'code': 'IT-CAG', 'country': country, 'region': None, 'name': "Cagliari"},
            # {'code': 'IT-CMD', 'country': country, 'region': None, 'name': "Campoformido"}, #no comerical flights at airport and city with 8.000 people
            {'code': 'IT-CTA', 'country': country, 'region': None, 'name': "Catania"},
            {'code': 'IT-CIY', 'country': country, 'region': None, 'name': "Comiso"},
            {'code': 'IT-CUN', 'country': country, 'region': None, 'name': "Cuneo"},
            {'code': 'IT-EBA', 'country': country, 'region': None, 'name': "Elba"},
            {'code': 'IT-FRR', 'country': country, 'region': None, 'name': "Ferrara"},
            {'code': 'IT-FLR', 'country': country, 'region': None, 'name': "Florence"},
            {'code': 'IT-FOG', 'country': country, 'region': None, 'name': "Foggia"},
            {'code': 'IT-FRL', 'country': country, 'region': None, 'name': "Forlì"},
            {'code': 'IT-GOA', 'country': country, 'region': None, 'name': "Genova"},
            # {'code': 'IT-GRS', 'country': country, 'region': None, 'name': "Grosseto"}, #no comerical flights at airport and city with 80.000 people
            {'code': 'IT-SUF', 'country': country, 'region': None, 'name': "Lamezia Terme"},
            {'code': 'IT-LMP', 'country': country, 'region': None, 'name': "Lampedusa"},
            {'code': 'IT-LTN', 'country': country, 'region': None, 'name': "Latina"},
            {'code': 'IT-SPE', 'country': country, 'region': None, 'name': "La Spezia"},
            {'code': 'IT-LIV', 'country': country, 'region': None, 'name': "Livorno"},
            # {'code': 'IT-LCV', 'country': country, 'region': None, 'name': "Lucca"}, #no comerical flights at airport and city with 87.000 people
            {'code': 'IT-MSN', 'country': country, 'region': None, 'name': 'Messina'},
            {'code': 'IT-MIL', 'country': country, 'region': None, 'name': 'Milan'},
            {'code': 'IT-MZA', 'country': country, 'region': None, 'name': "Monza"},
            {'code': 'IT-NAP', 'country': country, 'region': None, 'name': "Naples"},
            {'code': 'IT-NVR', 'country': country, 'region': None, 'name': "Novara"},
            {'code': 'IT-OLB', 'country': country, 'region': None, 'name': "Olbia"},
            {'code': 'IT-PD4', 'country': country, 'region': None, 'name': "Padua"},
            {'code': 'IT-PMO', 'country': country, 'region': None, 'name': "Palermo"},
            {'code': 'IT-PNL', 'country': country, 'region': None, 'name': "Pantelleria"},
            {'code': 'IT-PMF', 'country': country, 'region': None, 'name': "Parma"},
            {'code': 'IT-PEG', 'country': country, 'region': None, 'name': "Perugia"},
            {'code': 'IT-PSR', 'country': country, 'region': None, 'name': "Pescara"},
            {'code': 'IT-PCZ', 'country': country, 'region': None, 'name': "Piacenza"},
            {'code': 'IT-PSA', 'country': country, 'region': None, 'name': "Pisa"},
            {'code': 'IT-RAN', 'country': country, 'region': None, 'name': "Ravenna"},
            {'code': 'IT-REG', 'country': country, 'region': None, 'name': "Reggio Calabria"},
            {'code': 'IT-RNE', 'country': country, 'region': None, 'name': "Reggio Emilia"},
            {'code': 'IT-RMI', 'country': country, 'region': None, 'name': "Rimini"},
            {'code': 'IT-ROM', 'country': country, 'region': None, 'name': "Rome"},
            {'code': 'IT-RDL', 'country': country, 'region': None, 'name': "Ronchi dei Legionari"},
            {'code': 'IT-SAL', 'country': country, 'region': None, 'name': "Salerno"},
            {'code': 'IT-QSS', 'country': country, 'region': None, 'name': "Sassari"},
            {'code': 'IT-SNA', 'country': country, 'region': None, 'name': "Siena"},
            {'code': 'IT-SIR', 'country': country, 'region': None, 'name': "Syracuse"},
            {'code': 'IT-TER', 'country': country, 'region': None, 'name': "Terni"},
            {'code': 'IT-TRN', 'country': country, 'region': None, 'name': "Torino"},
            {'code': 'IT-TPS', 'country': country, 'region': None, 'name': "Trapani"},
            {'code': 'IT-TRT', 'country': country, 'region': None, 'name': "Trento"},
            {'code': 'IT-TRV', 'country': country, 'region': None, 'name': "Treviso"},
            {'code': 'IT-TRS', 'country': country, 'region': None, 'name': "Trieste"}, #Airport TRS is 40km away --> included in Ronchi dei Legionari. Rail station iata TXB
            {'code': 'IT-UDN', 'country': country, 'region': None, 'name': "Udine"},
            {'code': 'IT-VCE', 'country': country, 'region': None, 'name': "Venice"},
            {'code': 'IT-VRN', 'country': country, 'region': None, 'name': "Verona"},
            {'code': 'IT-VIC', 'country': country, 'region': None, 'name': "Vicenza"},
        ]


        country = 'CH'
        cities_CH = [
            {'code': "CH-BSL", 'country': country, 'region': None, 'name': "Basel"},
            {'code': "CH-BRN", 'country': country, 'region': None, 'name': "Bern"},
            {'code': "CH-GVA", 'country': country, 'region': None, 'name': "Geneve"},
            # {'code': "CH-ZHI", 'country': country, 'region': None, 'name': "Grenchen"}, #population of 16.000 and airport with no flights
            {'code': "CH-LAU", 'country': country, 'region': None, 'name': "Lausanne"},
            {'code': "CH-LUG", 'country': country, 'region': None, 'name': "Lugano"},
            {'code': "CH-SAM", 'country': country, 'region': None, 'name': "Samedan"},
            {'code': "CH-SIR", 'country': country, 'region': None, 'name': "Sion"},
            {'code': "CH-ATR", 'country': country, 'region': None, 'name': "Thal"},
            {'code': "CH-WIN", 'country': country, 'region': None, 'name': "Winterthur"},
            {'code': "CH-ZRH", 'country': country, 'region': None, 'name': "Zurich"},
        ]

        country = 'NL'
        cities_NL = [
            {'code': "NL-ALK", 'country': country, 'region': None, 'name': "Alkmaar"},
            {'code': "NL-AER", 'country': country, 'region': None, 'name': "Almere"},
            {'code': "NL-APN", 'country': country, 'region': None, 'name': "Alphen aan den Rijn"},
            {'code': "NL-AME", 'country': country, 'region': None, 'name': "Amersfoort"},
            {'code': "NL-AMS", 'country': country, 'region': None, 'name': "Amsterdam"},
            {'code': "NL-APE", 'country': country, 'region': None, 'name': "Apeldoorn"},
            {'code': "NL-ARN", 'country': country, 'region': None, 'name': "Arnhem"},
            {'code': "NL-BRD", 'country': country, 'region': None, 'name': "Breda"},
            # # {'code': "NL-DFT", 'country': country, 'region': None, 'name': "Delft"}, #belongs to the Hague
            {'code': "NL-DOR", 'country': country, 'region': None, 'name': "Dordrecht"},
            {'code': "NL-EDE", 'country': country, 'region': None, 'name': "Ede"},
            {'code': "NL-EIN", 'country': country, 'region': None, 'name': "Eindhoven"},
            {'code': "NL-EMM", 'country': country, 'region': None, 'name': "Emmen"},
            {'code': "NL-ENS", 'country': country, 'region': None, 'name': "Enschede"},
            {'code': "NL-GRQ", 'country': country, 'region': None, 'name': "Groningen"},
            # {'code': "NL-HAA", 'country': country, 'region': None, 'name': "Haarlem"}, #belongs to Amsterdam
            # {'code': "NL-HVH", 'country': country, 'region': None, 'name': "Hook of Holland"},
            {'code': "NL-LWR", 'country': country, 'region': None, 'name': "Leeuwarden"},
            {'code': "NL-LID", 'country': country, 'region': None, 'name': "Leiden"},
            {'code': "NL-LEY", 'country': country, 'region': None, 'name': "Lelystad"},
            {'code': "NL-MST", 'country': country, 'region': None, 'name': "Maastricht"},
            {'code': "NL-NIJ", 'country': country, 'region': None, 'name': "Nijmegen"},
            {'code': "NL-RTM", 'country': country, 'region': None, 'name': "Rotterdam"},
            {'code': "NL-HTB", 'country': country, 'region': None, 'name': "’s-Hertogenbosch"},
            {'code': "NL-HA9", 'country': country, 'region': None, 'name': "The Hague"},
            {'code': "NL-TLB", 'country': country, 'region': None, 'name': "Tilburg"},
            {'code': "NL-UTC", 'country': country, 'region': None, 'name': "Utrecht"},
            {'code': "NL-VEN", 'country': country, 'region': None, 'name': "Venlo"},
            # # {'code': "NL-ZST", 'country': country, 'region': None, 'name': "Zaanstad"}, #belongs to Amsterdam
            # # {'code': "NL-ZTM", 'country': country, 'region': None, 'name': "Zoetermeer"}, #belongs to the Hague
            {'code': "NL-ZWO", 'country': country, 'region': None, 'name': "Zwolle"},
        ]

        country = 'BE'
        cities_BE = [
            {"code": "BE-ANR", "country": country, "region": None, "name": "Antwerpen"},
            {"code": "BE-BGS", "country": country, "region": None, "name": "Bruges"},
            {"code": "BE-BRU", "country": country, "region": None, "name": "Brussels"},
            {"code": "BE-CRL", "country": country, "region": None, "name": "Charleroi"},
            {"code": "BE-GNE", "country": country, "region": None, "name": "Ghent"},
            {"code": "BE-LEU", "country": country, "region": None, "name": "Leuven"},
            {"code": "BE-LGG", "country": country, "region": None, "name": "Liège"},
            {"code": "BE-MQS", "country": country, "region": None, "name": "Mons"},
            {"code": "BE-NAM", "country": country, "region": None, "name": "Namur"},
        ]

        country = 'DK'
        cities_DK = [
            {'code': 'DK-AAR', 'country': country, 'region': None, 'name': 'Aarhus'},
            {'code': 'DK-AAL', 'country': country, 'region': None, 'name': 'Alborg'},
            # {'code': 'DK-ANH', 'country': country, 'region': None, 'name': 'Anholt'},
            {'code': 'DK-BLL', 'country': country, 'region': None, 'name': 'Billund'},
            # {'code': 'DK-BOS', 'country': country, 'region': None, 'name': 'Bojden'},
            {'code': 'DK-BHL', 'country': country, 'region': None, 'name': 'Bornholm'},
            {'code': 'DK-CPH', 'country': country, 'region': None, 'name': 'Copenhagen'},
            {'code': 'DK-EBJ', 'country': country, 'region': None, 'name': 'Esbjerg'},
            # {'code': 'DK-FYH', 'country': country, 'region': None, 'name': 'Fynshav'},
            # {'code': 'DK-GRE', 'country': country, 'region': None, 'name': 'Grenaa'}, #too small
            # {'code': 'DK-HLS', 'country': country, 'region': None, 'name': 'Helsingør'}, #population of 61.000 only
            # {'code': 'DK-HIR', 'country': country, 'region': None, 'name': 'Hirtshals'}, #too small
            # {'code': 'DK-KAL', 'country': country, 'region': None, 'name': 'Kalundborg'},
            {'code': 'DK-KRP', 'country': country, 'region': None, 'name': 'Karup'},
            {'code': 'DK-LES', 'country': country, 'region': None, 'name': 'Læsø'},
            # {'code': 'DK-MRS', 'country': country, 'region': None, 'name': 'Marstal'},
            {'code': 'DK-ODE', 'country': country, 'region': None, 'name': 'Odense'},
            # {'code': 'DK-ROD', 'country': country, 'region': None, 'name': 'Rodbyhavn'},
            # {'code': 'DK-RNN', 'country': country, 'region': None, 'name': 'Rønne'},
            {'code': 'DK-RKE', 'country': country, 'region': None, 'name': 'Roskilde'},
            {'code': 'DK-SGD', 'country': country, 'region': None, 'name': 'Sønderborg'},
        ]

        country = 'FO'
        cities_FO = [
            # {'code': 'FO-TOR', 'country': country, 'region': None, 'name': 'Tórshavn'},
            {'code': 'FO-FAE', 'country': country, 'region': None, 'name': 'Vágar, Faroe'},
         ]


        country = 'SE'
        cities_SE = [
            {'code': 'SE-ANG', 'country': country, 'region': None, 'name': 'Ängelholm'},
            {'code': 'SE-AJR', 'country': country, 'region': None, 'name': 'Arvidsjaur'},
            {'code': 'SE-BLE', 'country': country, 'region': None, 'name': 'Borlänge'},
            {'code': 'SE-GEV', 'country': country, 'region': None, 'name': 'Gällivare'},
            {'code': 'SE-GOT', 'country': country, 'region': None, 'name': 'Gothenburg'}, # Tens posat Göteborg a ses ciutats
            {'code': 'SE-HFS', 'country': country, 'region': None, 'name': 'Hagfors'},
            {'code': 'SE-HAD', 'country': country, 'region': None, 'name': 'Halmstad'},
            {'code': 'SE-HMV', 'country': country, 'region': None, 'name': 'Hemavan'},
            {'code': 'SE-JKG', 'country': country, 'region': None, 'name': 'Jönköping'},
            {'code': 'SE-KLR', 'country': country, 'region': None, 'name': 'Kalmar'},
            {'code': 'SE-KSD', 'country': country, 'region': None, 'name': 'Karlstad'},
            {'code': 'SE-KRN', 'country': country, 'region': None, 'name': 'Kiruna'},
            {'code': 'SE-KRF', 'country': country, 'region': None, 'name': 'Kramfors'},
            {'code': 'SE-KID', 'country': country, 'region': None, 'name': 'Kristianstad'},
            {'code': 'SE-LPI', 'country': country, 'region': None, 'name': 'Linköping'},
            {'code': 'SE-LLA', 'country': country, 'region': None, 'name': 'Luleå'},
            {'code': 'SE-LYC', 'country': country, 'region': None, 'name': 'Lycksele'},
            {'code': 'SE-MMA', 'country': country, 'region': None, 'name': 'Malmö'},
            {'code': 'SE-MRA', 'country': country, 'region': None, 'name': 'Mora'},
            {'code': 'SE-NRK', 'country': country, 'region': None, 'name': 'Norrköping'},
            {'code': 'SE-NYO', 'country': country, 'region': None, 'name': 'Nyköping'},
            {'code': 'SE-ORB', 'country': country, 'region': None, 'name': 'Örebro'},
            {'code': 'SE-OER', 'country': country, 'region': None, 'name': 'Örnsköldsvik'},
            {'code': 'SE-OSD', 'country': country, 'region': None, 'name': 'Östersund'},
            {'code': 'SE-PJA', 'country': country, 'region': None, 'name': 'Pajala'},
            {'code': 'SE-RNB', 'country': country, 'region': None, 'name': 'Ronneby'},
            {'code': 'SE-SFT', 'country': country, 'region': None, 'name': 'Skellefteå'},
            {'code': 'SE-STO', 'country': country, 'region': None, 'name': 'Stockholm'},
            {'code': 'SE-SDL', 'country': country, 'region': None, 'name': 'Sundsvall'},
            {'code': 'SE-TYF', 'country': country, 'region': None, 'name': 'Torsby'},
            {'code': 'SE-THN', 'country': country, 'region': None, 'name': 'Trollhättan'},
            {'code': 'SE-UME', 'country': country, 'region': None, 'name': 'Umeå'},
            {'code': 'SE-UPP', 'country': country, 'region': None, 'name': 'Uppsala'},
            {'code': 'SE-VST', 'country': country, 'region': None, 'name': 'Västerås'},
            {'code': 'SE-VHM', 'country': country, 'region': None, 'name': 'Vilhelmina'},
            {'code': 'SE-VBY', 'country': country, 'region': None, 'name': 'Visby'},
            {'code': 'SE-VXO', 'country': country, 'region': None, 'name': 'Växjö'},

        ]

        country = 'NO'
        cities_NO = [
            {"code": "NO-AES", "country": country, "region": None, "name": "Ålesund"},
            {"code": "NO-ALF", "country": country, "region": None, "name": "Alta"},
            {"code": "NO-ADN", "country": country, "region": None, "name": "Andenes"},
            {"code": "NO-BDU", "country": country, "region": None, "name": "Bardufoss"},
            {"code": "NO-BJF", "country": country, "region": None, "name": "Båtsfjord"},
            {"code": "NO-BGO", "country": country, "region": None, "name": "Bergen"},
            {"code": "NO-BVG", "country": country, "region": None, "name": "Berlevåg"},
            {"code": "NO-BOO", "country": country, "region": None, "name": "Bodø"},
            {"code": "NO-BKS", "country": country, "region": None, "name": "Brekstad"},
            {"code": "NO-BNN", "country": country, "region": None, "name": "Brønnøysund"},
            {"code": "NO-FGN", "country": country, "region": None, "name": "Fagernes"},
            {"code": "NO-FRO", "country": country, "region": None, "name": "Florø"},
            {"code": "NO-FDE", "country": country, "region": None, "name": "Førde"},
            {"code": "NO-HFT", "country": country, "region": None, "name": "Hammerfest"},
            {"code": "NO-HRD", "country": country, "region": None, "name": "Harstad"},
            {"code": "NO-HVK", "country": country, "region": None, "name": "Hasvik"},
            {"code": "NO-HAU", "country": country, "region": None, "name": "Haugesund"},
            {"code": "NO-HVG", "country": country, "region": None, "name": "Honningsvåg"},
            {"code": "NO-KKN", "country": country, "region": None, "name": "Kirkenes"},
            {"code": "NO-KRS", "country": country, "region": None, "name": "Kristiansand"},
            {"code": "NO-KSU", "country": country, "region": None, "name": "Kristiansund"},
            {"code": "NO-LKL", "country": country, "region": None, "name": "Lakselv"},
            {"code": "NO-LRI", "country": country, "region": None, "name": "Leirvik"},
            {"code": "NO-LKN", "country": country, "region": None, "name": "Leknes"},
            # {"code": "Longyearbyen", "country": country, "region": None, "name": "Longyearbyen"},
            {"code": "NO-MEH", "country": country, "region": None, "name": "Mehamn"},
            {"code": "NO-MQN", "country": country, "region": None, "name": "Mo i Rana"},
            {"code": "NO-MOL", "country": country, "region": None, "name": "Molde"},
            {"code": "NO-MJF", "country": country, "region": None, "name": "Mosjøen"},
            {"code": "NO-OSY", "country": country, "region": None, "name": "Namsos"},
            {"code": "NO-NTB", "country": country, "region": None, "name": "Notodden"},
            # {"code": "Ny-Ålesund", "country": country, "region": None, "name": "Ny-Ålesund"},
            {"code": "NO-ORS", "country": country, "region": None, "name": "Ørsta"},
            {"code": "NO-OSL", "country": country, "region": None, "name": "Oslo"},
            {"code": "NO-RRS", "country": country, "region": None, "name": "Røros"},
            {"code": "NO-RVK", "country": country, "region": None, "name": "Rørvik"},
            {"code": "NO-RET", "country": country, "region": None, "name": "Røst"},
            {"code": "NO-SDN", "country": country, "region": None, "name": "Sandane"},
            {"code": "NO-TRF", "country": country, "region": None, "name": "Sandefjord"},
            {"code": "NO-SSJ", "country": country, "region": None, "name": "Sandnessjøen"},
            {"code": "NO-SOG", "country": country, "region": None, "name": "Sogndal"},
            {"code": "NO-SOJ", "country": country, "region": None, "name": "Sørkjosen"},
            {"code": "NO-SVG", "country": country, "region": None, "name": "Stavanger"},
            {"code": "NO-SKN", "country": country, "region": None, "name": "Stokmarknes"},
            # {"code": "Sveagruva", "country": country, "region": None, "name": "Sveagruva"},
            {"code": "NO-SVJ", "country": country, "region": None, "name": "Svolvær"},
            {"code": "NO-TOS", "country": country, "region": None, "name": "Tromsø"},
            {"code": "NO-TRD", "country": country, "region": None, "name": "Trondheim"},
            {"code": "NO-VDS", "country": country, "region": None, "name": "Vadsø"},
            {"code": "NO-VEY", "country": country, "region": None, "name": "Værøy"},
            {"code": "NO-VAO", "country": country, "region": None, "name": "Vardø"},

        ]

        country = 'FI'
        cities_FI = [
            {"code": "FI-ENF", "country": country, "region": None, "name": "Enontekiö"}, #Enontekiö Airport
            {"code": "FI-HEL", "country": country, "region": None, "name": "Helsinki"}, #Helsinki-Vantaa Airport
            {"code": "FI-IVL", "country": country, "region": None, "name": "Ivalo"}, #Ivalo Airport
            {"code": "FI-JOE", "country": country, "region": None, "name": "Joensuu"}, #Joensuu Airport
            {"code": "FI-JYV", "country": country, "region": None, "name": "Jyväskylä"}, #Jyväskylä Airport
            {"code": "FI-KAJ", "country": country, "region": None, "name": "Kajaani"}, #Kajaani Airport
            {"code": "FI-KEM", "country": country, "region": None, "name": "Kemi"}, #Kemi-Tornio Airport
            {"code": "FI-KTT", "country": country, "region": None, "name": "Kittilä"}, #Kittilä Airport
            {"code": "FI-KOK", "country": country, "region": None, "name": "Kokkola"}, #Kokkola-Pietarsaari Airport
            {"code": "FI-KUO", "country": country, "region": None, "name": "Kuopio"}, #Kuopio Airport
            {"code": "FI-KAO", "country": country, "region": None, "name": "Kuusamo"}, #Kuusamo Airport
            {"code": "FI-LHI", "country": country, "region": None, "name": "Lahti"},
            {"code": "FI-LPP", "country": country, "region": None, "name": "Lappeenranta"}, #Lappeenranta Airport
            {"code": "FI-MHQ", "country": country, "region": None, "name": "Mariehamn"}, #Mariehamn Airport
            {"code": "FI-OUL", "country": country, "region": None, "name": "Oulu"}, #Oulu Airport
            {"code": "FI-POR", "country": country, "region": None, "name": "Pori"}, #Pori Airport
            {"code": "FI-RVN", "country": country, "region": None, "name": "Rovaniemi"}, #Rovaniemi Airport
            {"code": "FI-SVL", "country": country, "region": None, "name": "Savonlinna"}, #Savonlinna Airport
            {"code": "FI-TMP", "country": country, "region": None, "name": "Tampere"}, #Tampere-Pirkkala Airport
            {"code": "FI-TKU", "country": country, "region": None, "name": "Turku"}, #Turku Airport
            {"code": "FI-VAA", "country": country, "region": None, "name": "Vaasa"}, #Vaasa Airport
        ]

        country = 'CZ'
        cities_CZ = [
            {"code": "CZ-BRQ", "country": country, "region": None, "name": "Brno"}, #Brno-Tuřany Airport
            {"code": "CZ-KLV", "country": country, "region": None, "name": "Karlovy Vary"}, #Karlovy Vary Airport
            {"code": "CZ-LBR", "country": country, "region": None, "name": "Liberec"},
            {"code": "CZ-OLO", "country": country, "region": None, "name": "Olomouc"},
            {"code": "CZ-OSR", "country": country, "region": None, "name": "Ostrava"}, #Ostrava Airport
            {"code": "CZ-PRB", "country": country, "region": None, "name": "Pardubice"}, #Pardubice Airport
            {"code": "CZ-PLZ", "country": country, "region": None, "name": "Pilsen"},
            {"code": "CZ-PRG", "country": country, "region": None, "name": "Prague"}, #Prague Airport
        ]

        country = 'AT'
        cities_AT = [
            {"code": "AT-GRZ", "country": country, "region": None, "name": "Graz"}, #Graz Airport
            {"code": "AT-INN", "country": country, "region": None, "name": "Innsbruck"}, #Innsbruck Airport
            {"code": "AT-KLU", "country": country, "region": None, "name": "Klagenfurt"}, #Klagenfurt Airport
            {"code": "AT-LNZ", "country": country, "region": None, "name": "Linz"}, #Linz Airport
            {"code": "AT-SZG", "country": country, "region": None, "name": "Salzburg"}, #Salzburg Airport
            {"code": "AT-VIE", "country": country, "region": None, "name": "Vienna"}, #Vienna Airport
        ]

        country = 'LU'
        cities_LU = [
            {"code": "LU-LUX", "country": country, "region": None, "name": "Luxembourg City"}, #Luxembourg Findel Airport
        ]

        country = 'IS'
        cities_IS = [
            {"code": "IS-AKU", "country": country, "region": None, "name": "Akureyri"}, #Akureyri Airport
            # {"code": "IS-BIU", "country": country, "region": None, "name": "Bíldudalur"}, #Bíldudalur Airport
            {"code": "IS-EGS", "country": country, "region": None, "name": "Egilsstaðir"}, #Egilsstaðir Airport
            # {"code": "IS-DPV", "country": country, "region": None, "name": "Djúpavík"}, #Gjögur Airport
            # {"code": "IS-GRY", "country": country, "region": None, "name": "Grímsey"}, #Grímsey Airport
            # {"code": "IS-HFN", "country": country, "region": None, "name": "Höfn"}, #Hornafjörður Airport
            # {"code": "IS-ISA", "country": country, "region": None, "name": "Ísafjörður"}, #Ísafjörður Airport
            # {"code": "IS-KEF", "country": country, "region": None, "name": "Keflavík"}, #Keflavík Airport
            {"code": "IS-REY", "country": country, "region": None, "name": "Reykjavík"}, #Reykjavík Airport
            # {"code": "Þórshöfn", "country": country, "region": None, "name": "Þórshöfn"}, #Þórshöfn Airport
            # {"code": "IS-VPN", "country": country, "region": None, "name": "Vopnafjörður"}, #Vopnafjörður Airport
        ]

        country = 'GR'
        cities_GR = [
            {"code": "GR-AXD", "country": country, "region": None, "name": "Alexandroupoli"}, #Alexandroupolis Airport
            # {"code": "GR-AMO", "country": country, "region": None, "name": "Amorgós"},
            {"code": "GR-JTY", "country": country, "region": None, "name": "Astypalaia"}, #Astypalaia Island National Airport
            {"code": "GR-ATH", "country": country, "region": None, "name": "Athens"}, #Athens Airport
            {"code": "GR-CHQ", "country": country, "region": None, "name": "Chania"}, #Chania Airport
            {"code": "GR-JKH", "country": country, "region": None, "name": "Chios"}, #Chios Island National Airport
            {"code": "GR-CFU", "country": country, "region": None, "name": "Corfu"}, #Corfu Airport
            # {"code": "GR-DON", "country": country, "region": None, "name": "Donousa Kykladon"},
            {"code": "GR-HKL", "country": country, "region": None, "name": "Heraklion"}, #Heraklion Airport
            {"code": "GR-JIK", "country": country, "region": None, "name": "Ikaria"}, #Ikaria Island National Airport
            {"code": "GR-IOA", "country": country, "region": None, "name": "Ioannina"}, #Ioannina National Airport
            {"code": "GR-KLX", "country": country, "region": None, "name": "Kalamata"}, #Kalamata Airport
            {"code": "GR-KMI", "country": country, "region": None, "name": "Kalymnos"}, #Kalymnos Island National Airport
            {"code": "GR-AOK", "country": country, "region": None, "name": "Karpathos"}, #Karpathos Island National Airport
            {"code": "GR-KSJ", "country": country, "region": None, "name": "Kasos"}, #Kassos Island Public Airport
            {"code": "GR-KZS", "country": country, "region": None, "name": "Kastelorizo"}, #Kastelorizo Island Public Airport
            {"code": "GR-KSO", "country": country, "region": None, "name": "Kastoria"}, #Kastoria National Airport
            {"code": "GR-KVA", "country": country, "region": None, "name": "Kavala"}, #Kavala Airport
            {"code": "GR-K33", "country": country, "region": None, "name": "Kefalonia"}, #Kefalonia Island Airport
            {"code": "GR-KGS", "country": country, "region": None, "name": "Kos"}, #Kos Island Airport
            {"code": "GR-KZI", "country": country, "region": None, "name": "Kozani"}, #Kozani National Airport
            {"code": "GR-KIT", "country": country, "region": None, "name": "Kythira"}, #Kythira Island National Airport
            {"code": "GR-LRA", "country": country, "region": None, "name": "Lárisa"},
            {"code": "GR-LXS", "country": country, "region": None, "name": "Lemnos"}, #Lemnos Airport
            {"code": "GR-LRS", "country": country, "region": None, "name": "Leros"}, #Leros Municipal Airport
            {"code": "GR-MLO", "country": country, "region": None, "name": "Milos"}, #Milos Island National Airport
            {"code": "GR-JMK", "country": country, "region": None, "name": "Mykonos"}, #Mykonos Island National Airport
            {"code": "GR-MJT", "country": country, "region": None, "name": "Mytilene"}, #Mytilene Airport
            {"code": "GR-JNX", "country": country, "region": None, "name": "Naxos Island"}, #Naxos Island National Airport
            {"code": "GR-GPA", "country": country, "region": None, "name": "Patras"}, #Araxos National Airport
            # {"code": "GR-PIR", "country": country, "region": None, "name": "Pireás"}, #part of Athens
            # {"code": "GR-RAF", "country": country, "region": None, "name": "Rafina"},
            {"code": "GR-RHO", "country": country, "region": None, "name": "Rhodes"}, #Rhodes Airport
            {"code": "GR-SMI", "country": country, "region": None, "name": "Samos"}, #Samos Airport
            {"code": "GR-ATN", "country": country, "region": None, "name": "Santorini"}, #Santorini (Thira) National Airport
            {"code": "GR-JSH", "country": country, "region": None, "name": "Sitia"}, #Sitia Public Airport
            {"code": "GR-JSI", "country": country, "region": None, "name": "Skiathos"}, #Skiathos Island National Airport
            {"code": "GR-SKU", "country": country, "region": None, "name": "Skyros"}, #Skyros Island National Airport
            {"code": "GR-SKG", "country": country, "region": None, "name": "Thessaloniki"}, #Thessaloniki Airport
            {"code": "GR-VOL", "country": country, "region": None, "name": "Volos"}, #Nea Anchialos National Airport
            {"code": "GR-ZTH", "country": country, "region": None, "name": "Zakynthos"}, #Zakynthos Airport
        ]

        country = 'LT'
        cities_LT = [
            {"code": "LT-KUN", "country": country, "region": None, "name": "Kaunas"}, #Kaunas Airport
            {"code": "LT-KLJ", "country": country, "region": None, "name": "Klaipėda"},
            {"code": "LT-PLQ", "country": country, "region": None, "name": "Palanga"}, #Palanga Airport
            {"code": "LT-PNV", "country": country, "region": None, "name": "Panevėžys"},
            {"code": "LT-SQQ", "country": country, "region": None, "name": "Šiauliai"},
            {"code": "LT-VIL", "country": country, "region": None, "name": "Vilnius"}, #Vilnius Airport
        ]

        country = 'LV'
        cities_LV = [
            {"code": "LV-DGP", "country": country, "region": None, "name": "Daugavpils"},
            {"code": "LV-LPX", "country": country, "region": None, "name": "Liepāja"}, #Liepāja Airport
            {"code": "LV-RIX", "country": country, "region": None, "name": "Riga"}, #Riga Airport
        ]

        country = 'EE'
        cities_EE = [
            {"code": "EE-KDL", "country": country, "region": None, "name": "Kärdla"}, #Kärdla Airport
            # {"code": "EE-KHN", "country": country, "region": None, "name": "Kihnu"}, #Kihnu Airfield - no flights
            {"code": "EE-URE", "country": country, "region": None, "name": "Kuressaare"}, #Kuressaare Airport
            {"code": "EE-PRN", "country": country, "region": None, "name": "Pärnu"}, #Pärnu Airport
            # {"code": "Ruhnu", "country": country, "region": None, "name": "Ruhnu"}, #Ruhnu Airfield - no flights
            {"code": "EE-TLL", "country": country, "region": None, "name": "Tallinn"}, #Tallinn Airport
            {"code": "EE-TAY", "country": country, "region": None, "name": "Tartu"}, #Tartu Airport
        ]

        country = 'SI'
        cities_SI = [
            {"code": "SI-MBX", "country": country, "region": None, "name": "Maribor"}, #Maribor Airport
            {"code": "SI-LJA", "country": country, "region": None, "name": "Ljubljana"}, #Ljubljana Airport
        ]

        country = 'HR'
        cities_HR = [
            {"code": "HR-SUP", "country": country, "region": None, "name": "Brač"}, #Brač Airport
            {"code": "HR-DBV", "country": country, "region": None, "name": "Dubrovnik"}, #Dubrovnik Airport
            {"code": "HR-OSI", "country": country, "region": None, "name": "Osijek"}, #Osijek Airport
            {"code": "HR-PUY", "country": country, "region": None, "name": "Pula"}, #Pula Airport
            {"code": "HR-RJK", "country": country, "region": None, "name": "Rijeka"}, #Rijeka Airport
            {"code": "HR-SPU", "country": country, "region": None, "name": "Split"}, #Split Airport
            {"code": "HR-ZAD", "country": country, "region": None, "name": "Zadar"}, #Zadar Airport
            {"code": "HR-ZAG", "country": country, "region": None, "name": "Zagreb"}, #Zagreb Airport
        ]

        country = 'MT'
        cities_MT = [
            {"code": "MT-MLA", "country": country, "region": None, "name": "Malta"}, #Malta Airport
        ]

        country = 'HU'
        cities_HU = [
            {"code": "HU-BTN", "country": country, "region": None, "name": "Balaton"}, #Hévíz-Balaton Airport
            {"code": "HU-BUD", "country": country, "region": None, "name": "Budapest"}, #Budapest Airport
            {"code": "HU-DEB", "country": country, "region": None, "name": "Debrecen"}, #Debrecen Airport
            {"code": "HU-GYO", "country": country, "region": None, "name": "Győr"}, #Győr-Pér Airport
            {"code": "HU-MCQ", "country": country, "region": None, "name": "Miskolc"},
            {"code": "HU-NGH", "country": country, "region": None, "name": "Nyíregyháza"},
            {"code": "HU-PEC", "country": country, "region": None, "name": "Pécs"},
            {"code": "HU-SZE", "country": country, "region": None, "name": "Szeged"},
            {"code": "HU-SZR", "country": country, "region": None, "name": "Székesfehérvár"},

        ]

        country = 'PL'
        cities_PL = [
            {"code": "PL-BZG", "country": country, "region": None, "name": "Bydgoszcz"}, #Bydgoszcz Ignacy Jan Paderewski Airport
            {"code": "PL-GDN", "country": country, "region": None, "name": "Gdańsk"}, #Gdańsk Lech Wałęsa Airport
            {"code": "PL-KTW", "country": country, "region": None, "name": "Katowice"}, #Katowice Airport
            {"code": "PL-KRK", "country": country, "region": None, "name": "Kraków"}, #John Paul II Airport Kraków-Balice
            {"code": "PL-LOD", "country": country, "region": None, "name": "Łódź"}, #Łódź Władysław Reymont Airport
            {"code": "PL-LUL", "country": country, "region": None, "name": "Lublin"}, #Lublin Airport
            {"code": "PL-OLS", "country": country, "region": None, "name": "Olsztyn"}, #Olsztyn-Mazury Airport
            {"code": "PL-POZ", "country": country, "region": None, "name": "Poznań"}, #Poznań-Ławica Airport
            {"code": "PL-RDM", "country": country, "region": None, "name": "Radom"}, #Radom Airport
            {"code": "PL-RZE", "country": country, "region": None, "name": "Rzeszów"}, #Rzeszów-Jasionka Airport
            {"code": "PL-SZZ", "country": country, "region": None, "name": "Szczecin"}, #"Solidarity" Szczecin-Goleniów Airport
            {"code": "PL-WAW", "country": country, "region": None, "name": "Warsaw"}, #Warsaw Chopin Airport #Warsaw-Modlin Mazovia Airport
            {"code": "PL-WRO", "country": country, "region": None, "name": "Wrocław"}, #Wrocław Airport
            {"code": "PL-IEG", "country": country, "region": None, "name": "Zielona Góra"}, #Zielona Góra Airport
        ]

        country = 'SK'
        cities_SK = [
            {"code": "SK-BTS", "country": country, "region": None, "name": "Bratislava"}, #M. R. Štefánik Airport
            {"code": "SK-KSC", "country": country, "region": None, "name": "Košice"}, #Košice Airport
            {"code": "SK-POP", "country": country, "region": None, "name": "Poprad"}, #Poprad-Tatry Airport
            {"code": "SK-SLD", "country": country, "region": None, "name": "Sliač"}, #Sliač Airport
        ]

        country = 'BA'
        cities_BA = [
            {"code": "BA-BNX", "country": country, "region": None, "name": "Banja Luka"}, #Banja Luka Airport
            {"code": "BA-BHC", "country": country, "region": None, "name": "Bihać"},
            {"code": "BA-OMO", "country": country, "region": None, "name": "Mostar"}, #Mostar Airport
            {"code": "BA-SJJ", "country": country, "region": None, "name": "Sarajevo"}, #Sarajevo Airport
            {"code": "BA-TZL", "country": country, "region": None, "name": "Tuzla"}, #Tuzla Airport
            {"code": "BA-ZCA", "country": country, "region": None, "name": "Zenica"},
        ]

        country = 'RS'
        cities_RS = [
            {"code": "RS-BEG", "country": country, "region": None, "name": "Belgrade"}, #Belgrade Nikola Tesla Airport
            # {"code": "RS-BOR", "country": country, "region": None, "name": "Bor"}, #Bor Airport without iata code
            {"code": "RS-KGV", "country": country, "region": None, "name": "Kragujevac"},
            {"code": "RS-LVC", "country": country, "region": None, "name": "Leskovac"},
            {"code": "RS-INI", "country": country, "region": None, "name": "Niš"}, #Niš Constantine the Great Airport
            {"code": "RS-NVS", "country": country, "region": None, "name": "Novi Sad"},
            {"code": "RS-PYJ", "country": country, "region": None, "name": "Pančevo"},
            # {"code": "RS-PRN", "country": country, "region": None, "name": "Priština"},
            # {"code": "RS-PRZ", "country": country, "region": None, "name": "Prizren"},
            {"code": "RS-SUB", "country": country, "region": None, "name": "Subotica"},
        ]

        country = 'ME'
        cities_ME = [
            {"code": "ME-TGD", "country": country, "region": None, "name": "Podgorica"}, #Podgorica Airport
            {"code": "ME-TIV", "country": country, "region": None, "name": "Tivat"}, #Tivat Airport
        ]

        country = 'CY'
        cities_CY = [
            {"code": "CY-LCA", "country": country, "region": None, "name": "Larnaca"}, #Larnaca Airport
            {"code": "CY-NIC", "country": country, "region": None, "name": "Nicosia"}, #Ercan Airport
            {"code": "CY-PFO", "country": country, "region": None, "name": "Paphos"}, #Paphos Airport
        ]

        country = 'MK'
        cities_MK = [
            {"code": "MK-OHD", "country": country, "region": None, "name": "Ohrid"}, #Ohrid "St. Paul the Apostle" Airport
            {"code": "MK-SKP", "country": country, "region": None, "name": "Skopje"}, #Skopje "Alexander the Great" Airport
        ]

        country = 'AL'
        cities_AL = [
            # {"code": "AL-TIA", "country": country, "region": None, "name": "Tirana"}, #Tirana Airport

            {"code": "AL-DRZ", "country": country, "region": None, "name": "Durrës"},
            {"code": "AL-NPP", "country": country, "region": None, "name": "Elbasan"},
            {"code": "AL-TIA", "country": country, "region": None, "name": "Tirana"}, #Tirana Airport
            {"code": "AL-VOA", "country": country, "region": None, "name": "Vlorë"},
        ]

        country = 'RO'
        cities_RO = [
            {"code": "RO-ARW", "country": country, "region": None, "name": "Arad"}, #Arad Airport
            {"code": "RO-BCM", "country": country, "region": None, "name": "Bacău"}, #Bacău Airport
            {"code": "RO-BAY", "country": country, "region": None, "name": "Baia Mare"}, #Baia Mare Airport
            {"code": "RO-BOS", "country": country, "region": None, "name": "Botoșani"},
            {"code": "RO-BRA", "country": country, "region": None, "name": "Brăila"},
            {"code": "RO-BRV", "country": country, "region": None, "name": "Brașov"},
            {"code": "RO-BUH", "country": country, "region": None, "name": "Bucharest"}, #Henri Coandă Airport
            {"code": "RO-BUZ", "country": country, "region": None, "name": "Buzău"},
            {"code": "RO-CLJ", "country": country, "region": None, "name": "Cluj-Napoca"}, #Cluj Airport
            {"code": "RO-CND", "country": country, "region": None, "name": "Constanța"}, #Mihail Kogălniceanu Airport
            {"code": "RO-CRV", "country": country, "region": None, "name": "Craiova"}, #Craiova Airport
            {"code": "RO-GAL", "country": country, "region": None, "name": "Galați"},
            {"code": "RO-IAS", "country": country, "region": None, "name": "Iași"}, #Iași Airport
            {"code": "RO-OMR", "country": country, "region": None, "name": "Oradea"}, #Oradea Airport
            {"code": "RO-PIT", "country": country, "region": None, "name": "Pitești"},
            {"code": "RO-PLT", "country": country, "region": None, "name": "Ploiești"},
            {"code": "RO-SUJ", "country": country, "region": None, "name": "Satu Mare"}, #Satu Mare Airport
            {"code": "RO-SBZ", "country": country, "region": None, "name": "Sibiu"}, #Sibiu Airport
            {"code": "RO-SCV", "country": country, "region": None, "name": "Suceava"}, #Suceava Airport
            {"code": "RO-TGM", "country": country, "region": None, "name": "Târgu Mureș"}, #Târgu Mureș Airport
            {"code": "RO-TSR", "country": country, "region": None, "name": "Timișoara"}, #Timișoara Airport

        ]

        country = 'BG'
        cities_BG = [
            {"code": "BG-BOJ", "country": country, "region": None, "name": "Burgas"}, #Burgas Airport
            {"code": "BG-PVN", "country": country, "region": None, "name": "Pleven"},
            {"code": "BG-PDV", "country": country, "region": None, "name": "Plovdiv"}, #Plovdiv Airport
            {"code": "BG-RDU", "country": country, "region": None, "name": "Ruse"},
            {"code": "BG-SOF", "country": country, "region": None, "name": "Sofia"}, #Sofia Airport
            {"code": "BG-SZR", "country": country, "region": None, "name": "Stara Zagora"},
            {"code": "BG-VAR", "country": country, "region": None, "name": "Varna"}, #Varna Airport
        ]

        country = 'RU'
        cities_RU = [
            {"code": "RU-KGD", "country": country, "region": None, "name": "Kaliningrad"},
            {"code": "RU-KZN", "country": country, "region": None, "name": "Kazan"},
            # {"code": "RU-KRR", "country": country, "region": None, "name": "Krasnodar"},
            {"code": "RU-MOW", "country": country, "region": None, "name": "Moscow"},
            {"code": "RU-GOJ", "country": country, "region": None, "name": "Nizhny Novgorod"},
            {"code": "RU-RND", "country": country, "region": None, "name": "Rostov-on-Don"},
            {"code": "RU-LED", "country": country, "region": None, "name": "Saint Petersburg"},
            {"code": "RU-KUF", "country": country, "region": None, "name": "Samara"},
            {"code": "RU-SKX", "country": country, "region": None, "name": "Saransk"},
            {"code": "RU-AER", "country": country, "region": None, "name": "Sochi"},
            # {"code": "RU-UFA", "country": country, "region": None, "name": "Ufa"},
            {"code": "RU-VOG", "country": country, "region": None, "name": "Volgograd"},
            {"code": "RU-YEK", "country": country, "region": None, "name": "Yekaterinburg"},
        ]

        country = 'GI'
        cities_GI = [
            {"code": "GI-GIB", "country": country, "region": None, "name": "Gibraltar"},
        ]

        country = 'AD'
        cities_AD = [
            {"code": "AD-ALV", "country": country, "region": None, "name": "Andorra la Vella"},
        ]

        country = 'TR'
        cities_TR = [
            # {"code": "TR-ADA", "country": country, "region": None, "name": "Adana"},
            {"code": "TR-ANK", "country": country, "region": None, "name": "Ankara"},
            {"code": "TR-AYT", "country": country, "region": None, "name": "Antalya"},
            # {"code": "TR-BTZ", "country": country, "region": None, "name": "Bursa"}, #no airport in Bursa
            {"code": "TR-IST", "country": country, "region": None, "name": "Istanbul"},
            {"code": "TR-IZM", "country": country, "region": None, "name": "İzmir"},
        ]

        country = 'XK'
        cities_XK = [
            {"code": "XK-DKV", "country": country, "region": None, "name": "Đakovica"},
            {"code": "XK-GNJ", "country": country, "region": None, "name": "Gnjilane"},
            {"code": "XK-MIT", "country": country, "region": None, "name": "Mitrovicë"}, #També es diu Kosovska Mitrovica
            {"code": "XK-PRN", "country": country, "region": None, "name": "Pristina"}, #Pristina International Airport Adem Jashari
            {"code": "XK-PRZ", "country": country, "region": None, "name": "Prizren"},
        ]

        country = 'LI'
        cities_LI = [
            {"code": "LI-SCN", "country": country, "region": None, "name": "Liechtenstein"},
            # {"code": "LI-SCN", "country": country, "region": None, "name": "Schaan"},
            # {"code": "LI-VDZ", "country": country, "region": None, "name": "Vaduz"},
        ]


        country = 'UA'
        cities_UA = [
            {"code": "UA-ACK", "country": country, "region": None, "name": "Alchevsk"},
            {"code": "UA-ERD", "country": country, "region": None, "name": "Berdyansk"},
            {"code": "UA-BZW", "country": country, "region": None, "name": "Bila Tserkva"}, #També es diu Belaja Zerkow
            {"code": "UA-KBP", "country": country, "region": None, "name": "Borýspil"}, # Boryspil Airport # DELETE CITY: population 56000 and airport included in Kiev
            {"code": "UA-ZUQ", "country": country, "region": None, "name": "Chernihiv"},
            {"code": "UA-CWC", "country": country, "region": None, "name": "Chernivtsi"}, #Chernivtsi Airport
            {"code": "UA-DNK", "country": country, "region": None, "name": "Dnipropetrovsk"}, #Dnipropetrovsk Airport
            {"code": "UA-DOK", "country": country, "region": None, "name": "Donetsk"},
            {"code": "UA-HOR", "country": country, "region": None, "name": "Hórlivka"}, #locode inventat. També es diu Górlovka
            {"code": "UA-IFO", "country": country, "region": None, "name": "Ivano-Frankivsk"}, #Ivano-Frankivsk Airport
            {"code": "UA-KHM", "country": country, "region": None, "name": "Jmelnitski"}, #També es diu Khmelnytskyi
            {"code": "UA-DZK", "country": country, "region": None, "name": "Kamianské"},
            {"code": "UA-KEH", "country": country, "region": None, "name": "Kerch"},
            {"code": "UA-KIV", "country": country, "region": None, "name": "Kharkiv"}, #Kharkiv Airport
            {"code": "UA-KHE", "country": country, "region": None, "name": "Kherson"}, #Kherson Airport
            {"code": "UA-IEV", "country": country, "region": None, "name": "Kiev"}, #Kiev Zhuliany Airport #More than one code found for this city_name: ['UA-IEV', 'UA-KIE']
            {"code": "UA-KIR", "country": country, "region": None, "name": "Kirovogrado"}, #també Kirovohrad
            {"code": "UA-KRQ", "country": country, "region": None, "name": "Kramatorsk"},
            {"code": "UA-KRE", "country": country, "region": None, "name": "Kremenchuk"},
            {"code": "UA-KWR", "country": country, "region": None, "name": "Kryvyi Rih"}, #Kryvyi Rih Airport
            {"code": "UA-VSG", "country": country, "region": None, "name": "Lugansk"},
            {"code": "UA-UCK", "country": country, "region": None, "name": "Lutsk"},
            {"code": "UA-LVV", "country": country, "region": None, "name": "Lviv"}, #Lviv Danylo Halytskyi Airport
            {"code": "UA-ISI", "country": country, "region": None, "name": "Lysychansk"}, #També es diu Lisichansk
            {"code": "UA-MKV", "country": country, "region": None, "name": "Makiivka"},
            {"code": "UA-MPW", "country": country, "region": None, "name": "Mariupol"},
            {"code": "UA-ZZO", "country": country, "region": None, "name": "Melitopol'"}, #Melitopol'
            {"code": "UA-NLV", "country": country, "region": None, "name": "Mykolaiv"},
            {"code": "UA-POL", "country": country, "region": None, "name": "Nikopol’"}, # Nikopol’
            {"code": "UA-ODS", "country": country, "region": None, "name": "Odessa"}, #Odessa Airport
            {"code": "UA-PAH", "country": country, "region": None, "name": "Pavlohrad"},
            {"code": "UA-PLV", "country": country, "region": None, "name": "Poltava"},
            {"code": "UA-RIV", "country": country, "region": None, "name": "Rivne"},
            {"code": "UA-ZUC", "country": country, "region": None, "name": "Sievierodonetsk"}, #També es diu Severodonetsk
            {"code": "UA-SIP", "country": country, "region": None, "name": "Simferopol"}, #Simferopol Airport
            {"code": "UA-SYA", "country": country, "region": None, "name": "Sloviansk"}, #També es diu Slov'yans'k
            {"code": "UA-UMY", "country": country, "region": None, "name": "Sumy"},
            {"code": "UA-TNL", "country": country, "region": None, "name": "Ternópil"},
            {"code": "UA-UZH", "country": country, "region": None, "name": "Úzhgorod"},
            {"code": "UA-VIN", "country": country, "region": None, "name": "Vinnytsia"}, #Havryshivka Airport
            {"code": "UA-YEN", "country": country, "region": None, "name": "Yenákiyeve"},
            {"code": "UA-ZPR", "country": country, "region": None, "name": "Zaporizhia"}, #Zaporizhia Airport
            {"code": "UA-ZTR", "country": country, "region": None, "name": "Zhytómyr"},

        ]

        country = 'BY'
        cities_BY = [
            {"code": "BY-MBV", "country": country, "region": None, "name": "Barysaŭ"}, #També es diu Borísov
            {"code": "BY-BQT", "country": country, "region": None, "name": "Brest, Belarus"}, #Brest Airport
            {"code": "BY-GME", "country": country, "region": None, "name": "Gomel"}, #Gomel Airport
            {"code": "BY-GDO", "country": country, "region": None, "name": "Grodno"}, #Hrodna Airport
            {"code": "BY-MSQ", "country": country, "region": None, "name": "Minsk"}, #Minsk National Airport
            {"code": "BY-MVQ", "country": country, "region": None, "name": "Mogilev"}, #Mogilev Airport
            {"code": "BY-SHO", "country": country, "region": None, "name": "Salihorsk"},
            {"code": "BY-VTB", "country": country, "region": None, "name": "Vitebsk"}, #Vitebsk Vostochny Airport

        ]

        country = 'MD'
        cities_MD = [
            {"code": "MD-KIV", "country": country, "region": None, "name": "Chișinău"},
            {"code": "MD-BEL", "country": country, "region": None, "name": "Bălți"},

        ]

        # country = 'SM' #no bus, train or car-pooling to be found in APIs
        # cities_SM = [
        #     {"code": "SM-SAI", "country": country, "region": None, "name": "San Marino"},
        # ]

        # country = 'MC' #no bus, train or car-pooling to be found in APIs
        # cities_MC = [
        #     {"code": "MC-MON", "country": country, "region": None, "name": "Montecarlo"},
        # ]




        cities = (cities_DE + cities_ES + cities_PT + cities_FR + cities_GB + cities_IT + cities_IE +
                  cities_CH + cities_NL + cities_BE + cities_DK+ cities_FO + cities_SE + cities_NO + cities_FI +
                  cities_CZ + cities_AT + cities_LU + cities_IS + cities_GR + cities_LT + cities_LV +
                  cities_EE + cities_SI + cities_HR + cities_MT + cities_HU + cities_PL + cities_SK +
                  cities_BA + cities_RS + cities_ME + cities_CY + cities_MK + cities_AL + cities_RO + cities_BG + cities_RU +
                  cities_GI + cities_TR + cities_AD + cities_XK + cities_LI + cities_BY + cities_UA + cities_MD)

        return cities

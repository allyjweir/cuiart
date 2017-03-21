# -*- coding: utf-8 -*-
import zeep

# Documentation for their original SOAP API can be found here:
# https://lite.realtime.nationalrail.co.uk/OpenLDBWS/
class NationalRailAPI:
    '''Wrapper class to access the National Rail's realtime SOAP API.'''

    wsdl_url = "https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16"

    def __init__(self, key):
        self.api_key = key
        self.client = zeep.Client(self.wsdl_url)

    def get_next_trains(self, from_station, to_station, num_services = 10):
        '''
        Gets next 10 trains that cover the requested route'''
        result = self.client.service.GetDepartureBoard(crs=from_station,
                    filterCrs = to_station,
                    numRows = num_services,
                    _soapheaders={"AccessToken": self.api_key})

        services = self._transform_services(result["trainServices"])

        return { "generated_at": result["generatedAt"],
                 "from_name": result["locationName"],
                 "from_crs": result["crs"],
                 "to_name": result["filterLocationName"],
                 "to_crs": result["filtercrs"],
                 "services": services }

    def _transform_services(self, trainServices):
        if trainServices == None:
            return []
        return [ Service(x) for x in trainServices["services"] ]

class Service:
    '''Describes a train service within the National Rail network.'''

    def __init__(self, api_object):
        '''Uses a `service` dictionary from the SOAP API and converts it to a
        Service Python object'''

        self.service_id = api_object["serviceID"]
        self.sta = api_object["sta"]
        self.eta = api_object["eta"]
        self.std = api_object["std"]
        self.etd = api_object["etd"]
        self.platform = api_object["platform"]
        self.operator = api_object["operator"]
        self.train_length = api_object["length"]  # Number of carraiges
        self.detach_front = api_object["detachFront"]  # Does the train detatch and leave from front of platform
        self.cancel_reason = api_object["cancelReason"]
        self.delay_reason = api_object["delayReason"]
        self.origin = Station(api_object["origin"]["location"][0])
        self.destination = Station(api_object["destination"]["location"][0])



class Station:
    '''Describes a station within the National Rail network'''

    def __init__(self, api_object):
        '''Takes a `location` dictionary from the response of the SOAP API and
        initialises a Station object from the containing details.
        '''

        self.name = api_object["locationName"]
        self.crs = api_object["crs"]
        self.via = api_object["via"]

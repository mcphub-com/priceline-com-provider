import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/tipsters/api/priceline-com-provider'

mcp = FastMCP('priceline-com-provider')

@mcp.tool()
def search_car_rentals(date_time_pickup: Annotated[str, Field(description='Pickup date and time')],
                       location_return: Annotated[str, Field(description='Location return code or id')],
                       location_pickup: Annotated[str, Field(description='Location pickup code or id. Ex: JFK or 1365100023, use Search locations api point')],
                       date_time_return: Annotated[str, Field(description='Return date and time')]) -> dict: 
    '''Search car rentals by filter. Indicate the `location_id` -> use `Search locations` api point'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/cars-rentals/search'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date_time_pickup': date_time_pickup,
        'location_return': location_return,
        'location_pickup': location_pickup,
        'date_time_return': date_time_return,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_hotels(date_checkout: Annotated[str, Field(description='Checkout date')],
                  date_checkin: Annotated[str, Field(description='Checkin date')],
                  sort_order: Annotated[Literal['HDR', 'PRICE', 'STAR', 'PROXIMITY', 'DEALS'], Field(description='')],
                  location_id: Annotated[str, Field(description='Location id, use Search locations api point')],
                  page_number: Annotated[Union[int, float, None], Field(description='Number of page Default: 0 Minimum: 0 Maximum: 500')] = None,
                  star_rating_ids: Annotated[Union[str, None], Field(description='Hotel star ratings')] = None,
                  rooms_number: Annotated[Union[int, float, None], Field(description='Rooms number Default: 1 Minimum: 1 Maximum: 8')] = None,
                  amenities_ids: Annotated[Union[str, None], Field(description='Amenities')] = None) -> dict: 
    '''Get available hotels by the filter. Indicate the `location_id` -> use `Search locations`, check-in and check-out date'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/hotels/search'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date_checkout': date_checkout,
        'date_checkin': date_checkin,
        'sort_order': sort_order,
        'location_id': location_id,
        'page_number': page_number,
        'star_rating_ids': star_rating_ids,
        'rooms_number': rooms_number,
        'amenities_ids': amenities_ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_cars_locations(name: Annotated[str, Field(description='Name')]) -> dict: 
    '''Search locations by name'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/cars-rentals/locations'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hotel_details(hotel_id: Annotated[Union[int, float], Field(description='Hotel id Default: 6733503 Minimum: 1')],
                  offset_of_reviews: Annotated[Union[int, float, None], Field(description='Offset of reviews Default: 0 Minimum: 0 Maximum: 1000')] = None) -> dict: 
    '''Get all reviews and images of the hotel by hotel_id'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/hotels/details'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'offset_of_reviews': offset_of_reviews,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_hotels_locations(name: Annotated[str, Field(description='Name')],
                            search_type: Annotated[Literal['ALL', 'CITY', 'AIRPORT', 'POI', 'HOTEL'], Field(description='')]) -> dict: 
    '''Search locations by name'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/hotels/locations'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'search_type': search_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_flights_locations(name: Annotated[str, Field(description='Name')]) -> dict: 
    '''Search airports and locations by name'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/flights/locations'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_flights(location_departure: Annotated[str, Field(description='Departure location code. Use Search locations api point')],
                   itinerary_type: Annotated[Literal['ONE_WAY', 'ROUND_TRIP'], Field(description='')],
                   date_departure: Annotated[str, Field(description='Departure date')],
                   class_type: Annotated[Literal['ECO', 'BUS', 'PEC', 'FST'], Field(description='')],
                   sort_order: Annotated[Literal['PRICE', 'ARRIVETIME', 'DEPARTTIME', 'TRAVELTIME'], Field(description='')],
                   location_arrival: Annotated[str, Field(description='Arrival location code')],
                   date_departure_return: Annotated[Union[str, None], Field(description='Departure date back')] = None,
                   price_max: Annotated[Union[int, float, None], Field(description='Price max Default: 20000 Minimum: 1 Maximum: 1000000')] = None,
                   price_min: Annotated[Union[int, float, None], Field(description='Price min Default: 100 Minimum: 1 Maximum: 1000000')] = None,
                   number_of_passengers: Annotated[Union[int, float, None], Field(description='Number of passengers Default: 1 Minimum: 1 Maximum: 7')] = None,
                   number_of_stops: Annotated[Union[int, float, None], Field(description='Number of stops. 0 - is direct flight Default: 1 Minimum: 0 Maximum: 3')] = None,
                   duration_max: Annotated[Union[int, float, None], Field(description='Duration max. Minutes Default: 2051 Minimum: 1 Maximum: 10000')] = None) -> dict: 
    '''Search flights. Type: only `ONE_WAY`. Set location_departure and location_arrival, use `/flights/locations` api point. You can filter out tickets by price, max duration and number of stops'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/flights/search'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_departure': location_departure,
        'itinerary_type': itinerary_type,
        'date_departure': date_departure,
        'class_type': class_type,
        'sort_order': sort_order,
        'location_arrival': location_arrival,
        'date_departure_return': date_departure_return,
        'price_max': price_max,
        'price_min': price_min,
        'number_of_passengers': number_of_passengers,
        'number_of_stops': number_of_stops,
        'duration_max': duration_max,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_hotels_locations_by_geolocation(longitude: Annotated[Union[int, float], Field(description='Longitude Default: 14.41854 Minimum: -180 Maximum: 180')],
                                           latitude: Annotated[Union[int, float], Field(description='Latitude Default: 50.073658 Minimum: -90 Maximum: 90')]) -> dict: 
    '''Search locations by coordinates. Set coordinates latitude and longitude'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/hotels/locations-by-geo'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'longitude': longitude,
        'latitude': latitude,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def booking_details_of_the_hotel(date_checkout: Annotated[str, Field(description='Checkout date')],
                                 hotel_id: Annotated[Union[int, float], Field(description='Hotel id Default: 6733503 Minimum: 1')],
                                 date_checkin: Annotated[str, Field(description='Checkin date')],
                                 rooms_number: Annotated[Union[int, float, None], Field(description='Rooms number Default: 1 Minimum: 1 Maximum: 8')] = None) -> dict: 
    '''Get hotel descriptions, prices and available booking options. Indicate the hotel_id, check-in and check-out date'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v1/hotels/booking-details'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date_checkout': date_checkout,
        'hotel_id': hotel_id,
        'date_checkin': date_checkin,
        'rooms_number': rooms_number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seat_map(ppn_bundle: Annotated[str, Field(description='The ppn_bundle for the seat map. Can be retrieved from the ppn_seat_bundle of FlightContract, or FlightLookUp.')],
             sid: Annotated[str, Field(description='Session ID. Random string ex.: j10k11l12m13n14')]) -> dict: 
    '''Gets the seat map of all flights in a contract bundle through the getFlightSeatMap endpoint'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/flight/seatMap'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ppn_bundle': ppn_bundle,
        'sid': sid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def contract(sid: Annotated[str, Field(description='Session ID. Random string ex.: j10k11l12m13n14')],
             ppn_bundle: Annotated[Union[str, None], Field(description='The ppn_bundle for the seat map. Can be retrieved from the ppn_seat_bundle of Flight Contract, or LookUp')] = None,
             convert_currency: Annotated[Union[str, None], Field(description='Requested currency for the results. ISO 4217 format.')] = None) -> dict: 
    '''Gets the contract for the PPN bundle provided by a flight return, departure, or combined (round trip/multi-city) through the getFlightContract endpoint'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/flight/contract'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sid': sid,
        'ppn_bundle': ppn_bundle,
        'convert_currency': convert_currency,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(sid: Annotated[str, Field(description='Session ID. Random string')],
           adults: Annotated[Union[int, float], Field(description='Number of adults Default: 1 Minimum: 1 Maximum: 8')],
           departure_date: Annotated[str, Field(description='Departure date')],
           page: Annotated[Union[int, float, None], Field(description='How many pages the results are spread over. Used in conjunction with results per page.')] = None,
           number_of_itineraries: Annotated[Union[int, float, None], Field(description='Number of itineraries to retrieve')] = None,
           airline_filter: Annotated[Union[str, None], Field(description='2 Letter code used to specify which airline that has been used.')] = None,
           convert_currency: Annotated[Union[str, None], Field(description='Requested currency for the results. ISO 4217 format.')] = None,
           cabin_class: Annotated[Union[str, None], Field(description='economy premium business first')] = None,
           origin_airport_code: Annotated[Union[str, None], Field(description='Airport code')] = None,
           destination_city_id: Annotated[Union[str, None], Field(description='City id')] = None,
           results_per_page: Annotated[Union[int, float, None], Field(description='Number of results per page. Used in conjunction with page.')] = None,
           currency: Annotated[Union[str, None], Field(description='Requested currency for the results. ISO 4217 format.')] = None,
           children: Annotated[Union[int, float, None], Field(description='Number of children Minimum: 0 Maximum: 8')] = None,
           destination_airport_code: Annotated[Union[str, None], Field(description='Airport code')] = None,
           origin_city_id: Annotated[Union[str, None], Field(description='City id')] = None) -> dict: 
    '''Returns a contract for a flight round trip search through the getFlightRoundTrip endpoint'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/flight/roundTrip'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sid': sid,
        'adults': adults,
        'departure_date': departure_date,
        'page': page,
        'number_of_itineraries': number_of_itineraries,
        'airline_filter': airline_filter,
        'convert_currency': convert_currency,
        'cabin_class': cabin_class,
        'origin_airport_code': origin_airport_code,
        'destination_city_id': destination_city_id,
        'results_per_page': results_per_page,
        'currency': currency,
        'children': children,
        'destination_airport_code': destination_airport_code,
        'origin_city_id': origin_city_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_airports(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                      limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 500')] = None) -> dict: 
    '''Downloads a list of airports with IATA codes for Flight search'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/flight/downloadAirports'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def auto_complete(string: Annotated[str, Field(description='Airport or City being searched')],
                  hotels: Annotated[Union[bool, None], Field(description='Include hotels in search results')] = None,
                  regions: Annotated[Union[bool, None], Field(description='Include regions in search results')] = None,
                  airports: Annotated[Union[bool, None], Field(description='Include airports in search results')] = None,
                  cities: Annotated[Union[bool, None], Field(description='Include cities in search results')] = None,
                  longitude: Annotated[Union[str, None], Field(description='Search for property availability around a specific longitude coordinate.')] = None,
                  latitude: Annotated[Union[str, None], Field(description='Search for property availability around a specific latitude coordinate.')] = None,
                  pois: Annotated[Union[bool, None], Field(description='Include pois in search results')] = None,
                  spellcheck: Annotated[Union[bool, None], Field(description='If the spell check is strict.')] = None) -> dict: 
    '''Gets airport and city ids for the air product related to words in passed string through the getAutoComplete endpoint'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/flight/autoComplete'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'string': string,
        'hotels': hotels,
        'regions': regions,
        'airports': airports,
        'cities': cities,
        'longitude': longitude,
        'latitude': latitude,
        'pois': pois,
        'spellcheck': spellcheck,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_companies(limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 500')] = None,
                       resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None) -> dict: 
    '''Downloads a list of companies'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/cars/downloadCompanies'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'resume_key': resume_key,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_cities(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 500')] = None) -> dict: 
    '''Downloads a list of cities'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/cars/downloadCities'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_locations(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                       limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 500')] = None) -> dict: 
    '''Downloads a list of Locations'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/cars/downloadLocations'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_property_types(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                            limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None) -> dict: 
    '''Downloads Property Types list'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadPropertyTypes'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def downalods_hotels(hotel_address: Annotated[Union[str, None], Field(description='Filter by address of hotel.')] = None,
                     active_vmer: Annotated[Union[str, None], Field(description='Show hotels with vacation merchant rates.')] = None,
                     active_bkg: Annotated[Union[str, None], Field(description='Show hotels with Booking rates.')] = None,
                     longitude_range_end: Annotated[Union[str, None], Field(description='Requires longitude to have value.')] = None,
                     latitude: Annotated[Union[str, None], Field(description='Filter by latitude of the hotel.')] = None,
                     latitude_range_end: Annotated[Union[str, None], Field(description='Requires latitude to have value.')] = None,
                     language: Annotated[Union[str, None], Field(description='Language code: en-US, es-ES, fr-FR, pt-BR')] = None,
                     state_code: Annotated[Union[str, None], Field(description='Filter by the state code of the hotel.')] = None,
                     country_code: Annotated[Union[str, None], Field(description='Filter by the country code of the hotel.')] = None,
                     active_agd: Annotated[Union[str, None], Field(description='Show hotels with Agoda rates.')] = None,
                     changes_since: Annotated[Union[str, None], Field(description='Date/time to filter the hotels that have been updated on or after this date. This will discover the last_changed_date of hotels in inventory (inclusive of the selected date). Date should be in a valid ISO 8601: https://en.wikipedia.org/wiki/ISO_8601 (YYYY-MM-DDThh:mm:ss{UTC_Offset}) format.')] = None,
                     hotelid_ppn: Annotated[Union[str, None], Field(description='Filter by PPN hotel ID.')] = None,
                     property_type_ids: Annotated[Union[str, None], Field(description='Filter by property type ids. See the Property Type Filter Guide for more detail.')] = None,
                     longitude: Annotated[Union[str, None], Field(description='Requires longitude to have value.')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None,
                     active_smop: Annotated[Union[str, None], Field(description='Show hotels with semi opaque rates.')] = None,
                     active_mer: Annotated[Union[str, None], Field(description='Show hotels with Priceline rates.')] = None,
                     resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                     cityid_ppn: Annotated[Union[str, None], Field(description='Filter by PPN city ID.')] = None) -> dict: 
    '''Downalods a list of Hotels'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadHotels'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_address': hotel_address,
        'active_vmer': active_vmer,
        'active_bkg': active_bkg,
        'longitude_range_end': longitude_range_end,
        'latitude': latitude,
        'latitude_range_end': latitude_range_end,
        'language': language,
        'state_code': state_code,
        'country_code': country_code,
        'active_agd': active_agd,
        'changes_since': changes_since,
        'hotelid_ppn': hotelid_ppn,
        'property_type_ids': property_type_ids,
        'longitude': longitude,
        'limit': limit,
        'active_smop': active_smop,
        'active_mer': active_mer,
        'resume_key': resume_key,
        'cityid_ppn': cityid_ppn,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_areas(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                   limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None) -> dict: 
    '''Downloads an Area list'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadAreas'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_countries(limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None,
                       resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None) -> dict: 
    '''Downloads a list of countries'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadCountries'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'resume_key': resume_key,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_chains(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None) -> dict: 
    '''Downloads a list of Hotel chains'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadChains'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_amenities(limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None,
                       language: Annotated[Union[str, None], Field(description='Language code: en-US, es-ES, fr-FR, pt-BR')] = None,
                       resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None) -> dict: 
    '''Downloads a list of Amenities'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadAmenities'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'language': language,
        'resume_key': resume_key,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_states(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None) -> dict: 
    '''Downloads a list of Satets'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadStates'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_cities_clusters(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                             limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None) -> dict: 
    '''Downloads a list of Hotel cities clusters'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadCitiesClusters'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hotel_reviews(hotel_id: Annotated[str, Field(description='The PPN Hotel ID identifying the desired property.')],
                  languages: Annotated[Union[str, None], Field(description='Limits the number of results from the response.')] = None,
                  offset: Annotated[Union[int, float, None], Field(description='Used with limit to only retrieve a subset of all results at a time. Determines the nuber of properties to skip (starting at 0) before returning results.')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None,
                  order_by: Annotated[Union[str, None], Field(description='CSV of sorting order metrics. Valid Options: creation_date, average_rating, or verified_guest followed by .asc or .desc.')] = None,
                  only_verified_guests: Annotated[Union[bool, None], Field(description='Set on to only include only reviews with verified_guests. A verified guest is a guest that has had a review verified by aaa. Valid Options: 0 = Off, 1 = On.')] = None) -> dict: 
    '''This API returns a list of reviews'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/reviews'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languages': languages,
        'offset': offset,
        'limit': limit,
        'order_by': order_by,
        'only_verified_guests': only_verified_guests,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_express_results(check_in: Annotated[str, Field(description='Check In Date (YYYY-MM-DD or MM/DD/YYYY)')],
                           check_out: Annotated[str, Field(description='Check In Date (YYYY-MM-DD or MM/DD/YYYY)')],
                           rate_limit: Annotated[Union[int, float, None], Field(description='Number passed to limit the number of rates returned. Defaults to returning all available rates')] = None,
                           limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None,
                           radius: Annotated[Union[int, float, None], Field(description='Radius in miles the results are from')] = None,
                           limit_to_country: Annotated[Union[bool, None], Field(description='Limits results to country provided. Valid Options: true or false.')] = None,
                           rate_identifier: Annotated[Union[bool, None], Field(description='A toggle to show if rate identifier is being passed. Valid Options: 0 = false, 1 = true. Rate is a string that is set for each hotel and holds all the information regarding the rate that we send to priceline.')] = None,
                           multiple_deals: Annotated[Union[bool, None], Field(description='Multi Rates are provided Valid Options: 0 = false, 1 = true.')] = None,
                           sid: Annotated[Union[str, None], Field(description='Session ID. Random string')] = None,
                           language: Annotated[Union[str, None], Field(description='Language code: en-US, es-ES, fr-FR, pt-BR')] = None,
                           adults: Annotated[Union[int, float, None], Field(description='The total number of adult occupants for all rooms requested. Used with children parameter to determine occupancy. Example: Two rooms, each with one adult and one child occupants, adults=2 and children=2')] = None,
                           hotel_ids: Annotated[Union[str, None], Field(description='Comma separated string of PPN hotel ids (Semi Opaque Only)')] = None,
                           rooms: Annotated[Union[int, float, None], Field(description='Number of rooms required for all occupants')] = None,
                           country_code: Annotated[Union[str, None], Field(description='Pass the user s country to see rates with regional pricing. This is a two character ISO Alpha-2 country code.')] = None,
                           sort_by: Annotated[Union[str, None], Field(description='Sort results by a given option. Default sort is by guest_score. Valid Options: gs = guest_score, sr = star_rating, lp = lowest_price, hp = highest_price, ds = distance, mp = most_popular.')] = None,
                           currency: Annotated[Union[str, None], Field(description='Requested currency for the results. ISO 4217 format.')] = None,
                           latitude: Annotated[Union[str, None], Field(description='Search for property availability around a specific latitude coordinate.')] = None,
                           output_version: Annotated[Union[int, float, None], Field(description='Enum: 1 2 3 4 Default: 3')] = None,
                           children: Annotated[Union[int, float, None], Field(description='The total number of child occupants for all rooms requested. Used with adults parameter to determine occupancy. Example: Two rooms, each with one adult and one child occupants, adults=2 and children=2')] = None,
                           city_id: Annotated[Union[str, None], Field(description='Accepts a single PPN City ID.)')] = None,
                           airport_code: Annotated[Union[str, None], Field(description='Accepts a 3-character IATA airport code.')] = None,
                           longitude: Annotated[Union[str, None], Field(description='Search for property availability around a specific longitude coordinate')] = None) -> dict: 
    '''Provides discounted Express (Cached) and Closed User Group (Live) Rates using the getExpress.Results endpoint.'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/expressResults'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'check_in': check_in,
        'check_out': check_out,
        'rate_limit': rate_limit,
        'limit': limit,
        'radius': radius,
        'limit_to_country': limit_to_country,
        'rate_identifier': rate_identifier,
        'multiple_deals': multiple_deals,
        'sid': sid,
        'language': language,
        'adults': adults,
        'hotel_ids': hotel_ids,
        'rooms': rooms,
        'country_code': country_code,
        'sort_by': sort_by,
        'currency': currency,
        'latitude': latitude,
        'output_version': output_version,
        'children': children,
        'city_id': city_id,
        'airport_code': airport_code,
        'longitude': longitude,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def auto_suggest(string: Annotated[str, Field(description='Search string that will enable a list of selection to be listed to the traveller.')],
                 order: Annotated[Union[str, None], Field(description='Method of ordering the results of the search. Valid options: asc or desc.')] = None,
                 get_cities: Annotated[Union[bool, None], Field(description='Include cities in search results. Valid Options: True or False.')] = None,
                 get_airports: Annotated[Union[bool, None], Field(description='Include airports in search results. Valid Options: True or False.')] = None,
                 combine_regions: Annotated[Union[bool, None], Field(description='Enables the spell check option for the search string using either true or false.')] = None,
                 spellcheck: Annotated[Union[bool, None], Field(description='Enables the spell check option for the search string using either true or false.')] = None,
                 sort: Annotated[Union[str, None], Field(description='Enum: rank, name. Method of sorting the results. Valid options: rank, name')] = None,
                 show_all_cities: Annotated[Union[bool, None], Field(description='Will filter out cities with no hotels. Valid Options: False = filter out cities without hotels, True = show cities with and without hotels.')] = None,
                 get_hotels: Annotated[Union[bool, None], Field(description='Include hotels in search results. Valid Options: True or False.')] = None,
                 max_results: Annotated[Union[int, float, None], Field(description='Number passed is the maximum number of results returned.')] = None,
                 get_pois: Annotated[Union[bool, None], Field(description='Include Points of Interest in search results. Valid Options: True or False')] = None,
                 get_regions: Annotated[Union[bool, None], Field(description='Include Regions in search results. Valid Options: True or False.')] = None) -> dict: 
    '''This API will provide a list of possible cities and hotels for a given search string'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/autoSuggest'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'string': string,
        'order': order,
        'get_cities': get_cities,
        'get_airports': get_airports,
        'combine_regions': combine_regions,
        'spellcheck': spellcheck,
        'sort': sort,
        'show_all_cities': show_all_cities,
        'get_hotels': get_hotels,
        'max_results': max_results,
        'get_pois': get_pois,
        'get_regions': get_regions,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hotel_photos(hotel_ids: Annotated[str, Field(description='Comma separated string of PPN hotel ids (Semi Opaque Only)')],
                 image_size: Annotated[Union[str, None], Field(description='The size of the image returned. Valid Options: small (60px), medium(300 to 312px) or large(500 to 800px)')] = None) -> dict: 
    '''This API returns a list of photos per hotel'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/photos'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_ids': hotel_ids,
        'image_size': image_size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def express_contract(language: Annotated[Union[str, None], Field(description='Language code: en-US, es-ES, fr-FR, pt-BR')] = None,
                     country_code: Annotated[Union[str, None], Field(description='Pass the user s country to see rates with regional pricing. This is a two character ISO Alpha-2 country code.')] = None,
                     rate_identifier: Annotated[Union[bool, None], Field(description='A toggle to show if rate identifier is being passed. Valid Options: 0 = false, 1 = true. Rate is a string that is set for each hotel and holds all the information regarding the rate that we send to priceline.')] = None,
                     output_version: Annotated[Union[int, float, None], Field(description='Enum: 1 2 3 4 Default: 3')] = None,
                     ppn_bundle: Annotated[Union[str, None], Field(description='ppn_bundle is a unique ID that ppn uses to identify a specific rate')] = None,
                     sid: Annotated[Union[str, None], Field(description='Session ID. Random string')] = None) -> dict: 
    '''Provides the hotel inventory and corresponding rates for Express (cache) or Closed User Group (live)'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/expressContract'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'language': language,
        'country_code': country_code,
        'rate_identifier': rate_identifier,
        'output_version': output_version,
        'ppn_bundle': ppn_bundle,
        'sid': sid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def download_filter_amenities(resume_key: Annotated[Union[str, None], Field(description='Resume results from given ID.')] = None,
                              limit: Annotated[Union[int, float, None], Field(description='Limits the number of results from the response. Default: 100')] = None) -> dict: 
    '''Downloads an Amenity list filtered'''
    url = 'https://priceline-com-provider.p.rapidapi.com/v2/hotels/downloadFilterAmenities'
    headers = {'x-rapidapi-host': 'priceline-com-provider.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resume_key': resume_key,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")

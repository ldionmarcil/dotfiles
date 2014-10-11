import os
import sys
import pygeoip
import unicodedata

if len(sys.argv) < 2:
    sys.exit(1)

IP_ADDR = sys.argv[1]
current_dir = os.path.dirname(os.path.abspath(__file__))

ASN_DB = 'GeoIPASNum.dat'
CITY_DB = 'GeoLiteCity.dat'

asn_db_path = os.path.join(current_dir, ASN_DB)
city_db_path = os.path.join(current_dir, CITY_DB)

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', str(input_str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

try:
    GEOIP_ASN = pygeoip.GeoIP(asn_db_path, pygeoip.MEMORY_CACHE)
    print("ORG: %s" % remove_accents(GEOIP_ASN.org_by_addr(IP_ADDR)))

    GEOIP_CITY = pygeoip.GeoIP(city_db_path, pygeoip.MEMORY_CACHE)
    for i,j in GEOIP_CITY.record_by_addr(IP_ADDR).items():
        print("%s: %s" % (remove_accents(i.upper()),remove_accents(j)))
except:
    sys.exit(-1)

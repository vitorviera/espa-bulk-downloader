

##############################################################################
# Used in cdr_ecv_cron.py

# Specifies the buffer length for an order line in the order file
# The Hadoop File System block size should be a multiple of this value
ORDER_BUFFER_LENGTH = 2048

# Set the hadoop timeouts to a ridiculous number so jobs don't get killed
# before they are done
HADOOP_TIMEOUT = 172800000  # which is 2 days

# Specifies the hadoop queue to use based on priority
# 'all' must be present as it is the default in the cron
HADOOP_QUEUE_MAPPING = {
    'all': 'ondemand',
    'low': 'ondemand',
    'medium': 'ondemand',
    'high': 'ondemand'
}


##############################################################################
# Used in cdr_ecv.py

# Path to the Landsat L1T source data location
LANDSAT_BASE_SOURCE_PATH = '/data/standard_l1t'

# filename extension for landsat input products
LANDSAT_INPUT_FILENAME_EXTENSION = '.tar.gz'

# host for landsat input checks
LANDSAT_INPUT_CHECK_HOST = 'edclpdsftp.cr.usgs.gov'

# port for landsat input checks
LANDSAT_INPUT_CHECK_PORT = 50000

LANDSAT_INPUT_CHECK_BASE_PATH = "/RPC2"


##############################################################################
# Used in modis.py

# Path to the MODIS Terra source data location
TERRA_BASE_SOURCE_PATH = '/MOLT'
# Path to the MODIS Aqua source data location
AQUA_BASE_SOURCE_PATH = '/MOLA'

# file extension for modis input products
MODIS_INPUT_FILENAME_EXTENSION = '.hdf'

# host for modis input checks
MODIS_INPUT_CHECK_HOST = 'e4ftl01.cr.usgs.gov'

# port for modis input checks
MODIS_INPUT_CHECK_PORT = 80

MODIS_INPUT_CHECK_BASE_PATH = "/"


##############################################################################
# Used in cdr_ecv.py and modis.py

# Path to place the completed orders
ESPA_BASE_OUTPUT_PATH = '/data2/LSRD'


##############################################################################
# Used in lpcs_cron.py

# Path to the completed orders
ESPA_CACHE_DIRECTORY = '/data2/LSRD'
# Can override this by setting the environment variable DEV_CACHE_DIRECTORY


ESPA_EMAIL_ADDRESS = 'espa@usgs.gov'

ESPA_EMAIL_SERVER = 'gssdsflh01.cr.usgs.gov'


##############################################################################
# Used by browse.py and science.py

# Default resolution for browse generation
DEFAULT_BROWSE_RESOLUTION = 50


##############################################################################
# Used by science.py

# Default name for the solr collection
DEFAULT_SOLR_COLLECTION_NAME = 'DEFAULT_COLLECTION'

# The limit value for when to start splitting clouds
# It is used as a string in the code since it is passed to the cfmask
# executable
CFMASK_MAX_CLOUD_PIXELS = '5000000'


##############################################################################
# Used by distribution.py

# Number of seconds to sleep when errors are encountered before attempting the
# task again
DEFAULT_SLEEP_SECONDS = 2

# Maximum number of times to attempt packaging, delivery, and distribution
MAX_PACKAGING_ATTEMPTS = 3
MAX_DELIVERY_ATTEMPTS = 3
MAX_DISTRIBUTION_ATTEMPTS = 5


##############################################################################
# Used by util.py and lpcs.py

# List of hostnames to choose from for the access to the online cache
# 140 is here twice so the load is 2/3 + 1/3.  machines are mismatched
ESPA_CACHE_HOST_LIST = ['edclxs67p', 'edclxs140p', 'edclxs140p']
MODIS_INPUT_HOSTNAME = 'e4ftl01.cr.usgs.gov'
# Developers can override these for LPCS by setting the environment variable
# DEV_CACHE_HOSTNAME

# Where to place the temporary scene processing log files
LOGFILE_PATH = '/tmp'


##############################################################################
# Used by statistics.py

# Band type data ranges.  They are intended to be used for removing outliers
# from the data before statistics generation
# Must match DATA_MAX_Y and DATA_MIN_Y values in plot.py
# The types must match the types in cdr_ecv.py and modis.py
BAND_TYPE_STAT_RANGES = {
    'SR': {
        'UPPER_BOUND': 10000,
        'LOWER_BOUND': 0
    },
    'TOA': {
        'UPPER_BOUND': 10000,
        'LOWER_BOUND': 0
    },
    'INDEX': {
        'UPPER_BOUND': 10000,
        'LOWER_BOUND': -1000
    },
    'LST': {
        'UPPER_BOUND': 65535,
        'LOWER_BOUND': 7500
    },
    'EMIS': {
        'UPPER_BOUND': 255,
        'LOWER_BOUND': 1
    }
}

'''Resolves system-wide identification of sensor name based on three letter
 prefix
'''
SENSOR_NAMES = {
    'LE7': 'etm',
    'LT4': 'tm',
    'LT5': 'tm',
    'MYD': 'aqua',
    'MOD': 'terra'
}

'''Default pixel sizes based on the input products'''
DEFAULT_PIXEL_SIZE = {
    'meters': {
        '09A1': 500,
        '09GA': 500,
        '09GQ': 250,
        '09Q1': 250,
        '13Q1': 250,
        '13A3': 1000,
        '13A2': 1000,
        '13A1': 500,
        'LE7': 30,
        'LT4': 30,
        'LT5': 30
    },
    'dd': {
        '09A1': 0.00449155,
        '09GA': 0.00449155,
        '09GQ': 0.002245775,
        '09Q1': 0.002245775,
        '13Q1': 0.002245775,
        '13A3': 0.0089831,
        '13A2': 0.0089831,
        '13A1': 0.00449155,
        'LE7': 0.0002695,
        'LT4': 0.0002695,
        'LT5': 0.0002695
        }
}


''' Constant dictionary to hold the cache keys used in Django
 caching/memcached'''
CACHE_KEYS = {


}


'''
LOGGING DEFINITIONS
'''

LOGGING_CONFIG = {}

LOGGER_ALIAS = {
    'PROCESSING': 'processing',
    'WEB': 'web',
    'CRON': 'cron'
}
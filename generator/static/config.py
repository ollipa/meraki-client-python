"""Package Constants."""

# Base URL preceding all endpoint resources
DEFAULT_BASE_URL = "https://api.meraki.com/api/v1"

# Alternate base URLs
CANADA_BASE_URL = "https://api.meraki.ca/api/v1"
CHINA_BASE_URL = "https://api.meraki.cn/api/v1"
INDIA_BASE_URL = "https://api.meraki.in/api/v1"
UNITED_STATES_FED_BASE_URL = "https://api.gov-meraki.com/api/v1"

# Maximum number of seconds for each API call
SINGLE_REQUEST_TIMEOUT = 60

# Path for TLS/SSL certificate verification if behind local proxy
CERTIFICATE_PATH = ""

# Proxy server and port, if needed, for HTTPS
REQUESTS_PROXY = ""

# Retry if 429 rate limit error encountered?
# Please note, setting to False means your application will not retry upon a 429. Not intended for production apps.
WAIT_ON_RATE_LIMIT = True

# Retry up to this many times when encountering 429s or other server-side errors
MAXIMUM_RETRIES = 2

# Use iterator for pages. May offer improved performance in some instances. Off by default for backwards compatibility.
USE_ITERATOR_FOR_GET_PAGES = False

# Number of concurrent API requests for asynchronous class
AIO_MAXIMUM_CONCURRENT_REQUESTS = 8

# Legacy partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID
# This is no longer used. Please use MERAKI_PYTHON_SDK_CALLER instead.
BE_GEO_ID = ""

# Optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER
# It's good practice to use this to identify your application using the format:
# CamelCasedApplicationName/OptionalVersionNumber CamelCasedVendorName
# Please note:
# 1. Application name precedes vendor name in all cases.
# 2. If your application or vendor name normally contains spaces or special casing, you should omit them in favor of
#    normal CamelCasing here.
# 3. The slash and version number are optional. Leave both out if you like.
# 4. The slash is a forward slash, '/' -- not a backslash.
# 5. Don't use the 'Meraki' or 'Cisco' names in your application name here. Maybe in general? I'm a config file, not a
#    lawyer.
# Example 1: if your application is named 'Mambo', version number is 5.0, and your vendor/company name is Vega, then
# you would use, at minimum: 'Mambo Vega'. Optionally: 'Mambo/5.0 Vega'.
# Example 2: if your application is named 'Sunshine Rainbows', and company name is 'hunter2 for Life', and if you
# don't want to report version number, then you would use, at minimum: 'SunshineRainbows hunter2ForLife'
# The choice is yours as long as you follow the format. You should **not** include other information in this string.
# If you are an official ecosystem partner, this is required.
# For more guidance, please refer to https://developer.cisco.com/meraki/api-v1/user-agents-overview/
MERAKI_PYTHON_SDK_CALLER = ""

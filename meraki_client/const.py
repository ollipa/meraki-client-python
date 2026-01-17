"""Meraki dashboard API SDK constants."""

# Maximum number of seconds for each API call
SINGLE_REQUEST_TIMEOUT = 30

# Total time to wait for all requests to complete (including retries)
TOTAL_REQUEST_TIMEOUT = 60

# Retry if 429 rate limit error encountered
WAIT_ON_RATE_LIMIT = True

# Retry up to this many times when encountering 429s or 5xx errors
MAXIMUM_RETRIES = 2

# Number of concurrent API requests for asynchronous operations
ASYNC_MAXIMUM_CONCURRENT_REQUESTS = 8

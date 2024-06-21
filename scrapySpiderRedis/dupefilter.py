from scrapy_redis.dupefilter import RFPDupeFilter
from scrapy.utils.request import fingerprint

class CustomRFPDupeFilter(RFPDupeFilter):
    def __init__(self, server, key, debug=False):
        super().__init__(server, key, debug)
    def request_fingerprint(self, request):
        """Returns a fingerprint for a given request.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        str

        """
        return fingerprint(request)
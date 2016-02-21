import idna
import tldextract


class Domain(object):
    """
    Standardized Domain object, with full support for IDNs
    and punycodes.
    """

    def __init__(self, domain_name):
        """
        This function creates and parses the domain name
        provided by the application.

        First we should detect if the domain given is an
        IDN, and if so, parse the domain correctly and give
        it a punycode and it's correct UTF-8 representation.

        :param domain_name: The domain name to parse (can by puny or IDN)
        """

        is_idn = False
        domain = None
        idn = None

        # Let's make sure that it's in a str representation
        if type(domain_name) == bytes:
            domain_name = domain_name.decode('utf-8')

        # If it begins with 'xn--' then it's an IDN
        if domain_name.startswith('xn--'):
            is_idn = True
            domain = domain_name
            idn = idna.decode(domain_name)

        # If it can't be converted to ASCII, it's an IDN
        try:
            domain_name.encode('ascii')
        except UnicodeEncodeError:
            is_idn = True
            domain = idna.encode(domain_name).decode('utf-8')
            idn = domain_name

        if domain is None:
            domain = domain_name

        self.__domain_obj = tldextract.extract(domain)
        self.__is_idn = is_idn
        self.__idn_obj = tldextract.extract(idn) if is_idn else None

    @property
    def domain(self):
        """
        This function will return the domain name.

        If the domain is an IDN, then it will return
        the punycode version of the domain.

        If you want to retrieve the international version,
        use the `idn` attribute to get the UTF-8 version.


        :return: The domain in punycode format
        """
        return '.'.join([self.__domain_obj.domain, self.__domain_obj.suffix])

    @property
    def idn(self):
        """
        This function returns the domain name in a UTF-8
        representation in the domain's natural language
        if it is an IDN, otherwise it will return the
        domain in its normal alphanumeric format.

        :return: The domain in its natural language
        """

        if not self.__is_idn:
            return self.domain

        return '.'.join([self.__idn_obj.domain, self.__idn_obj.suffix])

    @property
    def is_idn(self):
        """
        This function checks if the domain is an IDN.

        :return: Domain is an IDN
        """
        return self.__is_idn

    def __str__(self):
        """
        This function should always return the punycode
        representation of the domain, if it's not an IDN,
        just return the domain name normally.

        :return: The string representation of this domain
        """
        return self.domain

    def __repr__(self):
        """
        The representative string of this object is the exact
        same as the __str__() returns, so let's just alias this
        function to it.

        :return: The string representation of this domain
        """
        return self.__str__()
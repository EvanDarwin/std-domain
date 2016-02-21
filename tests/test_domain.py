# coding=utf-8

from . import TestCase

from stddomain import Domain


class TestDomain(TestCase):
    def test_domain_ascii(self):
        domain = Domain('example.com')

        assert domain.domain == 'example.com'
        assert domain.idn == 'example.com'
        assert domain.is_idn == False

    def test_domain_idn(self):
        domain = Domain(u'名がドメイン.com')

        assert domain.domain == 'xn--v8jxj3d1dzdz08w.com'
        assert domain.idn == u'名がドメイン.com'
        assert domain.is_idn == True
        assert domain.__str__() == 'xn--v8jxj3d1dzdz08w.com'
        assert repr(domain) == 'xn--v8jxj3d1dzdz08w.com'

    def test_domain_punycode(self):
        domain = Domain(u'xn--v8jxj3d1dzdz08w.com')

        assert domain.domain == 'xn--v8jxj3d1dzdz08w.com'
        assert domain.idn == u'名がドメイン.com'
        assert domain.is_idn == True
        assert domain.__str__() == 'xn--v8jxj3d1dzdz08w.com'
        assert repr(domain) == 'xn--v8jxj3d1dzdz08w.com'

    def test_domain_bytes(self):
        domain = Domain(bytes('example.com', 'utf8'))

        assert domain.domain == 'example.com'
        assert domain.idn == 'example.com'
        assert domain.is_idn == False
        assert domain.__str__() == 'example.com'
        assert repr(domain) == 'example.com'

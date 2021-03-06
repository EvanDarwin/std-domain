# coding=utf-8

from . import TestCase

from stddomain import InternationalDomain

import sys


class TestDomain(TestCase):
    def test_domain_ascii(self):
        domain = InternationalDomain('example.com')

        self.assertEqual(domain.domain, 'example.com')
        self.assertEqual(domain.idn, 'example.com')

        self.assertEqual(domain.get_tld(), 'com')
        self.assertEqual(domain.get_tld(True), 'com')
        self.assertEqual(domain.get_domain(), 'example')
        self.assertEqual(domain.get_domain(True), 'example')

        self.assertFalse(domain.is_idn)

    def test_domain_idn(self):
        domain = InternationalDomain(u'名がドメイン.中国')

        self.assertEqual(domain.domain, 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')
        self.assertEqual(domain.domain, 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')

        self.assertEqual(domain.idn, u'名がドメイン.中国')
        self.assertTrue(domain.is_idn)

        self.assertEqual(domain.get_tld(), 'xn--fiqs8s')
        self.assertEqual(domain.get_tld(True), u'中国')
        self.assertEqual(domain.get_domain(), u'xn--v8jxj3d1dzdz08w')
        self.assertEqual(domain.get_domain(True), u'名がドメイン')

        self.assertEqual(domain.__str__(), 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')
        self.assertEqual(repr(domain), 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')

    def test_domain_idn_mixed_content(self):
        domain = InternationalDomain(u'名がドメイン.xn--fiqs8s')

        self.assertEqual(domain.domain, 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')
        self.assertEqual(domain.domain, 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')
    
        self.assertEqual(domain.idn, u'名がドメイン.中国')
        self.assertTrue(domain.is_idn)

        self.assertEqual(domain.get_tld(), 'xn--fiqs8s')
        self.assertEqual(domain.get_tld(True), u'中国')
        self.assertEqual(domain.get_domain(), 'xn--v8jxj3d1dzdz08w')
        self.assertEqual(domain.get_domain(True), u'名がドメイン')

        self.assertEqual(domain.__str__(), 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')
        self.assertEqual(repr(domain), 'xn--v8jxj3d1dzdz08w.xn--fiqs8s')

    def test_domain_punycode(self):
        domain = InternationalDomain(u'xn--v8jxj3d1dzdz08w.com')

        self.assertEqual(domain.domain, 'xn--v8jxj3d1dzdz08w.com')
        self.assertEqual(domain.idn, u'名がドメイン.com')
        self.assertTrue(domain.is_idn)

        self.assertEqual(domain.get_tld(), 'com')
        self.assertEqual(domain.get_tld(True), u'com')
        self.assertEqual(domain.get_domain(), 'xn--v8jxj3d1dzdz08w')
        self.assertEqual(domain.get_domain(True), u'名がドメイン')

        self.assertEqual(domain.__str__(), 'xn--v8jxj3d1dzdz08w.com')
        self.assertEqual(repr(domain), 'xn--v8jxj3d1dzdz08w.com')

    def test_domain_bytes(self):
        domain_name = 'example.com'
        
        if sys.version_info >= (3, 0):
            domain = InternationalDomain(bytes(domain_name, 'utf8'))
        else:
            domain = InternationalDomain(bytes(domain_name))
            
        self.assertEqual(domain.domain, domain_name)
        self.assertEqual(domain.idn, domain_name)
        self.assertFalse(domain.is_idn)

        self.assertEqual(domain.__str__(), domain_name)
        self.assertEqual(repr(domain), domain_name)

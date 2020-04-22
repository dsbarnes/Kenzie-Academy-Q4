from django.test import TestCase
from .helpers import *

class HelperTestCase(TestCase):
    def testFetchTicker(self):
        """
        Test that the data returned is a dict
        and that the correct ticker is returned
        from the network request.
        """
        aapl = fetchTicker('AAPL')
        amzn = fetchTicker('AMZN')
        msft = fetchTicker('MSFT')
        tsla = fetchTicker('TSLA')

        self.assertTrue(isinstance(aapl, dict))
        self.assertTrue(isinstance(amzn, dict))
        self.assertTrue(isinstance(msft, dict))
        self.assertTrue(isinstance(tsla, dict))

        self.assertEqual(aapl['symbol'], 'AAPL')
        self.assertEqual(amzn['symbol'], 'AMZN')
        self.assertEqual(msft['symbol'], 'MSFT')
        self.assertEqual(tsla['symbol'], 'TSLA')

    def testFetchCompany(self):
        """
        Test that the fetch retuns a dict
        that the correct symbol is returned
        and that companyName, industry, website, and description
        are not ''
        """
        aapl = fetchCompanyData('AAPL')
        amzn = fetchCompanyData('AMZN')
        msft = fetchCompanyData('MSFT')
        tsla = fetchCompanyData('TSLA')

        self.assertTrue(isinstance(aapl, dict))
        self.assertTrue(isinstance(amzn, dict))
        self.assertTrue(isinstance(msft, dict))
        self.assertTrue(isinstance(tsla, dict))

        self.assertEqual(aapl['symbol'], 'AAPL')
        self.assertEqual(amzn['symbol'], 'AMZN')
        self.assertEqual(msft['symbol'], 'MSFT')
        self.assertEqual(tsla['symbol'], 'TSLA')

        self.assertNotEqual(aapl['companyName'], '')
        self.assertNotEqual(aapl['industry'], '' )
        self.assertNotEqual(aapl['website'], '') 
        self.assertNotEqual(aapl['description'], '')

        self.assertNotEqual(amzn['companyName'], '')
        self.assertNotEqual(amzn['industry'], '' )
        self.assertNotEqual(amzn['website'], '') 
        self.assertNotEqual(amzn['description'], '')

        self.assertNotEqual(msft['companyName'], '')
        self.assertNotEqual(msft['industry'], '' )
        self.assertNotEqual(msft['website'], '') 
        self.assertNotEqual(msft['description'], '')
        
        self.assertNotEqual(tsla['companyName'], '')
        self.assertNotEqual(tsla['industry'], '' )
        self.assertNotEqual(tsla['website'], '') 
        self.assertNotEqual(tsla['description'], '')

    def testMultiFetcher(self):
        """ Test the Multifetcher """
        stock_list = multiFetcher(['AMZN', 'AAPL', 'TSLA', 'MSFT'])

        self.assertTrue(len(stock_list) == len(['amzn', 'aapl', 'tsla', 'msft']))
        self.assertTrue(isinstance(stock_list[0], dict))
        self.assertTrue(isinstance(stock_list[1], dict))
        self.assertTrue(isinstance(stock_list[2], dict))
        self.assertTrue(isinstance(stock_list[3], dict))

        self.assertEqual(stock_list[0]['symbol'], 'AMZN')
        self.assertEqual(stock_list[1]['symbol'], 'AAPL')
        self.assertEqual(stock_list[2]['symbol'], 'TSLA')
        self.assertEqual(stock_list[3]['symbol'], 'MSFT')

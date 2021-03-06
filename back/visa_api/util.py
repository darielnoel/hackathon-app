from . import vdp_utils
import json

__author__ = '2b||!2b'

BASE_URL = 'https://sandbox.api.visa.com'


def reverse_funds(S):
    uri = '/visadirect/fundstransfer/v1/reversefundstransactions/'
    body = json.loads('''{
	  "acquirerCountryCode": "608",
	  "acquiringBin": "408999",
	  "amount": "24.01",
	  "cardAcceptor": {
	    "address": {
	      "country": "USA",
	      "county": "San Mateo",
	      "state": "CA",
	      "zipCode": "94404"
	    },
	    "idCode": "VMT200911026070",
	    "name": "Visa Inc. USA-Foster City",
	    "terminalId": "365539"
	  },
	  "localTransactionDateTime": "2016-04-16T22:24:51",
	  "originalDataElements": {
	    "acquiringBin": "408999",
	    "approvalCode": "20304B",
	    "systemsTraceAuditNumber": "897825",
	    "transmissionDateTime": "2016-04-16T22:24:51"
	  },
	  "pointOfServiceCapability": {
	    "posTerminalEntryCapability": "2",
	    "posTerminalType": "4"
	  },
	  "pointOfServiceData": {
	    "motoECIIndicator": "0",
	    "panEntryMode": "90",
	    "posConditionCode": "00"
	  },
	  "retrievalReferenceNumber": "330000550000",
	  "senderCardExpiryDate": "2015-10",
	  "senderCurrencyCode": "USD",
	  "senderPrimaryAccountNumber": "4895100000055127",
	  "systemsTraceAuditNumber": "451050",
	  "transactionIdentifier": "381228649430011"
	}''')
    r = S.post(BASE_URL + uri, json=body)
    return r

def pull_funds(S):
    uri = '/visadirect/fundstransfer/v1/pullfundstransactions/'
    body = json.loads('''{
      "acquirerCountryCode": "840",
      "acquiringBin": "408999",
      "amount": "1124.02",
      "businessApplicationId": "AA",
      "cardAcceptor": {
        "address": {
          "country": "USA",
          "county": "San Mateo",
          "state": "CA",
          "zipCode": "94404"
        },
        "idCode": "ABCD1234ABCD123",
        "name": "Visa Inc. USA-Foster City",
        "terminalId": "ABCD1234"
      },
      "cavv": "0700100038238906000013405823891061668252",
      "foreignExchangeFeeTransaction": "11.99",
      "localTransactionDateTime": "2016-04-16T14:44:04",
      "retrievalReferenceNumber": "330000550000",
      "senderCardExpiryDate": "2015-10",
      "senderCurrencyCode": "USD",
      "senderPrimaryAccountNumber": "4895142232120006",
      "surcharge": "0",
      "systemsTraceAuditNumber": "451001"
    }''')
    r = S.post(BASE_URL + uri, json=body)
    return r

def push_funds(S):
    uri = '/visadirect/fundstransfer/v1/pushfundstransactions/'
    body = json.loads('''{
      "acquirerCountryCode": "840",
      "acquiringBin": "408999",
      "amount": "124.05",
      "businessApplicationId": "AA",
      "cardAcceptor": {
        "address": {
          "country": "USA",
          "county": "San Mateo",
          "state": "CA",
          "zipCode": "94404"
        },
        "idCode": "CA-IDCode-77765",
        "name": "Visa Inc. USA-Foster City",
        "terminalId": "TID-9999"
      },
      "localTransactionDateTime": "2016-04-16T21:40:04",
      "merchantCategoryCode": "6012",
      "pointOfServiceData": {
        "motoECIIndicator": "0",
        "panEntryMode": "90",
        "posConditionCode": "00"
      },
      "recipientName": "rohan",
      "recipientPrimaryAccountNumber": "4957030420210496",
      "retrievalReferenceNumber": "412770451018",
      "senderAccountNumber": "4653459515756154",
      "senderAddress": "901 Metro Center Blvd",
      "senderCity": "Foster City",
      "senderCountryCode": "124",
      "senderName": "Mohammed Qasim",
      "senderReference": "",
      "senderStateCode": "CA",
      "sourceOfFundsCode": "05",
      "systemsTraceAuditNumber": "451018",
      "transactionCurrencyCode": "USD",
      "transactionIdentifier": "381228649430015"
    }''')
    r = S.post(BASE_URL + uri, json=body)
    return r

def reverse():
    user_id = '5RR5JQ34LMHPV8ZRQYOG21U5avMv8m06-Sv04yCoWlP_xI6ag'
    password = 'k7zV8AgB4F3q33BDJ'
    cert = './visa_api/cert_newest.pem'
    key = './visa_api/key_newest.pem'

    with vdp_utils.MSession(user_id, password, cert, key) as S:
        S.headers.update({'content-type': 'application/json',
                          'accept': 'application/json'})
        r = reverse_funds(S)

    print(r.status_code)
    print(r.content)
    return r

def push():
    user_id = '5RR5JQ34LMHPV8ZRQYOG21U5avMv8m06-Sv04yCoWlP_xI6ag'
    password = 'k7zV8AgB4F3q33BDJ'
    cert = './visa_api/cert_newest.pem'
    key = './visa_api/key_newest.pem'

    with vdp_utils.MSession(user_id, password, cert, key) as S:
        S.headers.update({'content-type': 'application/json',
                          'accept': 'application/json'})
        r = push_funds(S)

    print(r.status_code)
    print(r.content)
    return r


def pull():
    user_id = '5RR5JQ34LMHPV8ZRQYOG21U5avMv8m06-Sv04yCoWlP_xI6ag'
    password = 'k7zV8AgB4F3q33BDJ'
    cert = './visa_api/cert_newest.pem'
    key = './visa_api/key_newest.pem'

    with vdp_utils.MSession(user_id, password, cert, key) as S:
        S.headers.update({'content-type': 'application/json',
                          'accept': 'application/json'})
        r = pull_funds(S)

    print(r.status_code)
    print(r.content)
    return r

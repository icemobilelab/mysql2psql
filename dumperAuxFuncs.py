__author__ = 'ggarrido'

import datetime
import re

validTimeRE = re.compile(ur'\d\d:\d\d')

def convertStr(value, col_attrs=None):
    if not value:
        return None
    if (isinstance(value, (float, int))):
        return str(int(value)) 
    return str(value) 

def convertStrBoolean(value, col_attrs=None):
    if not value or not (isinstance(value, (str, int))):
        return False
    # avoid the error parsing "invalid literal for int() with base 10: '\x01' "
    if str(value) == "\x01":
        return True
    return False if value == 0 or int(value) == 0 else True

def convertInt(value, col_attrs=None):
    if not (isinstance(value, (str, int, float))) or len(str(value)) == 0:
        return None
    return int(value)

def defaultDate(value, format, defaultValue, nullable):
    if value is None or value[:4] == '0000':
        return None if nullable else '1900-01-01'
    return value

def notNullableDate(value, col_attrs=None):
    nullable = col_attrs['nullable'] if col_attrs else False
    format, defaultValue = "%d%m%Y", "01011900"
    return defaultDate(value, format, defaultValue, nullable)


def notNullableDatetime(value, col_attrs=None):
    nullable = col_attrs['nullable'] if col_attrs else False
    format, defaultValue = "%d%m%Y %H:%M:%S", "01011900 00:00:00"
    return defaultDate(value, format, defaultValue, nullable)

def refToNullable(value, col_attrs=None):
    nullable = col_attrs['nullable'] if col_attrs else False
    if (value == 0 or value == '0' or str(value).strip() == '') and nullable: return None
    return value

def makeItEmpty(value, col_attrs=None):
    nullable = col_attrs['nullable'] if col_attrs else False
    return None if nullable else ''

def makeItTime(value, col_attrs=None):
    nullable = col_attrs['nullable'] if col_attrs else False
    if value is not None and re.match(validTimeRE, value): return value
    return None if nullable else '00:00'

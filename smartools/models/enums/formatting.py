from enum import Enum

class FontFamily(Enum):

    ARIAL = 0
    TAHOMA = 1
    TIMES_NEW_ROMAN = 2
    VERDANA = 3

class FontSize(Enum):

    EIGHT = 0
    f8 = 0
    NINE = 1
    f9 = 1
    TEN = 2
    f10 = 2
    TWELVE = 3
    f12 = 3
    FOURTEEN = 4
    f14 = 4
    SIXTEEN = 5
    f16 = 5
    EIGHTEEN = 6
    f18 = 6
    TWENTY = 7
    f20 = 7
    TWENTYFOUR = 8
    f24 = 8
    TWENTYEIGHT = 9
    f28 = 9
    THIRTYTWO = 10
    f32 = 10
    THIRTYSIX = 11
    f36 = 11

class FormatSetting(Enum):

    NONE = 0
    OFF = 0
    ON = 1

class HorizontalAlign(Enum):
    
    DEFAULT = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3

class VerticalAlign(Enum):

    DEFAULT = 0
    TOP = 1
    MIDDLE = 2
    BOTTOM = 3

class Color(Enum):

    NONE = 0
    x000000 = 1
    xFFFFFF = 2
    TRANSPARENT = 3
    xFFEBEE = 4
    xFFF3DF = 5
    xFFFEE6 = 6
    xE7F5E9 = 7
    xE2F2FE = 8
    xF4E4F5 = 9
    xF2E8DE = 10
    xFFCCD2 = 11
    xFFE1AF = 12
    xFEFF85 = 13
    xC6E7C8 = 14
    xB9DDFC = 15
    xEBC7EF = 16
    xEEDCCA = 17
    xE5E5E5 = 18
    xF87E7D = 19
    xFFCD7A = 20
    xFEFF00 = 21
    x7ED085 = 22
    x5FB3F9 = 23
    xD190DA = 24
    xD0AF8F = 25
    xBDBDBD = 26
    xEA352E = 27
    xFF8D00 = 28
    xFFED00 = 29
    x40B14B = 30
    x1061C3 = 31
    x9210AD = 32
    x974C00 = 33
    x757575 = 34
    x991310 = 35
    xEA5000 = 36
    xEBC700 = 37
    x237F2E = 38
    x0B347D = 39
    x61058B = 40
    x592C00 = 41

class Currency(Enum):
    NONE = 0
    ARS = 1
    AUD = 2
    BRL = 3
    CAD = 4
    CLP = 5
    EUR = 6
    ILS = 7
    INR = 8
    JPY = 9
    MXN = 10
    RUB = 11
    USD = 12
    ZAR = 13
    CHF = 14
    CNY = 15
    DKK = 16
    HKD = 17
    KRW = 18
    NOK = 19
    NZD = 20
    SEK = 21
    SGD = 22

class DecimalCount(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

class NumberFormat(Enum):
    NONE = 0
    NUMBER = 1
    CURRENCY = 2
    PERCENT = 3

class DateFormat(Enum):
    LOCALE_BASED = 0
    MMMM_D_YYYY = 1
    MMM_D_YYYY = 2
    D_MMM_YYYY = 3
    YYYY_MM_DD_HYPHEN = 4
    YYYY_MM_DD_DOT = 5
    DWWWW_MMMM_D_YYYY = 6
    DWWW_DD_MMM_YYYY = 7
    DWWW_MM_DD_YYYY = 8
    MMMM_D = 9
    D_MMMM = 10

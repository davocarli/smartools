import six
from smartsheet.util import deserialize
from smartsheet.types import String

from ..types.enumerated_value import SmartoolsEnumeratedValue
from .enums.format import *

class CellFormat(object):

    FORMAT_ORDER = [
        'font_family',
        'font_size',
        'bold',
        'italic',
        'underline',
        'strikethrough',
        'horizontal_align',
        'vertical_align',
        'text_color',
        'background_color',
        'taskbar_color',
        'currency',
        'decimal_count',
        'thousands_separator',
        'number_format',
        'text_wrap',
        'date_format',
    ]
    FONT_SIZES = {
        8: 'EIGHT',
        9: 'NINE',
        10: 'TEN',
        12: 'TWELVE',
        14: 'FOURTEEN',
        16: 'SIXTEEN',
        18: 'EIGHTEEN',
        20: 'TWENTY',
        24: 'TWENTYFOUR',
        28: 'TWENTYEIGHT',
        32: 'THIRTYTWO',
        36: 'THIRTYSIX',
    }

    def __init__(self, initial_value=None, level=0):
        self._font_family = SmartoolsEnumeratedValue(FontFamily)
        self._font_size = SmartoolsEnumeratedValue(FontSize)

        self._bold = SmartoolsEnumeratedValue(FormatSetting)
        self._italic = SmartoolsEnumeratedValue(FormatSetting)
        self._underline = SmartoolsEnumeratedValue(FormatSetting)
        self._strikethrough = SmartoolsEnumeratedValue(FormatSetting)

        self._horizontal_align = SmartoolsEnumeratedValue(HorizontalAlign)
        self._vertical_align = SmartoolsEnumeratedValue(VerticalAlign)
        self._text_color = SmartoolsEnumeratedValue(Color)
        self._background_color = SmartoolsEnumeratedValue(Color)
        self._taskbar_color = SmartoolsEnumeratedValue(Color)
        self._currency = SmartoolsEnumeratedValue(Currency)
        self._decimal_count = SmartoolsEnumeratedValue(DecimalCount)
        self._thousands_separator = SmartoolsEnumeratedValue(FormatSetting)
        self._number_format = SmartoolsEnumeratedValue(NumberFormat)
        self._text_wrap = SmartoolsEnumeratedValue(FormatSetting)
        self._date_format = SmartoolsEnumeratedValue(DateFormat)

        self._level = level

        self._value = ['' for _ in range(17)]
        if isinstance(initial_value, String):
            initial_value = initial_value.value
        elif isinstance(initial_value, CellFormat):
            initial_value = initial_value.to_list()
        if initial_value:
            self.value = initial_value

    def serialize(self):
        return self.value

    def summarize(self):
        result = ''
        for option in self.FORMAT_ORDER:
            result += f'{option}: {getattr(self, option)}\n'
        result += str(self.value)
        return result

    # Used to "fully apply" currency formatting as would occur when currency in-app
    def apply_currency(self, currency=None):
        self.decimal_count = "TWO"
        self.number_format = "CURRENCY"
        self.thousands_separator = "ON"
        if currency is not None:
            self.currency = currency

    # Used to "fully apply" percentage formatting as would occur when applying in-app
    def apply_percent(self, decimal_count=None):
        self.thousands_separator = "ON"
        self.number_format = "PERCENT"
        if decimal_count is not None:
            self.decimal_count = decimal_count

    def to_list(self):
        return self._value

    @property
    def value(self):
        if all(x == '' for x in self._value):
            return None
        return ','.join(self._value)

    @value.setter
    def value(self, value):
        if isinstance(value, dict):
            deserialize(self, value)
        else:
            if isinstance(value, (six.string_types, str)):
                value = value.split(',')
            for i in range(len(value)):
                val = None
                try:
                    val = int(value[i])
                except ValueError:
                    pass
                self.__setattr__(self.FORMAT_ORDER[i], val)

    def __str__(self):
        return str(self.value)

    @property
    def font_family(self):
        return self._font_family
    
    @font_family.setter
    def font_family(self, value):
        self._font_family.set(value)
        if self._font_family.value is None:
            self._value[0] = ''
        else:
            self._value[0] = str(self._font_family.value.value)

    @property
    def font_size(self):
        return self._font_size
    
    @font_size.setter
    def font_size(self, value):
        if isinstance(value, int) and self._level > 0:
            value = self.FONT_SIZES[value]
        self._font_size.set(value)
        if self.font_size.value is None:
            self._value[1] = ''
        else:
            self._value[1] = str(self._font_size.value.value)

    @property
    def bold(self):
        return self._bold

    @bold.setter
    def bold(self, value):
        self._bold.set(value)
        if self._bold.value is None:
            self._value[2] = ''
        else:
            self._value[2] = str(self._bold.value.value)
        return self

    @property
    def italic(self):
        return self._italic

    @italic.setter
    def italic(self, value):
        self._italic.set(value)
        if self._italic.value is None:
            self._value[3] = ''
        else:
            self._value[3] = str(self._italic.value.value)
        return self

    @property
    def underline(self):
        return self._underline

    @underline.setter
    def underline(self, value):
        self._underline.set(value)
        if self._underline.value is None:
            self._value[4] = ''
        else:
            self._value[4] = str(self._underline.value.value)
        return self

    @property
    def strikethrough(self):
        return self._strikethrough

    @strikethrough.setter
    def strikethrough(self, value):
        self._strikethrough.set(value)
        if self._strikethrough.value is None:
            self._value[5] = ''
        else:
            self._value[5] = str(self._strikethrough.value.value)
        return self

    @property
    def horizontal_align(self):
        return self._horizontal_align
    
    @horizontal_align.setter
    def horizontal_align(self, value):
        self._horizontal_align.set(value)
        if self._horizontal_align.value is None:
            self._value[6] = ''
        else:
            self._value[6] = str(self._horizontal_align.value.value)
        return self

    @property
    def vertical_align(self):
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        self._vertical_align.set(value)
        if self._vertical_align.value is None:
            self._value[7] = ''
        else:
            self._value[7] = str(self._vertical_align.value.value)
        return self

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        if isinstance(value, str):
            if value.startswith('#'):
                value = value.replace('#', 'c')
            try:
                Color[value]
                self._text_color.set(value)
            except KeyError:
                self._text_color.set('c'+value)
        else:
            self._text_color.set(value)
        if self._text_color.value is None:
            self._value[8] = ''
        else:
            self._value[8] = str(self._text_color.value.value)
        return self

    @property
    def background_color(self):
        return self._background_color
    
    @background_color.setter
    def background_color(self, value):
        if isinstance(value, str):
            try:
                Color[value]
                self._background_color.set(value)
            except KeyError:
                self._background_color.set('c'+value)
        else:
            self._background_color.set(value)
        if self._background_color.value is None:
            self._value[9] = ''
        else:
            self._value[9] = str(self._background_color.value.value)
        return self

    @property
    def taskbar_color(self):
        return self._taskbar_color
    
    @taskbar_color.setter
    def taskbar_color(self, value):
        if isinstance(value, str):
            try:
                Color[value]
                self._taskbar_color.set(value)
            except KeyError:
                self._taskbar_color.set('c'+value)
        else:
            self._taskbar_color.set(value)
        if self._taskbar_color.value is None:
            self._value[10] = ''
        else:
            self._value[10] = str(self._taskbar_color.value.value)
        return self

    @property
    def currency(self):
        return self._currency
    
    @currency.setter
    def currency(self, value):
        self._currency.set(value)
        if self._currency.value is None:
            self._value[11] = ''
        else:
            self._value[11] = str(self._currency.value.value)
        return self

    @property
    def decimal_count(self):
        return self._decimal_count
    
    @decimal_count.setter
    def decimal_count(self, value):
        self._decimal_count.set(value)
        if self._decimal_count.value is None:
            self._value[12] = ''
        else:
            self._value[12] = str(self._decimal_count.value.value)
        return self

    @property
    def thousands_separator(self):
        return self._thousands_separator
    
    @thousands_separator.setter
    def thousands_separator(self, value):
        self._thousands_separator.set(value)
        if self._thousands_separator.value is None:
            self._value[13] = ''
        else:
            self._value[13] = str(self._thousands_separator.value.value)
        return self

    @property
    def number_format(self):
        return self._number_format
    
    @number_format.setter
    def number_format(self, value):
        self._number_format.set(value)
        if self._number_format.value is None:
            self._value[14] = ''
        else:
            self._value[14] = str(self._number_format.value.value)
        return self

    @property
    def text_wrap(self):
        return self._text_wrap
    
    @text_wrap.setter
    def text_wrap(self, value):
        self._text_wrap.set(value)
        if self._text_wrap.value is None:
            self._value[15] = ''
        else:
            self._value[15] = str(self._text_wrap.value.value)
        return self

    @property
    def date_format(self):
        return self._date_format
    
    @date_format.setter
    def date_format(self, value):
        self._date_format.set(value)
        if self._date_format.value is None:
            self._value[16] = ''
        else:
            self._value[16] = str(self._date_format.value.value)
        return self

import smartsheet
smartsheet.models.CellFormat = CellFormat
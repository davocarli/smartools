# Cell Formatting

Cell formatting can be set using the new `CellFormat` class that can be initalized with `smartools.models.CellFormat()`. The class optionally takes a dictionary of initial values, much like initializing other models.

A complete list of the supported formatting settings and their available options can be found below.

#### Font Family

```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.font_family = 'TAHOMA'  # Sets font to TAHOMA

# Available options
ARIAL
TAHOMA
TIMES_NEW_ROMAN
VERDANA
```

#### Font Size
To ensure compatibility with legacy code, the `font_size` property functions like the rest of the CellFormat properties, in that providing an integer will set the property to the value corresponding to that integer per the smartsheet API documentation. For example, this means that setting `format.font_size = 8` will set the font size to `24`.

If you would like to set font sizes using integers (such that `format.font_size = 8` would set the font size to `8`), you can initialize the CellFormat object with the parameter "level=1".

By default, font sizes can also be set using words (`"EIGHT", "TWELVE"`) or numbers prefixed by an f (`"f18", "f14"`).
```
cell_format_1 = smartsheet.models.CellFormat()
cell_format_2 = smartsheet.models.CellFormat(level=1)

# Examples
cell_format_1.font_size = 'EIGHT'    # Sets font size to 8
cell_format_1.font_size = 'f10'      # Sets font size to 10
cell_format_1.font_size = 3          # Sets the font size to 12 (option 3)

cell_format_2.font_size = 'TWELVE'   # Sets the font size to 12
cell_format_2.font_size = 'f16'      # Sets the font size to 16
cell_format_2.font_size = 18         # Sets the font size to 18

# Available options
EIGHT       |  f8
NINE        |  f9
TEN         |  f10
TWELVE      |  f12
FOURTEEN    |  f14
SIXTEEN     |  f16
EIGHTEEN    |  f18
TWENTY      |  f20
TWENTYFOUR  |  f24
TWENTYEIGHT |  f28
THIRTYTWO   |  f32
THIRTYSIX   |  f36
```

#### Bold, Italic, Underline, Strikethrough, Thousands Separator, Text Wrap
These properties are all on/off properties, and share the same options. They also have several aliases.
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.bold = 'ON'
cell_format.italic = 'OFF'
cell_format.strikethrough = 'TRUE'
cell_format.underline = 'YES'
cell_format.thousands_separator = 'NO'

# Available options
OFF  |  FALSE  |  NO   |  NONE
ON   |  TRUE   |  YES
```

#### Horizontal Align
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.horizontal_align = 'LEFT'

# Available options
DEFAULT
LEFT
CENTER
RIGHT
```

#### Vertial Align
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.vertical_align = 'BOTTOM'

# Available options
DEFAULT
TOP
MIDDLE
BOTTOM
```

#### Text Color, Background Color, Taskbar Color
The Color enums are intentionally built with a lot of different aliases to allow you to set colors in different ways. Colors can be set with with a hex color code such as `"#E7F5E9"` or `"cE7F5E9"` or `"E7F5E9"`, but keep in mind that the color selected must be available in the smartsheet *sheet* color picker. The colors can also be set with x/y coordinates of the picker, with the top left being x1y1, and increasing as you move towards the bottom left. Additionally, you can use color names - setting the color to `"ORANGE"`, for example, will set the color to the *middle* hue of the orange column. You can also use `"ORANGE_1"` - `"ORANGE_5"` to move from the top to the bottom of the color picker (lightest to darkest). Lastly, you can use colors such as `"RED_DARK"`, `"RED_MID_DARK"`, `"RED_MID"`, `"RED_MID_LIGHT"`, or `"RED_LIGHT"` to set the different range of red colors.

```
cell_format = smartsheet.models.CellFormat()

# Examples
cell_format.background_color = "RED_DARK"
cell_format.text_color = "WHITE"
cell_format.taskbar_color = "#E7F5E9"

# Available Options
| NONE        |          |                  |                  |                  |                |          |        |            |                |                |            |            |      |
| c000000     | BLACK    | x8y1             |                  |                  |                |          |        |            |                |                |            |            |      |
| cFFFFFF     | WHITE    | x8y5             |                  |                  |                |          |        |            |                |                |            |            |      |
| TRANSPARENT |          |                  |                  |                  |                |          |        |            |                |                |            |            |      |
| cFFEBEE     | RED_1    | RED_LIGHT        | x1y1             |                  |                |          |        |            |                |                |            |            |      |
| cFFF3DF     | ORANGE_1 | ORANGE_LIGHT     | x2y1             |                  |                |          |        |            |                |                |            |            |      |
| cFFFEE6     | x3y1     | YELLOW_1         | YELLOW_LIGHT     |                  |                |          |        |            |                |                |            |            |      |
| cE7F5E9     | GREEN_1  | GREEN_LIGHT      | x4y1             |                  |                |          |        |            |                |                |            |            |      |
| cE2F2FE     | BLUE_1   | BLUE_LIGHT       | x5y1             |                  |                |          |        |            |                |                |            |            |      |
| cF4E4F5     | PURPLE_1 | PURPLE_LIGHT     | x6y1             |                  |                |          |        |            |                |                |            |            |      |
| cF2E8DE     | BROWN_1  | BROWN_LIGHT      | x7y1             |                  |                |          |        |            |                |                |            |            |      |
| cFFCCD2     | RED_2    | RED_LIGHT_MID    | RED_MID_LIGHT    | x1y2             |                |          |        |            |                |                |            |            |      |
| cFFE1AF     | ORANGE_2 | ORANGE_LIGHT_MID | ORANGE_MID_LIGHT | x2y2             |                |          |        |            |                |                |            |            |      |
| cFEFF85     | x3y2     | YELLOW_2         | YELLOW_LIGHT_MID | YELLOW_MID_LIGHT |                |          |        |            |                |                |            |            |      |
| cC6E7C8     | GREEN_2  | GREEN_LIGHT_MID  | GREEN_MID_LIGHT  | x4y2             |                |          |        |            |                |                |            |            |      |
| cB9DDFC     | BLUE_2   | BLUE_LIGHT_MID   | BLUE_MID_LIGHT   | x5y2             |                |          |        |            |                |                |            |            |      |
| cEBC7EF     | PURPLE_2 | PURPLE_LIGHT_MID | PURPLE_MID_LIGHT | x6y2             |                |          |        |            |                |                |            |            |      |
| cEEDCCA     | BROWN_2  | BROWN_LIGHT_MID  | BROWN_MID_LIGHT  | x7y2             |                |          |        |            |                |                |            |            |      |
| cE5E5E5     | GRAY_1   | GRAY_2           | GRAY_LIGHT       | GRAY_LIGHT_MID   | GRAY_MID_LIGHT | GREY_1   | GREY_2 | GREY_LIGHT | GREY_LIGHT_MID | GREY_MID_LIGHT | LIGHT_GRAY | LIGHT_GREY | x8y2 |
| cF87E7D     | RED      | RED_3            | RED_MID          | x1y3             |                |          |        |            |                |                |            |            |      |
| cFFCD7A     | ORANGE   | ORANGE_3         | ORANGE_MID       | x2y3             |                |          |        |            |                |                |            |            |      |
| cFEFF00     | x3y3     | YELLOW           | YELLOW_3         | YELLOW_MID       |                |          |        |            |                |                |            |            |      |
| c7ED085     | GREEN    | GREEN_3          | GREEN_MID        | x4y3             |                |          |        |            |                |                |            |            |      |
| c5FB3F9     | BLUE     | BLUE_3           | BLUE_MID         | x5y3             |                |          |        |            |                |                |            |            |      |
| cD190DA     | PURPLE   | PURPLE_3         | PURPLE_MID       | x6y3             |                |          |        |            |                |                |            |            |      |
| cD0AF8F     | BROWN    | BROWN_3          | BROWN_MID        | x7y3             |                |          |        |            |                |                |            |            |      |
| cBDBDBD     | GRAY     | GRAY_3           | GRAY_MID         | GREY             | GREY_3         | GREY_MID | x8y3   |            |                |                |            |            |      |
| cEA352E     | RED_4    | RED_DARK_MID     | RED_MID_DARK     | x1y4             |                |          |        |            |                |                |            |            |      |
| cFF8D00     | ORANGE_4 | ORANGE_DARK_MID  | ORANGE_MID_DARK  | x2y4             |                |          |        |            |                |                |            |            |      |
| cFFED00     | x3y4     | YELLOW_4         | YELLOW_DARK_MID  | YELLOW_MID_DARK  |                |          |        |            |                |                |            |            |      |
| c40B14B     | GREEN_4  | GREEN_DARK_MID   | GREEN_MID_DARK   | x4y4             |                |          |        |            |                |                |            |            |      |
| c1061C3     | BLUE_4   | BLUE_DARK_MID    | BLUE_MID_DARK    | x5y4             |                |          |        |            |                |                |            |            |      |
| c9210AD     | PURPLE_4 | PURPLE_DARK_MID  | PURPLE_MID_DARK  | x6y4             |                |          |        |            |                |                |            |            |      |
| c974C00     | BROWN_4  | BROWN_DARK_MID   | BROWN_MID_DARK   | x7y4             |                |          |        |            |                |                |            |            |      |
| c757575     | GRAY_4   | GRAY_5           | GRAY_DARK        | GRAY_DARK_MID    | GRAY_MID_DARK  | GREY_4   | GREY_5 | GREY_DARK  | GREY_DARK_MID  | GREY_MID_DARK  | x8y4       |            |      |
| c991310     | RED_5    | RED_DARK         | x1y5             |                  |                |          |        |            |                |                |            |            |      |
| cEA5000     | ORANGE_5 | ORANGE_DARK      | x2y5             |                  |                |          |        |            |                |                |            |            |      |
| cEBC700     | x3y5     | YELLOW_5         | YELLOW_DARK      |                  |                |          |        |            |                |                |            |            |      |
| c237F2E     | GREEN_5  | GREEN_DARK       | x4y5             |                  |                |          |        |            |                |                |            |            |      |
| c0B347D     | BLUE_5   | BLUE_DARK        | x5y5             |                  |                |          |        |            |                |                |            |            |      |
| c61058B     | PURPLE_5 | PURPLE_DARK      | x6y5             |                  |                |          |        |            |                |                |            |            |      |
| c592C00     | BROWN_5  | BROWN_DARK       | x7y5             |                  |                |          |        |            |                |                |            |            |      |
```

#### Currency
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.currency = 'ARS'

# Available options
NONE
ARS
AUD
BRL
CAD
CLP
EUR
ILS
INR
JPY
MXN
RUB
USD
ZAR
CHF
CNY
DKK
HKD
KRW
NOK
NZD
SEK
SGD
```

#### Decimal Count
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.decimal_count = 'THREE'
cell_format.decimal_count = 3

# Available options
ZERO   |  0
ONE    |  1
TWO    |  2
THREE  |  3
FOUR   |  4
FIVE   |  5
```

#### Number Format
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.number_format = 'CURRENCY'

# Available options
NONE
NUMBER
CURRENCY
PERCENT
```

### Date Format
```
cell_format = smartsheet.models.CellFormat()

# Example
cell_format.date_format = 'MMMM_D_YYYY'

# Available options
LOCALE_BASED
MMMM_D_YYYY
MMM_D_YYYY
D_MMM_YYYY
YYYY_MM_DD_HYPHEN
YYYY_MM_DD_DOT
DWWWW_MMMM_D_YYYY
DWWW_DD_MMM_YYYY
DWWW_MM_DD_YYYY
MMMM_D
D_MMMM
```

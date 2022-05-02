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

If you would like to set font sizes using integers (such that `format.font_size = 8` would set the font size to `8`), you can initialize the CellFormat object with "level=1".

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

# Available Options
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

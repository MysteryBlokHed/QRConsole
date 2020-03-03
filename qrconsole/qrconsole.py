# Created by Adam Thompson-Sharpe on 02/03/2020.
# Licensed under MIT.
from PIL import Image
class QRConsole(object):
    """
    `char: str` - The char to use for white in the QR Code. Must be one character only.
    """
    def __init__(self, char: str="@"):
        # Double-check char length & type
        if type(char) is not str:
            raise TypeError(f"Expected str for char, got {type(char).__name__}.")
        elif len(char) != 1:
            raise ValueError(f"char should be of length 1, but it was of length {len(char)}.")
        else:
            self._char = char
    
    def consoleify(self, qr_img: str):
        """
        Turn a QR code into something console-printable.

        `qr_img: str` - The path to the QR Code image.

        Returns: `str` - The console-ified version of the QR Code.
        """
        qr = Image.open(qr_img)
        qr_pixels = qr.load()
        # Start rendering
        render = ""
        # Iterate through all pixels
        for y in range(qr.size[1]):
            for x in range(qr.size[0]):
                if qr_pixels[x,y][0] > 128 and qr_pixels[x,y][1] > 128 and qr_pixels[x,y][2] > 128:
                    render += self._char*2
                else:
                    render += "  "
            render += "\n"
        return render

from PIL import Image

_wordMatrix =   Image.open('../images/word_matrix.png')
_mask       =   Image.open('../images/mask.png')
_oasisSomeMightSay  =   Image.open('../images/oasis-some-might-say.png')

_mask   =   _mask.resize(_wordMatrix.size)
_mask.putalpha(200)

_wordMatrix.paste(_mask, (0, 0), mask=_mask)
_wordMatrix.show()
_wordMatrix.save('result.png')
import re
from os import path
from .grammar import Grammar

# NOTE: hyphen is not part of the word


my_path = path.abspath(path.dirname(__file__))
yml_path = path.join(my_path, 'listing.yml')

_g = Grammar()
_g.load(yml_path)

_g.putr('unknown_char',  '[^{consonant_with_nuktak_raw}{consonant_raw}{nuktak}{matra_raw}{halanta}{joiner}{non_joiner}{vowel_raw}{nasal_raw}{ohm}{avagraha}{dot}{laghav}{number_raw}^]')
_g.putr('not_word', r'{unknown_char}+')
_g.putr('boundary', r'({unknown_char})\1*')

_g.putr('full_consonant', r'(?:{consonant}{nuktak}?|{consonant_with_nuktak})')
_g.putr('half_consonant', r'(?:{full_consonant}{halanta}[{joiner}{non_joiner}]?)')
_g.putr('vowel_syllable', r'(?:{vowel}{nasal}?)')
_g.putr('half_consonant_syllable', r'(?:{half_consonant}+)')
_g.putr('consonant_syllable', r'(?:{half_consonant_syllable}?{full_consonant}{matra}?{nasal}?)')
_g.putr('syllable', r'(?:(?:{consonant_syllable}|{vowel_syllable}){avagraha}*)')

_g.putr('word', '(?:[{dot}]?{syllable}+{half_consonant_syllable}?[{laghav}{dot}]?)')
_g.putr('pragmatic_word', r'(?:{word}|{number}+{word}?|{ohm})')


not_word_re = re.compile(_g.get('not_word'))
boundary_re = re.compile(_g.get('boundary'))
word_re = re.compile('^' + _g.get('pragmatic_word') + '$')

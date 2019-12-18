"""
For testing recursive-sentenceconcat
"""

from recursive_sentenceconcat import do_concat

test1 = "They had published an advertisement on the Internet on June 10, offering the cargo for sale, he added."
test2 = "On June 10, the ship's owners had published an advertisement on the Internet, offering the explosives for sale."

do_concat([test1, test2])


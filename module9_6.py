def all_variants(text):
    beginning = 0
    ending = 0
    for beginning in range(len(text)):
        for ending in range(beginning + 1, len(text) + 1):
            yield text[beginning:ending]


a = all_variants("abc")
for i in a:
    print(i)

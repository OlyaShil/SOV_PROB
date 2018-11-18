import re
from tabulate import tabulate
import pymorphy2

def funcprint(words, mas = []):
    frequency = {}
    for word in mas:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    print(tabulate(frequency.items(), headers=['NAME', 'VALUE'], tablefmt="grid"))

def formatfile(namefile):
    format = ['doc', 'docx', 'txt']
    for i in range(len(format)):
        s = namefile + '.' + format[i]
        try:
            text = open(s).read()
        except:
            i += 1

    return text


namefile = input('Введите название файла: ')

words = re.split(r'[.,;:?!-*"«»… \n]', formatfile(namefile))

prob_thresh = 0.4
morph = pymorphy2.MorphAnalyzer()
mas = []
mas_2 = []
for word in words:
    for p in morph.parse(word):
        if 'Name' in p.tag and p.score >= prob_thresh:
            t = p.normal_form
            mas.append(t)
        if 'Geox' in p.tag and p.score >= prob_thresh:
            s = p.normal_form
            mas_2.append(s)

funcprint(words, mas)
funcprint(words, mas_2)
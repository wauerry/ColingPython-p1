## Задание 1

Решите задачку с [leetcode](https://leetcode.com/problems/min-stack/).
Функциями ```min()```, ```sorted()``` пользоваться нельзя, потому что они не ```O(1)```

## Задание 2

Дана некоторая последовательность в виде строки из латинского алфавита. Ваша задача отсортировать данную строку по возрастанию.
Функцией ```sorted()``` и ```sort()``` для сортировки строки нельзя. Кроме того, нельзя преобразовывать строку в список. Можно использовать ```defaultdict``` и ```counter```

## Задание 3

Создать генератор пар ```ADJF``` и ```NOUN``` в именительном падеже и согласованных по роду с помощью ```itertools```, ```pymorphy``` и ```random``` (чтобы выдавать случайные сочетания), используя [словарь русских слов](https://drive.google.com/file/d/1CqIaWKI9eWMdOtfMS60Ylocnp9ZmIXgu/view?usp=sharing)

Hint 1: Лучше всего сначала создать два массива: один для существительных, второй для прилагательных. Затем можно использовать ```itertools.product()```, и, взяв значительное число словосочетаний, перемешать их и выдавать по одному.

Hint 2, согласование:

```python
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
krasivy = morph.parse('Красивый')[0]

krasivy.inflect({'femn'})

>>> Parse(word='красивая', tag=OpencorporaTag('ADJF,Qual femn,sing,nomn'), normal_form='красивый', score=1.0, methods_stack=((<DictionaryAnalyzer>, 'красивая', 1800, 7),))
```
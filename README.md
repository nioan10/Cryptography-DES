# Cryptography-DES

|&#x2611;|&#x2610;|&#x2612;|


Репозиторий, созданный для формализации разработки программы шифрования алгоритма DES. 
* Мастер-задача: &#x2610; реализовать приложение, удовлетворяющее условиям задания
* Минор-задачи:
  * &#x2610; реализовать интерфейс и меню для программы
  * &#x2610; реализовать функции ввода и вывода данных
  * &#x2610; реализовать функции шифрования и дешифровки
  * &#x2610; связать меню с функциями шифрования
### &#x2610; Реализовать приложение для шифрования, позволяющее выполнять следующие действия:
1. &#x2610; Шифровать данные по заданному в варианте алгоритму:
   * &#x2610; шифруемый текст должен храниться в одном файле, а ключ шифрования – в другом;
   * &#x2610; зашифрованный текст должен сохраняться в файл;
   * &#x2610; в процессе шифрования предусмотреть возможность просмотра и изменения ключа, шифруемого и зашифрованного текстов в шестнадцатеричном и символьном виде;
   * &#x2610; программа должна показывать время шифрования.
2. &#x2610; Исследовать лавинный эффект (исследования проводить на одном блоке текста):
   * &#x2610; для бита, который будет изменяться, приложение должно позволять задавать его позицию (номер) в открытом тексте или в ключе;
   * &#x2610; приложение должно уметь после каждого раунда шифрования подсчитывать число бит, изменившихся в зашифрованном тексте при изменении одного бита в открытом тексте либо в ключе;
   * &#x2610; приложение может строить графики зависимости числа бит, изменившихся в зашифрованном тексте, от раунда шифрования, либо графики можно строить в стороннем ПО, но тогда приложение для шифрования должно сохранять в файл необходимую для построения графиков информацию.

### &#x2610; Реализовать приложение для дешифрования, позволяющее выполнять следующие действия:
1. &#x2610; Дешифровать данные по заданному в варианте алгоритму:
   * &#x2610; зашифрованный текст должен храниться в одном файле, ключ – в другом;
   * &#x2610; расшифрованный текст должен сохраняться в файл;
   * &#x2610; в процессе дешифрования предусмотреть возможность просмотра и изменения ключа, зашифрованного и расшифрованного текстов в шестнадцатеричном и символьном виде.

### &#x2610; Реализовать приложение, вычисляющее значения 1–4 критериев для алгоритмов DES и ГОСТ. Можно взять стороннюю реализацию того алгоритма, который не указан в варианте.
### &#x2610; С помощью реализованных приложений выполнить следующие задания:
1. &#x2610; Протестировать правильность работы разработанных приложений.
2. &#x2610; Исследовать лавинный эффект при изменении одного бита в открытом тексте и в ключе: 
построить графики зависимостей числа бит, изменившихся в зашифрованном сообщении, от раунда шифрования (всего должно быть построено 2 графика).
3. &#x2610; Сравнить значения критериев 1–4 для алгоритмов DES и ГОСТ при изменении одного бита в блоке открытого текста и одного бита в ключе при использовании одного и того же сообщения. Сообщение должно состоять хотя бы из пяти блоков (чем больше, тем точнее будут оценки критериев 1–4).
4. &#x2610; Сделать выводы о проделанной работе.

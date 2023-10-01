Character classification
------------------------

It is often useful to examine a character and test whether it is upper
or lower case, or whether it is a character or a digit. C++ provides a
library of functions that perform this kind of character classification.
In order to use these functions, you have to include the header file
``cctype``.

::

     char letter = 'a';
     if (isalpha(letter)) {
       cout << "The character " << letter << " is a letter." << endl;
     }

You might expect the return value from ``isalpha`` to be a ``bool``, but
for reasons I don’t even want to think about, it is actually an integer
that is 0 if the argument is not a letter, and some non-zero value if it
is.

This oddity is not as inconvenient as it seems, because it is legal to
use this kind of integer in a conditional, as shown in the example. The
value 0 is treated as ``false``, and all non-zero values are treated as
``true``.

Technically, this sort of thing should not be allowed—integers are not
the same thing as boolean values. Nevertheless, the C++ habit of
converting automatically between types can be useful.

Other character classification functions include ``isdigit``, which
identifies the digits 0 through 9, and ``isspace``, which identifies all
kinds of “white” space, including spaces, tabs, newlines, and a few
others. There are also ``isupper`` and ``islower``, which distinguish
upper and lower case letters.

Finally, there are two functions that convert letters from one case to
the other, called ``toupper`` and ``tolower``. Both take a single
character as a parameter and return a (possibly converted) character.

::

     char letter = 'a';
     letter = toupper (letter);
     cout << letter << endl;

The output of this code is ``A``.

As an exercise, use the character classification and conversion library
to write functions named ``stringToUpper`` and ``stringToLower`` that
take a single ``string`` as a parameter, and that modify the string by
converting all the letters to upper or lower case. The return type
should be ``void``.

.. activecode:: character_classification_AC_1
  :language: cpp

  Try writing the ``stringToUpper`` and ``stringToLower`` functions in the 
  commented sections of the active code below. Both functions take a single ``string``
  as a parameter and have return type ``void``. ``stringToUpper`` should convert the string
  to uppercase, and ``stringToLower`` should convert the string to lowercase. Some functions that 
  you might find useful include ``isalpha``, ``isupper``, ``islower``, ``toupper``, and ``tolower``.
  If you get stuck, you can reveal the extra problems at the end for help. 
  ~~~~
  #include <iostream>
  #include <cctype>
  using namespace std;

  void stringToUpper (string &input) {
      // ``stringToUpper`` should convert a string to uppercase. 
      // Write your implementation here.
  }

  void stringToLower (string &input) {
      // ``stringToLower`` should convert a string to lowercase.   
      // Write your implementation here.
  }

  int main() {
      string upper = "This String Should Be Converted To Uppercase!";
      stringToUpper (upper);
      cout << upper << endl;
      string lower = "This String Should Be Converted To Lowercase!";
      stringToLower (lower);
      cout << lower << endl;
  }

.. reveal:: 7_14_1
   :showtitle: Reveal Problem
   :hidetitle: Hide Problem

   .. parsonsprob:: character_classification_1
      :numbered: left
      :adaptive:
   
      Let's write the code for the ``stringToUpper`` function. ``stringToUpper`` 
      should convert a string to uppercase.
      -----
      void stringToUpper (string &input) {
      =====
      void stringToUpper (string input) {                         #paired
      =====
         int i = 0;
      =====
         while (i < input.length()) {
      =====
         while (i < input.length() - 1) {  #paired
      =====
            if (isalpha(input[i]) && islower(input[i])) {
      =====
            if (isalpha(input[i]) && isupper(input[i])) {                        #paired 
      =====
               input[i] = toupper(input[i]);
            }
      =====
               toupper(input[i]);                        #paired
            }
      =====
            i++;
         }
      }

.. reveal:: 7_14_2
   :showtitle: Reveal Problem
   :hidetitle: Hide Problem

   .. parsonsprob:: character_classification_2
      :numbered: left
      :adaptive:
   
      Let's write the code for the ``stringToLower`` function. ``stringToLower`` 
      should convert a string to lowercase.
      -----
      void stringToLower (string &input) {
      =====
      void stringToLower (string input) {                         #paired
      =====
         int i = 0;
      =====
         while (i < input.length()) {
      =====
         while (i > input.length()) {  #paired 
      =====
            if (isalpha(input[i]) && isupper(input[i])) {
      =====
            if (isalpha(input[i]) || isupper(input[i])) {                        #paired 
      =====
               input[i] = tolower(input[i]);
            }
      =====
               input[i] = tolower(input[0]);                        #paired
            }
      =====
            i++;
         }
      }

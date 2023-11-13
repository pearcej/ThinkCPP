The ``find`` function
---------------------

The ``string`` class provides several other functions that you can
invoke on strings. The ``find`` function is like the opposite the ``[]``
operator. Instead of taking an index and extracting the character at
that index, ``find`` takes a character and finds the index where that
character appears.


.. activecode:: find_function_AC_1
  :language: cpp
  :caption: The find function

  Take a look at the active code below, which uses the ``find`` function to find
  the character ``'a'`` in string ``fruit`` and string ``dessert``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string fruit = "banana";
      size_t index = fruit.find('a');
      cout << index << endl;
      string dessert = "pudding";
      size_t another_index = dessert.find('a');
      cout << another_index << " = " << string::npos << endl;
  }

This example finds the index of the letter ``'a'`` in the string. In
this case, the letter appears three times, so it is not obvious what
``find`` should do. According to the documentation, it returns the index
of the *first* appearance, so the result is 1. If the given letter does
not appear in the string, ``find`` a *very* large integer. We can test
whether ``find`` found a given letter by checking to see if it equals
the constant defined by ``string::npos``.

In addition, there is a version of ``find`` that takes another
``string`` as an argument and that finds the index where the substring
appears in the string. 

.. activecode:: find_function_AC_2
  :language: cpp
  :compileargs: [ '-Wall', '-Werror', '-Wno-sign-compare' ]
  :caption: The find function

  The active code below finds the starting index of ``"nan"`` in ``fruit``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string fruit = "banana";
      size_t index = fruit.find("nan");
      cout << index;
  }

This example returns the value 2.

You should remember from :numref:`overloading` that
there can be more than one function with the same name, as long as they
take a different number of parameters or different types. In this case,
C++ knows which version of ``find`` to invoke by looking at the type of
the argument we provide.

.. clickablearea:: find_function_1
    :question: Click on the name of each variable that had been initialized with the value of 0.
    :iscode:
    :feedback: Remember that the index of a string begins at 0, not 1.

    :click-incorrect:def main() {::endclick:
        :click-incorrect:string fruit = "apple";:endclick:
        size_t:click-incorrect: index_a :endclick:= fruit.find('e');
        size_t:click-correct: index_b :endclick:= fruit.find("app");
        size_t:click-correct: index_c :endclick:= fruit.find('a');
        size_t:click-incorrect: index_d :endclick:= fruit.find('l');
    }

.. parsonsprob:: find_function_2
   :numbered: left
   :adaptive:

   Construct a block of code that correctly finds and prints where the first "B" is in the string. Declare ``city`` before ``index``.
   -----
   int main() {

      string city = "New Baltimore";

      string city = "New Baltimore" #distractor

      size_t index;

      index = city.find('B');

      index = city.find(B); #distractor

      index = city.find('b'); #distractor

      cout << index << endl;

   }

.. mchoice:: find_function_3
   :practice: T 

   What is printed when the code is run?

   .. code-block:: cpp

      string sentence = "Most seas are rough but this sea is so calm!";
      string target = "sea";
      size_t index = sentence.find(target);
      cout << "Index to find sea is " << index << endl;

   - Index to find sea is 29

     - ``find`` returns the index of the *first* occurence of "sea".

   - Index to find sea is 5

     + Correct! ``index`` only has to look for a sequence arranged as "sea" in the string.

   - Index to find sea is ``string::npos``

     - "sea" is present in the ``sentence`` string.

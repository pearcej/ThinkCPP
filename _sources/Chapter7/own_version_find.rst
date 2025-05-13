Our own version of ``find``
---------------------------

If we are looking for a letter in a ``string``, we may not want to
start at the beginning of the string. One way to generalize the ``find``
function is to write a version that takes an additional parameter—the
index where we should start looking. Here is an implementation of this
function.

::

   size_t find (string s, char c, size_t i) {
     while (i < s.length()) {
       if (s[i] == c) return i;
       i = i + 1;
     }
     return string::npos;
   }

Instead of invoking this function on an ``string``, like the first
version of ``find``, we have to pass the ``string`` as the first
argument. The other arguments are the character we are looking for and
the index where we should start.

.. activecode:: own_version_find_AC_1
  :language: cpp
  :caption: Our own find function

  In the active code below, we are finding the number of ``'e'`` characters in 
  the "Shepard" part of "German Shepard" using our function. 
  Then we use the built-in ``find`` function to demonstrate how they work differently.
  ~~~~
  #include <iostream>
  using namespace std;

  size_t find (string s, char c, size_t i) {
      size_t length = s.length();
      while (i < length) {
          if (s[i] == c) {
              return i;
          }
          i = i + 1;
      }
      return string::npos;
  }

  int main() {
      string dog = "German Shepard";
      size_t start_shepard = 7;
      cout << find(dog, 'e', start_shepard) << endl;
      cout << dog.find('e') << endl;
  }

.. mchoice:: own_version_find_1
   :practice: T

   What is the correct output of the code below?

   .. code-block:: cpp

      int main() {
        string quote = "The way to get started is to quit talking and begin doing.";
        cout << find(quote, 't', 11) << ", " << find(quote, 't', 42) << ", " << quote.find('t');
      }

   - 13, ``string::npos``, 8
     
     + Notice how the built-in ``find`` function works differently from ours.

   - 13, 0, 7

     - Remember that when a character isn't found, the function returns ``string::npos``.

   - 13, ``string::npos``, 0

     - Keep in mind that the find function is case sensitive, so 'A' is different from 'a'.

   - 14, ``string::npos``, 9

     - Remember that indexing begins at 0 for C++.

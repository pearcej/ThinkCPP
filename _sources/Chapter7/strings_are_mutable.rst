``string``\ s are mutable
-------------------------

You can change the letters in an ``string`` one at a time using the
``[]`` operator on the left side of an assignment.

.. activecode:: sevenfourteen
  :language: cpp
  :caption: String are mutable

  The active code below changes the first letter in ``greeting`` to be
  ``'J'``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string greeting = "Hello, world!";
      greeting[0] = 'J';
      cout << greeting << endl;
  }

produces the output ``Jello, world!``.

.. mchoice:: string_mutable_1
   :practice: T
   :answer_a: icd cream
   :answer_b: icedcream
   :answer_c: ice cream
   :answer_d: iced
   :correct: b
   :feedback_a: Remember that indexing begins at 0, not 1.
   :feedback_b: Correct, index 3 was a space and now it is "d".
   :feedback_c: The character at index 3 should be changed to "d".
   :feedback_d: The character at index 3 should be changed to "d", and the rest stays the same.


   What is printed by the following statements?

   .. code-block:: cpp

      string fav_food = "ice cream";
      fav_food[3] = "d";
      cout << fav_food << endl;

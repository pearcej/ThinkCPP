``string``\ s are mutable
-------------------------

You can change the letters in an ``string`` one at a time using the
``[]`` operator on the left side of an assignment.

.. activecode:: strings_are_mutable_AC_1
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

This produces the output ``Jello, world!``.

.. mchoice:: string_mutable_1
   :practice: T
   :answer_a: icd cream
   :answer_b: icedcream
   :answer_c: ice cream
   :answer_d: iced
   :correct: b
   :feedback_a: Remember that indexing begins at 0, not 1.
   :feedback_b: Index 3 was a space and now it is "d".
   :feedback_c: The character at index 3 should be changed to "d".
   :feedback_d: The character at index 3 should be changed to "d", and the rest stays the same.


   What is printed by the following statements?

   .. code-block:: cpp

      string fav_food = "ice cream";
      fav_food[3] = "d";
      cout << fav_food << endl;

.. mchoice:: string_mutable_2
   :practice: T
   :answer_a: message[9] = "w";
   :answer_b: message[10] = "w";
   :answer_c: "w" = message[9];
   :answer_d: message[8] = "w";
   :correct: a
   :feedback_a: Since "l" is at index 9, replacing it with "w" fixes the message.
   :feedback_b: Remember indexing starts at 0.
   :feedback_c: In order to change a letter in a string, the ``[]`` operator must be on the left of the assignment.
   :feedback_d: Remember indexing starts at 0.

   How can we fix the message to be "You're a wizard Harry"?

   .. code-block:: cpp

      string message = "You're a lizard Harry";

.. parsonsprob:: string_mutable_3
      :numbered: left
      :adaptive:
   
      On the strange planet of Noes, there's a law that prohibits the usage of the letter "e". 
      As a result, they hired you to write a function called ``censorE`` that replaces all occurences
      of the letter "e" in a string with an asterisk and returns the censored string. For example, 
      if the input is "hello world", the function returns "h*llo world".
      -----
      string censorE (string input) {
      =====
      void censorE (string input) {  #paired
      =====
        string copy = input;  #distractor
      =====
        for (int i = 0; i < input.length(); ++i) {
      =====
        for (int i = 0; i < input.length() - 1; ++i) {  #paired
      =====
          if (input[i] == 'e') {
      =====
          if (input[i] = 'e') {  #paired
      =====
            input[i] = '*';
          }
        }
      =====
            '*' = input[i];  #paired
          }
        }
      =====
        return input;
      }

.. parsonsprob:: string_mutable_4
      :numbered: left
      :adaptive:
   
      Your work for the planet of Noes impressed the nearby planets of Noas, Nois, Noos, and Nous.
      They want you to write different functions that censor out each planet's corresponding forbidden letter.
      However, your galaxy brain knows better than to write a different function for each planet.
      Using generalization, write the function ``censorLetter`` which takes a string input and a char to censor 
      as parameters and returns a censored string. For example, censorLetter("Bye world", 'o') returns the
      string "Bye w*rld".
      -----
      string censorLetter (string input, char letter) {
      =====
      string censorLetter (string input) {  #paired
      =====
        for (int i = 0; i < input.length(); ++i) {
      =====
        for (int i = 1; i < input.length(); ++i) {  #paired
      =====
          if (input[i] == letter) {
      =====
          if (input[i] == "letter") {  #paired
      =====
            input[i] = '*';
          }
        }
      =====
            '*' = input[i];  #paired
          }
        }
      =====
        return input;
      }
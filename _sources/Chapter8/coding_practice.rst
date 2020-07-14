Coding Practice
---------------

.. tabbed:: cp_8_1

    .. tab:: Question

        A palindrome is a word, phrase, or sentence that reads the same forwards and backwards.
        Write a function ``isPalindrome`` that takes a string input as a parameter and returns 
        a boolean that is true if the input is a palindrome and false otherwise.  

        .. activecode:: cp_8_AC_1q
           :language: cpp

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           bool isPalindrome (string input) {
               // Write your implementation here.
           }

           int main() {
               cout << isPalindrome ("racecar") << endl;               // Should output 1
               cout << isPalindrome ("no lemon, no melon") << endl;    // Should output 1
               cout << isPalindrome ("kangaroo") << endl;              // Should output 0
           }


    .. tab:: Answer

        Below is one way to implement the program. We use the ``isalpha`` function
        to ignore the non alphabetical characters. Then we continuously check to see 
        if the letters in the front are equal to the ones in the back until we reach the 
        middle of the string.

        .. activecode:: cp_8_AC_1a
           :language: cpp

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           bool isPalindrome (string input) {
               int front = 0;
               int back = input.length() - 1;
               while (front < back) {
                   while (!isalpha(input[front])) {
                       front++;
                   }
                   while (!isalpha(input[back])) {
                       back--;
                   }
                   if (input[front] != input[back]) {
                       return false;
                   }
                   front++;
                   back--;
               }
               return true;
           }

           int main() {
               cout << isPalindrome ("racecar") << endl;               // Should output 1
               cout << isPalindrome ("no lemon, no melon") << endl;    // Should output 1
               cout << isPalindrome ("kangaroo") << endl;              // Should output 0
           }

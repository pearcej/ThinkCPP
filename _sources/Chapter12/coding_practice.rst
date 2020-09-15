Coding Practice
---------------

.. tabbed:: cp_12_1

    .. tab:: Question

        A palindrome is a word, phrase, or sentence that reads the same forwards and backwards.
        Write a function ``isPalindrome`` that takes a ``string input`` as a parameter and returns 
        a boolean that is true if the input is a palindrome and false otherwise. Run and test your code!

        .. activecode:: cp_12_AC_1q
           :language: cpp
           :practice: T

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           bool isPalindrome (string input) {
               // Write your implementation here.
           }
           ====
           #define CATCH_CONFIG_MAIN
           #include <catch.hpp>

           TEST_CASE("factorial function") {
               REQUIRE(isPalindrome ("racecar") == 1); 
               REQUIRE(isPalindrome ("no lemon, no melon") == 1); 
               REQUIRE(isPalindrome ("kangaroo") == 0); 
           }


    .. tab:: Answer

        Below is one way to implement the program. We use the ``isalpha`` function
        to ignore the non alphabetical characters. Then we continuously check to see 
        if the letters in the front are equal to the ones in the back until we reach the 
        middle of the string.

        .. activecode:: cp_12_AC_1a
           :language: cpp
           :optional:

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
           ====
           #define CATCH_CONFIG_MAIN
           #include <catch.hpp>

           TEST_CASE("factorial function") {
               REQUIRE(isPalindrome ("racecar") == 1); 
               REQUIRE(isPalindrome ("no lemon, no melon") == 1); 
               REQUIRE(isPalindrome ("kangaroo") == 0); 
           }

.. activecode:: cp_12_AC_2q
    :language: cpp
    :practice: T

    How much does Bubba love shrimp? Probably a lot. But how many times does the word "shrimp" come
    up in his monologue? Write a function ``countWord`` that counts the number of times a given word 
    appears in a given string. ``countWord`` should take two strings ``input`` and ``word`` as parameters and return an ``int``.
    Feel free to use the ``stringToLower`` function we wrote earlier.
    ~~~~
    #include <iostream>
    #include "ctype.h"
    using namespace std;

    void stringToLower (string &input) {
        int i = 0;
        while (i < input.length()) {
            if (isalpha(input[i]) && isupper(input[i])) {
                input[i] = tolower(input[i]);
            }
            i++;
        }
    }

    int countWord (string input, string word) {
        // Write your implementation here.
    }

    int main() {
        string quote =
            "Anyway, like I was sayin', shrimp is the fruit of the sea. You can "
            "barbecue it, boil it, broil it, bake it, saute it. Dey's uh, "
            "shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, "
            "stir-fried. There's pineapple shrimp, lemon shrimp, coconut shrimp, "
            "pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and "
            "potatoes, shrimp burger, shrimp sandwich. That- that's about "
            "it.";
        cout << "Your output: " << countWord(quote, "shrimp") << ", Correct output: 14" << endl; 
    }
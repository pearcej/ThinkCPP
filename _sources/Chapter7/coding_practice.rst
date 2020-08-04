Coding Practice
---------------

.. tabbed:: cp_7_1

    .. tab:: Question

        A palindrome is a word, phrase, or sentence that reads the same forwards and backwards.
        Write a function ``isPalindrome`` that takes a ``string input`` as a parameter and returns 
        a boolean that is true if the input is a palindrome and false otherwise.  

        .. activecode:: cp_7_AC_1q
           :language: cpp
           :practice: T

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

        .. activecode:: cp_7_AC_1a
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

           int main() {
               cout << isPalindrome ("racecar") << endl;               // Should output 1
               cout << isPalindrome ("no lemon, no melon") << endl;    // Should output 1
               cout << isPalindrome ("kangaroo") << endl;              // Should output 0
           }

.. activecode:: cp_7_AC_2q
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
        cout << countWord(quote, "shrimp");    // There should be 14 instances of the word "shrimp"
    }

.. tabbed:: cp_7_3

    .. tab:: Question

        Write a void function ``censorWord`` that censors a given word from a given string and prints
        out the new string. ``censorWord`` should take two strings ``input`` and ``word`` as parameters
        and prints out ``input`` with every occurence of ``word`` censored with asterisks. For example, 
        ``censorWord ("I really, really, really, really, really, really like you", "really")`` results in 
        the following output:

        :: 
   
           I ******, ******, ******, ******, ******, ****** like you

        .. activecode:: cp_7_AC_3q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           void censorWord (string input, string word) {
               // Write your implementation here.
           }

           int main() {
               censorWord ("I really, really, really, really, really, really like you", "really");
           }


    .. tab:: Answer

        Below is one way to implement the program. We use a while loop to
        repeatedly search for instances of word in input. Once found, we replace 
        the length of the word with asterisks.

        .. activecode:: cp_7_AC_3a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           void censorWord(string input, string word) {
               int length = word.length();
               while ((int)input.find(word) != -1) {
                   int index = input.find(word);
                   int i = 0;
                   while (i < length) {
                       input[index + i] = '*';
                       i++;
                   }
               }
               cout << input;
           }

           int main() {
               censorWord ("I really, really, really, really, really, really like you", "really");
           }

.. activecode:: cp_7_AC_4q
    :language: cpp
    :practice: T

    Write a void function ``removeWord`` that removes a given word from a given string and prints
    out the new string. ``removeWord`` should take two strings ``input`` and ``word`` as parameters
    and prints out ``input`` with every occurence of ``word`` removed. Use string concatenation and the C++
    string function ``substr``. ``substr`` takes two parameters, a starting index and a length. For example, 
    if ``string greeting = "hello world"``, then ``greeting.substr(6, 5)`` returns the string ``"world"``.  
    Test your function in main. The output should be:
    
    :: 

        Gucci , Gucci , Gucci , Gucci
    ~~~~
    #include <iostream>
    using namespace std;

    void removeWord (string input, string word) {
        // Write your implementation here.
    }

    int main() {
        removeWord ("Gucci gang, Gucci gang, Gucci gang, Gucci gang", "gang");
    }

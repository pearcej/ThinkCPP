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
               cout << "Your output: " << isPalindrome ("racecar") << ", Correct output: 1" << endl; 
               cout << "Your output: " << isPalindrome ("no lemon, no melon") << ", Correct output: 1" << endl; 
               cout << "Your output: " << isPalindrome ("kangaroo") << ", Correct output: 0" << endl; 
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
               cout << "Your output: " << isPalindrome ("racecar") << ", Correct output: 1" << endl; 
               cout << "Your output: " << isPalindrome ("no lemon, no melon") << ", Correct output: 1" << endl; 
               cout << "Your output: " << isPalindrome ("kangaroo") << ", Correct output: 0" << endl; 
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
        cout << "Your output: " << countWord(quote, "shrimp") << ", Correct output: 14" << endl; 
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

.. tabbed:: cp_7_5

    .. tab:: Question

        ROT13 is a simple letter substitution cipher that shifts every letter forward by 13,
        looping around if necessary. For example, the letter 'a', 1st in the alphabet, becomes
        the letter 'n', 14th in the alphabet. The letter 'r', 18th in the alphabet, becomes the 
        letter 'e', 5th in the alphabet. Since the alphabet has 26 letters and 13 is exactly half, 
        a message encrypted using ROT13 can be decrypted by calling ROT13 on the encrypted message.
        Write the function ``ROT13``, which takes a ``string input`` as a parameter and returns 
        an encrypted ``string``. Test your function in ``main``.

        .. activecode:: cp_7_AC_5q
           :language: cpp
           :practice: T

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           string ROT13 (string input) {
               // Write your implementation here.
           }

           int main() {
               string original = "Encrypt me then decrypt me!";
               string encrypted = ROT13 (original);
               string decrypted = ROT13 (encrypted);
               cout << "Original string: " << original << endl;
               cout << "Encrypted string: " << encrypted << endl;
               cout << "Decrypted string: " << decrypted << endl;

               // Uncomment and run the code below once your function works!
               // string secretMessage = "Pbatenghyngvbaf! Lbh'ir fhpprffshyyl vzcyrzragrq EBG13 naq qrpbqrq gur frperg zrffntr :)";
               // cout << ROT13 (secretMessage) << endl;
           }


    .. tab:: Answer

        Below is one way to implement the ``ROT13`` function. We use a ``while`` loop to
        go through all the letters in the ``string``. If the letter is between 'a' and 'n' or 
        'A' and 'N', we use character operations to add 13 to each letter. Otherwise,
        we subtract 13 from each letter. We return the encrypted message at the end.

        .. activecode:: cp_7_AC_5a
           :language: cpp
           :optional:

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           string ROT13(string input) {
               int n = 0;
               while (n < (int)input.length()) {
                   if (isalpha(input[n])) {
                       if ((input[n] >= 'a' && input[n] < 'n') || (input[n] >= 'A' && input[n] < 'N')) {
                           input[n] = input[n] + 13;
                       }
                       else {
                           input[n] = input[n] - 13;
                       }
                   }
                   n++;
               }
               return input;
           }

           int main() {
               string original = "Encrypt me then decrypt me!";
               string encrypted = ROT13 (original);
               string decrypted = ROT13 (encrypted);
               cout << "Original string: " << original << endl;
               cout << "Encrypted string: " << encrypted << endl;
               cout << "Decrypted string: " << decrypted << endl;

               // Uncomment and run the code below once your function works!
               // string secretMessage = "Pbatenghyngvbaf! Lbh'ir fhpprffshyyl vzcyrzragrq EBG13 naq qrpbqrq gur frperg zrffntr :)";
               // cout << ROT13 (secretMessage) << endl;
           }

.. activecode:: cp_7_AC_6q
    :language: cpp
    :practice: T

    Write the function ``reverseString`` which takes a ``string input``, reverses it,
    and returns the reversed ``string``. Test your function in ``main``.
    ~~~~
    #include <iostream>
    using namespace std;

    string reverseWord (string input) {
        // Write your implementation here.
    }

    int main() {
        cout << "Your output: " << reverseWord ("hello") << ", Correct output: olleh" << endl; 
        cout << "Your output: " << reverseWord ("world") << ", Correct output: dlrow" << endl; 
        cout << "Your output: " << reverseWord ("racecar") << ", Correct output: racecar" << endl; 
    }

.. tabbed:: cp_7_7

    .. tab:: Question

        Write the function ``capitalize``, which takes a ``string input`` as a parameter.
        ``capitalize`` capitalizes the first letter of every word, and returns the new ``string``.
        Test your function in ``main``.

        .. activecode:: cp_7_AC_7q
           :language: cpp
           :practice: T

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           string capitalize (string input) {
               // Write your implementation here.
           }

           int main() {
               cout << capitalize ("every word in this string should be capitalized!") << endl;
               cout << capitalize ("this String As well") << endl;
           }


    .. tab:: Answer

        Below is one way to implement the ``capitalize`` function. We use a ``while`` loop to
        go through all the ``char``\s in the ``string``. We capitalize the first character
        and all characters following a space using ``toupper``. At the end, we return the ``string``.

        .. activecode:: cp_7_AC_7a
           :language: cpp
           :optional:

           #include <iostream>
           #include "ctype.h"
           using namespace std;

           string capitalize (string input) {
               int n = 0;
               while (n < (int)input.length()) {
                   if (n == 0) {
                       input[n] = toupper(input[n]);
                   }
                   else if (input[n-1] == ' ') {
                       input[n] = toupper(input[n]);
                   }
                   n++;
               }
               return input;
           }

           int main() {
               cout << capitalize ("every word in this string should be capitalized!") << endl;
               cout << capitalize ("this String As well") << endl;
           }

.. activecode:: cp_7_AC_8q
    :language: cpp
    :practice: T

    Write the function ``countVowels`` which takes a ``string input`` and returns
    the number of vowels in the ``string``. Remember, 'a', 'e', 'i', 'o', and 'u'
    are vowels.
    ~~~~
    #include <iostream>
    using namespace std;

    int countVowels (string input) {
        // Write your implementation here.
    }

    int main() {
        cout << "Your output: " << countVowels ("onomatopoeia") << ", Correct output: 8" << endl; 
        cout << "Your output: " << countVowels ("cysts") << ", Correct output: 0" << endl; 
        cout << "Your output: " << countVowels ("vowels") << ", Correct output: 2" << endl; 
    }

.. tabbed:: cp_7_9

    .. tab:: Question

        Write the function ``longestWord``, which takes a ``string input`` as a parameter.
        ``longestWord`` returns the words with the most letters in ``input``. If there's a tie,
        return the first word. Use the ``substr`` function. Test your function in ``main``.

        .. activecode:: cp_7_AC_9q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           string longestWord (string input) {
               // Write your implementation here.
           }

           int main() {
               cout << "Your output: " << longestWord ("what is the longest word in this string") << ", Correct output: longest" << endl; 
               cout << "Your output: " << longestWord ("these words are very close in size") << ", Correct output: these" << endl; 
           }


    .. tab:: Answer

        Below is one way to implement the ``longestWord`` function. We use a ``while`` loop to
        go through all the ``char``\s in the ``string``. We use variables to keep track of the
        longest word, the longest amount of letters, and the length of the current word. We
        can determine the length of a word by counting the number of ``char``\s between spaces.
        If the length is greater than the max, length becomes the new max and we update the longest word.
        This keeps repeating until we reach the end of the string, and the longest word is returned.

        .. activecode:: cp_7_AC_9a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           string longestWord (string input) {
               int n = 0;
               string longest;
               int maxLength = 0;
               while (n < (int)input.length()) {
                   int wordLength = 0;
                   while (input[n] != ' ' && n < (int)input.length()) {
                       wordLength++;
                       n++;
                   }
                   if (wordLength > maxLength) {
                       maxLength = wordLength;
                       longest = input.substr(n - maxLength, maxLength);
                   }
                   n++;
               }
               return longest;
           }

           int main() {
               cout << "Your output: " << longestWord ("what is the longest word in this string") << ", Correct output: longest" << endl; 
               cout << "Your output: " << longestWord ("these words are very close in size") << ", Correct output: these" << endl; 
           }

.. activecode:: cp_7_AC_10q
    :language: cpp
    :practice: T

    Camel case is the practice of writing phrases without spaces or punctuation,
    indicating the separation of words using capital letter. For example, "camel case"
    in camel case is "camelCase". Snake case is the practice of writing phrases
    where each space is replaced by an underscore. For example, "snake case"
    in snake case is "snake_case". Write the functions ``snakeToCamel`` and ``camelToSnake``.
    Each function takes a ``string input`` and returns the input using the other stylization.
    Test your functions in ``main``. Feel free to use any ``string`` functions you'd like.
    ~~~~
    #include <iostream>
    #include "ctype.h"
    using namespace std;

    string snakeToCamel (string input) {
        // Write your implementation here.
    }

    string camelToSnake (string input) {
        // Write your implementation here.
    }

    int main() {
        cout << "Your output: " << snakeToCamel ("turn_this_into_camel_case") << ", Correct output: turnThisIntoCamelCase" << endl; 
        cout << "Your output: " << camelToSnake ("turnThisIntoSnakeCase") << ", Correct output: turn_this_into_snake_case" << endl; 
    }
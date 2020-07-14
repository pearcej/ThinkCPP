Multiple Choice Exercises
-------------------------

.. mchoice:: mce_7_1

    Which variable below is declared as a ``string`` type?

    .. code-block:: cpp

     int main() {
       int x = 0;
       double y = 4.5;
       string word = "hello";
       char c = 'c';
       bool isPrime = 1;
     }

    - ``x``

      - ``x`` is an ``int``.

    - ``y``
    
      - ``y`` is a ``double``.

    - ``word``

      + ``word`` is a ``string``.

    - ``c``

      - ``c`` is a ``char``.

    - ``isPrime``

      - ``isPrime`` is a ``bool``.

.. mchoice:: mce_7_2

    What value should replace the question mark to output the character 'p'?

    .. code-block:: cpp

     int main() {
       string quote = "Not my tempo.";
       cout << quote[?];
     }

    - 11

      - Remember that indexing begins at 0 in C++.

    - 10
    
      + 'p' is located at index 10 in quote.

    - 4

      - The character 'm' is located at index 4.

    - 0

      - The character "N" is located at index 0.

.. mchoice:: mce_7_3

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string quote = "I love you 3000.";
       int x = 3;
       int y = 3 * x;
       int z = 1;
       if (y > 12) {
         z = z + x + y;
       } 
       else {
         z = z + y - x;
       }
       cout << quote[z];
     }

    - I

      - In order to access the character 'I', ``z`` would have to be 0.

    - 0
    
      - What is the value of ``z``?

    - o

      - The value of ``z`` is not 3.

    - y

      + The final value of ``z`` is 7, and 'y' is at index 7 of ``quote``.

.. mchoice:: mce_7_4

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string quote = "Look at me. I'm the captain now.";
       int x = quote.length();
       cout << quote[x];
     }

    - -1

      - -1 is not in ``quote``.

    - w
    
      - ``x`` is not the index value of the character 'w'.

    - .

      - ``x`` is not the index value of the last period.

    - Error, we are indexing out of bounds.

      + ``x`` has a value of 32 and there is no index 32 in ``quote``.

.. mchoice:: mce_7_5

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string quote = "With great power comes great responsiblity.";
       int n = 0;
       while (n < quote.length()) {
         if (n % 5 == 0) {
           cout << quote[n];
         }
         n++;
       }
     }

    - teeest

      - Remember that indexing begins at 0 in C++.

    - Wg reeest
    
      + If we print out every fifth character, including the first, this is the answer.

    - ith reatpowe coms grat rsponibliy.

      - This is what we would get if we removed every fifth character.

    - With great power comes great responsiblity.

      - Take a look at the conditional in the while loop.

.. mchoice:: mce_7_6

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string quote = "Why so serious?";
       int index = quote.find("a");
       cout << index;
     }

    - -1

      + Since 'a' is not found in ``quote``, the ``find`` function returns -1.

    - 0
    
      - 'a' is not the first character in ``quote``.

    - 8

      - The character at index 8 is 'e'.

    - 15

      - There is no index ``15`` in quote.

.. mchoice:: mce_7_7

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string tongue_twister = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?";
       int index = quote.find("wood");
       cout << index;
     }

    - 9

      + The index of 'w' in the first "wood" is at index 9.

    - 10
    
      - Remember indexing begins at 0 in C++.

    - 12

      - The ``find`` function returns the index of the first character of the found string.

    - 22

      - The ``find`` function returns the index of the first instance of the input.

.. mchoice:: mce_7_8

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string tongue_twister = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?";
       int index = find (quote, 'w', quote.find("wood") + 1);
       cout << index;
     }

    - 9

      - Take a closer look at the starting index for where we should start looking.

    - 22
    
      + After the first 'w', the second 'w' appears at index 22.

    - 43

      - Take a closer look at the ``find`` function and its arguments.

    - 65

      - Take a closer look at the ``find`` function and its arguments.

.. mchoice:: mce_7_9

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string quote = "Life is like a box of chocolates. You never know what you’re gonna get.";
       int i = 0;
       int count = 0;
       while (i < quote.length()) {
         if (quote[i] == 'e') {
           count++;
         }
         i++;
       }
       cout << count;
     }

    - 0

      - Are there any occurences of the letter 'e' in ``quote``?

    - 6
    
      - Count the number of 'e's in ``quote``.

    - 7

      + There are 7 occurences of the letter 'e' in ``quote``.

    - 12

      - Count the number of 'e's in ``quote``.

.. mchoice:: mce_7_10

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string call = "Marco!";
       string response = "Polo!";
       string output = "call" + "response";
       cout << output;
     }

    - Marco! Polo!

      - Take a closer look at the initialization of ``output``.

    - Marco!Polo!
    
      - Take a closer look at the initialization of ``output``.

    - call response

      - Can we concatenate "call" and "response"?

    - callresponse

      - Can we concatenate "call" and "response"?
   
    - Error, we cannot concatenate native C strings.

      + We cannot concatenate "call" and "response", so this code results in an error.

.. mchoice:: mce_7_11

    An error occured while delivering a message. All instances of the letter 's'
    got replaced by 'X's. Can you complete the code below to fix this error by selecting 
    the correct line of code to replace the question marks?

    .. code-block:: cpp

     int main() {
       string question = "Honey? Where'X my Xuper Xuit?";
       int i = 0;
       while (i < question.length()) {
         if (question[i] == 'X') {
           ?????
         }
         i++;
       }
       cout << question;
     }

    - ``question['X'] = 's';``

      - The argument in the ``[]`` operator should be a position in the string.

    - ``'s' = question[i];``
    
      - Check the order of your assignment.

    - ``'X' = 's';``

      - We cannot assign the value of 's' to 'X'.

    - ``question[i] = 's';``

      + This will successfully replace all instances of 'X' with 's'.

.. mchoice:: mce_7_12

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       cout << "butter" < "butterfly";
     }

    - butterbutterfly

      - The operator between "butter" and "butterfly" is the ``<`` operator, not ``<<``.

    - 0
    
      - Does "butter" come before or after "butterfly"?

    - 1

      + "butter" comes before "butterfly" in the dictionary.

    - False

      - In C++, boolean values are outputted as either a 0 or 1.
    
    - True

      - In C++, boolean values are outputted as either a 0 or 1.

Multiple Choice Exercises
-------------------------

.. mchoice:: mce_7_1
   :practice: T
   :answer_a: x
   :answer_b: y
   :answer_c: word
   :answer_d: c
   :answer_e: isPrime
   :correct: c
   :feedback_a: x is an int.
   :feedback_b: y is a double.
   :feedback_c: word is a string.
   :feedback_d: c is a char.
   :feedback_e: isPrime is a bool.

   Which variable below is declared as a ``string`` type?

   .. code-block:: cpp

     int main() {
       int x = 0;
       double y = 4.5;
       string word = "hello";
       char c = 'c';
       bool isPrime = 1;
     }

.. mchoice:: mce_7_2
   :practice: T
   :answer_a: 11
   :answer_b: 10
   :answer_c: 4
   :answer_d: 0
   :correct: b
   :feedback_a: Remember that indexing begins at 0 in C++.
   :feedback_b: 'p' is located at index 10 in quote.
   :feedback_c: The character 'm' is located at index 4.
   :feedback_d: The character "N" is located at index 0.

   What value should replace the question mark to output the character 'p'?

   .. code-block:: cpp

     int main() {
       string quote = "Not my tempo.";
       cout << quote[?];
     }

.. mchoice:: mce_7_3
   :practice: T
   :answer_a: I
   :answer_b: 0
   :answer_c: o
   :answer_d: y
   :correct: d
   :feedback_a: In order to access the character 'I', z would have to be 0.
   :feedback_b: What is the value of z?
   :feedback_c: The value of z is not 3.
   :feedback_d: The final value of z is 7, and 'y' is at index 7 of quote.

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

.. mchoice:: mce_7_4
   :practice: T
   :answer_a: -1
   :answer_b: w
   :answer_c: .
   :answer_d: Error, we are indexing out of bounds.
   :correct: d
   :feedback_a: -1 is not in quote.
   :feedback_b: x is not the index value of the character 'w'.
   :feedback_c: x is not the index value of the last period.
   :feedback_d: x has a value of 32 and there is no index 32 in quote.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       string quote = "Look at me. I'm the captain now.";
       int x = quote.length();
       cout << quote[x];
     }

.. mchoice:: mce_7_5
   :practice: T
   :answer_a:  teeest
   :answer_b: Wg reeest
   :answer_c: ith reatpowe coms grat rsponibliy.
   :answer_d: With great power comes great responsiblity.
   :correct: b
   :feedback_a: Remember indexing starts at 0 in C++.
   :feedback_b: If we print out every fifth character, including the first, this is the answer.
   :feedback_c: This is what we would get if we removed every fifth character.
   :feedback_d: Take a look at the conditional in the while loop.

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

.. mchoice:: mce_7_6
   :practice: T
   :answer_a: -1
   :answer_b: 0
   :answer_c: 8
   :answer_d: 15
   :correct: a
   :feedback_a: Since 'a' is not found in quote, the find function returns -1.
   :feedback_b: 'a' is not the first character in quote.
   :feedback_c: The character at index 8 is 'e'.
   :feedback_d: There is no index 15 in quote.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       string quote = "Why so serious?";
       int index = quote.find("a");
       cout << index;
     }

.. mchoice:: mce_7_7
   :practice: T
   :answer_a: 9
   :answer_b: 10
   :answer_c: 12
   :answer_d: 22
   :correct: a
   :feedback_a: The index of 'w' in the first "wood" is at index 9.
   :feedback_b: Remember indexing begins at 0 in C++.
   :feedback_c: The find function returns the index of the first character of the found string.
   :feedback_d: The find function returns the index of the first instance of the input.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       string tongue_twister = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?";
       int index = quote.find("wood");
       cout << index;
     }

.. mchoice:: mce_7_8
   :practice: T
   :answer_a: 9
   :answer_b: 22
   :answer_c: 43
   :answer_d: 65
   :correct: b
   :feedback_a: Take a closer look at the starting index for where we should start looking.
   :feedback_b: After the first 'w', the second 'w' appears at index 22.
   :feedback_c: Take a closer look at the find function and its arguments.
   :feedback_d: Take a closer look at the find function and its arguments.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       string tongue_twister = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?";
       int index = find (quote, 'w', quote.find("wood") + 1);
       cout << index;
     }

.. mchoice:: mce_7_9
   :practice: T
   :answer_a: 0
   :answer_b: 6
   :answer_c: 7
   :answer_d: 12
   :correct: c
   :feedback_a: Are there any occurences of the letter 'e' in quote?
   :feedback_b: Count the number of 'e's in quote.
   :feedback_c: There are 7 occurences of the letter 'e' in quote.
   :feedback_d: Count the number of 'e's in quote.

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

.. mchoice:: mce_7_10
   :practice: T
   :answer_a: Marco! Polo!
   :answer_b: Marco!Polo!
   :answer_c: call response
   :answer_d: callresponse
   :answer_e: Error, we cannot concatenate native C strings.
   :correct: e
   :feedback_a: Take a closer look at the initialization of output.
   :feedback_b: Take a closer look at the initialization of output.
   :feedback_c: Can we concatenate "call" and "response"?
   :feedback_d: Can we concatenate "call" and "response"?
   :feedback_e: We cannot concatenate "call" and "response", so this code results in an error.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       string call = "Marco!";
       string response = "Polo!";
       string output = "call" + "response";
       cout << output;
     }

.. mchoice:: mce_7_11
   :practice: T
   :answer_a: question['X'] = 's';
   :answer_b: 's' = question[i];
   :answer_c: 'X' = 's';
   :answer_d: question[i] = 's';
   :correct: d
   :feedback_a: The argument in the [] operator should be a position in the string.
   :feedback_b: Check the order of your assignment.
   :feedback_c: We cannot assign the value of 's' to 'X'.
   :feedback_d: This will successfully replace all instances of 'X' with 's'.

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

.. mchoice:: mce_7_12
   :practice: T
   :answer_a: butterbutterfly
   :answer_b: 0
   :answer_c: 1
   :answer_d: False
   :answer_e: True
   :correct: c
   :feedback_a: The operator between "butter" and "butterfly" is the < operator, not <<.
   :feedback_b: "butter" comes before "butterfly" in the dictionary.
   :feedback_c: Does "butter" come before or after "butterfly"?
   :feedback_d: In C++, boolean values are outputted as either a 0 or 1.
   :feedback_e: In C++, boolean values are outputted as either a 0 or 1.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       cout << "butter" < "butterfly";
     }
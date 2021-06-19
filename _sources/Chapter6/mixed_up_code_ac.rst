Activecode Exercises
--------------------

Answer the following **Activecode** questions to
assess what you have learned in this chapter.


.. tabbed:: mucp_6_1_ac

   .. tab:: Question

      .. activecode:: mucp_6_1_ac_q
         :language: cpp

         Write a program that prints out the even numbers between 20 and 40, inclusive.
         ~~~~
         #include <iostream>
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_1_ac_a
         :language: cpp

         Below is one way to write the program
         ~~~~
         #include <iostream>
         using namespace std

         int main() {
            int n = 20;
            while (n <= 40){
               cout << n << endl;
               n = n + 2;
            }
         }


.. tabbed:: mucp_6_2_ac

   .. tab:: Question

      .. activecode:: mucp_6_2_ac_q
         :language: cpp

         Write a program that counts down from 100 to 0 in decrements of 10.
         ~~~~
         #include <iostream> 
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_2_ac_a
         :language: cpp

         Below is one way to write the program
         ~~~~
         #include <iostream> 
         using namespace std

         int main() {
            int n = 100;
            while (n >= 0){
               cout << n << endl;
               n -= 10;
            }
         }


.. tabbed:: mucp_6_3_ac

   .. tab:: Question

      .. activecode:: mucp_6_3_ac_q
         :language: cpp

         Write a program that finds the sum of the first 10 natural numbers.
         ~~~~
         #include <iostream>
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_3_aq_a
         :language: cpp

         Below is one way to write the program.
         ~~~~
         #include <iostream> 
         using namespace std

         int main() {
            int n = 1;
            int sum = 0;
            while (n <= 10) {
               sum = sum + n;
               n++
            }
         }


.. tabbed:: mucp_6_4_ac

   .. tab:: Question

      .. activecode:: mucp_6_4_ac_q
         :language: cpp

         Write a function, repreatHello, that is a void function that takes no arguments and uses a while loop to print out "hello" three times.
         ~~~~
         #include <iostream> 
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_4_ac_a
         :language: cpp

         Below is one way to write the function
         ~~~~
         #include <iostream>
         using namespace

         void repeatHello() {
            int n = 0;
            while (n < 3) {
               cout << "hello" << endl;
               n++;
            }
         }


.. tabbed:: mucp_6_5_ac

   .. tab:: Question

      .. activecode:: mucp_6_5_ac_q
         :language: cpp

         Now let's generalize the repeatHello function so that it repeats a given string three times.
         Let's write the code for the repeatString function, which takes
         input as a parameter and uses a while loop to print out the string three times.
         ~~~~
         #include <iostream>
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_5_ac_a
         :language: cpp

         Below is one way to write the function.
         ~~~~
         #include <iostream>
         using namespace std

         void repeatString (string input) {
            int n = 0;
            while (n < 3) {
               cout << input << endl;
               n++;
            }
         }
            

.. tabbed:: mucp_6_6_ac

   .. tab:: Question

      .. activecode:: mucp_6_6_ac_q
         :language: cpp

         We can further generalize repeatString so that it repeats a given string a given number of times.
         Let's write the code for the new repeatString function, which takes
         input and x as parameters and uses a while loop to print out the string x number of times.
         ~~~~
         #include <iostream> 
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_6_ac_a
         :language: cpp

         Below is one way to write the function
         ~~~~
         #include <iostream>
         using namespace std

         void repeatString (string input, int x) {
            int n = 0;
            while (n < x) {
               cout << input << endl;
               n = n + 1;
            }
         }


.. tabbed:: mucp_6_7_ac

   .. tab:: Question

      .. activecode:: mucp_6_7_ac_q
         :language: cpp

         On the last day of every year, we count down the seconds before the new year arrives.
         Write the function newYearCountdown, which prints out a countdown from 10 and then
         prints out "Happy New Year!".         
         ~~~~
         #include <iostream>
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_7_ac_a
         :language: cpp

         Below is one way to write the function.
         ~~~~
         #include <iostream> 
         using namespace std

         void newYearCountdown() {
            int n = 10;
            while (n > 0) {
               cout << n << " ";
               n--;
            }
            cout << "Happy New Year!" << endl;
         }


.. tabbed:: mucp_6_8_ac

   .. tab:: Question

      .. activecode:: mucp_6_8_ac_q
         :language: cpp

         Help Goku reach power levels of over 9000! Write the function
         powerUp which takes powerLevel as a parameter.
         powerUp checks to see if powerLevel is over 9000. If it
         isn't, it repeatedly prints "More power!" and increments powerLevel by
         1000 until powerLevel is over 9000. Then powerUp prints "It's over 9000!".         
         Write the necessary code for the powerUp function.
         ~~~~
         #include <iostream> 
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_8_ac_a
         :language: cpp

         Below is one way to write the function
         ~~~~
         #include <iostream>
         using namespace std

         void powerUp (int powerLevel) {
            while (powerLevel < 9000) {
               cout << "More power!" << endl;
               powerLevel = powerLevel + 1000;
            }
            cout << "It's over 9000!" << endl;
         }


.. tabbed:: mucp_6_9_ac

   .. tab:: Question

      .. activecode:: mucp_6_9_ac_q
         :language: cpp

         Write the function summation which takes two
         parameters, start and end. summation adds
         all the integers from start to end, inclusive, together and returns
         the sum. Write the necessary code for the summation function.
         ~~~~
         #include <iostream> 
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_9_ac_a
         :language: cpp

         Below is one way to write the function
         ~~~~
         #include <iostream>
         using namespace std

         int summation (int start, int end) {
            int n = start;
            int sum = 0;
            while (n <= end) {
               sum = sum + n;
               n++;
            }
            return sum;
         }        


.. tabbed:: mucp_6_10_ac

   .. tab:: Question

      .. activecode:: mucp_6_10_ac_q
         :language: cpp

         Write the function reverseNumber which takes num
         as a parameter and returns num but with its digits reversed.
         For example, reverseNumber (1324) returns 4231.
         Write the necessary code, with reverse
         declared first, then temp, and lastly remainder.
         ~~~~
         #include <iostream>
         using namespace std
         // YOUR CODE HERE


   .. tab:: Answer

      .. activecode:: mucp_6_10_ac_a
         :language: cpp

         Below is one way to write the function
         ~~~~
         #include <iostream> 
         using namespace std

         int reverseNumber (int num) {
            int reverse = 0;
            int temp = num;
            int remainder = 0;
            while (temp > 0) {
               remainder - temp % 10;
               reverse = reverse * 10 + remainder;
               temp = temp / 10;
            }
            return reverse;
         }

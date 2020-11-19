Activecode Exercises
--------------------

Answer the following **Activecode** questions to assess what you have learned in this chapter.


.. tabbed:: vectors_a1

   .. tab:: Question

      .. activecode:: vectors_a1q
         :language: cpp

         Fix the code below so that it creates a vector with 5 elements initialized to 1, and changes
         the third element of that vector to a 2.
         ~~~~
         #include <iostream>


         using namespace std;

         int main () {
             vector<int> nums (5) = 1;
             nums[3] = 2;
         }

   .. tab:: Answer

      .. activecode:: vectors_a1a
         :language: cpp

         Below is one way to fix the program.  You must always include the ``<vector>`` header when
         dealing with vectors.  Furthermore, to initialize a vector's elements to a certain value, you
         must include that value as a second argument to the size.  Finally, vectors are zero-indexed.
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;

         int main () {
             vector<int> nums (5, 1);
             nums[2] = 2;
         }


.. activecode::  vectors_a2
   :language: cpp

   Fix the function below so that it returns how many even numbers are in ``nums``.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;

   int evenCount (const vector<int>& vec) {
       for (int i = 0; i < vec.size(); i++) {
           if (i % 2 == 0) {
               count = count + 1;
           }
       }
       return count;
   }


.. tabbed:: vectors_a3

   .. tab:: Question

      .. activecode:: vectors_a3q
         :language: cpp

         Fix the function below so that it creates a vector of all of the words in ``words`` that end with
         the passed character.
         ~~~~
         #include <iostream>
         #include <string>
         #include <vector>
         using namespace std;

         int endsWith (const vector<string>& vec, char c) {
             int count;
             for (size_t i = 0; i < vec.size(); i++) {
                 last = vec.size() - 1;
                 if (vec[last] == c) {
                     count++;
                 }
             }
             return count;
         }

   .. tab:: Answer

      .. activecode:: vectors_a3a
         :language: cpp

         Below is one way to fix the function.  You must initialize ``count`` to zero.
         You also must initialize ``last`` as an integer.  To access a string *inside* 
         of ``vec``,  we use ``vec[i]``.  To get the last character, we must index the
         string to the last index, which is one less than the length of the string.
         ~~~~
         #include <iostream>
         #include <string>
         #include <vector>
         using namespace std;

         int endsWith (const vector<string>& vec, char c) {
             int count = 0;
             for (size_t i = 0; i < vec.size(); i++) {
                 int last = vec[i].size() - 1;
                 if (vec[i][last] == c) {
                     count++;
                 }
             }
             return count;
         }


.. activecode::  vectors_a4
   :language: cpp

   Someone could have COVID19 if their temperature is above 99.9 degrees Fahrenheit.  Finish 
   the code below so that it counts how many students in the class may have been exposed.
   ~~~~
   #include <iostream>


   using namespace std;

   int main () {
       vector<double> temps = {98.6, 97.8, 100.3, 97.2, 98.7, 97.8, 99.8, 96.9, 98.2, 99.1, 99.9};

       int covid_count = 0;
       for (int i = 0; i < temps.size(); i++) {
           

       }
   }


.. tabbed:: vectors_a5

   .. tab:: Question

      .. activecode:: vectors_a5q
         :language: cpp

         Finish the code below so that it creates removes elements from the end of the vector until
         it ends with ``"stop"``.
         ~~~~
         #include <iostream>


         using namespace std;

         int main () {
             vector<string> words = {"roses", "are", "red", "violets", "stop", "are", "blue"}
         
             while(          ) {

             }

         }

   .. tab:: Answer

      .. activecode:: vectors_a5a
         :language: cpp

         Below is one way to finish the program.  We just use the ``pop_back`` function until the 
         last element of the vector is ``"stop"``.
         ~~~~
         #include <iostream>
         #include <vector>

         using namespace std;

         int main () {
             vector<string> words = {"roses", "are", "red", "violets", "stop", "are", "blue"};
         
             while (words[words.size() - 1] != "stop"){
                 words.pop_back();
             }
         }


.. activecode::  vectors_a6
   :language: cpp

   Write the function ``endsEven`` that takes a vector and removes elements from the end of the vector until
   it ends with an even number.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;


.. tabbed:: vectors_a7

   .. tab:: Question

      .. activecode:: vectors_a7q
         :language: cpp

         Write a function called ``has_char`` that returns a boolean of whether every string in the
         vector ``vec`` contains the character ``let``.  It should return true if all strings contain the ``let``.
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;


   .. tab:: Answer

      .. activecode:: vectors_a7a
         :language: cpp

         Below is one way to finish the program.  We loop through the vector, and we loop through each string
         inside it.  If the string has the character, it is added to ``count``.  We then check whether ``count``
         is equal to the number of elements in ``vec`` and return a boolean.
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;


         int has_char (const vector<string>& vec, char let) {
             int count = 0;
             for (size_t i = 0; i < vec.size(); i++) {
                 for (size_t c = 0; c < vec[i].size(); c++) {
                     if (vec[i][c] == let) {
                         count++;
                     }
                 }
             }
             if (count == vec.size()) {
                 return true;
             }
             return false;
         }
         

.. activecode::  vectors_a8
   :language: cpp

   Write the function ``randomNums`` that takes two integers: ``num`` which is the number of random numbers
   you wish to generate, and ``max``, which is the maximum value of random number you wish to generate.  Your
   function should return a vector of ``num`` integers that are between 1 and ``max``, inclusive.
   ~~~~
   #include <iostream>
   #include <cstdlib>
   #include <vector>
   using namespace std;


.. tabbed:: vectors_a9

   .. tab:: Question

      .. activecode:: vectors_a9q
         :language: cpp

         Write the function ``mean`` which returns the average of a vector of numbers.
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;


   .. tab:: Answer

      .. activecode:: vectors_a9a
         :language: cpp

         Below is one way to finish the program.  First we take the sum, then divide the sum by the number
         of elements in ``nums``.
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;

         double mean (const vector<double> nums) {
             double sum = 0;
             for (size_t i = 0; i < nums.size(); ++i) {
                 sum = sum + nums[i];
             }
             return sum/nums.size();
         }


.. activecode::  vectors_a10
   :language: cpp

   Write the function ``hundyBundy`` that returns a count of all numbers in the passed vector
   ``vec`` that are divisible by 100.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;


.. tabbed:: vectors_a11

   .. tab:: Question

      .. activecode:: vectors_a11q
         :language: cpp

         Write the function ``make_odd`` which subtracts 1 from every even number in a vector of integers.
         We don't want any negative values so don't subtract 1 from 0.
         ( remember to take in the vector by reference to make changes to the actual vector! )
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;


   .. tab:: Answer

      .. activecode:: vectors_a11a
         :language: cpp

         Below is one way to finish the program.  We us the modulus operator to check for even numbers and decrement them.
         we keep an extra check for 0 to make sure wew are not decrementing 0.
         ~~~~
         #include <iostream>
         #include <vector>
         using namespace std;

         void make_odd ( vector<int> &nums) {
             for (size_t i = 0; i < nums.size(); ++i) {

                 if((nums[i] % 2 == 0) && (nums[i] != 0)){
                     nums[i]--;
                 } 

             }
         }


.. activecode::  vectors_a12
   :language: cpp

   Write the function ``weird_print`` that prints the first half of a vector of integers in reverse order
   and then prints the second half in the order present in the vector.
   If we had ``vec = {1,2,3,4,5,6}``
   we would print ``3 2 1 4 5 6``.
   You can assume the size of the vector will always be even.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;
   
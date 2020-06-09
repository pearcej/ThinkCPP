The Return Statement
--------------------

The return statement allows you to terminate the execution of a function
before you reach the end. One reason to use it is if you detect an error
condition:

.. activecode:: return_statement_AC_1
   :language: cpp
   :caption: Terminating a Function with a Return

   #include <iostream>
   #include <cmath>
   using namespace std;

   void printLogarithm (double x) {
       if (x <= 0.0) {
           cout << "Positive numbers only, please." << endl;
           return;
       }
       double result = log (x);
       cout << "The log of x is " << result;
   }

    int main() {
        double y = -9.8;
        printLogarithm(y);
        return 0;
    }

This defines a function named printLogarithm that takes a double named x
as a parameter. The first thing it does is check whether x is less than
or equal to zero, in which case it displays an error message and then
uses return to exit the function. The flow of execution immediately
returns to the caller and the remaining lines of the function are not
executed.

I used a floating-point value on the right side of the condition because
there is a floating-point variable on the left.

Remember that any time you want to use one a function from the math
library, you have to include the header file <cmath>.

Putting ``return 0;`` in your code ends your program. Let's look back at a program from section 4.3. How would your answer change?


.. mchoice:: return_statement_1
   :answer_a: One! Two! Three!
   :answer_b: Three!
   :answer_c: Two!
   :answer_d: One!
   :correct: d
   :feedback_a: Try again! Remember the function of return 0.
   :feedback_b: Try again! Remember the function of return 0.
   :feedback_c: Try again! Remember the function of return 0.
   :feedback_d: The function will return after it fulfills any of the conditionals.

   What will print?

   ::

       #include <iostream>
       using namespace std;

       int main () {
         int x = 10;
         if (x > 8) {
           cout << "One! ";
           return 0;
         }
         if (x > 6) {
           cout << "Two! ";
           return 0;
         }
         if (x > 3) {
           cout << "Three!" << endl;
           return 0;
         }
         return 0;
       }


.. mchoice:: return_statement_2
   :answer_a: One! Two! Three!
   :answer_b: Three!
   :answer_c: Two!
   :answer_c: One!
   :correct: a
   :feedback_a: Correct!
   :feedback_b: All of the following are "if" statements. There are no "else" statements.
   :feedback_c: All of the following are "if" statements. There are no "else" statements.
   :feedback_d: All of the following are "if" statements. There are no "else" statements.

   What will print?

   ::

       #include <iostream>
       using namespace std;

       int main () {
         int x = 10;
         if (x > 8) {
           cout << "One! ";
         }
         if (x > 6) {
           cout << "Two! ";
         }
         if (x > 3) {
           cout << "Three!" << endl;
           return 0;
         }
         return 0;
       }


.. mchoice:: return_statement_3
   :answer_a: One! Two! Three!
   :answer_b: Two! Three!
   :answer_c: Three!
   :answer_d: Two!
   :correct: b
   :feedback_a: The first condition is not met.  Also, if the if is executed, the else cannot be.
   :feedback_b: The fist "if" / else combination does not affect the execution of subsequent "if" / "else" statements.
   :feedback_c: The first pair of "if" and "else" statements do not have an effect on the second "if" statement.
   :feedback_d: The first pair of "if" and "else" statements do not have an effect on the second "if" statement.

   What will print?

   ::

       #include <iostream>
       using namespace std;

       int main () {
         int x = 7;
         if (x > 8) {
           cout << "One! ";
         }
         else (x > 6) {
           cout << "Two! ";
         }
         if (x > 3) {
           cout << "Three!" << endl;
           return 0;
         }
         return 0;
       }


.. activecode:: return_statement_AC_2
   :language: cpp
   :caption: Changing Values
   
   Observe below! Try changing the values in the conditions or the value 
   of x to see what can change!
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int x = 10;
       if (x > 8) {
           cout << "One! ";
           return 0;
       }
       if (x > 6) {
           cout << "Two! ";
           return 0;
       }
       if (x >3) {
           cout << "Three!" << endl;
           return 0;
       }
       return 0;
   }

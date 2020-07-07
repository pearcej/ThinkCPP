Multiple Choice Exercises
-------------------------

.. mchoice:: mce_6_1
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 9
   :answer_d: 10
   :correct: c
   :feedback_a: x is initialized to 0, but it's value is reassigned in the while loop. Can you figure out what the final value assigned to x is?
   :feedback_b: When i is 1, x is assigned the value of i, so x is 1. However, the while loop continuously increments i, so the final value of x is not 1.
   :feedback_c: x is assigned the value of 9 during the last iteration of the while loop, and thus 9 is the output of the program.
   :feedback_d: i is incremented to a value of 10, but since i < 10 is false, the contents of the while loop is not executed, so x is never assigned the value of 10.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       int x = 0;
       int i = 1;
       while (i < 10) {
         x = i;
         i++;
       }
       cout << x;
     }

.. mchoice:: mce_6_2
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 9
   :answer_d: 10
   :correct: d
   :feedback_a: i is initialized with a value of 1 and is incremented, so it will never have a value of 0.
   :feedback_b: i is initialized with a value of 1 but it is incremented during the while loop.
   :feedback_c: This is the final value of x when the code is finished running.
   :feedback_d: In order for the while loop to terminate, the condition i < 10 must be false, and this is achieved when i is incremented to 10.

   What is the final value of ``i`` when the code is finished running?

   .. code-block:: cpp

     int main() {
       int x = 0;
       int i = 1;
       while (i < 10) {
         x = i;
         i++;
       }
       cout << x;
     }

.. mchoice:: mce_6_3
   :practice: T
   :answer_a: 1
   :answer_b: 3
   :answer_c: 5
   :answer_d: The loop will run infinitely.
   :correct: d
   :feedback_a: Take a closer look at the while loop and conditional.
   :feedback_b: Take a closer look at the while loop and conditional.
   :feedback_c: Take a closer look at the while loop and conditional.
   :feedback_d: The value of i will always be greater than 2, resulting in an infinite loop.

   How many times does the following while loop run?

   .. code-block:: cpp

     int main() {
       int i = 6;
       while (i > 2) {
         x = x + 4;
         if (x > 8) {
           x = x - 5;
       }
     }

.. mchoice:: mce_6_4
   :practice: T
   :answer_a: na na na na na na na na Batman!
   :answer_b: na na na na na na na Batman!
   :answer_c: Da na na na na na na na na Batman!
   :answer_d: The end condition is never met, so it will result in an infinite loop.
   :correct: a
   :feedback_a: The code prints out eight "na"s before printing out "Batman!"
   :feedback_b: Look over the code carefully. There are output statements before the while loop.
   :feedback_c: Will "Da" ever be printed?
   :feedback_d: Since we repeatedly decrement n inside the while loop, it will eventually be equal to 3 and the while loop will terminate.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       int n = 10;
       // cout << "Da ";
       cout << "na ";
       while (n != 3) {
         cout << "na ";
         n--;
       }
       cout << "Batman!";
     }

.. mchoice:: mce_6_5
   :practice: T
   :answer_a: Batman!
   :answer_b: Da Batman!
   :answer_c: Da na na na na na na na na Batman!
   :answer_d: The end condition is never met, so it will result in an infinite loop.
   :correct: d
   :feedback_a: Take a closer look at the while loop.
   :feedback_b: Take a closer look at the while loop.
   :feedback_c: Take a closer look at the while loop.
   :feedback_d: Since we never change the value of n, 10 will never equal 3 so the code will run forever.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       int n = 10;
       cout << "Da ";
       cout << "na ";
       while (n != 3) {
         cout << "na ";
       }
       cout << "Batman!";
     }

.. mchoice:: mce_6_6
   :practice: T
   :answer_a: The first six perfect fifths.
   :answer_b: The first six perfect squares.
   :answer_c: The first five perfect squares.
   :answer_d: The first five perfect cubes.
   :correct: c
   :feedback_a: Take a closer look at the while loop and what x was initialized to.
   :feedback_b: Take a closer look at the while loop and what x was initialized to.
   :feedback_c: Dividing x to the power of 5 by x to the power of 3 effectively results in perfect squares.
   :feedback_d: Take a closer look at the mathematical expression inside the while loop.

   What is the output of the code below?

   .. code-block:: cpp

     int main() {
       int x = 1;
       while (x < 6) {
         cout << x << "\t" << pow (x, 5) / pow (x, 3) << endl;
         x++;
       }
     }

.. mchoice:: mce_6_7
   :practice: T
   :answer_a: We're using the same variable, but just reassigning the value from 0 to 1.
   :answer_b: Although the name of both variables is x, they represent different locations in memory, and thus are different variables.
   :answer_c: We can assign them different values but not the same value. Thus, if both were initialized to 0, then we'd get an error.
   :answer_d: We're not allowed to do this. The code will result in an error.
   :correct: b
   :feedback_a: We are actually using two different variables that happen to have the same name.
   :feedback_b: One x is a local variable of superSecretFunction while the other is a local variable of main.
   :feedback_c: Since they are not in the same storage location, they can store any value, including the same value.
   :feedback_d: The code does not produce an error.

   Why are we allowed to use the variable ``x`` in both ``main`` and in the function definition of ``superSecretFunction``?

   .. code-block:: cpp
   
     int superSecretFunction (int n) {
       int x = 0;
       return (2 + (n * n) - 5 * n / 7) * x;
     }

     int main() {
       int x = 1;
       cout << "After using the super secret function, we get " << superSecretFunction (x);
     }
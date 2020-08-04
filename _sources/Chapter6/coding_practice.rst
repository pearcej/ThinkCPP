Coding Practice
---------------

.. tabbed:: cp_6_1

    .. tab:: Question

        Write a program that prints out a 5x5 triangle using asterisks. 
        An example is shown below. Your code should use while loops.

        :: 
   
           *
           **
           ***
           ****
           *****

        .. activecode:: cp_6_AC_1q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           int main() {
               // Write your implementation here.
           }


    .. tab:: Answer

        Below is one way to implement the program. We use nested loops
        similar to the last version of the ``printMultTable`` function
        to print out the triangular shape.

        .. activecode:: cp_6_AC_1a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           int main() {
               int row = 0;
               while (row < 5) {
                   int col = 0;
                   while (col <= row) {
                       cout << "*";
                       col++;
                   }
                   cout << endl;
                   row++;
               }
           }

.. activecode:: cp_6_AC_2q
    :language: cpp
    :practice: F

    Encapsulate the triangle printing program into a function called
    ``printTriangle``. Generalize it so that it takes a parameter
    ``int n`` to generate a nxn triangle. Call your function in main
    with an input of 4, which should result in the following output:

    :: 

        *
        **
        ***
        ****
    ~~~~
    #include <iostream>
    using namespace std;

    void printTriangle (int n) {
        // Write your implementation here.
    }

    int main() {
        // Write your implementation here.
    }

.. tabbed:: cp_6_3

    .. tab:: Question

        A common coding interview question that's also a popular children's game used to teach division is
        FizzBuzz. Write a program that uses a while loop and prints the numbers 1 through 100, but every
        multiple of 3 is replaced with the word "Fizz," every multiple of 5 is replaced with the word "Buzz," 
        and every multiple of both 3 and 5 is replaced with "FizzBuzz." Your output should be the following:

        :: 
   
           1
           2
           Fizz
           4
           Buzz
           ...
           14
           FizzBuzz
           16
           ...
           98
           Fizz
           Buzz

        .. activecode:: cp_6_AC_3q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           int main() {
               // Write your implementation here.
           }


    .. tab:: Answer

        Below is one way to implement the "FizzBuzz" program. We use conditionals
        with modulus operators in a while loop to categorize every number and print
        the correct output. Feel free to search up on the FizzBuzz coding interview 
        problem if you are interested in other ways to code this program!

        .. activecode:: cp_6_AC_3a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           int main() {
               int n = 1;
               while (n <= 100) {
                   if (n % 3 == 0 && n % 5 == 0) {
                       cout << "FizzBuzz" << endl;
                   }
                   else if (n % 3 == 0) {
                       cout << "Fizz" << endl;
                   }
                   else if (n % 5 == 0) {
                       cout << "Buzz" << endl;
                   }
                   else {
                       cout << n << endl;
                   }
                   n++;
               }
           }

.. activecode:: cp_6_AC_4q
    :language: cpp
    :practice: T

    Write the function ``printAddTable`` which takes an ``int n`` as a parameter
    and prints out a nxn addition table. Call your function in ``main`` with
    "10" as the argument. Your output should look like this:

    :: 

        0       1       2       3       4       5       6       7       8       9       10
        1       2       3       4       5       6       7       8       9       10      11
        2       3       4       5       6       7       8       9       10      11      12
        3       4       5       6       7       8       9       10      11      12      13
        4       5       6       7       8       9       10      11      12      13      14
        5       6       7       8       9       10      11      12      13      14      15
        6       7       8       9       10      11      12      13      14      15      16
        7       8       9       10      11      12      13      14      15      16      17
        8       9       10      11      12      13      14      15      16      17      18
        9       10      11      12      13      14      15      16      17      18      19
        10      11      12      13      14      15      16      17      18      19      20
    ~~~~
    #include <iostream>
    using namespace std;

    void printAddTable (int n) {
        // Write your implementation here.
    }

    int main() {
        // Call your function here.
    }
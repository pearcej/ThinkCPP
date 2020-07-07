Coding Practice
---------------

.. tabbed:: cp_7_1

    .. tab:: Question

        Write a program that prints out a 5x5 triangle using asterisks. 
        An example is shown below. Your code should use while loops.

        :: 
   
           *
           **
           ***
           ****
           *****

        .. activecode:: cp_7_AC_1q
           :language: cpp

           #include <iostream>
           using namespace std;

           int main() {
               // Write your implementation here.
           }


    .. tab:: Answer

        Below is one way to implement the program. We use nested loops
        similar to the last version of the ``printMultTable`` function
        to print out the triangular shape.

        .. activecode:: cp_7_AC_1a
           :language: cpp

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


find and replace
counter
pokemon types using concatenation
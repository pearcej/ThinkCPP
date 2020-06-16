Programs with Multiple Functions
--------------------------------

When you look at a class definition that contains several functions, it
is tempting to read it from top to bottom, but that is likely to be
confusing, because that is not the **order of execution** of the
program.

.. note::
   The order of execution is not necessarily the order in which functions
   are defined!  For example, the last function that you write might be the 
   first one that you call in the ``main`` function.

Execution always begins at the first statement of ``main``, regardless of
where it is in the program (often it is at the bottom). Statements are
executed one at a time, in order, until you reach a function call.
Function calls are like a detour in the flow of execution. Instead of
going to the next statement, you go to the first line of the called
function, execute all the statements there, and then come back and pick
up again where you left off.

That sounds simple enough, except that you have to remember that one
function can call another. Thus, while we are in the middle of ``main``, we
might have to go off and execute the statements in ``threeLine``. But while
we are executing ``threeLine``, we get interrupted three times to go off and
execute ``newLine``.

Fortunately, C++ is adept at keeping track of where it is, so each time
``newLine`` completes, the program picks up where it left off in ``threeLine``,
and eventually gets back to ``main`` so the program can terminate.


.. activecode:: multiple_functions_AC_1
   :language: cpp
   :caption: Multiply / Add Two

   This program calls the multiplyTwo and addTwo functions in the
   main.  See if you can follow the order of execution.
   ~~~~
   #include <iostream>
   using namespace std;

   void printTotal (int x) {
       cout << x << endl;
   }

   int multiplyTwo (int x) {
       int total = x * 2;
       printTotal(total);
       return total;
   }

   int addTwo (int x) {
       int total = x + 2;
       return total;
   }

   int main () {
       int num = 2;
       int new = multiplyTwo(num);
       int newer = addTwo(new);
       return 0;
   }


What’s the moral of this sordid tale? When you read a program, don’t
read from top to bottom. Instead, **follow the flow of execution**.


.. dragndrop:: multiple_functions_1
   :feedback: Try again!
   :match_1: multiplyTwo|||executes next
   :match_2: printTotal|||executes last
   :match_3: main|||executes first

   Match the function to the order it is executed in the program above.


.. mchoice:: multiple_functions_2
   :answer_a: 12, 13, 14, 8, 9, 10, 15, 16, 17
   :answer_b: 12, 13, 14, 8, 9, 4, 5, 6, 4, 5, 6, 4, 5, 6, 10, 15, 16, 17
   :answer_c: 1, 2, 12, 13, 14, 8, 9, 10, 15, 16, 17
   :answer_d: 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17
   :answer_e: 1, 2, 12, 13, 14, 8, 9, 4, 5, 6, 4, 5, 6, 4, 5, 6, 10, 15, 16, 17
   :correct: b
   :feedback_a: Keep in mind that one of the functions is being called three times.
   :feedback_b: Execution begins in the main, then functions are executed as they are called.
   :feedback_c: Keep in mind that one of the functions is being called three times.  Also, note that function execution begins in int main.
   :feedback_d: Keep in mind that execution begins in the main.  Remember to follow the order of execution, which is not necessarily the order the program is written.
   :feedback_e: Keep in mind that execution begins in the main.

   Consider the following C++ code. Note that line numbers are included 
   on the left.

   .. code-block:: cpp
      :linenos:

      #include <iostream>
      using namespace std;

      void newLine () {
        cout << endl;
      }

      void threeLine () {
        newLine ();  newLine ();  newLine ();
      }

      int main () {
        cout << "First Line." << endl;
        threeLine ();
        cout << "Second Line." << endl;
        return 0;
      }

   Which of the following reflects the order in which these lines 
   of code are executed in C++?
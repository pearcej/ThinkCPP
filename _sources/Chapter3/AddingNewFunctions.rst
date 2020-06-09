Adding New Functions
--------------------

So far we have only been using the functions that are built into C++,
but it is also possible to add new functions. Actually, we have already
seen one function definition: main. The function named main is special
because it indicates where the execution of the program begins, but the
syntax for main is the same as for any other function definition:

::

    void NAME ( LIST OF PARAMETERS ) {
      STATEMENTS
    }

You can make up any name you want for your function, except that you
can’t call it main or any other C++ keyword. The list of parameters
specifies what information, if any, you have to provide in order to use
(or **call**) the new function.

``main`` doesn’t take any parameters, as indicated by the empty parentheses
() in it’s definition. The first couple of functions we are going to
write also have no parameters, so the syntax looks like this:

::

    void newLine () {
      cout << endl;
    }

This function is named newLine; it contains only a single statement,
which outputs a newline character, represented by the special value
endl.

In main we can call this new function using syntax that is similar to
the way we call the built-in C++ commands:

::

    int main () {
      cout << "First Line." << endl;
      newLine ();
      cout << "Second Line." << endl;
      return 0;
    }

The output of this program is

::

    First line.

    Second line.

Notice the extra space between the two lines. What if we wanted more
space between the lines? We could call the same function repeatedly:

::

    int main () {
      cout << "First Line." << endl;
      newLine ();
      newLine ();
      newLine ();
      cout << "Second Line." << endl;
      return 0;
    }

Or we could write a new function, named threeLine, that prints three new
lines:


.. activecode:: new_functions_AC_1
   :language: cpp
   :caption: The threeLine Function

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


You should notice a few things about this program:

-  You can call the same procedure repeatedly. In fact, it is quite
   common and useful to do so.

-  You can have one function call another function. In this case, main
   calls threeLine and threeLine calls newLine. Again, this is common
   and useful.

-  In threeLine I wrote three statements all on the same line, which is
   syntactically legal (remember that spaces and new lines usually don’t
   change the meaning of a program). On the other hand, **it is usually a
   better idea to put each statement on a line by itself**, to make your
   program easy to read. I sometimes break that rule in this book to
   save space.

So far, it may not be clear why it is worth the trouble to create all
these new functions. Actually, there are a lot of reasons, but this
example only demonstrates two:

#. Creating a new function gives you an opportunity to give a name to a
   group of statements. Functions can simplify a program by hiding a
   complex computation behind a single command, and by using English
   words in place of arcane code. Which is clearer, ``newLine`` or ``cout <<
   endl``?

#. Creating a new function can make a program smaller by eliminating
   repetitive code. For example, a short way to print nine consecutive
   new lines is to call threeLine three times. How would you print 27
   new lines?


.. mchoice:: new_functions_1
   :answer_a: void printName()
   :answer_b: totalCost(double cost, double tax) {
   :answer_c: string todaysWeather(int temperature) {
   :answer_d: double finalGrade {
   :correct: c
   :feedback_a: This function header is missing a {, which is need to start and end a function definition.
   :feedback_b: This function header is missing a return type.
   :feedback_c: Correct!
   :feedback_d: This function header is missing parentheses. Even if a function does not take in any parameters, empty parentheses should be used.

   Which of the following is a correct function header (first line of 
   a function definition)?


.. mchoice:: new_functions_2
   :answer_a: You can name a function anything you want.
   :answer_b: You can have a fucntion with several parameters or a function with none.
   :answer_c: You can call a function inside of another function.
   :answer_d: You can write multiple statements on one line.
   :correct: a
   :feedback_a: You can't name a function the same name as a reserved keyword.
   :feedback_b: This is true! However, you must always use parentheses.
   :feedback_c: This is true! It is common and useful.
   :feedback_d: This is true! As long as each statement ends with a semicolon.

   Which of the following is **false** about functions?


.. clickablearea:: new_functions_3
   :question: Click on all function headers statements.
   :iscode:
   :feedback: Remember, the operator '=' is used for assignment.

   :click-correct:void printX(){:endclick:
       :click-incorrect:cout << "X";:endclick:
   }
   
   :click-incorrect:int pi = 3.14159;:endclick:

   :click-correct:int main() {:endclick:
       :click-incorrect:int x = 4;:endclick:
       for (int i = 0; i < 5; ++i){
           :click-incorrect:y = i;:endclick:
           :click-incorrect:if y > 2{:endclick:
               cout << y;
           }
       }
       :click-incorrect:printX();:endclick:
       :click-incorrect:double result = x / y;:endclick:
       :click-incorrect:return result;:endclick:
   }

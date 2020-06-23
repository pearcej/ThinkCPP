Composition
-----------

Just as with mathematical functions, C++ functions can be **composed**,
meaning that you use one expression as part of another. For example, you
can use any expression as an argument to a function:

::

    double x = cos (angle + pi / 2);

This statement takes the value of pi, divides it by two and adds the
result to the value of angle. The sum is then passed as an argument to
the ``cos`` function.

You can also take the result of one function and pass it as an argument
to another:


.. activecode:: function_comp_AC_1
   :language: cpp
   :caption: Composition of Math Functions

   This program finds the log base e of 10 and raises e to that power.  The
   result of this computation is assigned to x.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   int main () {
       double x = exp (log (10.0));
       cout << x;
   }


.. mchoice:: function_comp_1
   :answer_a: double x = log2 (12)
   :answer_b: double val = tan (angle + pi/3);
   :answer_c: double num = exp (cos(1.34))
   :answer_d: double y = exp (cosine(9.8)) + exp (tan(4.5));
   :correct: b
   :feedback_a: log2 is not a built in cmath function, but you could write an implementation for it if you wanted!
   :feedback_b: This correctly uses cmath functions!
   :feedback_c: This would be correct if it ended in a semi-colon.
   :feedback_d: Make sure to use the math keywords reserved in C++ when using math functions. Using **cosine** instead of *cos* is incorrect.

   Which of these statements has correct syntax?


.. fillintheblank:: function_comp_2

   What is the value of x?

   ::

       double x = sin ( log10 (1000) * exp (2) );

   - :-0\.175112: Correct!
     :.*: Try again! (try modifying the active code to test it out!)

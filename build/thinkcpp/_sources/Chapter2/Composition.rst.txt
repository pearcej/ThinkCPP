Composition
-----------

So far we have looked at the elements of a programming
language—variables, expressions, and statements—in isolation, without
talking about how to combine them.

One of the most useful features of programming languages is their
ability to take small building blocks and **compose** them. For example,
we know how to multiply integers and we know how to output values; it
turns out we can do both at the same time:


.. activecode:: composition_AC_1
   :language: cpp
   :caption: Multiplication Output

   This program performs multiplication and prints the result simultaneously.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       cout << 17 * 3;
   }


Actually, I shouldn’t say “at the same time,” since in reality the
multiplication has to happen before the output, but the point is that
any expression, involving numbers, characters, and variables, can be
used inside an output statement. We’ve already seen one example:


.. activecode:: composition_AC_2
   :language: cpp
   :caption: Variable Output

   This program performs a calculation involving variables and prints
   the result at the same time.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int hour = 7;
       int minute = 1;
       cout << hour * 60 + minute << endl;
   }


You can also put arbitrary expressions on the right-hand side of an
assignment statement:


.. activecode:: composition_AC_3
   :language: cpp
   :caption: Performing Calculations Before Assignment

   This program performs a calculation involving variables and 
   simultaneously assigns the result to a variable.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int minute = 3;
       int percentage;
       percentage = (minute * 100) / 60;
       cout << percentage;
   }


This ability may not seem so impressive now, but we will see other
examples where composition makes it possible to express complex
computations neatly and concisely.

.. Warning::
   There are limits on where you can use certain expressions; most
   notably, the left-hand side of an assignment statement has to be a
   *variable* name, not an expression. 

That’s because the left side indicates the storage location where the 
result will go. Expressions do not represent storage locations, only 
values. So the following is illegal: ``minute + 1 = hour;``.


.. mchoice:: compos_1
   :answer_a: Change the fourth line in main to pets = dogs + cats;
   :answer_b: Change the fourth line in main to int pets = dogs + cats;
   :answer_c: Change the fourth line in main to pets == dogs + cats;
   :answer_d: Change the fourth line in main to int pets == dogs + cats;
   :correct: a
   :feedback_a: Assignment statements operate such that the evaluated expression on the right is assigned to the variable on the left.
   :feedback_b: pets has already been declared as an int.
   :feedback_c: The == operator checks if the left side EQUALS the right side.  It is not the correct operator here.
   :feedback_d: pets has already been declared as an int.  Also, the == operator is not the proper choice here.

   What must be changed in order for this code block to work?

   ::

       #include <iostream>
       using namespace std;

       int main () {
         int dogs = 3;
         int cats = 6;
         int pets;
         dogs + cats = pets;
         cout << "I have " << pets << " pets!";
         return 0;
       }


.. fillintheblank:: compos_2

   The left-hand side of an assignment statement has to be a |blank| 
   name, not an expression.

   - :[Vv][Aa][Rr][Ii][Aa][Bb][Ll][Ee]: Correct!
     :.*: Try again!


.. fillintheblank:: compos_3

   In programming, another word for **combine** is |blank|.

   - :[Cc][Oo][Mm][Pp][Oo][Ss][Ee]: Correct!
     :.*: Try again!

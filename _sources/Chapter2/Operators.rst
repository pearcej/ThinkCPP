Operators
---------

**Operators** are special symbols that are used to represent simple
computations like addition and multiplication. Most of the operators in
C++ do exactly what you would expect them to do, because they are common
mathematical symbols. For example, the operator for adding two integers
is ``+``.

The following are all legal C++ expressions whose meaning is more or
less obvious:

::

    1 + 1
    hour - 1
    hour * 60 + minute
    minute / 60

Expressions can contain both variables names and integer values. In each
case the name of the variable is replaced with its value before the
computation is performed.

Addition, subtraction and multiplication all do what you expect, but you
might be surprised by division. For example, compile the following program around
observe the output.

.. activecode:: operators_AC_1
   :language: cpp
   :caption: Integer Division

   This program is supposed to print the fraction of the hour that has
   passed since midnight.  You'll notice that the result isn't quite what
   you expect.  Read on to find out why!
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int hour, minute;
       hour = 12;
       minute = 59;
       cout << "Number of minutes since midnight: ";
       cout << hour * 60 + minute << endl;
       cout << "Fraction of the hour that has passed: ";
       cout << minute / 60 << endl;
       return 0;
   }

The first line is what we expected, but the second line is odd. The
value of the variable minute is 59, and 59 divided by 60 is 0.98333, not
0. The reason for the discrepancy is that C++ is performing **integer
division**.

When both of the **operands** are integers (operands are the things
operators operate on), the result must also be an integer, and by
definition integer division always rounds *down*, even in cases like
this where the next integer is so close.

A possible alternative in this case is to calculate a percentage rather
than a fraction:

::

    cout << "Percentage of the hour that has passed: ";
    cout << minute * 100 / 60 << endl;

The result is:

::

    Percentage of the hour that has passed: 98

Again the result is rounded down, but at least now the answer is
approximately correct. In order to get an even more accurate answer, we
could use a different type of variable, called floating-point, that is
capable of storing fractional values. 

.. note::
   In C++, floating-points are declared as type ``double``. We’ll get 
   to that in the next chapter.


.. dragndrop:: operators_1
   :feedback: Try again!
   :match_1:  x*10|||100
   :match_2: x-10|||0
   :match_3: 100/x|||10
   :match_4: (x+x+x+x+x)*20|||1000

   Match the statement to the result, given that x = 10.


.. mchoice:: operators_2
   :answer_a: 0
   :answer_b: 1
   :answer_c: .667
   :answer_d: .6666666667
   :correct: a
   :feedback_a: Correct! In integer division, the decimal part is simply discarded, which is why the result would be 0.
   :feedback_b: The decimal part is discarded. This means we do not round up, only down.
   :feedback_c: In integer division, an integer must be the result.
   :feedback_d: In integer division, an integer must be the result.

   What is the output?

   ::

       int main () {
         int sum = 2 / 3;
         cout << sum;
       }


.. fillintheblank:: operators_3

   Integer division always rounds |blank| to the nearest |blank|.

   - :[Dd][Oo][Ww][Nn]: Correct!
     :x: Try again!
   - :[Ii][Nn][Tt][Ee][Gg][Ee][Rr]: Correct!
     :.*: Try again!


.. parsonsprob:: operators_4
   :numbered: left
   :adaptive:
   
   Construct a code block that prints the total cost of your meal,
   including the 6.0% sales tax, after you purchase two orders of
   fries, three burgers, and a milkshake.  Start by initializing
   the value of sales tax, then the prices of the food.  Once you
   have initialized the variables, you can perform your calculations
   and save the result in the price variable.  At the very end, you
   will print out the total price.
   -----
   int main () {
   =====
    double tax = 0.06;
   =====
    double fries, milkshake, burger;
   =====
    string fries, milkshake, burger; #paired
   =====
    fries = 2.50;
    milkshake = 3.75;
    burger = 3.00;
   =====
    double price = 2 * fries + 3 * burger + milkshake;
   =====
    double priceWithTax = price + price * tax;
   =====
    double priceWithTax = price * tax; #paired
   =====
    cout << "The total cost of your meal is $"; 
    cout << priceWithTax << "." << endl;
   =====
    cout << "The total cost of your meal is $"; #paired
    cout << price << "." << endl;
   =====
   }
   

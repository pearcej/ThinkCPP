Order of Operations
-------------------

When more than one operator appears in an expression the order of
evaluation depends on the rules of **precedence**. A complete
explanation of precedence can get complicated, but just to get you
started:

-  Multiplication and division happen before addition and subtraction.
   So ``2 * 3 - 1`` yields 5, not 4, and ``2 / 3 - 1`` yields -1, not 1 
   (remember that in integer division ``2/3`` is 0).

-  If the operators have the same precedence they are evaluated from
   left to right. So in the expression ``minute * 100 / 60``, the multiplication
   happens first, yielding ``5900 / 60``, which in turn yields 98. If the
   operations had gone from right to left, the result would be 59 * 1
   which is 59, which is wrong.

-  Any time you want to override the rules of precedence (or you are not
   sure what they are) you can use parentheses. Expressions in parentheses 
   are evaluated first, so ``2 * (3 - 1) is 4``. You can also use parentheses 
   to make an expression easier to read, as in ``(minute * 100) / 60``, even 
   though it doesn’t change the result.


.. activecode:: order_of_operations_AC_1
   :language: cpp
   :caption: The Role of Parentheses
  
   Observe the output of the code below to see how the placement of parentheses 
   can change the result of a calculation.

   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       cout << (2 * 3) - 1 << endl;
       cout << 2 * (3 - 1) << endl;
       cout << 2 / 3 - 1 << endl;
       cout << 2 / (3 -1) << endl;
   }


.. dragndrop:: order_of_operations_1
   :feedback: Try again!
   :match_1:  (6*4)+1|||25
   :match_2: 6*(4+1)|||30
   :match_3: (6/4)+1|||2
   :match_4: 6/(4+1)|||1

   Match the expression to its correct output. Don't forget to consider integer 
   division!


.. fillintheblank:: order_of_operations_2

   Any time you want to override the rules of precedence, you can use |blank|.

   - :[Pp][Aa][Rr][Ee][Nn][Tt][Hh][Ee][Ss][Ee][Ss]: Correct!
     :.*: Try again!


The next 4 questions walk you through an example of the rules of precedence.
Answer them in order to check what you remember about the order of operations!


.. clickablearea:: order_of_operations_3
   :question: Click on ALL PARTS of the expression that get evaluated first.  For example, if "1 + 1" gets evaluated first, click on "1", "+", and "1".
   :iscode:
   :feedback: Try again!

   :click-incorrect:1:endclick: :click-incorrect:+:endclick: :click-incorrect:2:endclick: :click-incorrect:*:endclick: ( :click-correct:10:endclick: :click-correct:-:endclick: :click-correct:2:endclick: ) :click-incorrect:/:endclick: :click-incorrect:4:endclick:


Once you've submitted your answer for Question 3, click on Question 4 below.


.. reveal:: reveal1
   :showtitle: Question 4
   :hidetitle: Hide Content

   .. clickablearea:: order_of_operations_4
      :question: Click on ALL PARTS of the expression that get evaluated NEXT.  For example, if "1 + 1" gets evaluated first, click on "1", "+", and "1".
      :iscode:
      :feedback: Try again!

      :click-incorrect:1:endclick: :click-incorrect:+:endclick: :click-correct:2:endclick: :click-correct:*:endclick: :click-correct:8:endclick: :click-incorrect:/:endclick: :click-incorrect:4:endclick:


Once you've submitted your answer for Question 4, click on Question 5 below.


.. reveal:: reveal2
   :showtitle: Question 5
   :hidetitle: Hide Content

   .. clickablearea:: order_of_operations_5
      :question: Click on ALL PARTS of the expression that get evaluated NEXT.  For example, if "1 + 1" gets evaluated first, click on "1", "+", and "1".
      :iscode:
      :feedback: Try again!

      :click-incorrect:1:endclick: :click-incorrect:+:endclick: :click-correct:16:endclick: :click-correct:/:endclick: :click-correct:4:endclick:


Once you've submitted your answer for Question 5, click on Question 6 below.


.. reveal:: reveal3
   :showtitle: Question 6
   :hidetitle: Hide Content

   ::

       1 + 5

   is the only operation remaining.  I'm not going to ask you any questions
   about it, I'm just going to ask you to wrap your head around the fact that
   the ``+`` operator appeared **first** in the calculation, but it was the **last**
   operator to be evaluated.  The order of operations can be kind of confusing
   at times, but I think you've got a good grasp of the concept!
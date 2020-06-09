Traversal
---------

A common thing to do with a string is start at the beginning, select
each character in turn, do something to it, and continue until the end.
This pattern of processing is called a **traversal**. A natural way to
encode a traversal is with a ``while`` statement.

.. activecode:: seventhree_
  :language: cpp
  :caption: Accessing a string character

  The active code below outputs each letter of ``fruit``
  using a while loop.
  ~~~~
  #include <string>
  #include <iostream>
  using namespace std;

  int main() {
      int index = 0;
      string fruit = "apple";
      int lengthfruit = fruit.length();
      while (index < lengthfruit) {
          char letter = fruit[index];
          cout << letter << endl;
          index = index + 1;
      }
  }

This loop traverses the string and outputs each letter on a line by
itself. Notice that the condition is ``index < lengthfruit``, which
means that when ``index`` is equal to the length of the string, the
condition is false and the body of the loop is not executed. The last
character we access is the one with the index ``fruit.length()-1``.

The name of the loop variable is ``index``. An **index** is a variable
or value used to specify one member of an ordered set, in this case the
set of characters in the string. The index indicates (hence the name)
which one you want. The set has to be ordered so that each letter has an
index and each index refers to a single character.

As an exercise, write a function that takes an ``string`` as an argument
and that outputs the letters backwards, all on one line.

.. activecode:: seveneight_ 
   :language: cpp

   Try writing the ``reverseWord`` function in the commented section
   of the active code below. If done correctly, the program should output "hello"
   backwards. If you get stuck, you can reveal the extra problem at the end for help. 
   ~~~~
   #include <iostream>
   using namespace std;

   void reverseWord (string word) {
       // ``reverseWord`` should take the letters of ``word``
       // and output them in reverse.
   }

   int main() {
       reverseWord("hello");
   }

.. reveal:: 7_5_1
   :showtitle: Reveal Problem
   :hidetitle: Hide Problem

   .. parsonsprob:: traversal_1
      :numbered: left
      :adaptive:
   
      Let's write the code for the ``reverseWord`` function. ``reverseWord``
      should take a string as a parameter and output the letters backwards.
      -----
      void reverseWord(string input) {
      =====
      int x;
      =====
      for(x=input.length() - 1;x>=0;x--) {
      =====
      for(x=input.length() - 1;x>0;x--) {  #distractor
      =====
      for(x=input.length();x>0;x++) {  #distractor
      =====
      for(x=input.length();x>=0;x++) {  #distractor
      =====
      cout<<input[x];}
      =====
      cout <<input[-x];} #distractor

.. mchoice:: traversal_2
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :correct: b
   :feedback_a: Incorrect, i goes through the odd numbers starting at 1.
   :feedback_b: Yes, i goes through the odd numbers starting at 1.  o is at position 1 and 8.
   :feedback_c: There are 2 o characters but idx does not take on the correct index values for both.


   How many times is the letter o printed by the following statements?

   .. code-block:: cpp

      string s = "coding rocks";
      int i = 1;
      int length = s.length();
      while (i < length) {
        cout << s[i] << endl;
        i = i + 2;
      }

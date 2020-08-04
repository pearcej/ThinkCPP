Mixed Up Code Practice
----------------------

.. parsonsprob:: mucp_6_1
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   The program below should print out the even numbers between 20 and 40 
   but the code is mixed up and contains extra blocks. Put the necessary blocks
   in the correct order.
   -----
   int main() {
   =====
   main(int) {                         #paired
   =====
      int n = 20;
   =====
      int n = 0 #distractor 
   =====
      while (n <= 40) {
   =====
      while (n < 40) {                        #paired 
   =====
         cout << n << endl;
   =====
         n = n + 2;
      }
   }
   =====
         n++;                 #distractor
      }
   }
   =====
         n = n * 2;                 #distractor
      }
   }

.. parsonsprob:: mucp_6_2
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   The program below should count down from 100 to 0 in decrements of 
   10 but the code is mixed up and contains extra blocks. Put the necessary blocks
   in the correct order.
   -----
   int main() {
   =====
      int n = 100;
   =====
      int n = 10 #distractor 
   =====
      while (n >= 0) {
   =====
      while (n < 0) { #distractor
   =====
      while (n > 0) { #distractor
   =====
         cout << n << endl;
   =====
         n -= 10;
      }
   }
   =====
         n += 10;                 #distractor
      }
   }

.. parsonsprob:: mucp_6_3
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   Let's write the code for the ``repeatHello`` function. ``repeatHello`` 
   should be a void function that takes no arguments and uses a while
   loop to print out "hello" three times.  
   -----
   void repeatHello () {
   =====
   repeatHello () {                         #paired
   =====
      int n = 0;
   =====
      int n = 0                        #paired 
   =====
      while (n < 3) {
   =====
      while (n > 3) {                        #paired 
   =====
         cout << "hello" << endl;
   =====
         n++;
      }
   }

.. parsonsprob:: mucp_6_4
   :numbered: left
   :adaptive:

   Now let's generalize the ``repeatHello`` function so that it repeats a given string three times.
   Let's write the code for the ``repeatString`` function, which is a void function that takes 
   a string input as a parameter and uses a while loop to print out the string three times.  
   -----
   void repeatString (string input) {
   =====
   void repeatString () {                         #paired
   =====
      int n = 0;
   =====
      while (n < 3) {
   =====
      while (3 > n) {                        #paired 
   =====
         cout << input << endl;
   =====
         cout << string << endl;                        #paired 
   =====
         n++;
      }
   }

.. parsonsprob:: mucp_6_5
   :numbered: left
   :adaptive:

   We can further generalize ``repeatString`` so that it repeats a given string a given number of times. 
   Let's write the code for the new ``repeatString`` function, which is a void function that takes 
   a string input and an int x as parameters and uses a while loop to print out the string x number of times.  
   -----
   void repeatString (string input, int x) {
   =====
   void repeatString (string input, string x) {                         #paired
   =====
      int n = 0;
   =====
      int n = x;                       #paired
   =====
      while (n < x) {
   =====
      while (x < n) {                        #paired 
   =====
         cout << input << endl;
   =====
         n++; 
      }
   }
   =====
         x++;                       #paired
      }
   }
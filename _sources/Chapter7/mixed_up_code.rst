Mixed Up Code Practice
----------------------

.. parsonsprob:: mucp_7_1
   :numbered: left
   :adaptive:

   Let's write the code for the ``cipherText`` function. ``cipherText`` 
   should be a void function that takes a string input as a parameter,
   increases the value of each character by 1. (i.e. "bad" turns into "cbe"),
   and outputs the encrypted string.
   -----
   void cipherText (string input) {
   =====
   string cipherText (string input) {  #paired
   =====
      for (int i = 0; i < input.length(); ++i) {
   =====
      for (int i = 0; i < input.length() - 1; ++i) {  #paired
   =====
         input[i] = input[i] + 1;
      }
   =====
         input[i] = input[i] - 1;  #paired
      }
   =====
      cout << input;
   }
   =====
      return input;
   }

.. parsonsprob:: mucp_7_2
   :numbered: left
   :adaptive:

   The program below should print out the number of occurences of the character 't'
   in the string tongue_twister but the code is mixed up. Put the necessary blocks 
   in the correct order, with tongue_twister declared before count.
   -----
   int main() {
   =====
      string tongue_twister = "twelve twins twirled twelve twigs";
   =====
      int count = 0;
   =====
      int count = 1;  #paired
   =====
      for (int i = 0; i < tongue_twister.length(); ++i) {
   =====
         if (tongue_twister[i] == 't') {
   =====
         if (tongue_twister[i] = 't') {  #paired
   =====
         count++;
         }
      }
   =====
      cout << count;
   }

.. parsonsprob:: mucp_7_3
   :numbered: left
   :adaptive:

   The program below should print out the index of the second instance of the 
   character 'i' but the code is mixed up and contains extra blocks. 
   Put the necessary blocks in the correct order.
   -----
   int main() {
   =====
      string quote = "Your time is limited, so don't waste it living someone else's life.";
   =====
      for (int i = 0; i < quote.length(); ++i {  #distractor
   =====
      int first = quote.find("i");
   =====
      int index = find (quote, 'i', first + 1);
   =====
      int index = find (quote, 'i', first);  #paired
   =====
      cout << index;
   }
   =====
      cout << first;  #paired
   }

.. parsonsprob:: mucp_7_4
   :numbered: left
   :adaptive:

   Deep in the forest live the 7 dwarves named Sorty, Torty, Vorty,
   Worty, Xorty, Yorty, and Zorty. The program below should print 
   out each of their names but the code is mixed up and contains extra blocks. 
   Put the necessary blocks in the correct order.
   -----
   int main() {
   =====d
      string name = “Sorty”; #distractor
   =====
      string suffix = "orty";
   =====
      char letter = 'S';
   =====
      while (letter <= 'Z') {
   =====
         if (letter != 'U') {
   =====
         if (letter == 'U') {  #paired
   =====
         cout << letter + suffix << endl;
         }
   =====
         letter++;
      }
   }
   =====
         suffix++;  #paired
      }
   }

.. parsonsprob:: mucp_7_5
   :numbered: left
   :adaptive:

   On the strange planet of Noes, there's a law that prohibits the usage of the letter "e". 
   As a result, they hired you to write a function called ``censorE`` that replaces all occurences
   of the letter "e" in a string with an asterisk and returns the censored string. For example, 
   if the input is "hello world", the function returns "h*llo world".
   -----
   string censorE (string input) {
   =====
   void censorE (string input) {  #paired
   =====
      string copy = input;  #distractor
   =====
      for (int i = 0; i < input.length(); ++i) {
   =====
      for (int i = 0; i < input.length() - 1; ++i) {  #paired
   =====
         if (input[i] == 'e') {
   =====
         if (input[i] = 'e') {  #paired
   =====
         input[i] = '*';
         }
      }
   =====
         '*' = input[i];  #paired
         }
      }
   =====
      return input;
   }

.. parsonsprob:: mucp_7_6
   :numbered: left
   :adaptive:

   Your work for the planet of Noes impressed the nearby planets of Noas, Nois, Noos, and Nous.
   They want you to write different functions that censor out each planet's corresponding forbidden letter.
   However, your galaxy brain knows better than to write a different function for each planet.
   Using generalization, write the function ``censorLetter`` which takes a string input and a char to censor 
   as parameters and returns a censored string. For example, censorLetter("Bye world", 'o') returns the
   string "Bye w*rld".
   -----
   string censorLetter (string input, char letter) {
   =====
   string censorLetter (string input) {  #paired
   =====
      for (int i = 0; i < input.length(); ++i) {
   =====
      for (int i = 1; i < input.length(); ++i) {  #paired
   =====
         if (input[i] == letter) {
   =====
         if (input[i] == "letter") {  #paired
   =====
         input[i] = '*';
         }
      }
   =====
         '*' = input[i];  #paired
         }
      }
   =====
      return input;
   }

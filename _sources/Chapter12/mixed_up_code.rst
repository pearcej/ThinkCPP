Mixed Up Code Practice
----------------------

.. parsonsprob:: mucp_12_1
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   Write a program that prints the 4th character of word, 
   and finds and replaces all instances of 'i' with 'e'.
   Finally, print out the string. Put the necessary blocks in the correct order.
   -----
   int main() {
   =====
      string word = "irritating";
   =====
      cout << word[3] << endl;
   =====
      cout << irritating[3] << endl;  #distractor
   =====
      cout << word.at(4) << endl;  #distractor
   =====
      cout << word[4] << endl;  #distractor
   =====
      while ((int)word.find('i') != -1) {
   =====
      while ((int)word.find('e') != -1) {  #distractor
   =====
      while ((int)word.find('i')) {  #distractor
   =====
         word[word.find('i')] = 'e';
   =====
         word[word.find('e')] = 'i';  #distractor
   =====
      }
   =====
      cout << word << endl;
   =====
   }
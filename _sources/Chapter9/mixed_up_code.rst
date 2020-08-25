Mixed Up Code Practice
----------------------

.. parsonsprob:: mucp_9_1
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   Let's write the code for the struct definition of Movie. 
   The Movie structure will have the instance variables title, 
   director, and releaseYear in that order. 
   Put the necessary blocks of code in the correct order.
   -----
   struct Movie {
   =====
   struct movie {  #distractor
   =====
   struct Movie (  #distractor
   =====
      string title;
   =====
      string director;
   =====
      int releaseYear;
   =====
      string releaseYear;  #distractor
   =====
      char title;  #distractor
   =====
   };
   =====
   } #distractor
   =====
   ) #distractor

.. parsonsprob:: mucp_9_2
   :numbered: left
   :adaptive:
   :noindent:

   Let's write the code for the printMovie function. 
   printMovie should print the information about a movie
   in the following format: "title" directed by director (releaseYear).
   Put the necessary blocks of code in the correct order.
   -----
   void printMovie (const Movie& m) {
   =====
   void printMovie (&Movie m const) {  #paired
   =====
   Movie printMovie (Movie m) {  #paired
   =====
      cout << "\"" << m.title << "\" directed by ";
   =====
      cout << m.director << " (" << m.releaseYear << ")" << endl;
   =====
      cout << title << director << releaseYear;  #distractor
   =====
      cout << "\"" << title << "\" directed by ";  #distractor
   =====
      cout << """ << m.title << "" directed by ";  #distractor
   =====
      cout << director << " (" << releaseYear << ")" << endl;  #distractor
   =====
   }

.. parsonsprob:: mucp_9_3
   :numbered: left
   :adaptive:
   :noindent:

   Let's write the code for the movieAge function. 
   movieAge should take a Movie and currentYear as a parameter and
   return how many years it has been since the releaseYear.
   Put the necessary blocks of code in the correct order.
   -----
   int movieAge (const Movie& m, int currentYear) {
   =====
   void movieAge (const Movie& m, int currentYear) {  #distractor
   =====
      return currentYear - m.releaseYear;
   =====
      return currentYear - releaseYear;  #distractor
   =====
      return m.releaseYear - currentYear;  #distractor;
   =====
   }

.. parsonsprob:: mucp_9_4
   :numbered: left
   :adaptive:
   :practice: T

   Let's write the code for the struct definition of Date. 
   The Date structure will have three integer instance variables: day, 
   month, and year in that order. 
   Put the necessary blocks of code in the correct order.
   -----
   struct Date {
   =====
   struct date {  #distractor
   =====
   struct Date (  #distractor
   =====
      int day;
   =====
      int month;
   =====
      int year;
   =====
      string day;  #distractor
   =====
      string month;  #distractor
   =====
      string year;  #distractor
   =====
   };
   =====
   } #distractor
   =====
   ) #distractor

.. parsonsprob:: mucp_9_5
   :numbered: left
   :adaptive:

   Let's write the code for the printDate function. 
   printDate should print the date in the following format: 
   month/date/year.
   Put the necessary blocks of code in the correct order.
   -----
   void printDate (const Date& d) {
   =====
   void printDate (&Date d) {  #paired
   =====
   Date printDate (Date d) {  #paired
   =====
      cout << d.month << "/" << d.day << "/" << d.year << endl;
   =====
      cout << month << "/" << day << "/" << year << endl;  #distractor
   =====
      cout << d.day << "/" << d.month << "/" << d.year << endl;  #distractor
   =====
   }
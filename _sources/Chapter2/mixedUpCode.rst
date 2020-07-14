Mixed-Up Code Exercises
-----------------------

Answer the following **Mixed-Up Code** questions to
assess what you have learned in this chapter.

Parsons (morning)

.. parsonsprob:: vars_types_p1

   Construct a block of code that prints: "Lions &" one the first line,
   "Tigers & Bears!" on the second line, and "Oh my!" on the FOURTH line.

   -----
   int main() {
   =====
    cout << "Lions &" << endl;
   =====
    cout << "Lions &"; #paired
   =====
    cout << "Tigers &";
   =====
    cout << "Tigers &" << endl; #paired
   =====
    cout << " Bears!" << endl;
   =====
    cout << "Bears!" << endl; # paired
   =====
    cout << endl;
   =====
    cout << Oh my!
   =====
   }


.. parsonsprob:: vars_types_p2

   Construct a block of code that swaps the value of integers x 
   and y, which have values 3 and 6, respectively.

   -----
   int main() {
   =====
    int x;
    int y;
   =====
    x = 3;
    y = 6;
   =====
    int x = 3 #distractor
    int y = 6
   =====
    x = 3; #distractor
    y = 6;
   =====
    int temp = x;
   =====
    x = y;
    y = temp;
   =====
    x = y; #distractor
    y = x;
   =====
   }


.. parsonsprob:: vars_types_p3

   Dan Humphrey is a 3.98 student at Constance High School.  His crush's
   first initial is S.  Construct a program that has assigns the variables
    name, GPA, and crush, in that order.

   -----
   int main() {
   =====
    string name = "Dan Humphrey";
   =====
    string name;  #paired
    name = Dan Humphrey;
   =====
    char name = 'Dan Humphrey'; #paired
   =====
    double GPA;
    GPA = 3.98;
   =====
    int GPA = 3.98; #paired
   =====
    int GPA = 3.98 #paired
   =====
    char crush = 'S';
   =====
    char crush = "S"; #paired
   =====
    char crush; #paired
    crush = "S";
   =====
   }


.. parsonsprob:: vars_types_p4

   You decide to make homemade Mac 'n' Cheese for you and your
   roomates.  Whoever wrote the recipe wanted to make things hard
   for you by stating that it calls for 1% of a gallon of milk.
   Construct a block of code that converts this to tablespoons.

   -----
   int main() {
   =====
    double gallons = 0.01;
   =====
    int gallons = 0.01; #paired
   =====
    int gallons = 0.01 #paired
   =====
    double cups = 16 * gallons;
   =====
    double cups; #paired
    16 * gallons = cups;
   =====
    int cups = 16 * gallons; #paired
   =====
    double tbsp;
    tbsp = 16 * cups;
   =====
    double tbsp = 16 * cups #paired
   =====
    int tbsp; #paired
    tbsp = 16 * cups;
   =====
   }


.. parsonsprob:: vars_types_p5

   Construct a block of code that takes the volume of the rectangular
   prism defined by length, width, and height and prints
   the result to the terminal.

   -----
   int main() {
   =====
    int length = 2;
    int width = 3;
    int height = 4;
   =====
    length = 2; #paired
    width = 3;
    height = 4;
   =====
    int volume;
   =====
    volume = height * width * length;
   =====
    int volume = length * width * height #distractor
   =====
    cout << volume;
   =====
    print(volume) #distractor
   =====
    return volume; #distractor
   =====
   }


.. parsonsprob:: vars_types_p6

   Construct a block of code that converts the character 'a' to 'z'
   using a complex set of operations.  Hint: Think about how many
   letters are between 'a' and 'z'.

   -----
   int main() {
   =====
    char a = 'a';
   =====
    char a = "a"; #paired
   =====
    string a = "a"; #paired
   =====
    a = 3 * (9 - 2 * 2) + a + 10;
   =====
    a = a + 1 + 5 * 5; #paired
   =====
    a = 4 * 5 + a - (2 * -3); #paired
   =====
   }


.. parsonsprob:: vars_types_p7

   Construct a block of code that outputs the volume of a cylinder
   with a radius of 3 and a height of 4.  There are many ways to do this using the
   choices below, but only the correct answer that uses the LEAST lines
   of code will be accepted.

   -----
   int main() {
   =====
    cout << 3.14 * 3 * 3 * 4;
   =====
    cout << 3.14 * 3 ^ 2 * 4; #distractor
   =====
    height = 4; #distractor
   =====
    base = 3.14 * 3 * 3; #distractor
   =====
    base = 3.14 * 3 ^ 2; #distractor
   =====
    cout << base * height; #distractor
   =====
    volume = base * height; #distractor
   =====
    cout << volume; #distractor
   }

.. parsonsprob:: vars_types_p8

   Construct a block of code that prints "My favorite class is MATH"
   on the same line.

   -----
   int main() {
   =====
    string favClass = "MATH";
   =====
    string favClass = 'MATH'; #paired
   =====
    string favClass = MATH; #paired
   =====
    cout << "My favorite class is ";
    cout << favClass;
   =====
    cout << "My favorite class is " << endl; #paired
    cout << favClass;
   =====
    cout << "My favorite class is" << favClass; #paired
   =====
   }

.. parsonsprob:: vars_types_p9

   It's Black Friday and the game system you'be been saving up for is marked
   down 60%!  Construct a block of code that calculates how much money
   you'd be saving if the system originally costed $359.99?

   -----
   int main() {
   =====
    double game = 359.99;
   =====
    double game = $359.99; #paired
   =====
    int game = 359.99; #paired
   =====
    double discountPrice = game * 0.60;
   =====
    double discountPrice = game / 0.60; #paired
   =====
    double moneySaved = game - discountPrice;
   =====
    double moneySaved = discountPrice; #paired
   =====
    double moneySaved = game + discountPrice; #paired
   =====
   }


.. parsonsprob:: vars_types_p10

   Your family just bought a dog and everyone has been fighting over
   what to name it.  It went from Champ to Copper to Higgins, and after
   a few days of being Higgins, everyone agreed on Buddy.  Construct
   a block of code that illustrates this concept.

   -----
   int main() {
   =====
    string name = "Champ";
   =====
    string name = 'Champ'; #paired
   =====
    name = "Copper";
   =====
    string name = "Copper"; #paired
   =====
    string newName = "Higgins";
    name = newName;
   =====
    string name = "Higgins"; #paired
   =====
    name = "Buddy";
   =====
    string name = "Buddy"; #paired
   =====
    name = "Buddy": #paired
   =====
   }
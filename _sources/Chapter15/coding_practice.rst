Coding Practice
---------------
.. datafile:: poem.txt
   :fromfile: poem.txt
   :hide:

.. tabbed:: cp_15_1

    .. tab:: Question

        Write a program that takes in an input file called ``poem.txt``
        and prints the first 5 lines to the terminal. Include proper
        file error checking.

        .. activecode:: cp_15_AC_1q
           :language: cpp
           :practice: T
           :datafile: poem.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           // Write your code here.

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            Two roads diverged in a yellow wood,
            And sorry I could not travel both
            And be one traveler, long I stood
            And looked down one as far as I could
            To where it bent in the undergrowth;
            Then took the other, as just as fair,
            And having perhaps the better claim
            Because it was grassy and wanted wear,
            Though as for that the passing there
            Had worn them really about the same,
            And both that morning equally lay
            In leaves no step had trodden black.
            Oh, I kept the first for another day!
            Yet knowing how way leads on to way
            I doubted if I should ever come back.
            I shall be telling this with a sigh
            Somewhere ages and ages hence:
            Two roads diverged in a wood, and I,
            I took the one less traveled by,
            And that has made all the difference.

    .. tab:: Answer

        Below is one way to implement this program. We create an ``ifstream`` object
        to open our file. We check to make sure the file is opened correctly before
        we use ``getline`` in a ``for`` loop to retrieve and print the first 5
        lines of the poem.

        .. activecode:: cp_15_AC_1a
           :language: cpp
           :optional:
           :datafile: poem.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           int main() {
               ifstream infile("poem.txt");
               string input;
               if (!infile.good()) {
                   cout << "Error. Unable to open file." << endl;
                   exit(1);
               } 
               for (int i = 0; i < 5; ++i) {
                   getline(infile, input);
                   cout << input << endl;
               }  
           }

.. datafile:: speech.txt
   :fromfile: speech.txt
   :hide:

.. tabbed:: cp_15_2

    .. tab:: Question

        Write a program that prompts a user for the name of an input file
        and for an integer ``n``. Then open the file and output the first 
        ``n`` lines of the file with each line reversed. For example,
        if you read in the line "hello world" you should print out
        "dlrow olleh" to the terminal. Include proper file error checking.

        .. activecode:: cp_15_AC_2q
           :language: cpp
           :practice: T
           :datafile: poem.txt
           :stdin: speech.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           // Write your code here.

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            We choose to go to the Moon. We choose to go to the Moon...
            We choose to go to the Moon in this decade and do the other things, 
            not because they are easy, but because they are hard; because that goal 
            will serve to organize and measure the best of our energies and skills, 
            because that challenge is one that we are willing to accept, one we are 
            unwilling to postpone, and one we intend to win, and the others, too.

.. datafile:: heights.txt
   :fromfile: heights.txt
   :hide:

.. tabbed:: cp_15_3

    .. tab:: Question

        Write a program that takes in an input file called ``heights.txt,``
        finds the median of the data, and prints 
        "The median height is: ``height`` inches" to the terminal. 
        Include proper file error checking.

        .. activecode:: cp_15_AC_3q
           :language: cpp
           :practice: T
           :datafile: heights.txt

           #include <iostream>
           #include <fstream>
           #include <vector>
           #include <algorithm>
           using namespace std;

           // Write your code here.

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            62	67	75	68	65
            67	70	72	74	66
            72	66	66	73	69
            61	60	73	72	60

    .. tab:: Answer

        Below is one way to implement this program. We create an ``ifstream`` object
        to open our file. We check to make sure the file is opened correctly before
        we read the data values into a vector. After sorting the vector, we find
        the median depending on whether the number of data values was even or odd.
        Finally, we output our result to the terminal.

        .. activecode:: cp_15_AC_3a
           :language: cpp
           :optional:
           :datafile: heights.txt

           #include <iostream>
           #include <fstream>
           #include <vector>
           #include <algorithm>
           using namespace std;

           int main() {
               ifstream infile("heights.txt");
               vector<int> data;
               double median;
               int height;
               if (!infile.good()) {
                   cout << "Error. Unable to open file." << endl;
                   exit(1);
               } 
               while (infile >> height) {
                   data.push_back(height);
               }
               sort(data.begin(), data.end());
               if (data.size() % 2 == 0) { 
                   median = (data[data.size() / 2 - 1] + data[data.size() / 2]) / 2.0;
               }
               else {
                   median = data[data.size() / 2];
               }
               cout << "The median height is: " << median << " inches" << endl;  
           }

.. datafile:: powers.txt
   :fromfile: powers.txt
   :hide:

.. activecode:: cp_15_AC_4q
    :language: cpp
    :practice: T
    :datafile: powers.txt

    Write a program that prompts a user for an integer ``n`` and print the first ``n``
    powers of 2 to an output file called ``powers.txt``. Include proper file error checking.
    To simulate what your output file would look like, the contents of your output file 
    will be displayed on the terminal.
    ~~~~
    #include <iostream>
    #include <fstream>
    using namespace std;

    int main() { 
        // Write your code here.





        // Do not modify the code below
        ifstream student_output("powers.txt");
        if (!student_output.good()) {
            cout << "Error opening student's output." << endl;
        }
        string answer;
        while (getline(student_output, answer)) {
            cout << answer << endl;
        }
    }

.. datafile:: message.txt
   :fromfile: message.txt
   :hide:

.. tabbed:: cp_15_5

    .. tab:: Question

        ROT13 is a simple Caesar cipher that replaces each letter in a string
        with the 13th letter after it in the alphabet. For example, using ROT13
        on the letter "a" would turn it into "n". Notice how since 13 is exactly
        half the number of characters in the alphabet, using ROT13 on the letter
        "n" would turn it into "a". Thus, ROT13 can be used to encrypt and decrypt
        messages. Write a program that takes in an input file called ``message.txt,``
        applies ROT13, and outputs the result to the terminal. 
        Include proper file error checking.

        .. activecode:: cp_15_AC_5q
           :language: cpp
           :practice: T
           :datafile: message.txt

           #include <iostream>
           #include <fstream>
           #include <ctype.h>
           using namespace std;

           int main() { 
               // Write your code here.
           }

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            Can you encrypt this message and decrypt the message below?
            Pbatenghyngvbaf! Lbh'ir qrpelcgrq guvf zrffntr.

    .. tab:: Answer

        Below is one way to implement this program. We create an ``ifstream`` object
        to open our file. We check to make sure the file is opened correctly before
        we read the data values into a string. We call our ``ROT13`` function and
        output the result to the output file. 

        .. activecode:: cp_15_AC_5a
           :language: cpp
           :optional:
           :datafile: message.txt

           #include <iostream>
           #include <fstream>
           #include <ctype.h>
           using namespace std;

           string ROT13 (string message) {
               for (size_t i = 0; i < message.size(); ++i) {
                   if (isalpha(message[i])) {
                       if (message[i] >= 'A' && message[i] <= 'Z') {
                           if (message[i] <= 'M') {
                               message[i] = message[i] + 13;
                           }
                           else {
                               message[i] = message[i] - 13;
                           }
                       }
                       else {
                            if (message[i] <= 'm') {
                               message[i] = message[i] + 13;
                           }
                           else {
                               message[i] = message[i] - 13;
                           }
                       }
                   }
               }
               return message;
           }

           int main() { 
               ifstream infile("message.txt");
               string message;
               if (!infile.good()) {
                   cout << "Error. Unable to open file." << endl;
                   exit(1);
               } 
               while (getline(infile, message)) {
                   cout << ROT13(message) << endl;
               }
           }

.. datafile:: dream.txt
   :fromfile: dream.txt
   :hide:        

.. tabbed:: cp_15_6

    .. tab:: Question

        Write a program that takes an input file called "dream.txt" and outputs
        the number of times the string "you" appears in the file to the terminal.
        Include proper file error checking.

        .. activecode:: cp_15_AC_6q
           :language: cpp
           :practice: T
           :datafile: dream.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           // Write your code here.

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            Have you ever had a dream that you, 
            um, you had, your, you- you could, 
            you’ll do, you- you wants, you, you 
            could do so, you- you’ll do, you could- 
            you, you want, you want them to do you 
            so much you could do anything?

.. datafile:: class_data.txt
   :fromfile: class_data.txt
   :hide:

.. tabbed:: cp_15_7

    .. tab:: Question

        Write a program that reads in data about a class from the file
        ``class_data.txt`` and outputs the rows of data where a
        student has a GPA of at least 3.5. Include proper file error checking.

        .. activecode:: cp_15_AC_7q
           :language: cpp
           :practice: T
           :datafile: class_data.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           int main() { 
               // Write your code here.
           }

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            First    Last       Grade    GPA    Age
            Alex     Jones      9        3.4    14
            Beth     Hamilton   12       3.7    18
            Charles  White      11       3.5    16
            Daniel   Kim        10       3.8    16
            Ethan    Brooks     11       3.9    17
            Faith    Flemmings  10       3.0    15
            Gina     Zhou       9        3.2    14       

    .. tab:: Answer

        Below is one way to implement this program. We create an ``ifstream`` object
        to open our file. We check to make sure the file is opened correctly before
        we read the data values into corresponding variables. We check if the GPA 
        is at least 3.5, and print the data values to the terminal if so.

        .. activecode:: cp_15_AC_7a
           :language: cpp
           :optional:
           :datafile: class_data.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           int main() { 
               ifstream infile("class_data.txt");
               string fname, lname;
               int grade, age;
               double gpa;
               if (!infile.good()) {
                   cout << "Error. Unable to open file." << endl;
                   exit(1);
               } 
               getline(infile, fname);
               while (infile >> fname >> lname >> grade >> gpa >> age) {
                   if (gpa >= 3.5) {
                       cout << fname << '\t' << lname << '\t' << grade
                            << '\t' << gpa << '\t' << age << endl;
                   }
               }
           }     

.. datafile:: shrimp.txt
   :fromfile: shrimp.txt
   :hide:

.. tabbed:: cp_15_8

    .. tab:: Question

        Write a program that takes an input file called "shrimp.txt" and outputs
        the quote with "shrimp" replaced by a word that the user inputs to the terminal.
        Include proper file error checking.

        .. activecode:: cp_15_AC_8q
           :language: cpp
           :practice: T
           :datafile: shrimp.txt

           #include <iostream>
           #include <fstream>
           using namespace std;

           // Write your code here.

    .. tab:: Input File

        Below are the contents of the input file.

        ::

            There's pineapple shrimp, lemon shrimp, coconut shrimp, 
            pepper shrimp, shrimp soup, shrimp stew, shrimp salad, 
            shrimp and potatoes, shrimp burger, shrimp sandwich. 
            That- that's about it.

.. datafile:: mult_table.txt
   :fromfile: mult_table.txt
   :hide:

.. tabbed:: cp_15_9

    .. tab:: Question

        Write a program that creates a multiplication table for the first 10
        numbers using a matrix and outputting the table to an output file
        called ``mult_table.txt``. Include proper file error checking.

        .. activecode:: cp_15_AC_9q
           :language: cpp
           :practice: T
           :datafile: mult_table.txt

           #include <iostream>
           #include <fstream>
           #include <vector>
           using namespace std;

           int main() { 
               // Write your code here.
           }  

    .. tab:: Answer

        Below is one way to implement this program. We create a 10x10 matrix
        and fill in the products. Then we traverse through the matrix and output
        the values into the output file.

        .. activecode:: cp_15_AC_9a
           :language: cpp
           :optional:
           :datafile: mult_table.txt

           #include <iostream>
           #include <fstream>
           #include <vector>
           using namespace std;

           int main() { 
               ofstream outfile("mult_table.txt");
               if (!outfile.good()) {
                   cout << "Error. Unable to open file." << endl;
                   exit(1);
               } 
               vector<int> rows(10);
               vector<vector<int> > mat;
               for (int i = 0; i < 10; ++i) {
                   mat.push_back(rows);
               }
               for (int i = 0; i < 10; ++i) {
                   for (int j = 0; i < 10; ++j) {
                       matrix[i][j] = (i + 1) * (j + 1);
                   }
               }
               for (int i = 0; i < 10; ++i) {
                   for (int j = 0; i < 10; ++j) {
                       outfile << matrix[i][j] << '\t';
                   }
                   cout << endl;
               }
           }

.. activecode:: cp_15_AC_10q
    :language: cpp
    :practice: T

    Write a program that computes the product of two matrices.
    Take a look at the example below. Two find the product of two
    matrices, take the ith row from the first matrix and the jth column
    from the second matrix, find the summation of the product of each component,
    and that's the value that goes into the (i, j) location of the new matrix.
    The product of an mxn and an nxp matrix is an mxp matrix.
    ~~~~
    #include <iostream>
    #include <fstream>
    using namespace std;

    int main() { 
        /*
          2x3 matrix A  X 3x2 matrix B                2x2 matrix C      
        [ a    b    c ]    [ g    h ]       [ ag + bi + cl    ah + bj + cm ]
        [ d    e    f ]    [ i    j ]   =   [ dg + ei + fl    ah + ej + fm ]
                           [ l    m ]
        */
        
        // Write your code here.
    }
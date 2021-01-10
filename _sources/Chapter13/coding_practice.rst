Coding Practice
---------------

.. tabbed:: cp_13_1

    .. tab:: Question

        Create the enumerated type Planet, which maps the planets in our solar system to integers
        starting at 1. Make sure to list the planets out in order! (Sadly, Pluto is not a planet :( )

        .. activecode:: cp_13_AC_1q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           // Write your code for the enumerated type Planet.

    .. tab:: Answer

        Below is one way to implement the program. The planets in our solar system
        are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.

        .. activecode:: cp_13_AC_1a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           enum Planet { MERCURY = 1, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE };

.. activecode:: cp_13_AC_2q
    :language: cpp

    How long is a year on other planets? Let's write a program that prints out the number of days
    in a year on each planet using a switch statement. These values are, in planetary order,
    88 days, 225 days, 365 days, 687 days, 4333 days, 10759 days, 30687 days, and 60190 days.
    Print out this information in the following format: Planet ``planet`` has ``numDays`` number of days in
    a year!
    ~~~~
    #include <iostream>
    using namespace std;

    enum Planet { MERCURY = 1, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE };

    int main() {
        Planet p = JUPITER;
        // Write your code here.
    }

.. tabbed:: cp_13_3

    .. tab:: Question

        A Bingo board has 25 Spaces in a matrix-like grid. A Space has a number value randomly selected from 1 to 75 and can
        either be filled or not. Write the struct definitions for ``Space`` and ``BingoBoard``.

        .. activecode:: cp_13_AC_3q
           :language: cpp
           :practice: T

           #include <iostream>
           #include <vector>
           using namespace std;

           // Write your code for the struct Space here.

           // Write your code for the struct BingoBoard here.

    .. tab:: Answer

        Below is one way to implement the program. We declare the ``Space`` and ``BingoBoard`` struct
        and create the instance variables in order. Make sure to set ``is_filled`` to ``false``!

        .. activecode:: cp_13_AC_3a
           :language: cpp
           :optional:

           #include <iostream>
           #include <vector>
           using namespace std;

           struct Space {
               int value;
               bool is_filled;
           };

           struct BingoBoard {
               vector<vector<Space> > board;
           };

.. activecode:: cp_13_AC_4q
    :language: cpp

    Now let's generate a ``BingoBoard``! We want to fill the 25 ``Space``\s on the ``BingoBoard`` with
    random values from 1 to 75 without repititon. To do this, we'll make a ``vector``
    of numbers from 1 to 75 and shuffle it using the same method as shown in this chapter. Then
    we will select the first 25 values for the 25 spaces on the ``BingoBoard``. We will
    do this entire process in multiple steps. First, write the function ``randomInt``, which
    generates a random value between low and high, inclusive. Be sure to include the relevant libraries!
    ~~~~
    #include <iostream>
    // Add any relevant libraries here.
    using namespace std;

    // Write your code for the randomInt function here.

.. tabbed:: cp_13_5

    .. tab:: Question

        Now we need a way to swap the values at two indices in a vector. Write the function ``swapValues``,
        which takes a ``vector`` of ``int``\s and two indices as parameters.

        .. activecode:: cp_13_AC_5q
           :language: cpp
           :practice: T

           #include <iostream>
           #include <vector>
           using namespace std;

           // Write your code for the swapValues function here.

    .. tab:: Answer

        Below is one way to implement the program. We store the value at ``index1`` in a ``temp``
        variable, replace the value at ``index1`` with the value at ``index2``, and then finally
        replace the value at ``index2`` with the value of ``temp``. Make sure to pass
        ``vec`` by reference!

        .. activecode:: cp_13_AC_5a
           :language: cpp
           :optional:

           #include <iostream>
           #include <vector>
           using namespace std;

           void swapValues (vector<int> &vec, int index1, int index2) {
               int temp = vec[index1];
               vec[index1] = vec[index2];
               vec[index2] = temp;
           }

.. activecode:: cp_13_AC_6q
    :language: cpp

    Now that we have the functions ``randomInt`` and ``swapValues``, we can write the function
    ``generateRandVec``. ``generateRandVec`` creates a ``vector`` with values from 1 to 75,
    shuffles it using ``randomInt`` and ``swapValues``, and returns the shuffled ``vector``.
    ~~~~
    #include <iostream>
    #include <vector>
    #include <cstdlib>
    #include <numeric>
    using namespace std;

    // Write your code for the generateRandVec function here.

.. tabbed:: cp_13_7

    .. tab:: Question

        We can now fill our ``BingoBoard`` with values! Write the ``BingoBoard``
        member function ``makeBoard``. Use the ``generateRandVec``
        function and select the first 25 values to fill up the board. Make sure
        to create a free space in the middle of the board! Set the value of the
        free space to 0 and ``is_filled`` to ``true``.  All other
        spaces should have ``is_filled`` set to ``false``. 

        .. activecode:: cp_13_AC_7q
           :language: cpp
           :practice: T

           #include <iostream>
           #include <vector>
           #include <cstdlib>
           #include <numeric>
           using namespace std;

           struct Space {
               int value;
               bool is_filled;
           };

           struct BingoBoard {
               vector<vector<Space> > board;
               void makeBoard ();
           };

           int randomInt (int low, int high);
           void swapValues (vector<int> &vec, int index1, int index2);
           vector<int> generateRandVec ();

           // Write your code for the makeBoard function here.
           ====
           int randomInt(int low, int high) {
               srand(time(NULL));
               int x = random();
               int y = x % (high - low + 1) + low;
               return y;
           }

           void swapValues(vector<int> &vec, int index1, int index2) {
               int temp = vec[index1];
               vec[index1] = vec[index2];
               vec[index2] = temp;
           }

           vector<int> generateRandVec() {
               vector<int> vec(75);
               iota(vec.begin(), vec.end(), 1);
               for (size_t i = 0; i < vec.size(); ++i) {
                   int x = randomInt(i, vec.size() - 1);
                   swapValues(vec, i, x);
               }
               return vec;
           }

    .. tab:: Answer

        Below is one way to implement the program. First we need to initialize
        the board to the correct dimensions. Then, we use ``generateRandVec``
        to create a ``vector`` of random values from 1 to 75. Afterwards, we set
        the values of the 25 ``Space``\s to the first 25 values in the
        random ``vector``. Lastly, we set the middle ``Space`` to 0 and
        set its ``is_filled`` to ``true``.

        .. activecode:: cp_13_AC_7a
           :language: cpp
           :optional:

           #include <iostream>
           #include <vector>
           #include <cstdlib>
           #include <numeric>
           using namespace std;

           struct Space {
               int value;
               bool is_filled;
           };

           struct BingoBoard {
               vector<vector<Space> > board;
               void makeBoard ();
           };

           int randomInt (int low, int high);
           void swapValues (vector<int> &vec, int index1, int index2);
           vector<int> generateRandVec ();

           void BingoBoard::makeBoard() {
               // Initialize board
               Space s = {0, false};
               vector<Space> cols(5, s);
               for (size_t i = 0; i < 5; ++i) {
                   board.push_back(cols);
               }

               // Fill board with random values
               vector<int> vec = generateRandVec();
               int count = 0;
               for (size_t row = 0; row < board.size(); ++row) {
                   for (size_t col = 0; col < board[row].size(); ++col) {
                   board[row][col].value = vec[count];
                   ++count;
                   }
               }

               // Create free space
               board[2][2].value = 0;
               board[2][2].is_filled = true;
           }
           ====
           int randomInt(int low, int high) {
               srand(time(NULL));
               int x = random();
               int y = x % (high - low + 1) + low;
               return y;
           }

           void swapValues(vector<int> &vec, int index1, int index2) {
               int temp = vec[index1];
               vec[index1] = vec[index2];
               vec[index2] = temp;
           }

           vector<int> generateRandVec() {
               vector<int> vec(75);
               iota(vec.begin(), vec.end(), 1);
               for (size_t i = 0; i < vec.size(); ++i) {
                   int x = randomInt(i, vec.size() - 1);
                   swapValues(vec, i, x);
               }
               return vec;
           }

.. activecode:: cp_13_AC_8q
    :language: cpp

    Let's print out our ``BingoBoard``! Write the ``BingoBoard`` member function
    ``printBoard``. Insert tabs between each value in each row to make the board
    print out neater.
    ~~~~
    #include <iostream>
    #include <vector>
    #include <cstdlib>
    #include <numeric>
    using namespace std;

    struct Space {
        int value;
        bool is_filled;
    };

    struct BingoBoard {
        vector<vector<Space> > board;
        void makeBoard ();
        void printBoard ();
    };

    int randomInt (int low, int high);
    void swapValues (vector<int> &vec, int index1, int index2);
    vector<int> generateRandVec ();

    // Write your code for the printBoard function here.

    int main() {
        BingoBoard bingo;
        bingo.makeBoard ();
        bingo.printBoard ();
    }
    ====
    int randomInt(int low, int high) {
        srand(time(NULL));
        int x = random();
        int y = x % (high - low + 1) + low;
        return y;
    }

    void swapValues(vector<int> &vec, int index1, int index2) {
        int temp = vec[index1];
        vec[index1] = vec[index2];
        vec[index2] = temp;
    }

    vector<int> generateRandVec() {
        vector<int> vec(75);
        iota(vec.begin(), vec.end(), 1);
        for (size_t i = 0; i < vec.size(); ++i) {
            int x = randomInt(i, vec.size() - 1);
            swapValues(vec, i, x);
        }
        return vec;
    }

    void BingoBoard::makeBoard() {
        // Initialize board
        Space s = {0, false};
        vector<Space> cols(5, s);
        for (size_t i = 0; i < 5; ++i) {
            board.push_back(cols);
        }

        // Fill board with random values
        vector<int> vec = generateRandVec();
        int count = 0;
        for (size_t row = 0; row < board.size(); ++row) {
            for (size_t col = 0; col < board[row].size(); ++col) {
            board[row][col].value = vec[count];
            ++count;
            }
        }

        // Create free space
        board[2][2].value = 0;
        board[2][2].is_filled = true;
    }

.. tabbed:: cp_13_9

    .. tab:: Question

        Bubble sort is a method of sorting that involves repeatedly swapping the
        adjacent elements if they are in the wrong order. For example, let's say
        we have the ``vector`` with elements {3, 2, 4, 1}. On the first pass, we take
        a look at the first two elements, 3 and 2. Since 3 is bigger than 2, we swap them.
        Thus, the ``vector`` now looks like {2, 3, 4, 1}. Next, we look at the next two
        elements, 3 and 4. Since 3 is less than 4, we don't swap. Lastly, we look at
        the last two elements, 4 and 1. Since 4 is greater than 1, we swap the.
        Thus the ``vector`` now looks like {2, 3, 1, 4}. Now we restart and look at the
        first two elements again and the process continues. This way, the biggest elements
        "bubble" to the back. Write the function ``bubbleSort``,
        which takes a ``vector`` as a parameter and sorts it. Feel free to use the provided
        ``swapValues`` function.

        .. activecode:: cp_13_AC_9q
           :language: cpp
           :practice: T

           #include <iostream>
           #include <vector>
           using namespace std;

           void swapValues(vector<int> &vec, int index1, int index2) {
               int temp = vec[index1];
               vec[index1] = vec[index2];
               vec[index2] = temp;
           }

           // Write your code for the bubbleSort function here.

           int main() {
               vector<int> vec = { 5, 1, 4, 2, 8 };
               bubbleSort (vec);
               for (size_t i = 0; i < vec.size(); ++i) {
                   cout << vec[i] << " ";
               }
           }

    .. tab:: Answer

        Below is one way to implement the program. We must loop through all elements
        in the vector. Since we know the last ``i`` elements are already in place,
        our inner loop only goes up to ``vec.size() - 1 - i``. If the next element
        is greater than the current element, we swap the two elements.

        .. activecode:: cp_13_AC_9a
           :language: cpp
           :optional:

           #include <iostream>
           #include <vector>
           using namespace std;

           void swapValues(vector<int> &vec, int index1, int index2) {
               int temp = vec[index1];
               vec[index1] = vec[index2];
               vec[index2] = temp;
           }

           void bubbleSort(vector<int> &vec) {
               for (size_t i = 0; i < vec.size() - 1; ++i) {
                   for (size_t j = 0; j < vec.size() - 1 - i; ++j) {
                       if (vec[j] > vec[j + 1]) {
                           swapValues(vec, j, j + 1);
                       }
                   }
               }
           }

           int main() {
               vector<int> vec = { 5, 1, 4, 2, 8 };
               bubbleSort (vec);
               for (size_t i = 0; i < vec.size(); ++i) {
                   cout << vec[i] << " ";
               }
           }

.. activecode:: cp_13_AC_10q
    :language: cpp

    You may have noticed that in some cases, our version of ``bubbleSort`` does
    an unnecessary amount of work. For example, if our ``vector`` was {1, 2, 3, 5, 4},
    ``bubbleSort`` would swap 4 and 5, but then keep going even though our ``vector``
    is already in order! We can save some work by including a ``bool`` called ``is_changed``.
    If we swap values during a pass, we set ``is_changed`` to true. If nothing has been swapped,
    then ``is_changed`` stays false, and we know to break out of the loop since our ``vector``
    is already sorted. Write the function ``fastBubbleSort``, which is ``bubbleSort`` with this
    modification.
    ~~~~
    #include <iostream>
    #include <vector>
    using namespace std;

    void swapValues(vector<int> &vec, int index1, int index2) {
        int temp = vec[index1];
        vec[index1] = vec[index2];
        vec[index2] = temp;
    }

    // Write your code for the fastBubbleSort function here.

    int main() {
        vector<int> vec = { 1, 3, 5, 4, 6, 8, 9 };
        fastBubbleSort (vec);
        for (size_t i = 0; i < vec.size(); ++i) {
            cout << vec[i] << " ";
        }
    }

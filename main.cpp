#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
bool isPlayerWinner(const std::vector<int>& choices) {
    if (choices.size() < 3) {
        return false;
    }

    for (size_t k = 0; k < choices.size(); ++k) {
        for (size_t l = k + 1; l < choices.size(); ++l) {
            for (size_t m = l + 1; m < choices.size(); ++m) {
                if (choices[k] + choices[l] + choices[m] == 15) {
                    return true;
                }
            }
        }
    }

    return false;
}

int main() {
    std::cout << "** HELLO IN NUMBER SCRABBLE **\n";
    std::cout << "** To win you must collect three numbers whose sum = 15 **\n\n";

    // main vector
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    // First vector to contain choices of player 1
    std::vector<int> numberList1;

    // Second vector to contain choices of player 2
    std::vector<int> numberList2;

    // let’s start the game
    std::cout << "-- LET'S START THE GAME ^.^ --\n";
    while (true) {
        // PLAYER 1:
        // 1) Show the main vector to player 1 to choose number
        std::cout << "\nThe main vector you have to choose from: ";
        for (const auto& number : numbers) {
            std::cout << number << " ";
        }
        std::cout << std::endl;

        // 2) Show player’s 1 choices
        if (!numberList1.empty()) {
            std::cout << "-> Your last choices: ";
            for (const auto& choice : numberList1) {
                std::cout << choice << " ";
            }
            std::cout << std::endl;
        }

        // 3) Get choices from player 1 and check if it's a numeric value or not
        int number;
        while (true) {
            std::cout << "-> PLAYER 1: Choose a number from the main list: ";
            if (std::cin >> number) {
                break;
            } else {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "\n** Invalid input. Please enter a numeric value **\n";
            }
        }

        // 4) Check if input number is in the main vector
        auto it = std::find(numbers.begin(), numbers.end(), number);
        if (it == numbers.end()) {
            std::cout << "\n* INVALID choice. Try again *\n";
            continue;
        }

        // 5) Remove choices of player 1 from the main vector
        numbers.erase(it);

        // 6) Add choices of player 1 to the list of player 1’s choices
        numberList1.push_back(number);

        // 7) Check if player 1 wins
        if (isPlayerWinner(numberList1)) {
            std::cout << "\n** player 1 wins **\n";
            std::cout << "------------------------------\n";
            std::cout << "   ** THE GAME IS FINISHED **\n";
            std::cout << "------------------------------\n";
            break;
        }

        // 8) Check if the game is a draw
        if (numbers.empty()) {
            std::cout << "=======================\n THE GAME IS A DRAW!\n=======================\n";
            break;
        }

        //--------------------------------------------------------------------------
        // PLAYER 2:
        // 1) Show the main vector to player 2 to choose number
        std::cout << "\nThe main vector you have to choose from: ";
        for (const auto& number : numbers) {
            std::cout << number << " ";
        }
        std::cout << std::endl;

        // 2) Show player’s 2 choices
        if (!numberList2.empty()) {
            std::cout << "-> Your last choices: ";
            for (const auto& choice : numberList2) {
                std::cout << choice << " ";
            }
            std::cout << std::endl;
        }

        // 3) Get choices from player 2 and check if it's a numeric value or not
        while (true) {
            std::cout << "-> PLAYER 2: Choose a number from the main list: ";
            if (std::cin >> number) {
                break;
            } else {
                std::cout.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "\n** Invalid input. Please enter a numeric value **\n";
            }
        }

        // 4) Check if input number is in the main vector
        it = std::find(numbers.begin(), numbers.end(), number);
        while (it == numbers.end()) {
            std::cout << "\n* INVALID choice. Try again *\n";
            std::cout << "\nAvailable numbers: ";
            for (const auto& number : numbers) {
                std::cout << number << " ";
            }
            std::cout << std::endl;
            std::cout << "-> PLAYER 2: Choose a number from the main list: ";
            std::cin >> number;
            it = std::find(numbers.begin(), numbers.end(), number);
        }

        // 5) Remove choices of player 2 from the main vector
        numbers.erase(it);

        // 6) Add choices of player 2 to the list of player 2’s choices
        numberList2.push_back(number);

        // 7) Check if player 2 wins
        if (isPlayerWinner(numberList2)) {
            std::cout << "\n** player 2 wins **\n";
            std::cout << "------------------------------\n";
            std::cout << "   ** THE GAME IS FINISHED **\n";
            std::cout << "------------------------------\n";
            break;
        }

        // 8) Check if the game is a draw
        if (numbers.empty()) {
            std::cout << "=======================\n THE GAME IS A DRAW!\n=======================\n";
            break;
        }
    }

    return 0;
}
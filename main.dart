void main() {
  // Declare and initialize variables
  int age = 25;
  double height = 1.75;
  String name = "Alice";
  bool isStudent = true;
  List<int> numbers = [1, 2, 3, 4, 5];
}


void convertAndDisplay(String numberString) {
  // Convert the string to an integer and double
  int numberInt = int.parse(numberString);
  double numberDouble = double.parse(numberString);

  // Print the results
  print("Integer: $numberInt");
  print("Double: $numberDouble");
}

void checkNumber(int number) {
  if (number > 0) {
    print("$number is positive.");
  } else if (number < 0) {
    print("$number is negative.");
  } else {
    print("$number is zero.");
  }
}

void   
 checkEligibility(int age) {
  if (age >= 18) {
    print("You are eligible to vote.");
  } else {
    print("You are not eligible to vote yet.");
  }
}

void printDay(int day) {
  switch (day) {
    case 1:
      print("Monday");
      break;
    case 2:
      print("Tuesday");
      break;
    // ... other cases
    default:
      print("Invalid day");
  }
}

// For loop
for (int i = 1; i <= 10; i++) {
  print(i);
}

// While loop
int j = 10;
while (j >= 1) {
  print(j);
  j--;
}

// Do-while loop
int k = 1;
do {
  print(k);
  k++;
} while (k <= 5);

void analyzeNumbers(List<int> numbers) {
  for (int number in numbers) {
    print(number);

    if (number % 2 == 0) {
      print("$number is even.");
    } else {
      print("$number is odd.");
    }

    if (number <= 10) {
      print("$number is small.");
    } else if (number <= 100) {
      print("$number is medium.");
    } else {
      print("$number is large.");
    }
  }
}
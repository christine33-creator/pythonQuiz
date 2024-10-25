from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Define the trivia questions
questions = [
    {
        "question": "What is the correct way to print 'Hello, World!' in Python?",
        "choices": [
            "echo('Hello, World!')",
            "print('Hello, World!')",
            "console.log('Hello, World!')",
            "System.out.print('Hello, World!')"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "Which of the following is NOT a valid variable name in Python?",
        "choices": [
            "my_var",
            "2cool",
            "_hidden",
            "myVar"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "What will 3 // 2 output in Python?",
        "choices": [
            "1.5",
            "1",
            "2",
            "1.0"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "What is the output of len('Hello')?",
        "choices": [
            "4",
            "5",
            "6",
            "Error"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "What does list(range(3)) return?",
        "choices": [
            "[1, 2, 3]",
            "[0, 1, 2, 3]",
            "[0, 1, 2]",
            "Error"
        ],
        "answer": 2,
        "level": "Beginner"
    },
    {
        "question": "What type of loop should you use if you know how many times to iterate?",
        "choices": [
            "while",
            "for",
            "if",
            "def"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "What is the output of print('Python'[0])?",
        "choices": [
            "Python",
            "P",
            "y",
            "0"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "In Python, what is the value of 3 ** 3?",
        "choices": [
            "6",
            "9",
            "27",
            "8"
        ],
        "answer": 2,
        "level": "Beginner"
    },
    {
        "question": "What is the correct syntax for defining a function in Python?",
        "choices": [
            "function myFunction():",
            "def myFunction():",
            "myFunction func():",
            "def function myFunction():"
        ],
        "answer": 1,
        "level": "Beginner"
    },
    {
        "question": "What will be the output of this code snippet?",
        "code": "my_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)",
        "choices": [
            "[1, 2, 3, 4]",
            "[4, 1, 2, 3]",
            "[1, 2, 3]",
            "Error"
        ],
        "answer": 0,
        "level": "Beginner"
    },
    {
        "question": "What is the output of the following code?",
        "code": "x = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
        "choices": [
            "[1, 2, 3, 4]",
            "[1, 2, 3]",
            "Error",
            "None"
        ],
        "answer": 0,
        "level": "Intermediate"
    },
    {
        "question": "Find the bug:",
        "code": "def add_numbers(a, b)\n    return a + b",
        "hint": "Check the function definition syntax.",
        "answer": "There should be a colon at the end of the function definition: def add_numbers(a, b):",
        "level": "Intermediate"
    },
    {
        "question": "What is the output of this code?",
        "code": "my_list = ['apple', 'banana', 'cherry']\nprint(my_list[1])",
        "choices": [
            "apple",
            "banana",
            "cherry",
            "Error"
        ],
        "answer": 1,
        "level": "Intermediate"
    },
    {
        "question": "What will be the output of the following code?",
        "code": "x = 10\nif x > 5:\n    print('x is greater than 5')\nelif x == 5:\n    print('x is 5')\nelse:\n    print('x is less than 5')",
        "answer": "x is greater than 5",
        "level": "Intermediate"
    },
    {
        "question": "What is a lambda function in Python?",
        "choices": [
            "A function defined with lambda keyword that can take multiple expressions.",
            "A single-expression function created with the lambda keyword.",
            "A function defined by the def keyword.",
            "None of the above."
        ],
        "answer": 1,
        "level": "Intermediate"
    },
    {
        "question": "What does the following code print?",
        "code": "def func(x, y=[]):\n    y.append(x)\n    return y\n\nprint(func(1))\nprint(func(2))\nprint(func(3, []))",
        "answer": "[1], [1, 2], [3] (The list y is mutable, so it keeps state across calls if not explicitly reset.)",
        "level": "Intermediate"
    },
    {
        "question": "What is the output of this code?",
        "code": "nums = [1, 2, 3, 4]\nprint([n**2 for n in nums if n % 2 == 0])",
        "answer": "[4, 16]",
        "level": "Intermediate"
    },
    {
        "question": "Which of the following is used to handle exceptions in Python?",
        "choices": [
            "try",
            "except",
            "finally",
            "All of the above"
        ],
        "answer": 3,
        "level": "Intermediate"
    },
    {
        "question": "What will be the output of this code?",
        "code": "def outer():\n    x = 'local'\n    def inner():\n        nonlocal x\n        x = 'nonlocal'\n        print('inner:', x)\n    inner()\n    print('outer:', x)\n\nouter()",
        "answer": "inner: nonlocal\nouter: nonlocal",
        "level": "Advanced"
    },
    {
        "question": "What does the @staticmethod decorator do in a class?",
        "choices": [
            "Makes a method into a class method.",
            "Allows a method to be called on an instance without self.",
            "Allows a method to be called on the class without any instance.",
            "None of the above."
        ],
        "answer": 2,
        "level": "Advanced"
    },
    {
        "question": "What will this code output?",
        "code": "def fib(n, cache={}):\n    if n in cache:\n        return cache[n]\n    if n < 2:\n        return n\n    result = fib(n-1) + fib(n-2)\n    cache[n] = result\n    return result\n\nprint(fib(5))",
        "answer": "5 (This is a recursive Fibonacci function with caching.)",
        "level": "Advanced"
    },
    {
        "question": "What will the following code print?",
        "code": "import itertools\nresult = list(itertools.permutations([1, 2, 3]))\nprint(result)",
        "answer": "[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]",
        "level": "Advanced"
    },
    {
        "question": "Find the bug:",
        "code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\nprint(factorial(-1))",
        "hint": "Factorials are undefined for negative numbers.",
        "answer": "Add a check for negative values: if n < 0: raise ValueError('Negative values not allowed')",
        "level": "Advanced"
    },
    {
        "question": "What will the output be of this code?",
        "code": "class A:\n    def __init__(self):\n        self.val = 'A'\n\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        self.val += 'B'\n\nobj = B()\nprint(obj.val)",
        "answer": "AB",
        "level": "Advanced"
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form.get('answer')
    
    if user_answers:
        user_answers = json.loads(user_answers)
    else:
        user_answers = []

    score = 0
    correct_answers = {}
    
    # Combine questions and user answers into a list of tuples
    combined_answers = []
    for i, question in enumerate(questions):
        question_text = question["question"]
        correct_answer = question["answer"]
        user_answer = user_answers[i] if i < len(user_answers) else None
        
        correct_answers[question_text] = {
            "correct_answer": correct_answer,
            "user_answer": user_answer
        }
        
        combined_answers.append((question_text, user_answer))

        if user_answer == correct_answer:
            score += 1

    return render_template('results.html', score=score, correct_answers=correct_answers, total=len(questions), combined_answers=combined_answers)

if __name__ == '__main__':
    app.run(debug=True)
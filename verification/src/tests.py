"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": 15,
            "answer": "Fizz Buzz"
        },
        {
            "input": 6,
            "answer": "Fizz"
        },
        {
            "input": 10,
            "answer": "Buzz"
        },
        {
            "input": 7,
            "answer": "7"
        },

    ],
    "Edge": [
        {
            "input": 1000,
            "answer": "Buzz"
        },
        {
            "input": 1,
            "answer": "1"
        },
        {
            "input": 990,
            "answer": "Fizz Buzz"
        },

    ],
    "Extra": [
        {
            "input": 45,
            "answer": "Fizz Buzz"
        },

        {
            "input": 46,
            "answer": "46"
        },

        {
            "input": 47,
            "answer": "47"
        },

        {
            "input": 48,
            "answer": "Fizz"
        },

        {
            "input": 49,
            "answer": "49"
        },

        {
            "input": 50,
            "answer": "Buzz"
        },
        {
            "input": 999,
            "answer": "Fizz"
        },

        {
            "input": 1000,
            "answer": "Buzz"
        },

        {
            "input": 989,
            "answer": "989"
        },


    ]
}

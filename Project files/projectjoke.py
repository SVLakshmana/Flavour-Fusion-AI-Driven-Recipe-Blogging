# Function to generate a joke
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)
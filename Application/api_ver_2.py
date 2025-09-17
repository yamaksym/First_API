from flask import Flask, jsonify, request, render_template
import random
import os.path

from idna.idnadata import scripts
from werkzeug.utils import send_from_directory

app = Flask(__name__,
            template_folder='../Templates',
            static_folder='../Static')



animals = [
    {"id": 1, "name": "Cat", "sound": "Meow-Meow", "emoji": "🐱", "habitat": "home"},
    {"id": 2, "name": "Dog", "sound": "Woof-Woof", "emoji": "🐶", "habitat": "home"},
    {"id": 3, "name": "Cow", "sound": "Moo-Moo", "emoji": "🐄", "habitat": "farm"},
    {"id": 4, "name": "Duck", "sound": "Quack-Quack", "emoji": "🦆", "habitat": "lake"},
    {"id": 5, "name": "Goose", "sound": "Oua-Oua", "emoji": "🪿", "habitat": "farm"},
    {"id": 6, "name": "Goat", "sound": "Baa-Baa", "emoji": "🐐", "habitat": "farm"},
    {"id": 7, "name": "Fish", "sound": " ", "emoji": "🐟", "habitat": "river"},
    {"id": 8, "name": "Lion", "sound": "Roar-ROar", "emoji": "🦁", "habitat": "savanna"},
]


colors = [
    {"colour": "red", "Hex":"#f54242", "emoji": "❤️"},
    {"colour": "blue", "Hex":"#4542f5", "emoji": "💙"},
    {"colour": "green", "Hex":"#00ff00", "emoji": "💚"},
    {"colour": "yellow", "Hex":"#ecfc05", "emoji": "💛"},
    {"colour": "pink", "Hex":"#fc05a6", "emoji": "🩷"},
    {"colour": "purple", "Hex":"#b205fc", "emoji": "💜"}
]


jokes = [
    "Why computer had gone to the doctor? Because he had a virus!",
    "What does cheese says when he takes a photo? Milk!",
    "Why fish doesn't play tennis? Because he's afraid of a net!",
    "Are you afraid of skydiving? – Yes. – Jump without one",
    "The stroller on the motorcycle was not well secured, so Alex and Alexa parted ways nicely.",
    "What do our people do when their lights are turned off? Right! They run to see who else has had their lights turned off…"
]

riddles = [
    {"id": 1, "riddle": "There is a trough, Full of water poured.", "answer": "pond"},
    {"id": 2, "riddle": "He leads through the water, and he himself does not move from his place.", "answer": "bridge"},
    {"id": 3, "riddle": "Below is a wedge, atop is a mill. Water flows, and it doesn't matter.", "answer": "umbrella"},
    {"id": 4, "riddle": "Like a small ball, hanging, not bouncing, ruddy, smooth, sweet to the taste.", "answer": "apple"},
    {"id": 5, "riddle": "Knock, knock, the peas scattered. it began to dawn – there is nothing to collect", "answer": "stars"},
    {"id": 6, "riddle": "If you want to read, then you must know me, and if you don't know me, then you won't read anything.", "answer": "alphabet"},
    {"id": 7, "riddle": "From the edge of the sky, from behind the oak grove, the black-browed oxen came out: they brought a jug of water, they watered both the forest and the field.", "answer": "clouds"}
]

def check_files():
    template_path = os.path.join(os.path.dirname(__file__), '../Templates')
    static_path = os.path.join(os.path.dirname(__file__), '../Static')
    if not os.path.exists(template_path, static_path):
        print(f"❌ ERROR: File index.html or/and style.css are not found on this path: {template_path}")
        print("📁 Make sure, that the structure of folders is like below:")
        print("   Templates/")
        print("   ├── index.html")
        print("   │ ")
        print("   ├── Static/")
        print("   │")
        print("   ├── CSS/")
        print("   │   └── style.css")
        print("   ├── JS/")
        print("   │   └── script.js")
        return False
    return True

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/CSS/<path:filename>')
def css_files(filename):
    return send_from_directory('../Static/CSS', filename)

@app.route('/JS/<path:filename>')
def js_files(filename):
    return send_from_directory('../Static/JS', filename)

@app.route('/api/animals')
def get_animals():
   return jsonify({
       "animals": animals,
       "count": len(animals)
   })


@app.route('/api/animals/<int:animal_id>')
def get_animal(animal_id):
   animal = next((a for a in animals if a["id"] == animal_id), None)
   if animal:
       return jsonify(animal)
   else:
       return jsonify({"error": "Animal not found 😢"}), 404


@app.route('/api/random-color')
def random_color():
   color = random.choice(colors)
   return jsonify({
       "color": color,
       "message": f"Your random colour is: {color}! 🎨"
   })


@app.route('/api/joke')
def get_joke():
   joke = random.choice(jokes)
   return jsonify({
       "joke": joke,
       "message": "Glad if you like this joke! 😄"
   })


@app.route('/api/math/<int:num1>/<int:num2>')
def add_numbers(num1, num2):
   result = num1 + num2
   return jsonify({
       "number1": num1,
       "number2": num2,
       "result": result,
       "message": f"{num1} + {num2} = {result} 🧮"
   })


@app.route('/api/greeting', methods=['POST'])
def getGreeting():
    try:
        data = request.json
        name = data['name']
        age = data.get('age', 0)

        if age > 0:
            message = f"👋 Hello, {name}! You're {age} - this is good! 🎈"
        else:
            message = f"👋 Hello, {name}! Nice to meet you! 😊"

        return jsonify({"message": message})
    except KeyError as e:
        return  jsonify({"error": "Name expected"}), 400

@app.route("/api/riddle")
def get_riddle():
    index = random.randint(0, len(riddles) - 1)
    return jsonify({
        "id": index,
        "riddle": riddles[index]["riddle"],
        "message": f"Answer it at /riddle/{index}/<your_answer>"
    })

@app.route("/api/riddle/<int:riddle_id>/<user_answer>")
def check_answer(riddle_id, user_answer):
    if not (0 <= riddle_id < len(riddles)):
        return jsonify({
            "success": False,
            "message": f"Invalid riddle id. Must be between 0 and {len(riddles)-1}."
        }), 400

    correct_answer = riddles[riddle_id]["answer"].lower()
    user_answer = user_answer.strip().lower()
    is_correct = (user_answer == correct_answer)

    return jsonify({
        "success": True,
        "riddle_id": riddle_id,
        "your_answer": user_answer,
        "correct_answer": correct_answer,
        "correct": is_correct,
        "message": "✅ Correct!" if is_correct else "❌ Wrong, try again!"
    })


if __name__ == '__main__':
   app.run(debug=True)



function getRandomAnimal() {
           fetch('/api/animal')
               .then(response => response.json())
               .then(data => showResult('random-result', data.message));
       }


       function getRandomColor() {
           fetch('/api/color')
               .then(response => response.json())
               .then(data => showResult('random-result', data.message));
       }


       function getJoke() {
           fetch('/api/joke')
               .then(response => response.json())
               .then(data => showResult('random-result', data.message));
       }


function calculate_add() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    if (!num1 || !num2) {
        showResult('calc-result', '❌ Write both numbers!');
        return;
    }

    const number1 = parseInt(num1);
    const number2 = parseInt(num2);

    if (isNaN(number1) || isNaN(number2)) {
        showResult('calc-result', '❌ Write numbers!');
        return;
    }

    fetch('/api/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num1: number1,
            num2: number2
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('calc-result', '❌ ' + data.error);
        } else {
            showResult('calc-result', data.message);
        }
    })
    .catch(error => showResult('calc-result', '❌ Error: ' + error.message));
}
function calculate_subtract() {
    const num3 = document.getElementById('num3').value;
    const num4 = document.getElementById('num4').value;

    if (!num3 || !num4) {
        showResult('calc-result2', '❌ Write both numbers!');
        return;
    }

    const number3 = parseInt(num3);
    const number4 = parseInt(num4);

    if (isNaN(number3) || isNaN(number4)) {
        showResult('calc-result2', '❌ Write numbers!');
        return;
    }

    fetch('/api/subtract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num3: number3,
            num4: number4
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('calc-result2', '❌ ' + data.error);
        } else {
            showResult('calc-result2', data.message);
        }
    })
    .catch(error => showResult('calc-result2', '❌ Error: ' + error.message));
}
function calculate_multiply() {
    const num5 = document.getElementById('num5').value;
    const num6 = document.getElementById('num6').value;

    if (!num5 || !num6) {
        showResult('calc-result3', '❌ Write both numbers!');
        return;
    }

    const number5 = parseInt(num5);
    const number6 = parseInt(num6);

    if (isNaN(number5) || isNaN(number6)) {
        showResult('calc-result3', '❌ Write numbers!');
        return;
    }

    fetch('/api/multiply', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num5: number5,
            num6: number6
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('calc-result3', '❌ ' + data.error);
        } else {
            showResult('calc-result3', data.message);
        }
    })
    .catch(error => showResult('calc-result3', '❌ Error: ' + error.message));
}
function calculate_divide() {
    const num7 = document.getElementById('num7').value;
    const num8 = document.getElementById('num8').value;

    if (!num7 || !num8) {
        showResult('calc-result4', '❌ Write both numbers!');
        return;
    }

    const number7 = parseInt(num7);
    const number8 = parseInt(num8);

    if (isNaN(number7) || isNaN(number8)) {
        showResult('calc-result4', '❌ Write numbers!');
        return;
    }

    fetch('/api/divide', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num7: number7,
            num8: number8
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('calc-result4', '❌ ' + data.error);
        } else {
            showResult('calc-result4', data.message);
        }
    })
    .catch(error => showResult('calc-result4', '❌ Error: ' + error.message));
}

       function getGreeting() {
           const name = document.getElementById('name').value;
           const age = document.getElementById('age').value;


           if (!name) {
               showResult('greeting-result', '❌ Write your name!');
               return;
           }


           fetch('/api/greeting', {
               method: 'POST',
               headers: {'Content-Type': 'application/json'},
               body: JSON.stringify({name: name, age: age ? parseInt(age) : 0})
           })
           .then(response => response.json())
           .then(data => showResult('greeting-result', data.message));
       }


       function countLetters() {
           const word = document.getElementById('word').value;


           if (!word) {
               showResult('letters-result', '❌ Type the word/sentence!');
               return;
           }


           fetch('/api/letters', {
               method: 'POST',
               headers: {'Content-Type': 'application/json'},
               body: JSON.stringify({word: word})
           })
           .then(response => response.json())
           .then(data => showResult('letters-result', data.message));
       }


       function showResult(elementId, message) {
           const element = document.getElementById(elementId);
           element.innerHTML = message;
           element.style.display = 'block';
       }
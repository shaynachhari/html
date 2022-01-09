function add(num1, num2) {

    return num1 + num2
}

function subtract(num1, num2) {

    return num1 - num2
}

function multi(num1, num2) {

    return num1 * num2
}

function divide(num1, num2) {

    return num1 / num2
}

let operator = null
let num1 = null
let num2 = null
let result = null

function operation(operator, num1, num2) {
    if (operator == "+") {
        return add(num1, num2)
        // console.log("sss")
    }

    else if (operator == "-") {
        return subtract(num1, num2)
    }

    else if (operator == "*") {
        return multi(num1, num2)
    }

    else if (operator == "/") {
        return divide(num1, num2)
    }

    else {
        alert("something went wrong reload and try again")
    }
}
// console.log(operation("+", 3, 6))
num1_div = document.getElementById("num1")
num2_div = document.getElementById("num2")
operator_div = document.getElementById("operator")
result_div = document.getElementById("result")

function numIn(number) {
    if (operator_div.innerHTML == "") {
        num1_div.innerHTML += number
    }
    else {
        num2_div.innerHTML += number
    }
}

function operatorIn(operator) {
    operator_div.innerHTML = operator
}

function resultIn() {
    num1 = Number(num1_div.innerHTML)
    num2 = Number(num2_div.innerHTML)
    operator = operator_div.innerHTML
    result = operation(operator, num1, num2)
    result_div.innerHTML = result
}




// document.getElementById("count-el").innerText = 5


// initialize count on 0
// listen for clicks on the increment button
// increment the count variable when the button is clicked
// change the count-el in the html to reflect a count
let count = 0
let  note = 0
function increment() {
    document.getElementById("count-el").innerText = count + 1
    count += 1
}

function decrement() {
    document.getElementById("count-el").innerText = count - 1
    count -= 1
}

function reset() {
    document.getElementById("count-el").innerText = note
    count = 0
}
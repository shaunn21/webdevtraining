function funcExample () {
    console.log("Hello World");
};

let my_name = "Will"; // variable declaration for a mutable variable

const my_last_name = "O'Connell"; // variabel declaration for an immutable variable

if (my_name === "Will") {
    console.log(`Hello, ${my_name}!`);
} else {
    console.log("You're not Will!");
};

function reallyGoodFunction (num1, num2) {
    let result = num1 + num2; 
    return result; 
};
    
    

function taskHider () {
    let element = document.getElementById("task-box")
    element.classList.toggle("hidden")
}

// function darkMode () {
//     let element = document.getElementById("base-body")
//     console.log(element)
//     element.classList.toggle("dark-mode")
// }

function lightDark() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}

// function displayDate(){
//     document.getElementById("date").innerHTML = date();
// }
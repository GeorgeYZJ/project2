function CheckAnswer() {
    var attemp = getElementById("Checker").toLowerCase();
    var answer = 123;
    if (answer == attemp)
    {
        document.getElementById("final").innerHTML = "Correct Answer!!!";
    }
    else
    {
        document.getElementById("final").innerHTML = "Wrong the correct answer is" ;
     }

    
}

//the form function 
function multiPrint() {
    var fullName = document.forms["fName"];
    var output = ""; var j;
    for (j = 0; j < fullName.length - 1; j++) {
        output += fullName.elements[j].value + ' ';
    }
    document.getElementById("final").innerHTML = output;
}
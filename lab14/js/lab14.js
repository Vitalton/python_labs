// Global functions and variables


// First Task

function load() {
    img_1 = document.getElementById("img_1");
    img_2 = document.getElementById("img_2");
    img_3 = document.getElementById("img_3");

    img_1.setAttribute("src", "images/complete.jpg");
    img_2.setAttribute("src", "images/complete.jpg");
    img_3.setAttribute("src", "images/complete.jpg");
}

function y(x) {
    return Math.log(Math.pow(x, 3)) + Math.pow(x, 2) + Math.sqrt(Math.SQRT2) + Math.SQRT1_2;
}

function loads() {
    var t1 = performance.now();
    load();
    var t2 = performance.now();
    alert("Время выполнения операции:  " + (t2 - t1) / 3 + "  сек");
}
function result() {
    var t1 = performance.now();
    var res = y(9);
    var t2 = performance.now();
    alert("y = " + res + "\n" + "Время выполнения операции:  " + (t2 - t1) + "  сек");
}
// Second Task

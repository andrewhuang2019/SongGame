var slider1 = document.getElementById("rating-slider");

slider1.oninput = function() {
    document.getElementById("rating-number").innerHTML = this.value;
}

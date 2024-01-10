for (let i = 0; i < 3; i++){
    var slider = document.getElementById("rating-slider".concat(i.toString()))
    slider.oninput = function() {
        document.getElementById("rating-number".concat(i.toString())).innerHTML = this.value;
    }
}
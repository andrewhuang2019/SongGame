function hide_element_by_id (id_name) {
    document.getElementById(id_name);
}

// allows song sliders 1-3 to update the number display
for (let i = 0; i < 3; i++){
    let slider = document.getElementById("rating-slider".concat(i.toString()));
    slider.oninput = function() {
        document.getElementById("rating-number".concat(i.toString())).innerHTML = this.value;
    }
}

let times_pressed = 0;
// update final value display and variable when slider is changed
const final_slider = document.getElementById("rating-slider-final");
let final_val = 5;
final_slider.oninput = function() {
    if(times_pressed == 0){
        final_val = this.value;
    }

    document.getElementById("rating-number-final").innerHTML = this.value;
}

const final_button = document.getElementById("rating-button-final");
const final_rating_number = document.getElementById("rating-number-final");
final_button.onclick = function() {
    times_pressed++;
    if(times_pressed == 1){ 
        // change prompt to asking name2 for their guess, reset slider and visual display
        final_slider.value = 5;
        final_rating_number.innerHTML= 5;

        document.getElementById("tip-container-final").innerHTML = "What does name2 think name1 would rate this?";
    }else if(times_pressed == 2){ 
        // display user's score, display score
        const score = 10 - Math.abs(final_val - final_slider.value);
        document.getElementById("tip-container-final").innerHTML = "Name2's score: ".concat(score.toString());
    }else{
        // do nothing
    }
}
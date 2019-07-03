
var slider = document.getElementById("loanAmount");
var output = document.getElementById("moveAmount");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
};

var slider = document.getElementById("loanMonth");
		var output = document.getElementById("moveMonth");
		output.innerHTML = slider.value;

		slider.oninput = function() {
		  output.innerHTML = this.value;
		};



var random_number = document.getElementById('random_number');

function generate_random_number() {
  var number = Math.floor((Math.random() * 10000) + 1);
  random_number.innerHTML = number;
}

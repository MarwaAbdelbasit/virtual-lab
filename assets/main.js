var random_number = document.getElementById('random_number'),
    error = document.querySelector(".errorList"),
    applyCoupon = document.querySelector('.applyCoupon');
    // couponCard = document.querySelector(".card-body");

function generate_random_number() {
  var number = Math.floor((Math.random() * 10000) + 1);
  random_number.innerHTML = number;
}

if (error) {
  console.log("error");
}

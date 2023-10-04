const slot_btn1 = document.getElementById('slot-btn-1');
const slot_btn2 = document.getElementById('slot-btn-2');
const slot_btn3 = document.getElementById('slot-btn-3');
const select_option = document.getElementById('division')


$('#slot-btn-1').click(function () {
  // alert('slot_btn1 has been click')
  console.log(select_option.value)
  $(this).toggleClass("btn-primary btn-danger")

  if ($(this).hasClass("btn-primary")) {
    // alert("contains btn-primary")
    $.ajax({
      type: "GET",
      url: "/slot_creation",
      data: {
        slot_id: slot_btn1.value,
        division_data: select_option.value,
      },
      success: function (data) {
        alert("successful")
        alert(data.message)
      },
      error: function () {
        alert("failure")
      }
    })
  }

  else if ($(this).hasClass("btn-danger")) {
    // alert("contains btn-danger")
    $.ajax({
      type: "GET",
      url: "/slot_deletion",
      data: {
        slot_id: slot_btn1.value,
        division_data: select_option.value,
      },
      success: function (data) {
        alert('successful')
        alert(alert.message)
      },
      error: function () {
        alert('failure')
      }
    })
  }
})

slot_btn2.addEventListener("click", function () {
  if (slot_btn2.classList.contains("btn-primary")) {
    console.log("contains btn-primary")
    slot_btn2.classList.remove("btn-primary");
    slot_btn2.classList.add("btn-danger");
    slot_btn2.innerText = "Lock";
  }
  else if (slot_btn2.classList.contains("btn-danger")) {
    console.log("contains btn-danger")
    slot_btn2.classList.remove("btn-danger");
    slot_btn2.classList.add("btn-primary");
    slot_btn2.innerText = "unlock";
  }
})


slot_btn3.addEventListener("click", function () {
  if (slot_btn3.classList.contains("btn-primary")) {
    console.log("contains btn-primary")
    slot_btn3.classList.remove("btn-primary");
    slot_btn3.classList.add("btn-danger");
    slot_btn3.innerText = "Lock";
  }
  else if (slot_btn3.classList.contains("btn-danger")) {
    console.log("contains btn-danger")
    slot_btn3.classList.remove("btn-danger");
    slot_btn3.classList.add("btn-primary");
    slot_btn3.innerText = "unlock";
  }
})




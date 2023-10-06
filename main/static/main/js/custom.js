const slot_btn1 = document.getElementById('slot-btn-1');
const slot_btn2 = document.getElementById('slot-btn-2');
const slot_btn3 = document.getElementById('slot-btn-3');
const select_option = document.getElementById('division')
console.log(slot_btn3.value)
console.log($('#slot-btn-3').value)

$('#slot-btn-1').click(function () {
  // alert('slot_btn1 has been click')
  //console.log(select_option.value)
  $(this).toggleClass("btn-primary btn-danger")

  if ($(this).hasClass("btn-primary")) {
    // alert("contains btn-primary")
    $.ajax({ // to delete the created slot
      type: "GET",
      url: "/slot_deletion",
      data: {
        slot_id: slot_btn1.value,
      },
      success: function (data) {
        alert('successful to delete a slot')
        alert(data.message)
      },
      error: function () {
        alert('failure to delete a slot')
      }
    })
  }

  else if ($(this).hasClass("btn-danger")) {
    // alert("contains btn-danger")
    $.ajax({ // to create a new slot
      type: "GET",
      url: "/slot_creation",
      data: {
        slot_id: slot_btn1.value,
        division_data: select_option.value,
      },
      success: function (data) {
        alert("successful to create a slot")
        alert(data.message)
      },
      error: function () {
        alert("failure to create a slot")
      }
    })
  }
})

$('#slot-btn-2').click(function () {
  // alert('slot_btn1 has been click')
  //console.log(select_option.value)
  $(this).toggleClass("btn-primary btn-danger")

  if ($(this).hasClass("btn-primary")) {
    // alert("contains btn-primary")
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

  else if ($(this).hasClass("btn-danger")) {
    // alert("contains btn-danger")
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
})



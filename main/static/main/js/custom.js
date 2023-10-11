const slot_btn1 = document.getElementById('slot-btn-1');
const slot_btn2 = document.getElementById('slot-btn-2');
const slot_btn3 = document.getElementById('slot-btn-3');
const select_option = document.getElementById('division')

const btns = document.getElementsByClassName('btn')

//to check whether there are any slot present in backend
$(document).ready(function () {
  $.ajax({
    type: "GET",
    url: "/check_slot",
    success: function (data) {
      if (data.slot_id) {
        for (let i = 0; i < btns.length; i++) {
          //console.log(btns[i])
          if (btns[i].value == data.slot_id) {
            //console.log("Match krra h bhau")
            btns[i].classList.replace("btn-primary", "btn-danger")
            btns[i].innerText = "Lock"
          }
        }
      }
    },
    error: function () {
      alert("No slot is opened!!!")
    }
  })
})

$('#slot-btn-1').click(function () {
  // alert('slot_btn1 has been click')
  //console.log(select_option.value)
  $(this).toggleClass("btn-primary btn-danger")

  if ($(this).hasClass("btn-primary")) {
    // alert("contains btn-primary")
    $(this).text("Unlock")
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
    $(this).text("Lock")
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
    $(this).text("Unlock")
    $.ajax({
      type: "GET",
      url: "/slot_deletion",
      data: {
        slot_id: slot_btn2.value,
        division_data: select_option.value,
      },
      success: function (data) {
        alert('successful')
        alert(data.message)
      },
      error: function () {
        alert('failure')
      }
    })
  }

  else if ($(this).hasClass("btn-danger")) {
    // alert("contains btn-danger")
    $(this).text("Lock")
    $.ajax({
      type: "GET",
      url: "/slot_creation",
      data: {
        slot_id: slot_btn2.value,
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

$('#slot-btn-3').click(function () {
  // alert('slot_btn1 has been click')
  //console.log(select_option.value)
  $(this).toggleClass("btn-primary btn-danger")

  if ($(this).hasClass("btn-primary")) {
    // alert("contains btn-primary")
    $(this).text("Unlock")
    $.ajax({
      type: "GET",
      url: "/slot_deletion",
      data: {
        slot_id: slot_btn3.value,
        division_data: select_option.value,
      },
      success: function (data) {
        alert('successful')
        alert(data.message)
      },
      error: function () {
        alert('failure')
      }
    })
  }

  else if ($(this).hasClass("btn-danger")) {
    // alert("contains btn-danger")
    $(this).text("Lock")
    $.ajax({
      type: "GET",
      url: "/slot_creation",
      data: {
        slot_id: slot_btn3.value,
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



$("#attendance_btn").click(function () {
  alert('Mark Attendance has been clicked')
  $.ajax({
    type: "GET",
    url: "/mark-attendance",
    data: {
      slot_id: $('#span_slot_id').text(),
    },
    success: function (data) {
      //alert("Attendance is marked")
      alert(data.message)
    },
    error: function (data) {
      alert("ajax failed")
    },
  })
})

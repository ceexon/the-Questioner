document.addEventListener('DOMContentLoaded',
  function () {
    const meetUps = document.querySelectorAll('div.meet-to-delete')
    meetUps.forEach(function (meet) {
      var divTop = document.createElement("div")
      divTop.style.position = "absolute";
      divTop.classList.add('del-meets')
      meet.addEventListener('mouseover', function (e) {
        e.preventDefault()
        meet.appendChild(divTop)
        console.log("now on meet")
      })
      meet.addEventListener('mouseout', function (e) {
        e.preventDefault()
        meet.removeChild(divTop)
        console.log("now off meet")
      })

    })
  })
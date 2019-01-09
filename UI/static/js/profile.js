document.addEventListener('DOMContentLoaded',
  function () {
    var showProf = document.querySelector('span.fas.fa-bars')
    var profile = document.querySelector('#prof-panel')
    showProf.addEventListener('click', function (e) {
      e.preventDefault()
      profile.classList.remove("hide-from-prof")
      profile.classList.add("show-on-prof")
      this.style.display = "none"
    })

    var hideProf = document.querySelector("span.fa-times")
    hideProf.addEventListener('click', function (e) {
      e.preventDefault()
      profile.classList.add("hide-from-prof")
      profile.classList.remove("show-on-prof")
      showProf.style.display = "block"
    })

  })
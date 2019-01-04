document.addEventListener('DOMContentLoaded',
    function () {
        const dropFormButton = document.querySelector('button.show-question-form')
        const dropForm = document.createElement('form')
        const formFieldT = document.createElement('textarea')
        const submitBtn = document.createElement('input')

        dropForm.classList.add("question-form-f")
        submitBtn.classList.add('class', "sign")
        submitBtn.classList.add('class', "send-remark")

        formFieldT.classList.add('textarea')
        submitBtn.setAttribute('type', 'submit')
        submitBtn.setAttribute('role', 'button')
        submitBtn.setAttribute('value', 'Add question')

        formFieldT.setAttribute('rows', 10)

        dropForm.appendChild(formFieldT)
        dropForm.appendChild(submitBtn)

        dropFormButton.addEventListener('click', function (e) {
            e.preventDefault()
            this.style.display = 'none'
            this.parentNode.setAttribute('class', 'a-question')
            this.parentNode.appendChild(dropForm)
        })

    })
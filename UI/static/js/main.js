document.addEventListener('DOMContentLoaded',
    function () {
        const dropFormButton = document.querySelector('button#addQuiz')
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
        formFieldT.style.borderColor = 'grey'

        dropForm.appendChild(formFieldT)
        dropForm.appendChild(submitBtn)

        dropFormButton.addEventListener('click', function (e) {
            e.preventDefault()
            this.style.display = 'none'
            this.parentNode.setAttribute('class', 'a-question')
            this.parentNode.appendChild(dropForm)
        })

        dropForm.addEventListener('submit', function (e) {
            e.preventDefault()
            var value = this.querySelector('textarea').value

            if (value == "" || value.trim() == "") {
                e.preventDefault()
                formFieldT.style.borderColor = "red"
            } else {
                contDiv = this.parentNode
                a_question = document.createElement('p')
                a_question.textContent = value
                userImage = document.createElement('img')
                userImage.setAttribute('src', '../static/images/question-main-page/questions-image.jpg')

                a_question.classList.add('quiz-content')

                contDiv.removeChild(dropForm)
                contDiv.appendChild(userImage)
                contDiv.appendChild(a_question)
                dropFormButton.style.display = "block"
            }
        })

        commentButtons = document.querySelectorAll('.comment-button')
        commentButtons.forEach(function (btn) {

            btn.addEventListener('click', function (e) {
                e.preventDefault();
                console.log(btn)
                commentBox = document.createElement('div');
                commentBox.style.display = "block";
                commentBox.style.width = "100%";
                submitBtn.setAttribute('value', 'Add Your comment');
                commentBox.appendChild(dropForm);
                btn.parentNode.appendChild(commentBox)
                btn.style.display = "none"
            })
        });

    })
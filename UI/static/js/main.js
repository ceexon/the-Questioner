document.addEventListener('DOMContentLoaded',
	function () {
		const dropFormButton = document.querySelector('button#addQuiz');
		const dropForm = document.createElement('form');
		const formFieldT = document.createElement('textarea');
		const submitBtn = document.createElement('input');
		const hideButton = document.createElement('span');

		dropForm.classList.add("question-form-f");
		submitBtn.classList.add('class', "sign");
		submitBtn.classList.add('class', "send-remark");
		hideButton.classList.add('fas');
		hideButton.classList.add('fa-times');
		hideButton.classList.add('hide-btn');

		formFieldT.classList.add('textarea');
		submitBtn.setAttribute('type', 'submit');
		submitBtn.setAttribute('role', 'button');
		submitBtn.setAttribute('value', 'Add question');

		formFieldT.setAttribute('rows', 10);

		dropForm.appendChild(formFieldT);
		dropForm.appendChild(submitBtn);

		dropFormButton.addEventListener('click', function (e) {
			e.preventDefault();
			this.style.display = 'none';
			this.parentNode.appendChild(dropForm);
			this.parentNode.appendChild(hideButton);
		})

		hideButton.addEventListener('click', function (e) {
			e.preventDefault();
			this.parentNode.removeChild(dropForm);
			this.parentNode.removeChild(this);
			dropFormButton.style.display = "block";
		})

		dropForm.addEventListener('submit', function (e) {
			e.preventDefault();
			var value = this.querySelector('textarea').value;

			if (value == "" || value.trim() == "") {
				e.preventDefault();
				formFieldT.style.borderColor = "red";
			} else {
				const questView = document.querySelector('.question-views');
				const questBox = document.querySelector('.question-asked');
				const newQuestion = questBox.cloneNode(true);
				questView.appendChild(newQuestion)
				questView.removeChild(dropFormButton.parentNode.parentNode)
				dropFormButton.parentNode.removeChild(dropForm)
				dropFormButton.parentNode.removeChild(hideButton)
				dropFormButton.style.display = "block"
				questView.appendChild(dropFormButton.parentNode.parentNode)
			}
		})
	})
function hideQuestion(questionId){
    var questionId = document.getElementById('question-' + questionId);
    questionId.parentElement.parentElement.parentElement.style.animationPlayState = 'running';
    questionId.parentElement.parentElement.parentElement.addEventListener('animationend', function () {
        questionId.parentElement.parentElement.parentElement.remove();
    });

}   
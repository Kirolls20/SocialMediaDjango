$(document).ready(function (){
    $('.vote').off('click','#vote-btn').on('click','#vote-btn', function (){
        var answerId = $(this).data('answer-id') ;
        var answerButton = $(this);
        var csrfToken = $(this).data('csrf-token');
        var answerCount = $('#votes-count-' + answerId);

        $.ajax({
            url: `/question/${answerId}/answer/like/`,
            method:'POST',
            data:{csrfmiddlewaretoken:csrfToken},
            success: function(data){
                if (data.voted) {
                    answerButton.html('<i class="fa-solid fa-thumbs-up">');
                } else {
                    answerButton.html('<i class="fa-regular fa-thumbs-up">');
                }
                answerCount.text(data.votes_cout + ' Votes')
            }
        });
    });
});
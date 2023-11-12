$(document).ready(function (){
    $('.like-container').on('click','#like-button', function (){
        var questionId = $(this).data('question-id');
        var csrfToken = $(this).data('csrf-token');
        var likeButton = $(this);
        var likeCount = $('#likes-count');
        $.ajax({
            url: `/question/like/${questionId}/`,
            method:'POST',
            date:{csrfmiddlewaretoken:csrfToken},

            success: function (data) {
                if (data.liked) {
                    likeButton.html('<i class="fa-solid fa-heart fa-2xl" style="color: #d62069;"></i>');
                } else {
                    likeButton.html('<i class="fa-regular fa-heart fa-2xl" style="color: #d62069;"></i>');
                }
                likeCount.text(data.likes_count + ' Likes');
            }
        });

    });


});
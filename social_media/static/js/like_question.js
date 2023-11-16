$(document).ready(function (){
    $('.like-container').off('click','#like-button').on('click','#like-button', function (){
        var questionId = $(this).data('question-id');
        var csrfToken = $(this).data('csrf-token');
        var likeButton = $(this);
        var likeCount = $('#likes-count-' + questionId);
        let count = parseInt(localStorage.getItem('likeCount')) || 0;
        
        $.ajax({
            url: `/question/like/${questionId}/`,
            method:'POST',
            data:{csrfmiddlewaretoken:csrfToken},

            success: function (data) {
                if (data.liked) {
                    likeButton.html('<i class="fa-solid fa-heart fa-2xl" style="color: #d62069;"></i>');
                } else {
                    likeButton.html('<i class="fa-regular fa-heart fa-2xl" style="color: #d62069;"></i>');
                }
                likeCount.text(data.likes_count + ' Likes');

                // Save the updated like count in local storage
                localStorage.setItem('likeCount', count);
            }
        });

    });


});
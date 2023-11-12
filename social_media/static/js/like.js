$(document).ready(function () {
     
    $('.blog-details').on('click', '#like-button', function () {
        var blogId = $(this).data('blog-id');
        var csrfToken = $(this).data('csrf-token');
        var likeButton = $(this);
        var likesCount = $('#likes-count-', blogId);
        $.ajax({
            url: `/blog/like/${blogId}/`,
            method: 'POST',
            data: { csrfmiddlewaretoken: csrfToken },
            
            success: function (data) {
                if (data.liked) {
                    likeButton.html('<i class="fa-solid fa-heart fa-2xl" style="color: #d62069;"></i>');
                } else {
                    likeButton.html('<i class="fa-regular fa-heart fa-2xl" style="color: #d62069;"></i>');
                }
                likesCount.text(data.likes_count + ' Likes');
            }
        });
    });
});
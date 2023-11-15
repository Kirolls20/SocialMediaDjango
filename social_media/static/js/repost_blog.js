$(document).ready(function (){
    $('.repost').off('click', '#repost-btn').on('click', '#repost-btn', function (){
        var postId = $(this).data('repost-id')
        var csrfToken = $(this).data('csrf-token');
        var repostButton = $(this);
        var repostCount  = $('#repost-count-' + postId)
        $.ajax({
            url: `/blog/${postId}/repost/`,
            method:'POST',
            data:{csrfmiddlewaretoken:csrfToken},
            success: function(data){
                alert('Blog Reposted!')
                repostCount.text(data.repost_count + ' Reposts' )
            }
        });
    });
});
    
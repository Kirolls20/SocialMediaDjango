$(document).ready(function (){
    $('.repost').off('click','#repost-btn').on('click','#repost-btn', function(){
        var questionId = $(this).data('repost-id');
        var csrfToken = $(this).data('csrf-token');
        var repostCount = $('#repost-count-' + questionId)
        $.ajax({
            url: `/question/${questionId}/repost/`,
            method: 'POST',
            data:{csrfmiddlewaretoken:csrfToken},
            success:function(data){
                alert('Question Repoted!')
                repostCount.text(data.repost_count)
            }
        })
    })


});
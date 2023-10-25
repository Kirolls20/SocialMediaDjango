document.querySelector('#posts').style.display = 'block';   
function showPage(page){
    document.querySelectorAll('.nav-content').forEach(div =>{
        div.style.display= 'none'
    });
    document.querySelector(`#${page}`).style.display='block';
};

document.querySelectorAll(".nav-btn").forEach(btn => {

    btn.onclick = function() {
        console.log('clicked')
        showPage(this.dataset.page);
    }
});

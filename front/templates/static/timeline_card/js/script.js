$(document).ready(function () {
    //Img slideshow on click (multimedia)
    m_element = $(".timeline-content-card > .post-content > #actual > .attached-media > *")
    $(m_element).on('click', function () {
        $(this).next().after($(this))       
    })
})
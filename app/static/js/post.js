function likePost(likeIcon) {
    var postId = likeIcon.dataset.postId;
    var likesCountElement = document.getElementById('likesCount_' + postId);

    axios.post('/posts/like', { post_id: postId })
        .then(function (response) {
            if (response.data.likes !== undefined) {
                likesCountElement.innerHTML = response.data.likes
            } else {
                window.location.href = "/user/auth/login";
            }
        })
        .catch(function (error) {
            console.error('Error when liking a post: ', error);
        });
}
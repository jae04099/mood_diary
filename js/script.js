// memo-color-change

    $('.palette').find('.c1').click(function () {
        alert('this is pink');
    })

//pink 버튼 클릭
//메모지 색 변경

$.ajax({
    type: 'GET',
    url: 'http://ws.audioscrobbler.com/2.0/?method=track.search&track=' + PostCode + '&api_key=48bee338cada7005923f7ef2dd843dfa&format=json',
    success: function (response) {
        let musicList = response["results"]["trackmatches"]["track"];
        console.log(musicList[1])
        for(let i = 0; i < musicList.length; i++){
            let albumImg = musicList[i][]
            let albumTitle =
            let albumArtist =
        }
    }
})
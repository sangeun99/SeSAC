function uploadPost() {
  let title = $("#input-title").val();
  let message = $("#input-text").val();

  $.ajax({
    type: "post",
    url: "/create",
    data: { title: title, message: message },
    success: function (resp) {
      console.log(resp);
      alert('저장완료' + resp);
      window.location = "/";
    }
  })
}

function getValue(id, title, message) {
  // 수정 버튼을 누르면 값이 채워지도록 만드는 함수
  $('#input-type-desc').text('메모 수정하기');
  $('#input-title').val(title);
  $('#input-text').val(message);

  $('#submit-btn').text('수정완료');
  $('#submit-btn').removeAttr("onclick");
  $('#submit-btn').attr("onclick", `updatePost(${id})`);
}

function updatePost(id) {
  // 수정완료 버튼을 누르면 값이 변하도록 db 보내는 함수
  let title = $('#input-title').val();
  let message = $('#input-text').val();
  $.ajax({
    type: "post",
    url: "/update",
    data: { id: id, title: title, message: message },
    success: function (resp) {
      alert('수정완료' + resp);
      window.location = '/';
    }
  })
}

function deletePost(id) {
  $.ajax({
    type: "post",
    url: "/delete",
    data: { id: id },
    success: function (resp) {
      alert('삭제완료' + resp);
      window.location = '/';
    }
  })
}

function makeCard(id, title, message, modified_at) {
  let card_content =
    `
    <div class="card-container">
      <div class="card-content-warp">
        <i class="fa-regular fa-copy" onclick="copyToClipboard('${message}')"></i>
        <h3 class="card-title">${title}</h3>
        <div class="card-message">
        <p>${message}</p>
        </div>
        <p class="card-time">${modified_at}</p>
      </div>
      <div class="card-btn-warp">
        <div class="card-btn left" onclick="getValue(${id}, '${title}', '${message}')">수정</div>
        <div class="card-btn right" onclick="deletePost(${id})">삭제</div>
      </div>
    </div>
    `
  $("#card-list").append(card_content);
}

function copyToClipboard(message) {
  navigator.clipboard.writeText(message);
  alert("텍스트 복사 완료!")
}

$('document').ready(function () {
  console.log('document is ready')
  $.ajax({
    type: "get",
    url: "/list",
    data: {},
    success: function (resp) {
      console.log(resp)
      for (let i = 0; i < resp.length; i++) {
        makeCard(resp[i]['id'], resp[i]['title'], resp[i]['message'], resp[i]['modified_at']);
      }
    }
  })
})
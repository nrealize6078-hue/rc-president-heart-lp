/* PRESIDENT JOURNEY 案内モーダル
   元サイトにはこの動作のJSが含まれていなかったため、
   ボタンが機能するよう最小構成で補完したもの。 */
(function () {
  var dialog = document.getElementById('guide');
  var invite = document.getElementById('invite');
  var copyBtn = document.getElementById('copy');
  var status = document.getElementById('copy-status');
  if (!dialog) return;

  // 「旅のはじめ方を見る」→ モーダルを開く
  if (invite) {
    invite.addEventListener('click', function () {
      if (typeof dialog.showModal === 'function') dialog.showModal();
      else dialog.setAttribute('open', '');
    });
  }

  // 「×」→ 閉じる
  var close = dialog.querySelector('.close');
  if (close) {
    close.addEventListener('click', function () {
      if (typeof dialog.close === 'function') dialog.close();
      else dialog.removeAttribute('open');
    });
  }

  // 案内希望の定型文をコピー
  var MESSAGE = 'PRESIDENT JOURNEYを体験したいです。ご案内をお願いいたします。';
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      function done(ok) {
        if (status) status.textContent = ok ? 'コピーしました。担当者へそのまま送信してください。' : 'コピーできませんでした。文章を長押しして選択してください。';
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(MESSAGE).then(function () { done(true); }, function () { done(false); });
      } else {
        done(false);
      }
    });
  }
})();

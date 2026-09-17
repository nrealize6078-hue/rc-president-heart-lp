/* 固定ボトムバーの出し入れと、LINE公式ボタンの読み込み失敗時の差し替え。
   ファーストビューを抜けたらバーを出す（IntersectionObserver）。 */
(function () {
  var bar = document.getElementById('ctabar');
  var hero = document.querySelector('.hero');

  if (bar && hero) {
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        // ヒーローが画面から出たら表示
        bar.hidden = entries[0].isIntersecting;
      }, { threshold: 0.12 }).observe(hero);
    } else {
      // 古い端末向け。スクロール量で判定する
      var onScroll = function () {
        bar.hidden = window.scrollY < hero.offsetHeight * 0.85;
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  }

  // LINE公式の画像が読めなかったときは緑のボタンに置き換える
  var img = document.querySelector('.line-cta img');
  if (img) {
    img.addEventListener('error', function () {
      var a = img.parentNode;
      img.remove();
      a.classList.add('is-fallback');
      a.textContent = 'LINEで友だち追加';
    });
  }
})();

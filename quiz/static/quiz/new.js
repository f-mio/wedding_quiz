/*
＜番号の属性追加手順＞
　1. クリック→発火
　2. タグのidを取得
　3. idが【quiz-X】となっていた場合に発火
　4. ページ内のselected属性が付いているものに下記の処理
　　　　・p.selected属性を削除
　　　　・div.selectedを削除し、div.none-selected属性を追加。
　5. 変数に取得したidを保存し、下記の処理
　　　　・p.selected属性,div.selected属性を追加
　　　　・div.none-selectedを削除。

＜回答済み属性追加手順＞
　1. id【id_answer_X】がクリックされた場合に発火
　2. pタグにanswered属性がついていない場合、answered属性を追加する

＜全回答の場合、提出ボタンを表示＞
　1. answered属性の個数をカウント
　2. answered属性が10個になるとhidden属性を削除し、submit-field属性へ変更する。

*/


// //////////////////////////////
// タブの切替によるquiz表示の変更
document.addEventListener('DOMContentLoaded', function(){

    const QuizNumList = document.querySelectorAll('.new-select-number');
    console.log(QuizNumList);
    QuizNumList.forEach( (all_num) => {
        all_num.addEventListener('mousedown', (event) =>{
            const selectNumber   = event.target.innerText;
            const currentNumbers = document.querySelectorAll('.num-selected');

            // 既存のnum-selected属性とquiz-selected属性を全て削除。
            currentNumbers.forEach((current) => {
                let currentP   = document.getElementById(`quiz-${current.innerText}`);
                let currentDiv = document.getElementById(`quiz-${current.innerText}-main`);
                currentP.removeAttribute('class', 'num-selected')
                currentP.setAttribute('class', 'num-none-selected')
                currentDiv.removeAttribute('class', 'quiz-selected')
                currentDiv.setAttribute('class', 'quiz-none-selected')
            });

            // 新しく選択したものにnum-selected属性とquiz-selected属性を追加する。
            let selectP   = document.getElementById(`quiz-${selectNumber}`);
            let selectDiv = document.getElementById(`quiz-${selectNumber}-main`)
            selectP.removeAttribute('clas', 'num-none-selected')
            selectP.setAttribute('class', 'num-selected')
            selectDiv.removeAttribute('class', 'quiz-none-selected')
            selectDiv.setAttribute('class', 'quiz-selected')
        });
    });

})


// //////////////////////////////
// タブへの回答済み表示




// //////////////////////////////
// 全回答した場合に提出ボタンを表示
/*
＜番号の属性追加手順＞
　1. クリック→発火
　2. タグのidを取得
　3. idが【quiz-X】となっていた場合に発火
　4. ページ内のselected属性が付いているものに下記の処理
　　　　・p.selected属性を削除
　　　　・div.selectedを削除し、div.not-selected属性を追加。
　5. 変数に取得したidを保存し、下記の処理
　　　　・p.selected属性,div.selected属性を追加
　　　　・div.not-selectedを削除。

*/

//　編集中

document.addEventListener('DOMContentLoaded', function(){

    // // //////////////////////////////
    // // タブの切替によるquiz表示の変更
    const QuizNumList = document.querySelectorAll('.select-number');
    QuizNumList.forEach( (all_num) => {
        all_num.addEventListener('mousedown', (event) =>{
            const selectNumber   = event.target.innerText;
            const previousNumbers = document.querySelectorAll('.num-selected');

            // 既存のnum-selected属性とquiz-selected属性を全て削除。
            previousNumbers.forEach((previous_num) => {
                let previousQuizNum   = document.getElementById(`quiz-${previous_num.innerText}`);
                let previousQuizField = document.getElementById(`quiz-${previous_num.innerText}-main`);
                previousQuizNum.removeAttribute('class', 'num-selected');
                previousQuizNum.setAttribute('class', 'num-not-selected');
                previousQuizField.removeAttribute('class', 'quiz-selected');
                previousQuizField.setAttribute('class', 'quiz-not-selected');
                let choiceBtns = document.getElementsByName(`answer_${previous_num.innerText}`)
                choiceBtns.forEach( (Btn) => {
                    Btn.disabled = true
                });
            });

            // 新しく選択したものにnum-selected属性とquiz-selected属性を追加する。
            let selectQuizNum   = document.getElementById(`quiz-${selectNumber}`);
            let selectQuizField = document.getElementById(`quiz-${selectNumber}-main`);
            selectQuizNum.removeAttribute('class', 'num-not-selected');
            selectQuizNum.setAttribute('class', 'num-selected');
            selectQuizField.removeAttribute('class', 'quiz-not-selected');
            selectQuizField.setAttribute('class', 'quiz-selected');
            let choiceBtns = document.getElementsByName(`answer_${selectNumber}`)
            choiceBtns.forEach( (Btn) => {
                Btn.disabled = false
            });
        });
    });
});

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



document.addEventListener('DOMContentLoaded', function(){

    // // //////////////////////////////
    // // タブの切替によるquiz表示の変更
    const QuizNumList = document.querySelectorAll('.new-select-number');
    QuizNumList.forEach( (all_num) => {
        all_num.addEventListener('mousedown', (event) =>{
            const selectNumber   = event.target.innerText;
            const previousNumbers = document.querySelectorAll('.num-selected');

            // 既存のnum-selected属性とquiz-selected属性を全て削除。
            previousNumbers.forEach((previous_num) => {
                let previousQuizNum   = document.getElementById(`quiz-${previous_num.innerText}`);
                let previousQuizField = document.getElementById(`quiz-${previous_num.innerText}-main`);
                previousQuizNum.removeAttribute('class', 'num-selected');
                previousQuizNum.setAttribute('class', 'num-none-selected');
                previousQuizField.removeAttribute('class', 'quiz-selected');
                previousQuizField.setAttribute('class', 'quiz-none-selected');
                let choiceBtns = document.getElementsByName(`answer_${previous_num.innerText}`)
                choiceBtns.forEach( (Btn) => {
                    Btn.disabled = true
                });
            });

            // 新しく選択したものにnum-selected属性とquiz-selected属性を追加する。
            let selectQuizNum   = document.getElementById(`quiz-${selectNumber}`);
            let selectQuizField = document.getElementById(`quiz-${selectNumber}-main`);
            selectQuizNum.removeAttribute('class', 'num-none-selected');
            selectQuizNum.setAttribute('class', 'num-selected');
            selectQuizField.removeAttribute('class', 'quiz-none-selected');
            selectQuizField.setAttribute('class', 'quiz-selected');
            let choiceBtns = document.getElementsByName(`answer_${selectNumber}`)
            choiceBtns.forEach( (Btn) => {
                Btn.disabled = false
            });
        });
    });

    // //////////////////////////////
    // タブへの回答済み表示
    const choices = document.querySelectorAll('.new-radio-select li');
    choices.forEach( (radioBtn) => {
        radioBtn.addEventListener('change', (e_radio) => {
            // spanにanswered属性を追加
            const quizNum = e_radio.target.id.slice(10,-2);
            const quizNum_span = document.getElementById(`quiz-${quizNum}-num`);
            quizNum_span.removeAttribute('class', 'unanswered')
            quizNum_span.setAttribute('class', 'answered')

            // //////////////////////////////
            // answeredの数が10の場合、送信ボタンを表示
            const answered = document.querySelectorAll('.answered')
            if (answered.length === 10) {
                const submitBtn = document.getElementById('submit-field');
                submitBtn.removeAttribute('class', 'hidden');
                submitBtn.setAttribute('class', 'submit-field')
            };
        });
    });
});

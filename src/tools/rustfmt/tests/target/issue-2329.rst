src/tools/rustfmt/tests/target/issue-2329.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Comments with characters which must be represented by multibyte.

// フー
use foo;
// バー
use bar;

impl MyStruct {
    // コメント
    fn f1() {} // こんにちは
    fn f2() {} // ありがとう
               // コメント
}

trait MyTrait {
    // コメント
    fn f1() {} // こんにちは
    fn f2() {} // ありがとう
               // コメント
}

fn main() {
    // コメント
    let x = 1; // Ｘ
    println!(
        "x = {}", // xの値
        x,        // Ｘ
    );
    // コメント
}



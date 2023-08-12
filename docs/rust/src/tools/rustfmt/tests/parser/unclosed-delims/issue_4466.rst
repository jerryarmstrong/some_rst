src/tools/rustfmt/tests/parser/unclosed-delims/issue_4466.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    if true {
        println!("answer: {}", a_func();
    } else {
        println!("don't think so.");
    }
}

fn a_func() -> i32 {
    42
} 


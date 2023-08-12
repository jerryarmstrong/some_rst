src/tools/rustfmt/tests/target/issue-3718.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &[i32] = &[2, 2];
    match x {
        [_a, _] => println!("Wrong username or password"),
        _ => println!("Logged in"),
    }
}



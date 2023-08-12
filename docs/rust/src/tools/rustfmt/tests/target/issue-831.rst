src/tools/rustfmt/tests/target/issue-831.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let y = a.iter().any(|x| {
        println!("a");
    }) || b.iter().any(|x| {
        println!("b");
    }) || c.iter().any(|x| {
        println!("c");
    });
}



tests/ui/associated-consts/associated-const-const-eval.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    const NUM: usize;
}

impl Foo for i32 {
    const NUM: usize = 1;
}

const FOO: usize = <i32 as Foo>::NUM;

fn main() {
    assert_eq!(1, FOO);

    match 1 {
        <i32 as Foo>::NUM => {},
        _ => assert!(false)
    }
}



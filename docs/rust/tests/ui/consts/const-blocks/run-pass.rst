tests/ui/consts/const-blocks/run-pass.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Debug, Eq, PartialEq)]
struct Bar;

fn main() {
    const FOO: Option<Bar> = None;
    const ARR: [Option<Bar>; 2] = [FOO; 2];

    assert_eq!(ARR, [None::<Bar>, None::<Bar>]);
}



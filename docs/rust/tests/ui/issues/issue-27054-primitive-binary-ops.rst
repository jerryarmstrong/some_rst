tests/ui/issues/issue-27054-primitive-binary-ops.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn main() {
    let x = &mut 1;
    assert_eq!(*x + { *x=2; 1 }, 2);
}



tests/ui/primitive-binop-lhs-mut.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let x = Box::new(0);
    assert_eq!(0, *x + { drop(x); let _ = Box::new(main); 0 });
}



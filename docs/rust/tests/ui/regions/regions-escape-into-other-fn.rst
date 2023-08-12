tests/ui/regions/regions-escape-into-other-fn.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn foo(x: &usize) -> &usize { x }
fn bar(x: &usize) -> usize { *x }

pub fn main() {
    let p: Box<_> = Box::new(3);
    assert_eq!(bar(foo(&*p)), 3);
}



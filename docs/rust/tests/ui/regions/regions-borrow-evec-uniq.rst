tests/ui/regions/regions-borrow-evec-uniq.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn foo(x: &[isize]) -> isize {
    x[0]
}

pub fn main() {
    let p = vec![1,2,3,4,5];
    let r = foo(&p);
    assert_eq!(r, 1);

    let p = vec![5,4,3,2,1];
    let r = foo(&p);
    assert_eq!(r, 5);
}



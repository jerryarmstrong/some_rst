src/tools/miri/tests/pass/recursive_static.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S(&'static S);
static S1: S = S(&S2);
static S2: S = S(&S1);

fn main() {
    let p: *const S = S2.0;
    let q: *const S = &S1;
    assert_eq!(p, q);
}



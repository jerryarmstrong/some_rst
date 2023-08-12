tests/ui/tuple/tuple-index-fat-types.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo<'a>(&'a [isize]);

fn main() {
    let x: &[isize] = &[1, 2, 3];
    let y = (x,);
    assert_eq!(y.0, x);

    let x: &[isize] = &[1, 2, 3];
    let y = Foo(x);
    assert_eq!(y.0, x);
}



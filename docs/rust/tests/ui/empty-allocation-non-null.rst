tests/ui/empty-allocation-non-null.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    assert!(Some(Box::new(())).is_some());

    let xs: Box<[()]> = Box::<[(); 0]>::new([]);
    assert!(Some(xs).is_some());

    struct Foo;
    assert!(Some(Box::new(Foo)).is_some());

    let ys: Box<[Foo]> = Box::<[Foo; 0]>::new([]);
    assert!(Some(ys).is_some());
}



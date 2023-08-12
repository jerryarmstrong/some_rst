tests/ui/issues/issue-5997-struct.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<T>() -> bool {
    struct S(T); //~ ERROR can't use generic parameters from outer function

    true
}

fn main() {
    let b = f::<isize>();
    assert!(b);
}



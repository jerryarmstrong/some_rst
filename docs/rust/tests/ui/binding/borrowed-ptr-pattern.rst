tests/ui/binding/borrowed-ptr-pattern.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo<T:Clone>(x: &T) -> T{
    match x {
        &ref a => (*a).clone()
    }
}

pub fn main() {
    assert_eq!(foo(&3), 3);
    assert_eq!(foo(&'a'), 'a');
}



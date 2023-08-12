tests/ui/generics/generic-alias-unique.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn id<T:Send>(t: T) -> T { return t; }

pub fn main() {
    let expected: Box<_> = Box::new(100);
    let actual = id::<Box<isize>>(expected.clone());
    println!("{}", *actual);
    assert_eq!(*expected, *actual);
}



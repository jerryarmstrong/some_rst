tests/ui/generics/generic-tup.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn get_third<T>(t: (T, T, T)) -> T { let (_, _, x) = t; return x; }

pub fn main() {
    println!("{}", get_third((1, 2, 3)));
    assert_eq!(get_third((1, 2, 3)), 3);
    assert_eq!(get_third((5u8, 6u8, 7u8)), 7u8);
}



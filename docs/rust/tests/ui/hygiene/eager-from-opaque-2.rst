tests/ui/hygiene/eager-from-opaque-2.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for the issue #63460.

// check-pass

#[macro_export]
macro_rules! separator {
    () => { "/" };
}

#[macro_export]
macro_rules! concat_separator {
    ( $e:literal, $($other:literal),+ ) => {
        concat!($e, $crate::separator!(), $crate::concat_separator!($($other),+))
    };
    ( $e:literal ) => {
        $e
    }
}

fn main() {
    println!("{}", concat_separator!(2, 3, 4))
}



tests/ui/macros/macro-crate-use.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn increment(x: usize) -> usize {
    x + 1
}

#[macro_export]
macro_rules! increment {
    ($x:expr) => ({
        use $crate::increment;
        increment($x)
    })
}

fn main() {
    assert_eq!(increment!(3), 4);
}



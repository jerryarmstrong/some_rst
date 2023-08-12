tests/ui/try-trait/yeet-for-option.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(yeet_expr)]

fn always_yeet() -> Option<String> {
    do yeet;
}

fn main() {
    assert_eq!(always_yeet(), None);
}



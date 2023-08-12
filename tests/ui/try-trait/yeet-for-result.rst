tests/ui/try-trait/yeet-for-result.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(yeet_expr)]

fn always_yeet() -> Result<i32, String> {
    do yeet "hello";
}

fn main() {
    assert_eq!(always_yeet(), Err("hello".to_string()));
}



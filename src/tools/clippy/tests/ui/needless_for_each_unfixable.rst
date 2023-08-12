src/tools/clippy/tests/ui/needless_for_each_unfixable.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::needless_for_each)]
#![allow(clippy::needless_return, clippy::uninlined_format_args)]

fn main() {
    let v: Vec<i32> = Vec::new();
    // This is unfixable because the closure includes `return`.
    v.iter().for_each(|v| {
        if *v == 10 {
            return;
        } else {
            println!("{}", v);
        }
    });
}



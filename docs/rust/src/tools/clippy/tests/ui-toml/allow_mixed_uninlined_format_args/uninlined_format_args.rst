src/tools/clippy/tests/ui-toml/allow_mixed_uninlined_format_args/uninlined_format_args.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::uninlined_format_args)]

fn main() {
    let local_i32 = 1;
    let local_f64 = 2.0;
    let local_opt: Option<i32> = Some(3);

    println!("val='{}'", local_i32);
    println!("Hello {} is {:.*}", "x", local_i32, local_f64);
    println!("Hello {} is {:.*}", local_i32, 5, local_f64);
    println!("Hello {} is {2:.*}", local_i32, 5, local_f64);
    println!("{}, {}", local_i32, local_opt.unwrap());
}



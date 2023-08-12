tests/ui/error-codes/E0029-teach.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z teach

fn main() {
    let s = "hoho";

    match s {
        "hello" ..= "world" => {}
        //~^ ERROR only `char` and numeric types are allowed in range patterns
        _ => {}
    }
}



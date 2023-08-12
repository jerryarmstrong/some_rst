tests/ui/closures/closure-reform-bad.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /* Any copyright is dedicated to the Public Domain.
 * http://creativecommons.org/publicdomain/zero/1.0/ */

fn call_bare(f: fn(&str)) {
    f("Hello ");
}

fn main() {
    let string = "world!";
    let f = |s: &str| println!("{}{}", s, string);
    call_bare(f)    //~ ERROR mismatched types
}



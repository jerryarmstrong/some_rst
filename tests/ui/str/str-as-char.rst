tests/ui/str/str-as-char.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    println!('●●'); //~ ERROR character literal may only contain one codepoint
}



tests/ui/parser/circular_modules_hello.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test: this is an auxiliary file for circular-modules-main.rs

#[path = "circular_modules_main.rs"]
mod circular_modules_main;

pub fn say_hello() {
    println!("{}", circular_modules_main::hi_str());
}



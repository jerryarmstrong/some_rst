tests/ui/suggestions/recover-from-semicolon-trailing-item.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // verify that after encountering a semicolon after an item the parser recovers
mod M {};
//~^ ERROR expected item, found `;`
struct S {};
//~^ ERROR expected item, found `;`
fn foo(a: usize) {};
//~^ ERROR expected item, found `;`
fn main() {
    struct X {};  // ok
    let _: usize = S {};
    //~^ ERROR mismatched types
    let _: usize = X {};
    //~^ ERROR mismatched types
    foo("");
    //~^ ERROR mismatched types
}



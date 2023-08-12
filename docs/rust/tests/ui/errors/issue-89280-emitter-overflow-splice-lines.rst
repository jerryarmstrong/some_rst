tests/ui/errors/issue-89280-emitter-overflow-splice-lines.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait X {
    fn test(x: u32, (
//~^ WARN anonymous parameters are deprecated and will be removed in the next edition
//~^^ WARN this is accepted in the current edition (Rust 2015) but is a hard error in Rust 2018!
    )) {}
}

fn main() {}



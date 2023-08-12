tests/ui/rfc-2294-if-let-guard/bindings.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

fn main() {
    match Some(None) {
        Some(x) if let Some(y) = x => (x, y),
        _ => y, //~ ERROR cannot find value `y`
    }
    y //~ ERROR cannot find value `y`
}



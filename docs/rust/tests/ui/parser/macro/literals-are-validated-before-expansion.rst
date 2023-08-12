tests/ui/parser/macro/literals-are-validated-before-expansion.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! black_hole {
    ($($tt:tt)*) => {}
}

fn main() {
    black_hole! { '\u{FFFFFF}' }
    //~^ ERROR: invalid unicode character escape
    black_hole! { "this is surrogate: \u{DAAA}" }
    //~^ ERROR: invalid unicode character escape
}



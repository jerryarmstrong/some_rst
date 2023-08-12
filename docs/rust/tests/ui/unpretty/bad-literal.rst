tests/ui/unpretty/bad-literal.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunpretty=hir
// check-fail

// In #100948 this caused an ICE with -Zunpretty=hir.
fn main() {
    1u;
    //~^ ERROR invalid suffix `u` for number literal
}



tests/ui/macros/macro-seq-followed-by-seq.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test of allowing two sequences repetitions in a row,
// functionality added as byproduct of RFC amendment #1384
//   https://github.com/rust-lang/rfcs/pull/1384

// Old version of Rust would reject this macro definition, even though
// there are no local ambiguities (the initial `banana` and `orange`
// tokens are enough for the expander to distinguish which case is
// intended).
macro_rules! foo {
    ( $(banana $a:ident)* $(orange $b:tt)* ) => { };
}

fn main() {
    foo!( banana id1 banana id2
          orange hi  orange (hello world) );
}



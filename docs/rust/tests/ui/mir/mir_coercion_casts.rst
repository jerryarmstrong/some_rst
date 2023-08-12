tests/ui/mir/mir_coercion_casts.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests the coercion casts are handled properly

fn main() {
    // This should produce only a reification of f,
    // not a fn -> fn cast as well
    let _ = f as fn(&());
}

fn f<'a>(_: &'a ()) { }



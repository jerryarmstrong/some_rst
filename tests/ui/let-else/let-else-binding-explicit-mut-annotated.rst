tests/ui/let-else/let-else-binding-explicit-mut-annotated.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // from rfc2005 test suite



// Verify the binding mode shifts - only when no `&` are auto-dereferenced is the
// final default binding mode mutable.

fn main() {
    let Some(n): &mut Option<i32> = &&Some(5i32) else { return }; //~ ERROR mismatched types
    *n += 1;
    let _ = n;

    let Some(n): &mut Option<i32> = &&mut Some(5i32) else { return }; //~ ERROR mismatched types
    *n += 1;
    let _ = n;
}



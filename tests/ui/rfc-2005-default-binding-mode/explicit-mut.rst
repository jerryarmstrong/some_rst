tests/ui/rfc-2005-default-binding-mode/explicit-mut.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verify the binding mode shifts - only when no `&` are auto-dereferenced is the
// final default binding mode mutable.

fn main() {
    match &&Some(5i32) {
        Some(n) => {
            *n += 1; //~ ERROR cannot assign to `*n`, which is behind a `&` reference
            let _ = n;
        }
        None => {},
    };

    match &mut &Some(5i32) {
        Some(n) => {
            *n += 1; //~ ERROR cannot assign to `*n`, which is behind a `&` reference
            let _ = n;
        }
        None => {},
    };

    match &&mut Some(5i32) {
        Some(n) => {
            *n += 1; //~ ERROR cannot assign to `*n`, which is behind a `&` reference
            let _ = n;
        }
        None => {},
    };
}



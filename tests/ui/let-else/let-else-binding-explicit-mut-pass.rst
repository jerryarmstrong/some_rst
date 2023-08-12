tests/ui/let-else/let-else-binding-explicit-mut-pass.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass



fn main() {
    let Some(n) = &mut &mut Some(5i32) else { return; };
    *n += 1; // OK
    let _ = n;

    let Some(n): &mut Option<i32> = &mut &mut Some(5i32) else { return; };
    *n += 1; // OK
    let _ = n;
}



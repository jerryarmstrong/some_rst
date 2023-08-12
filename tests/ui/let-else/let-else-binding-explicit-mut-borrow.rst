tests/ui/let-else/let-else-binding-explicit-mut-borrow.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Slightly different from explicit-mut-annotated -- this won't show an error until borrowck.
// Should it show a type error instead?



fn main() {
    let Some(n): &mut Option<i32> = &mut &Some(5i32) else {
        //~^ ERROR cannot borrow data in a `&` reference as mutable
        return
    };
    *n += 1;
    let _ = n;
}



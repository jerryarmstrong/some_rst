tests/ui/interior-mutability/interior-mutability.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::Cell;
use std::panic::catch_unwind;
fn main() {
    let mut x = Cell::new(22);
    catch_unwind(|| { x.set(23); });
    //~^ ERROR the type `UnsafeCell<i32>` may contain interior mutability and a
}



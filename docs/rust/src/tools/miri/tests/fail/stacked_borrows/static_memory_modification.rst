src/tools/miri/tests/fail/stacked_borrows/static_memory_modification.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static X: usize = 5;

#[allow(mutable_transmutes)]
fn main() {
    let _x = unsafe {
        std::mem::transmute::<&usize, &mut usize>(&X) //~ ERROR: writing to alloc1 which is read-only
    };
}



tests/ui/regions/regions-reborrow-from-shorter-mut-ref-mut-ref.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #8624. Test for reborrowing with 3 levels, not just two.

fn copy_borrowed_ptr<'a, 'b, 'c>(p: &'a mut &'b mut &'c mut isize) -> &'b mut isize {
    &mut ***p
    //~^ ERROR lifetime may not live long enough
}

fn main() {
}



tests/ui/repr/repr-transparent-other-items.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See also repr-transparent.rs

#[repr(transparent)] //~ ERROR should be applied to a struct
fn cant_repr_this() {}

#[repr(transparent)] //~ ERROR should be applied to a struct
static CANT_REPR_THIS: u32 = 0;

fn main() {}



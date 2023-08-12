tests/ui/dropck/relate_lt_in_type_outlives_bound.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Wrapper<'a, T>(&'a T)
where
    T: 'a;

impl<'a, T> Drop for Wrapper<'a, T>
where
    T: 'static,
    //~^ error: `Drop` impl requires `T: 'static` but the struct it is implemented for does not
{
    fn drop(&mut self) {}
}

fn main() {}



tests/ui/regions/outlives-with-missing.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait HandlerFamily {
    type Target;
}

struct HandlerWrapper<H: HandlerFamily>(H);

impl<H: HandlerFamily> HandlerWrapper<H> {
    pub fn set_handler(&self, handler: &H::Target)
    where
        T: Send + Sync + 'static,
        //~^ ERROR cannot find type `T` in this scope
    {
    }
}

fn main() {}



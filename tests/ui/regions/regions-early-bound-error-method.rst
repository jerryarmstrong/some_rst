tests/ui/regions/regions-early-bound-error-method.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that you can use a fn lifetime parameter as part of
// the value for a type parameter in a bound.

trait GetRef<'a> {
    fn get(&self) -> &'a isize;
}

struct Box<'a> {
    t: &'a isize
}

impl<'a> GetRef<'a> for Box<'a> {
    fn get(&self) -> &'a isize {
        self.t
    }
}

impl<'a> Box<'a> {
    fn or<'b,G:GetRef<'b>>(&self, g2: G) -> &'a isize {
        g2.get()
        //~^ ERROR lifetime may not live long enough
    }
}

fn main() {
}



tests/ui/nll/borrowed-universal-error-2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<'a>(x: &'a (u32,)) -> &'a u32 {
    let v = 22;
    &v
    //~^ ERROR cannot return reference to local variable `v` [E0515]
}

fn main() {}



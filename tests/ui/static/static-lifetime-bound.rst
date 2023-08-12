tests/ui/static/static-lifetime-bound.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<'a: 'static>(_: &'a i32) {} //~WARN unnecessary lifetime parameter `'a`

fn main() {
    let x = 0;
    f(&x); //~ERROR does not live long enough
}



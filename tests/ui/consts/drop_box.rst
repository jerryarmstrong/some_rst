tests/ui/consts/drop_box.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const fn f<T>(_: Box<T>) {}
//~^ ERROR destructor of

fn main() {}



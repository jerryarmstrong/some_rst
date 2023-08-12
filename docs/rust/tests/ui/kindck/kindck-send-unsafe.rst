tests/ui/kindck/kindck-send-unsafe.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate core;

fn assert_send<T:Send>() { }

fn test71<'a>() {
    assert_send::<*mut &'a isize>();
    //~^ ERROR `*mut &'a isize` cannot be sent between threads safely
}

fn main() {
}



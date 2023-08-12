tests/ui/typeck/deref-multi.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(x: &&i32) -> i32 {
    x
    //~^ ERROR mismatched types
}

fn a2(x: &&&&&i32) -> i32 {
    x
    //~^ ERROR mismatched types
}

fn b(x: &i32) -> i32 {
    &x
    //~^ ERROR mismatched types
}

fn c(x: Box<i32>) -> i32 {
    &x
    //~^ ERROR mismatched types
}

fn d(x: std::sync::Mutex<&i32>) -> i32 {
    x.lock().unwrap()
    //~^ ERROR mismatched types
}

fn main() {}



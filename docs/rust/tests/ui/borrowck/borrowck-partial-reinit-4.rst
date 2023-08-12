tests/ui/borrowck/borrowck-partial-reinit-4.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Test;

struct Test2(Option<Test>);

impl Drop for Test {
    fn drop(&mut self) {
        println!("dropping!");
    }
}

impl Drop for Test2 {
    fn drop(&mut self) {}
}

fn stuff() {
    let mut x : (Test2, Test2);
    (x.0).0 = Some(Test); //~ ERROR E0381
}

fn main() {
    stuff()
}



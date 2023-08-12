tests/ui/borrowck/borrowck-borrowed-uniq-rvalue-2.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Defer<'a> {
    x: &'a [&'a str],
}

impl<'a> Drop for Defer<'a> {
    fn drop(&mut self) {
        unsafe {
            println!("{:?}", self.x);
        }
    }
}

fn defer<'r>(x: &'r [&'r str]) -> Defer<'r> {
    Defer {
        x: x
    }
}

fn main() {
    let x = defer(&vec!["Goodbye", "world!"]); //~ ERROR temporary value dropped while borrowed
    x.x[0];
}



tests/ui/resolve/issue-2330.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Chan { }

trait Channel<T> {
    fn send(&self, v: T);
}

// `Chan` is not a trait, it's an enum
impl Chan for isize { //~ ERROR expected trait, found enum `Chan`
    fn send(&self, v: isize) { panic!() }
}

fn main() {
}



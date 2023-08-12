tests/ui/issues/issue-2823.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct C {
    x: isize,
}

impl Drop for C {
    fn drop(&mut self) {
        println!("dropping: {}", self.x);
    }
}

fn main() {
    let c = C{ x: 2};
    let _d = c.clone(); //~ ERROR no method named `clone` found
}



tests/ui/issues/issue-5321-immediates-with-bare-self.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Fooable {
    fn yes(self);
}

impl Fooable for usize {
    fn yes(self) {
        for _ in 0..self { println!("yes"); }
    }
}

pub fn main() {
    2.yes();
}



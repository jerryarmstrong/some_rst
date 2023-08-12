tests/run-make-fulldeps/split-debuginfo/bar.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Bar {
    x: u32,
}

impl Bar {
    pub fn print(&self) {
        println!("{}", self.x);
    }
}

pub fn make_bar(x: u32) -> Bar {
    Bar { x }
}



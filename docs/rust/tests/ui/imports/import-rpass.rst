tests/ui/imports/import-rpass.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
mod foo {
    pub fn x(y: isize) { println!("{}", y); }
}

mod bar {
    use foo::x;
    use foo::x as z;
    pub fn thing() { x(10); z(10); }
}

pub fn main() { bar::thing(); }



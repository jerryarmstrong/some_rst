tests/ui/dropck/drop-on-non-struct.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl<'a> Drop for &'a mut isize {
    //~^ ERROR the `Drop` trait may only be implemented for local structs, enums, and unions
    //~^^ ERROR E0117
    fn drop(&mut self) {
        println!("kaboom");
    }
}

impl Drop for Nonexistent {
    //~^ ERROR cannot find type `Nonexistent`
    fn drop(&mut self) {}
}

fn main() {}



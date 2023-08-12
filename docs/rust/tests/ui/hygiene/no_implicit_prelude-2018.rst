tests/ui/hygiene/no_implicit_prelude-2018.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#[no_implicit_prelude]
mod bar {
    fn f() {
        ::std::print!(""); // OK
        print!(); //~ ERROR cannot find macro `print` in this scope
    }
}

fn main() {}



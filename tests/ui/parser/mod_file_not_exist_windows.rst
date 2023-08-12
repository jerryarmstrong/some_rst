tests/ui/parser/mod_file_not_exist_windows.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows

mod not_a_real_file; //~ ERROR file not found for module `not_a_real_file`
//~^ HELP to create the module `not_a_real_file`, create file

fn main() {
    assert_eq!(mod_file_aux::bar(), 10);
    //~^ ERROR failed to resolve: use of undeclared crate or module `mod_file_aux`
}



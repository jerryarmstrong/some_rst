tests/ui/modules_and_files_visibility/mod_file_disambig.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod mod_file_disambig_aux; //~ ERROR file for module `mod_file_disambig_aux` found at both

fn main() {
    assert_eq!(mod_file_aux::bar(), 10);
    //~^ ERROR failed to resolve: use of undeclared crate or module `mod_file_aux`
}



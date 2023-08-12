tests/ui/modules_and_files_visibility/mod_file_correct_spans.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing that the source_map is maintained correctly when parsing mods from external files

mod mod_file_aux;

fn main() {
    assert!(mod_file_aux::bar() == 10);
    //~^ ERROR cannot find function `bar` in module `mod_file_aux`
}



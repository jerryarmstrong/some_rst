tests/ui/parser/mod_file_with_path_attr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "not_a_real_file.rs:.*\(" -> "not_a_real_file.rs: $$FILE_NOT_FOUND_MSG ("

#[path = "not_a_real_file.rs"]
mod m; //~ ERROR not_a_real_file.rs

fn main() {
    assert_eq!(m::foo(), 10);
}



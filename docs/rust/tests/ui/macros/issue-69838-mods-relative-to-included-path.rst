tests/ui/macros/issue-69838-mods-relative-to-included-path.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

include!("issue-69838-dir/included.rs");

fn main() {
    bar::i_am_in_bar();
}



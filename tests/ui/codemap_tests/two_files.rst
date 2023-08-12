tests/ui/codemap_tests/two_files.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    include!("two_files_data.rs");

struct Baz { }

impl Bar for Baz { } //~ ERROR expected trait, found type alias

fn main() { }



tests/ui/modules/special_module_name_ignore.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[path = "auxiliary/dummy_lib.rs"]
mod lib;

#[path = "auxiliary/dummy_lib.rs"]
mod main;

fn main() {}



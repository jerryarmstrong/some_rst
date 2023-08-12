tests/ui/modules/path-no-file-name.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "\.:.*\(" -> ".: $$ACCESS_DENIED_MSG ("
// normalize-stderr-test: "os error \d+" -> "os error $$ACCESS_DENIED_CODE"

#[path = "."]
mod m; //~ ERROR couldn't read

fn main() {}



tests/ui/parser/shebang/shebang-and-attrib.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #!/usr/bin/env run-cargo-script

// check-pass
#![allow(unused_variables)]


fn main() {
    let x = 5;
}



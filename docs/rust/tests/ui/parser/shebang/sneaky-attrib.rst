tests/ui/parser/shebang/sneaky-attrib.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #!//bin/bash


// This could not possibly be a shebang & also a valid rust file, since a Rust file
// can't start with `[`
/*
    [ (mixing comments to also test that we ignore both types of comments)

 */

[allow(unused_variables)]

// check-pass
fn main() {
    let x = 5;
}



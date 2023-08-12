src/tools/rustfmt/tests/target/issue-3614/version_two.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

fn main() {
    let toto = || {
        if true { 42 } else { 24 }
    };
    { T }
}



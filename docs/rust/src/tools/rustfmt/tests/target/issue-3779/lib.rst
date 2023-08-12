src/tools/rustfmt/tests/target/issue-3779/lib.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-unstable: true
// rustfmt-config: issue-3779.toml

#[path = "ice.rs"]
mod ice;

fn foo() {
    println!("abc");
}



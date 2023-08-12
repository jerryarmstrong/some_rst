src/tools/rustfmt/tests/mod-resolver/skip-files-issue-5065/main.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![rustfmt::skip]

mod foo;
mod one;

fn main() {println!("Hello, world!");
}

// trailing commet



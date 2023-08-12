tests/ui/meta/expected-error-correct-rev.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: a

// Counterpart to `expected-error-wrong-rev.rs`

#[cfg(a)]
fn foo() {
    let x: u32 = 22_usize; //[a]~ ERROR mismatched types
}

fn main() { }



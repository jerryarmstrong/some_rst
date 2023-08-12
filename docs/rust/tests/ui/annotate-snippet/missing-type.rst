tests/ui/annotate-snippet/missing-type.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --error-format human-annotate-rs -Z unstable-options

pub fn main() {
    let x: Iter; //~ ERROR cannot find type `Iter` in this scope
}



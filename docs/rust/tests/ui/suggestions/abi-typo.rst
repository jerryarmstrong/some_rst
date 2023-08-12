tests/ui/suggestions/abi-typo.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
extern "cdedl" fn cdedl() {} //~ ERROR invalid ABI

fn main() {
    cdedl();
}



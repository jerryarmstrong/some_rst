tests/ui/moves/move-of-addr-of-mut.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that taking a mutable raw ptr to an uninitialized variable does not change its
// initializedness.

struct S;

fn main() {
    let mut x: S;
    std::ptr::addr_of_mut!(x); //~ ERROR E0381

    let y = x; // Should error here if `addr_of_mut` is ever allowed on uninitialized variables
    drop(y);
}



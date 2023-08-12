tests/ui/atomic-from-mut-not-available.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86
// only-linux

fn main() {
    core::sync::atomic::AtomicU64::from_mut(&mut 0u64);
    //~^ ERROR: no function or associated item named `from_mut` found for struct `AtomicU64`
}



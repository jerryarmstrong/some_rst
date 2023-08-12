tests/ui/typeck/issue-104510-ice.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// only-x86_64

struct W<T: ?Sized>(Oops);
//~^ ERROR cannot find type `Oops` in this scope

unsafe fn test() {
    let j = W(());
    let pointer = &j as *const _;
    core::arch::asm!(
        "nop",
        in("eax") pointer,
    );
}

fn main() {}



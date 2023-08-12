tests/ui/feature-gates/issue-43106-gating-of-derive-2.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks cases where the derive-macro does not exist.

mod derive {
    #[derive(x3300)]
    //~^ ERROR cannot find derive macro `x3300` in this scope
    //~| ERROR cannot find derive macro `x3300` in this scope
    union U { f: i32 }

    #[derive(x3300)]
    //~^ ERROR cannot find derive macro `x3300` in this scope
    //~| ERROR cannot find derive macro `x3300` in this scope
    enum E { }

    #[derive(x3300)]
    //~^ ERROR cannot find derive macro `x3300` in this scope
    //~| ERROR cannot find derive macro `x3300` in this scope
    struct S;
}

fn main() {}



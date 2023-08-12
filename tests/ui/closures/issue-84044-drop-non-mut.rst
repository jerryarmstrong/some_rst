tests/ui/closures/issue-84044-drop-non-mut.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #84044: This used to ICE.

fn main() {
    let f = || {};
    drop(&mut f); //~ ERROR cannot borrow `f` as mutable, as it is not declared as mutable
}



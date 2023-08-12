src/tools/rustfmt/tests/source/issue-2644.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-max_width: 80
fn foo(e: Enum) {
    match e {
        Enum::Var {
            element1,
            element2,
        } => {
            return;
        }
    }
}



src/tools/rustfmt/tests/source/tuple_v2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

fn issue_4355() {
    let _ = ((1,),).0 .0;
}



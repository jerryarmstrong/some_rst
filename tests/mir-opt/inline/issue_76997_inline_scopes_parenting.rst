tests/mir-opt/inline/issue_76997_inline_scopes_parenting.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that MIR inliner can handle `SourceScopeData` parenting correctly. (#76997)

// EMIT_MIR issue_76997_inline_scopes_parenting.main.Inline.after.mir
fn main() {
    let f = |x| { let y = x; y };
    f(())
}



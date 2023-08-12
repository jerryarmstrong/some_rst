tests/mir-opt/const_prop/reify_fn_ptr.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR reify_fn_ptr.main.ConstProp.diff

fn main() {
    let _ = main as usize as *const fn();
}



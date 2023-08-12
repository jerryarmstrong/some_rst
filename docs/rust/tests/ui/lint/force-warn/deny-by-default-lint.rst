tests/ui/lint/force-warn/deny-by-default-lint.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT causes $LINT (which is deny-by-default) to warn
// compile-flags: --force-warn mutable_transmutes
// check-pass

fn main() {
    unsafe {
        let y = std::mem::transmute::<&i32, &mut i32>(&5); //~WARN: undefined behavior
    }
}



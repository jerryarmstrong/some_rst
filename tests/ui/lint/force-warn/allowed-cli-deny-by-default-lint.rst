tests/ui/lint/force-warn/allowed-cli-deny-by-default-lint.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT causes $LINT (which is deny-by-default) to warn
// despite $LINT being allowed on command line
// compile-flags: -A mutable_transmutes --force-warn mutable_transmutes
// check-pass

fn main() {
    unsafe {
        let y = std::mem::transmute::<&i32, &mut i32>(&5); //~WARN: undefined behavior
    }
}



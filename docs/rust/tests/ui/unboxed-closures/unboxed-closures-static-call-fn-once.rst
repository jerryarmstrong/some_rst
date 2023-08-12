tests/ui/unboxed-closures/unboxed-closures-static-call-fn-once.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn main() {
    let onetime = |x| x;
    onetime(0);
}



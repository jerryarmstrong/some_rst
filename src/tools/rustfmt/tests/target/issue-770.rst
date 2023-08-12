src/tools/rustfmt/tests/target/issue-770.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    if false {
        if false {
        } else {
            // A let binding here seems necessary to trigger it.
            let _ = ();
        }
    } else if let false = false {
    }
}



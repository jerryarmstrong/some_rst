tests/ui/limits/issue-69485-var-size-diffs-too-large.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// only-x86_64
// compile-flags: -Zmir-opt-level=0

fn main() {
    Bug::V([0; !0]); //~ ERROR are too big for the current
}

enum Bug {
    V([u8; !0]),
}



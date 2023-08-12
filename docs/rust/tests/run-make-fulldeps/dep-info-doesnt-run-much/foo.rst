tests/run-make-fulldeps/dep-info-doesnt-run-much/foo.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We're only emitting dep info, so we shouldn't be running static analysis to
// figure out that this program is erroneous.
fn main() {
    let a: u8 = "a";
}



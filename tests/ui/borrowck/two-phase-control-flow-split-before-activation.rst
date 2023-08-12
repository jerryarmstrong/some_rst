tests/ui/borrowck/two-phase-control-flow-split-before-activation.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let mut a = 0;
    let mut b = 0;
    let p = if maybe() {
        &mut a
    } else {
        &mut b
    };
    use_(p);
}

fn maybe() -> bool { false }
fn use_<T>(_: T) { }



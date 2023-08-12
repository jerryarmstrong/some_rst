tests/ui/pattern/usefulness/slice-patterns-reachability.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

fn main() {
    let s: &[bool] = &[];

    match s {
        [true, ..] => {}
        [true, ..] => {} //~ ERROR unreachable pattern
        [true] => {} //~ ERROR unreachable pattern
        [..] => {}
    }
    match s {
        [.., true] => {}
        [.., true] => {} //~ ERROR unreachable pattern
        [true] => {} //~ ERROR unreachable pattern
        [..] => {}
    }
    match s {
        [false, .., true] => {}
        [false, .., true] => {} //~ ERROR unreachable pattern
        [false, true] => {} //~ ERROR unreachable pattern
        [false] => {}
        [..] => {}
    }
}



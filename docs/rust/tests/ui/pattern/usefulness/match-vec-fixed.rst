tests/ui/pattern/usefulness/match-vec-fixed.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

fn a() {
    let v = [1, 2, 3];
    match v {
        [_, _, _] => {}
        [_, _, _] => {} //~ ERROR unreachable pattern
    }
    match v {
        [_, 1, _] => {}
        [_, 1, _] => {} //~ ERROR unreachable pattern
        _ => {}
    }
}

fn main() {
    a();
}



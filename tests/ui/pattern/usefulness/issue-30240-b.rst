tests/ui/pattern/usefulness/issue-30240-b.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

fn main() {
    match "world" {
        "hello" => {}
        _ => {},
    }

    match "world" {
        ref _x if false => {}
        "hello" => {}
        "hello" => {} //~ ERROR unreachable pattern
        _ => {},
    }
}



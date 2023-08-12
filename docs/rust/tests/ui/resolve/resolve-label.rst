tests/ui/resolve/resolve-label.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() {
    'l: loop {
        fn g() {
            loop {
                break 'l; //~ ERROR use of unreachable label
            }
        }
    }

    loop { 'w: while break 'w { } }
}

fn main() {}



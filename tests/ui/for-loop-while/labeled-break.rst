tests/ui/for-loop-while/labeled-break.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    'foo: loop {
        loop {
            break 'foo;
        }
    }

    'bar: for _ in 0..100 {
        loop {
            break 'bar;
        }
    }

    'foobar: while 1 + 1 == 2 {
        loop {
            break 'foobar;
        }
    }
}



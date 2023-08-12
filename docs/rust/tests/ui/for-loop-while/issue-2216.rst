tests/ui/for-loop-while/issue-2216.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unreachable_code)]
pub fn main() {
    let mut x = 0;

    'foo: loop {
        'bar: loop {
            loop {
                if 1 == 2 {
                    break 'foo;
                }
                else {
                    break 'bar;
                }
            }
            continue 'foo;
        }
        x = 42;
        break;
    }

    println!("{}", x);
    assert_eq!(x, 42);
}



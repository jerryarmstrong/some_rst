tests/ui/ret-bang.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn my_err(s: String) -> ! { println!("{}", s); panic!(); }

fn okay(i: usize) -> isize {
    if i == 3 {
        my_err("I don't like three".to_string());
    } else {
        return 42;
    }
}

pub fn main() { okay(4); }



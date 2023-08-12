tests/ui/loops/loop-no-implicit-break.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a: i8 = loop {
        1 //~ ERROR mismatched types
    };

    let b: i8 = loop {
        break 1;
    };
}

fn foo() -> i8 {
    let a: i8 = loop {
        1 //~ ERROR mismatched types
    };

    let b: i8 = loop {
        break 1;
    };

    loop {
        1 //~ ERROR mismatched types
    }

    loop {
        return 1;
    }

    loop {
        1 //~ ERROR mismatched types
    }
}



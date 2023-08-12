tests/ui/generator/reborrow-mut-upvar.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(generators)]

fn _run(bar: &mut i32) {
    || { //~ WARN unused generator that must be used
        {
            let _baz = &*bar;
            yield;
        }

        *bar = 2;
    };
}

fn main() {}



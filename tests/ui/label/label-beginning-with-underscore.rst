tests/ui/label/label-beginning-with-underscore.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(unused_labels)]

fn main() {
    // `unused_label` shouldn't warn labels beginning with `_`
    '_unused: loop {
        break;
    }
}



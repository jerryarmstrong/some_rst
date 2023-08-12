tests/ui/issues/issue-66702-break-outside-loop-val.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Breaks with values inside closures used to ICE (#66863)

fn main() {
    'some_label: loop {
        || break 'some_label ();
        //~^ ERROR: use of unreachable label `'some_label`
        //~| ERROR: `break` inside of a closure
    }
}



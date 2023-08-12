tests/ui/parser/recover-unticked-labels.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    'label: loop { break label };    //~ error: cannot find value `label` in this scope
    'label: loop { break label 0 };  //~ error: expected a label, found an identifier
    'label: loop { continue label }; //~ error: expected a label, found an identifier
}



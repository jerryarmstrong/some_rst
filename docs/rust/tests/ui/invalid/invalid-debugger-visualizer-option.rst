tests/ui/invalid/invalid-debugger-visualizer-option.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "foo.random:.*\(" -> "foo.random: $$FILE_NOT_FOUND_MSG ("
// normalize-stderr-test: "os error \d+" -> "os error $$FILE_NOT_FOUND_CODE"

#![feature(debugger_visualizer)]
#![debugger_visualizer(random_file = "../foo.random")] //~ ERROR invalid argument
#![debugger_visualizer(natvis_file = "../foo.random")] //~ ERROR
fn main() {}



tests/ui/invalid/invalid-debugger-visualizer-target.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(debugger_visualizer)]

#[debugger_visualizer(natvis_file = "../foo.natvis")] //~ ERROR attribute should be applied to a module
fn main() {}



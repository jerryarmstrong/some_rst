tests/ui/feature-gates/feature-gate-debugger-visualizer.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![debugger_visualizer(natvis_file = "auxiliary/debugger-visualizer.natvis")] //~ ERROR the `#[debugger_visualizer]` attribute is an experimental feature

fn main() {}



tests/ui/feature-gates/feature-gate-omit-gdb-pretty-printer-section.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[omit_gdb_pretty_printer_section] //~ ERROR the `#[omit_gdb_pretty_printer_section]` attribute is
fn main() {}



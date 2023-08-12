tests/ui/rfc-2091-track-caller/error-odd-syntax.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[track_caller(1)]
fn f() {}
//~^^ ERROR malformed `track_caller` attribute input

fn main() {}



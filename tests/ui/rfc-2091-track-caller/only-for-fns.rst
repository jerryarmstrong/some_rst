tests/ui/rfc-2091-track-caller/only-for-fns.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[track_caller]
struct S;
//~^^ ERROR attribute should be applied to a function definition

fn main() {}



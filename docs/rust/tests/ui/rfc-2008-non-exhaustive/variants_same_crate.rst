tests/ui/rfc-2008-non-exhaustive/variants_same_crate.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub enum NonExhaustiveVariants {
    #[non_exhaustive] Unit,
    #[non_exhaustive] Tuple(u32),
    #[non_exhaustive] Struct { field: u32 }
}

fn main() {
    let variant_tuple = NonExhaustiveVariants::Tuple(340);
    let _variant_struct = NonExhaustiveVariants::Struct { field: 340 };

    match variant_tuple {
        NonExhaustiveVariants::Unit => "",
        NonExhaustiveVariants::Tuple(_fe_tpl) => "",
        NonExhaustiveVariants::Struct { field: _ } => ""
    };
}



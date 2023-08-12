lang/syn/src/idl/relations.rs
=============================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use crate::Field;
use syn::Expr;

pub fn parse(acc: &Field, seeds_feature: bool) -> Vec<String> {
    if !seeds_feature {
        return vec![];
    }
    acc.constraints
        .has_one
        .iter()
        .flat_map(|s| match &s.join_target {
            Expr::Path(path) => path.path.segments.first().map(|l| l.ident.to_string()),
            _ => {
                println!("WARNING: unexpected seed: {:?}", s);
                None
            }
        })
        .collect()
}



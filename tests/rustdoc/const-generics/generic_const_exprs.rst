tests/rustdoc/const-generics/generic_const_exprs.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]
// make sure that `ConstEvaluatable` predicates dont cause rustdoc to ICE #77647
// @has foo/struct.Ice.html '//div[@class="item-decl"]/pre[@class="rust"]' \
//      'pub struct Ice<const N: usize>;'
pub struct Ice<const N: usize> where [(); N + 1]:;



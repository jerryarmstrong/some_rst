tests/ui/parser/impl-qpath.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z parse-only

impl <*const u8>::AssocTy {} // OK
impl <Type as Trait>::AssocTy {} // OK
impl <'a + Trait>::AssocTy {} // OK
impl <<Type>::AssocTy>::AssocTy {} // OK



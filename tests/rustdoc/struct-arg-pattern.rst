tests/rustdoc/struct-arg-pattern.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

struct BodyId {
    hir_id: usize,
}

// @has 'foo/fn.body_owner.html' '//div[@class="item-decl"]/pre[@class="rust"]' 'pub fn body_owner(_: BodyId)'
pub fn body_owner(BodyId { hir_id }: BodyId) {
    // ...
}



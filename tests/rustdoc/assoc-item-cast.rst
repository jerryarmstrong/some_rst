tests/rustdoc/assoc-item-cast.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub trait Expression {
    type SqlType;
}

pub trait AsExpression<T> {
    type Expression: Expression<SqlType = T>;
    fn as_expression(self) -> Self::Expression;
}

// @has foo/type.AsExprOf.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'type AsExprOf<Item, Type> = <Item as AsExpression<Type>>::Expression;'
pub type AsExprOf<Item, Type> = <Item as AsExpression<Type>>::Expression;



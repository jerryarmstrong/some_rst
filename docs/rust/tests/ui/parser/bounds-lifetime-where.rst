tests/ui/parser/bounds-lifetime-where.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A where 'a: 'b + 'c = u8; // OK
type A where 'a: 'b, = u8; // OK
type A where 'a: = u8; // OK
type A where 'a:, = u8; // OK
type A where 'a: 'b + 'c = u8; // OK
type A where = u8; // OK
type A where 'a: 'b + = u8; // OK
type A where , = u8; //~ ERROR expected one of `;`, `=`, `where`, lifetime, or type, found `,`

fn main() {}


